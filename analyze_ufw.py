#!/usr/bin/env python3
"""
Quick parser for UFW block logs.

Reads /var/log/ufw.log (or another file) and summarizes:
- total blocks, unique source IPs, destination ports
- top destination ports
- top protocols and TCP flag patterns
- top source IPs (optionally with geolocation via ip-api.com)
- top (source IP, destination port) pairs
- simple heuristic hints for VPN/proxy/hosting when geolocation is enabled
- hourly histogram and top inbound interfaces
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import ipaddress
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.error import URLError
from urllib.request import Request, urlopen


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize UFW block log entries.")
    parser.add_argument(
        "--log",
        default="/var/log/ufw.log",
        help="Path to the UFW log (default: /var/log/ufw.log)",
    )
    parser.add_argument(
        "--top-ports",
        type=int,
        default=10,
        help="Number of destination ports to show (default: 10)",
    )
    parser.add_argument(
        "--top-ips",
        type=int,
        default=10,
        help="Number of source IPs to show (default: 10)",
    )
    parser.add_argument(
        "--top-protos",
        type=int,
        default=5,
        help="Number of protocols to show (default: 5)",
    )
    parser.add_argument(
        "--top-flags",
        type=int,
        default=10,
        help="Number of TCP flag patterns to show (default: 10)",
    )
    parser.add_argument(
        "--top-interfaces",
        type=int,
        default=5,
        help="Number of inbound interfaces to show (default: 5)",
    )
    parser.add_argument(
        "--since-hours",
        type=float,
        default=None,
        help="Only process events from the last N hours (default: entire log)",
    )
    parser.add_argument(
        "--geo",
        action="store_true",
        help="Add geolocation and hosting/VPN/proxy hint (uses ip-api.com, heuristic)",
    )
    parser.add_argument(
        "--geo-limit",
        type=int,
        default=15,
        help="Maximum number of IPs to geolocate (default: 15)",
    )
    parser.add_argument(
        "--md-out",
        help="Path to a Markdown report file (default: no file)",
    )
    parser.add_argument(
        "--plots-dir",
        help="Directory to save chart images (jpg). If omitted, plots are not generated.",
    )
    return parser.parse_args()


def parse_block_line(line: str) -> Optional[Dict[str, object]]:
    """Parse a UFW BLOCK log line into a dict."""
    if "[UFW BLOCK]" not in line:
        return None
    parts = line.strip().split()
    if not parts:
        return None
    ts_raw = parts[0]
    try:
        timestamp = dt.datetime.fromisoformat(ts_raw)
    except ValueError:
        timestamp = None

    data: Dict[str, object] = {"timestamp": ts_raw}
    if timestamp:
        data["iso_ts"] = timestamp.isoformat()

    tcp_flags = []
    known_flags = {"FIN", "SYN", "RST", "PSH", "ACK", "URG", "ECE", "CWR"}
    for token in parts:
        if "=" not in token:
            continue
        key, value = token.split("=", 1)
        data[key] = value
    for token in parts:
        if "=" in token:
            continue
        if token in known_flags:
            tcp_flags.append(token)
    if tcp_flags:
        data["flags"] = tcp_flags
    return data


def iter_blocks(path: Path, since: Optional[dt.datetime] = None) -> Iterable[Dict[str, object]]:
    with path.open("r", errors="ignore") as fh:
        for line in fh:
            block = parse_block_line(line)
            if not block:
                continue
            ts_str = block.get("timestamp")
            if since and ts_str:
                try:
                    ts = dt.datetime.fromisoformat(ts_str)
                    if ts < since:
                        continue
                except ValueError:
                    pass
            yield block


def is_private_ip(ip: str) -> bool:
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False


GeoRecord = Dict[str, Optional[object]]
WORLD_MAP_CACHE = Path(__file__).resolve().parent / ".ufw_world_map.png"
WORLD_GEOJSON_CACHE = Path(__file__).resolve().parent / ".ufw_world_geo.json"

VPN_KEYWORDS = (
    "vpn",
    "m247",
    "torguard",
    "nordvpn",
    "expressvpn",
    "surfshark",
    "mullvad",
    "proton",
    "pia",
    "private internet access",
    "windscribe",
    "tunnelbear",
    "seedbox",
    "tor-exit",
    "tor exit",
)

DARK_FIG_BG = "#0b1724"
DARK_PANEL_BG = "#13263b"
DARK_TEXT = "#e9f1ff"
DARK_TICK = "#c7d4e6"
DARK_GRID = "#2f4d6a"
DARK_SPINE = "#3a536b"
DARK_TITLE = "#f5f9ff"
HOSTING_KEYWORDS = (
    "aws",
    "amazon",
    "ec2",
    "gce",
    "gcp",
    "google cloud",
    "google llc",
    "azure",
    "microsoft",
    "digitalocean",
    "linode",
    "ovh",
    "hetzner",
    "vultr",
    "contabo",
    "leaseweb",
    "scaleway",
    "upcloud",
    "colo",
    "colocation",
    "datacenter",
    "data center",
    "servers",
    "choopa",
    "sharktech",
    "alibaba",
    "tencent",
    "hostinger",
    "hostwinds",
    "psychz",
    "hivelocity",
    "clouvider",
    "kimsufi",
    "soyoustart",
)
CDN_KEYWORDS = (
    "akamai",
    "fastly",
    "cloudflare",
    "imperva",
    "incapsula",
)
MOBILE_KEYWORDS = (
    "mobile",
    "cellular",
    "wireless",
    "lte",
    "5g",
    "4g",
    "telefonica",
    "movistar",
    "claro",
    "vodafone",
    "tim brasil",
    "tim s.p.a",
    "telecom italia",
)


def _coerce_geo_record(raw: object) -> GeoRecord:
    if isinstance(raw, dict):
        return {
            "label": raw.get("label") or raw.get("location") or "lookup_failed",
            "lat": raw.get("lat"),
            "lon": raw.get("lon"),
            "country": raw.get("country"),
            "city": raw.get("city"),
            "org": raw.get("org"),
            "isp": raw.get("isp"),
            "asn": raw.get("asn") or raw.get("as"),
        }
    if isinstance(raw, str):
        return {"label": raw, "lat": None, "lon": None, "country": None, "city": None}
    return {"label": "lookup_failed", "lat": None, "lon": None, "country": None, "city": None}


def _keyword_hit(text: str, keywords: Iterable[str]) -> Optional[str]:
    for kw in keywords:
        if kw in text:
            return kw
    return None


def assess_network_origin(info: GeoRecord) -> Dict[str, object]:
    """
    Heuristic classification of the source network to infer hosting/VPN/proxy.
    Uses simple keyword matches in org/ISP/ASN/label; not deterministic.
    """
    label = str(info.get("label") or "")
    org = str(info.get("org") or "")
    isp = str(info.get("isp") or "")
    asn = str(info.get("asn") or "")
    text = " ".join([label, org, isp, asn]).lower()

    if info.get("label") == "private":
        return {"category": "Private/CGNAT", "evidence": [], "suspicious": False}
    if not text.strip():
        return {"category": "No data", "evidence": [], "suspicious": False}

    evidence: List[str] = []
    category = "No apparent signal"

    hit = _keyword_hit(text, VPN_KEYWORDS)
    if hit:
        evidence.append(hit)
        category = "VPN/Proxy suspected"
    else:
        hit = _keyword_hit(text, HOSTING_KEYWORDS)
        if hit:
            evidence.append(hit)
            category = "Hosting/Cloud"
        else:
            hit = _keyword_hit(text, CDN_KEYWORDS)
            if hit:
                evidence.append(hit)
                category = "CDN/Edge"

    if not evidence:
        hit = _keyword_hit(text, MOBILE_KEYWORDS)
        if hit:
            evidence.append(hit)
            category = "Mobile/CGNAT"

    suspicious = category in {"VPN/Proxy suspected", "Hosting/Cloud", "CDN/Edge"}
    return {"category": category, "evidence": evidence, "suspicious": suspicious}


def format_network_hint(info: GeoRecord, assessment: Optional[Dict[str, object]] = None) -> str:
    assessment = assessment or assess_network_origin(info)
    evidence = assessment.get("evidence") or []
    category = assessment.get("category") or "No data"
    if evidence:
        return f"{category} ({', '.join(evidence)})"
    return str(category)


def load_ufw_deny_ips() -> set[str]:
    commands = [
        ["/usr/sbin/ufw", "status"],
        ["sudo", "-n", "/usr/sbin/ufw", "status"],
    ]
    for cmd in commands:
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        except Exception:
            continue

        denies: set[str] = set()
        for line in result.stdout.splitlines():
            if "DENY" not in line:
                continue

            # UFW status can print either:
            # - "Anywhere DENY <ip>"
            # - "<ip> DENY Anywhere"
            # so we scan every token and keep valid IP literals.
            for token in line.split():
                candidate = token.strip("()[],")
                try:
                    ipaddress.ip_address(candidate)
                except ValueError:
                    continue
                denies.add(candidate)

        if denies or result.stdout.strip():
            return denies

    return set()


def geo_lookup(ip: str, cache: Dict[str, object]) -> GeoRecord:
    cached = cache.get(ip)
    if cached is not None:
        record = _coerce_geo_record(cached)
        if record.get("lat") is not None and record.get("lon") is not None:
            cache[ip] = record
            return record
        if record.get("label") == "private":
            cache[ip] = record
            return record
    if is_private_ip(ip):
        cache[ip] = {"label": "private", "lat": None, "lon": None}
        return cache[ip]  # type: ignore[return-value]
    url = (
        "http://ip-api.com/json/"
        f"{ip}?fields=status,country,regionName,city,org,isp,as,lat,lon,query"
    )
    try:
        with urlopen(url, timeout=4) as resp:
            payload = json.load(resp)
    except (URLError, TimeoutError, ValueError):
        cache[ip] = {"label": "lookup_failed", "lat": None, "lon": None}
        return cache[ip]  # type: ignore[return-value]
    if payload.get("status") != "success":
        cache[ip] = {"label": "lookup_failed", "lat": None, "lon": None}
        return cache[ip]  # type: ignore[return-value]
    parts = [
        payload.get("country"),
        payload.get("regionName"),
        payload.get("city"),
        payload.get("org") or payload.get("isp"),
    ]
    cache[ip] = {
        "label": " / ".join([p for p in parts if p]),
        "lat": payload.get("lat"),
        "lon": payload.get("lon"),
        "country": payload.get("country"),
        "city": payload.get("city"),
        "org": payload.get("org"),
        "isp": payload.get("isp"),
        "asn": payload.get("as"),
    }
    return cache[ip]  # type: ignore[return-value]


def load_geo_cache(cache_path: Path) -> Dict[str, object]:
    if cache_path.exists():
        try:
            return json.loads(cache_path.read_text())
        except Exception:
            return {}
    return {}


def save_geo_cache(cache_path: Path, cache: Dict[str, str]) -> None:
    try:
        cache_path.write_text(json.dumps(cache, indent=2, sort_keys=True))
    except Exception:
        pass


def _normalize_interface(value: Optional[object]) -> str:
    iface = str(value or "").strip()
    if iface:
        return iface
    return "unknown"


def _normalize_protocol(value: Optional[object]) -> str:
    proto = str(value or "").strip().upper()
    return proto or "UNKNOWN"


def _format_tcp_flags(flags: Iterable[str]) -> str:
    order = ("SYN", "ACK", "FIN", "RST", "PSH", "URG", "ECE", "CWR")
    uniq = {f for f in flags if f in order}
    if not uniq:
        return "none"
    ordered = [f for f in order if f in uniq]
    return "+".join(ordered)


def summarize(blocks: Iterable[Dict[str, object]], deny_ips: Optional[set[str]] = None):
    ports = collections.Counter()
    ports_blacklisted = collections.Counter()
    ports_non_blacklisted = collections.Counter()
    ips = collections.Counter()
    pairs = collections.Counter()
    hourly = collections.Counter()
    protocols = collections.Counter()
    tcp_flags = collections.Counter()
    interfaces = collections.Counter()
    total = 0
    deny_ips = deny_ips or set()

    for b in blocks:
        total += 1
        dpt = b.get("DPT", "unknown")
        src = b.get("SRC", "unknown")
        proto = _normalize_protocol(b.get("PROTO"))
        iface = _normalize_interface(b.get("IN"))
        ports[dpt] += 1
        if src in deny_ips:
            ports_blacklisted[dpt] += 1
        else:
            ports_non_blacklisted[dpt] += 1
        ips[src] += 1
        pairs[(src, dpt)] += 1
        protocols[proto] += 1
        interfaces[iface] += 1
        if proto == "TCP":
            flags = _format_tcp_flags(b.get("flags", []))
            tcp_flags[flags] += 1
        ts_str = b.get("timestamp")
        if ts_str:
            try:
                ts = dt.datetime.fromisoformat(ts_str)
                hour = ts.replace(minute=0, second=0, microsecond=0, tzinfo=None)
                hourly[hour] += 1
            except ValueError:
                pass
    return (
        total,
        ports,
        ports_blacklisted,
        ports_non_blacklisted,
        ips,
        pairs,
        hourly,
        protocols,
        tcp_flags,
        interfaces,
    )


def print_counter(counter: collections.Counter, title: str, limit: int, fmt=str):
    print(f"\n{title}")
    for item, count in counter.most_common(limit):
        print(f"  {fmt(item):<25} {count}")


def md_table(
    counter: collections.Counter,
    header_label: str,
    limit: int,
    fmt_item=str,
) -> str:
    if not counter:
        return "_No data_\n"
    total = sum(counter.values())
    lines = [
        f"| # | {header_label} | Count | % |",
        "| ---: | --- | ---: | ---: |",
    ]
    for idx, (item, count) in enumerate(counter.most_common(limit), start=1):
        pct = (count / total) * 100 if total else 0
        lines.append(f"| {idx} | {fmt_item(item)} | {count} | {pct:.1f}% |")
    return "\n".join(lines) + "\n"


def md_hourly_table(hourly: collections.Counter) -> str:
    if not hourly:
        return "_No data_\n"
    total = sum(hourly.values())
    lines = [
        "| Hour (UTC) | Count | % |",
        "| :--- | ---: | ---: |",
    ]
    for hour, count in sorted(hourly.items()):
        pct = (count / total) * 100 if total else 0
        lines.append(f"| {hour}:00 | {count} | {pct:.1f}% |")
    return "\n".join(lines) + "\n"


def build_geo_rows(
    ips: collections.Counter,
    cache: Dict[str, object],
    limit: int,
) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for ip, count in ips.most_common(limit):
        info = geo_lookup(ip, cache)
        assessment = assess_network_origin(info)
        rows.append(
            {
                "ip": ip,
                "count": count,
                "info": info,
                "assessment": assessment,
                "network_hint": format_network_hint(info, assessment),
            }
        )
    return rows


def geo_location_counter(rows: List[Dict[str, object]]) -> collections.Counter:
    counter: collections.Counter = collections.Counter()
    for row in rows:
        info = _coerce_geo_record(row.get("info"))
        city = str(info.get("city") or "").strip()
        country = str(info.get("country") or "").strip()
        if city and country:
            label = f"{city}, {country}"
        elif country:
            label = country
        elif city:
            label = city
        else:
            label = str(info.get("label") or row.get("ip") or "Unknown")
        try:
            count = int(row.get("count", 0))
        except (TypeError, ValueError):
            count = 0
        if count:
            counter[label] += count
    return counter


def md_geo_table(rows: List[Dict[str, object]]) -> str:
    if not rows:
        return "_No data_\n"
    total = sum(int(r.get("count", 0)) for r in rows)
    lines = [
        "| # | Source IP | Count | % | Location | Network / hint |",
        "| ---: | --- | ---: | ---: | --- | --- |",
    ]
    for idx, row in enumerate(rows, start=1):
        count = int(row.get("count", 0))
        pct = (count / total) * 100 if total else 0
        info = _coerce_geo_record(row.get("info"))
        label = info.get("label")
        hint = row.get("network_hint") or format_network_hint(info, row.get("assessment"))  # type: ignore[arg-type]
        lines.append(f"| {idx} | `{row.get('ip')}` | {count} | {pct:.1f}% | {label} | {hint} |")
    return "\n".join(lines) + "\n"


def md_suspicious_table(rows: List[Dict[str, object]]) -> str:
    suspicious = [r for r in rows if r.get("assessment", {}).get("suspicious")]
    if not suspicious:
        return "_No clear VPN/proxy/hosting signals in the top IPs_\n"
    total = sum(int(r.get("count", 0)) for r in suspicious)
    lines = [
        "| # | Source IP | Count | % | Suspicion | Location |",
        "| ---: | --- | ---: | ---: | --- | --- |",
    ]
    for idx, row in enumerate(suspicious, start=1):
        count = int(row.get("count", 0))
        pct = (count / total) * 100 if total else 0
        info = _coerce_geo_record(row.get("info"))
        label = info.get("label")
        hint = row.get("network_hint") or format_network_hint(info, row.get("assessment"))  # type: ignore[arg-type]
        lines.append(f"| {idx} | `{row.get('ip')}` | {count} | {pct:.1f}% | {hint} | {label} |")
    return "\n".join(lines) + "\n"


def _get_plt():
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    return plt


def _apply_dark_axes(fig, ax, grid_axis: Optional[str] = None):
    fig.patch.set_facecolor(DARK_FIG_BG)
    ax.set_facecolor(DARK_PANEL_BG)
    ax.xaxis.label.set_color(DARK_TEXT)
    ax.yaxis.label.set_color(DARK_TEXT)
    ax.title.set_color(DARK_TITLE)
    ax.tick_params(colors=DARK_TICK)
    for spine in ax.spines.values():
        spine.set_color(DARK_SPINE)
    if grid_axis:
        ax.grid(True, axis=grid_axis, linestyle="--", linewidth=0.8, color=DARK_GRID, alpha=0.55)


def _get_world_image(cache_path: Path, plt):
    if cache_path.exists():
        try:
            return plt.imread(cache_path)
        except Exception:
            pass
    urls = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/World_map_-_low_resolution.svg/1024px-World_map_-_low_resolution.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/BlankMap-World6-Equirectangular.svg/1024px-BlankMap-World6-Equirectangular.svg.png",
    ]
    for url in urls:
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0 ufw-geo-map"})
            with urlopen(req, timeout=8) as resp:
                data = resp.read()
            cache_path.write_bytes(data)
            return plt.imread(cache_path)
        except Exception:
            continue
    return None


def _load_world_geojson(cache_path: Path):
    if cache_path.exists():
        try:
            return json.loads(cache_path.read_text())
        except Exception:
            pass
    urls = [
        "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json",
        "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson",
    ]
    for url in urls:
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0 ufw-geo-map"})
            with urlopen(req, timeout=12) as resp:
                data = json.load(resp)
            cache_path.write_text(json.dumps(data))
            return data
        except Exception:
            continue
    return None


def _draw_world_map(ax, plt):
    """
    Draw a base map in equirectangular projection using GeoJSON polygons.
    Avoids projection offsets that happen with some downloaded images.
    """
    bg_color = DARK_FIG_BG
    data = _load_world_geojson(WORLD_GEOJSON_CACHE)
    if not data:
        ax.set_facecolor(bg_color)
        return False
    try:
        from matplotlib.collections import PatchCollection
        from matplotlib.patches import Polygon
    except Exception:
        ax.set_facecolor(bg_color)
        return False

    patches = []
    for feature in data.get("features", []):
        geom = feature.get("geometry") or {}
        gtype = geom.get("type")
        coords = geom.get("coordinates") or []
        if gtype == "Polygon":
            rings = coords
        elif gtype == "MultiPolygon":
            rings = [poly[0] for poly in coords if poly]
        else:
            continue
        for ring in rings:
            try:
                xy = [(float(lon), float(lat)) for lon, lat in ring]
            except Exception:
                continue
            patches.append(Polygon(xy, closed=True))

    if not patches:
        ax.set_facecolor(bg_color)
        return False

    pc = PatchCollection(
        patches,
        facecolor="#1c2f45",
        edgecolor="#365674",
        linewidth=0.4,
        alpha=0.95,
        zorder=0,
    )
    ax.add_collection(pc)
    ax.set_facecolor(bg_color)
    return True


def cluster_geo_points(points: List[Dict[str, object]], cell_size: float = 2.5) -> List[Dict[str, object]]:
    """
    Group nearby points on a simple equirectangular grid to avoid bubble overlap.
    `cell_size` is expressed in degrees.
    """
    if cell_size <= 0:
        cell_size = 2.5
    buckets: Dict[Tuple[int, int], Dict[str, object]] = {}
    for p in points:
        try:
            lat = float(p.get("lat"))  # type: ignore[arg-type]
            lon = float(p.get("lon"))  # type: ignore[arg-type]
            count = int(p.get("count", 0))  # type: ignore[arg-type]
        except (TypeError, ValueError):
            continue
        key = (round(lat / cell_size), round(lon / cell_size))
        bucket = buckets.setdefault(
            key,
            {"lat_sum": 0.0, "lon_sum": 0.0, "count": 0, "labels": []},
        )
        bucket["lat_sum"] = bucket.get("lat_sum", 0.0) + lat * count  # type: ignore[assignment]
        bucket["lon_sum"] = bucket.get("lon_sum", 0.0) + lon * count  # type: ignore[assignment]
        bucket["count"] = bucket.get("count", 0) + count  # type: ignore[assignment]
        label = p.get("city") or p.get("country") or p.get("label") or p.get("ip") or ""
        bucket["labels"].append((label, count))  # type: ignore[attr-defined]

    clustered: List[Dict[str, object]] = []
    for bucket in buckets.values():
        count = bucket["count"]  # type: ignore[assignment]
        if not count:
            continue
        lat = bucket["lat_sum"] / count  # type: ignore[assignment]
        lon = bucket["lon_sum"] / count  # type: ignore[assignment]
        labels = sorted(bucket["labels"], key=lambda x: x[1], reverse=True)  # type: ignore[arg-type]
        label = labels[0][0] if labels else ""
        if len(labels) > 1:
            label = f"{label}+{len(labels)-1}"
        clustered.append({"lat": lat, "lon": lon, "count": count, "label": label})
    return clustered


def plot_bar(
    counter: collections.Counter,
    outfile: Path,
    title: str,
    xlabel: str,
    limit: int = 10,
    *,
    horizontal: bool = False,
):
    if not counter:
        return None
    plt = _get_plt()
    items = counter.most_common(limit)
    labels = [str(i[0]) for i in items]
    counts = [i[1] for i in items]
    outfile = Path(outfile)
    outfile.parent.mkdir(parents=True, exist_ok=True)

    height = max(4.0, 0.6 * len(labels)) if horizontal else 4
    width = 10 if horizontal else 9
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_title(title)

    if horizontal:
        y_positions = list(range(len(labels)))
        ax.barh(y_positions, counts, color="#5fb0ff")
        ax.set_yticks(y_positions)
        ax.set_yticklabels(labels)
        ax.invert_yaxis()
        ax.set_xlabel("Count")
        ax.set_ylabel(xlabel)
    else:
        ax.bar(range(len(labels)), counts, color="#5fb0ff")
        ax.set_xlabel(xlabel)
        ax.set_ylabel("Count")
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=45, ha="right")

    _apply_dark_axes(fig, ax, grid_axis="x" if horizontal else "y")
    fig.tight_layout()
    fig.savefig(outfile, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    return outfile


def plot_stacked_ports(
    total: collections.Counter,
    blacklisted: collections.Counter,
    non_blacklisted: collections.Counter,
    outfile: Path,
    title: str,
    xlabel: str,
    limit: int = 10,
):
    if not total:
        return None
    plt = _get_plt()
    items = total.most_common(limit)
    labels = [str(i[0]) for i in items]
    total_counts = [i[1] for i in items]
    black_counts = [int(blacklisted.get(label, 0)) for label in labels]
    non_black_counts = [int(non_blacklisted.get(label, 0)) for label in labels]

    if not any(total_counts):
        return None

    outfile = Path(outfile)
    outfile.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.set_title(title)

    x_positions = list(range(len(labels)))
    ax.bar(x_positions, non_black_counts, color="#5fb0ff", label="Non-blacklisted")
    ax.bar(
        x_positions,
        black_counts,
        bottom=non_black_counts,
        color="#fb7185",
        label="Blacklisted",
    )
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Count")
    ax.set_xticks(x_positions)
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.legend(facecolor="#0f172a", edgecolor="#334155", labelcolor="#e2e8f0")

    _apply_dark_axes(fig, ax, grid_axis="y")
    fig.tight_layout()
    fig.savefig(outfile, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    return outfile


def plot_hourly(hourly: collections.Counter, outfile: Path):
    if not hourly:
        return None
    plt = _get_plt()
    items = sorted(hourly.items())
    labels = [h.strftime("%m-%d %Hh") for h, _ in items]
    counts = [c for _, c in items]
    outfile = Path(outfile)
    outfile.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(range(len(labels)), counts, marker="o", color="#d62728")
    ax.set_title("Blocks per hour (UTC)")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Count")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    _apply_dark_axes(fig, ax, grid_axis="y")
    fig.tight_layout()
    fig.savefig(outfile, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    return outfile


def plot_geo_bubbles(points: List[Dict[str, object]], outfile: Path):
    clustered = cluster_geo_points(points)
    if not clustered:
        return None

    plt = _get_plt()
    outfile = Path(outfile)
    outfile.parent.mkdir(parents=True, exist_ok=True)

    lons = [p["lon"] for p in clustered]
    lats = [p["lat"] for p in clustered]
    counts = [p["count"] for p in clustered]
    max_count = max(counts)
    min_count = min(counts)
    norm_max = max_count if max_count != min_count else max_count + 1
    norm = plt.Normalize(vmin=min_count, vmax=norm_max or 1)
    min_size = 40
    max_size = 360
    sizes = [
        min_size + (max_size - min_size) * (c / max_count) if max_count else min_size
        for c in counts
    ]

    cmap = plt.cm.magma

    bg_color = DARK_FIG_BG

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor(bg_color)

    map_drawn = _draw_world_map(ax, plt)
    if not map_drawn:
        bg = _get_world_image(WORLD_MAP_CACHE, plt)
        if bg is not None:
            ax.imshow(bg, extent=(-180, 180, -90, 90), zorder=0, alpha=0.55)
        else:
            ax.set_facecolor(bg_color)

    sc = ax.scatter(
        lons,
        lats,
        s=sizes,
        alpha=0.78,
        c=counts,
        cmap=cmap,
        norm=norm,
        edgecolor="#0b1724",
        linewidth=0.6,
        zorder=1,
    )

    cbar = fig.colorbar(sc, ax=ax, shrink=0.9, pad=0.02)
    cbar.set_label("Block count", color="#e9f1ff")
    cbar.ax.tick_params(colors="#c7d4e6")
    cbar.outline.set_edgecolor("#3a536b")

    # Place labels for every bubble with simple offset choices to reduce overlap.
    label_offsets = [
        (0.0, 0.0),
        (3.0, 2.2),
        (3.0, -2.2),
        (-3.0, 2.2),
        (-3.0, -2.2),
        (4.5, 0.0),
        (0.0, 4.5),
        (0.0, -4.5),
        (6.0, 3.0),
        (6.0, -3.0),
        (-6.0, 3.0),
        (-6.0, -3.0),
    ]
    placed_positions: List[Tuple[float, float]] = []

    def pick_offset(x: float, y: float) -> Tuple[float, float]:
        best = label_offsets[0]
        best_score = -1.0
        for dx, dy in label_offsets:
            px, py = x + dx, y + dy
            min_dist = min(
                (((px - ox) ** 2 + (py - oy) ** 2) ** 0.5 for ox, oy in placed_positions),
                default=1e9,
            )
            if min_dist > best_score:
                best_score = min_dist
                best = (dx, dy)
        placed_positions.append((x + best[0], y + best[1]))
        return best

    for p in sorted(clustered, key=lambda x: x["count"], reverse=True):
        label = str(p.get("label", "")) or str(p.get("ip", ""))
        dx, dy = pick_offset(float(p["lon"]), float(p["lat"]))
        if dx or dy:
            ax.plot(
                [p["lon"], p["lon"] + dx],
                [p["lat"], p["lat"] + dy],
                color="#c7d4e6",
                linewidth=0.4,
                alpha=0.6,
                zorder=1.5,
            )
        ax.text(
            p["lon"] + dx,
            p["lat"] + dy,
            label,
            fontsize=8,
            ha="center",
            va="center",
            color="#e9f1ff",
            weight="bold",
            zorder=2,
        )

    ax.set_xlim(-180, 180)
    ax.set_ylim(-90, 90)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title("Blocks by location (size & color ~ count)", color="#f5f9ff")
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)
    fig.tight_layout()
    fig.savefig(outfile, dpi=150)
    plt.close(fig)
    return outfile


def main():
    args = parse_args()
    log_path = Path(args.log)
    if not log_path.exists():
        sys.exit(f"Log not found: {log_path}")
    geo_cache_path = Path(".ufw_geo_cache.json") if args.geo else None
    geo_cache = load_geo_cache(geo_cache_path) if geo_cache_path else {}
    geo_rows: List[Dict[str, object]] = []
    suspicious_rows: List[Dict[str, object]] = []
    geo_points: List[Dict[str, object]] = []
    location_counts: collections.Counter = collections.Counter()

    since_dt = None
    if args.since_hours:
        since_dt = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=args.since_hours)

    blocks = list(iter_blocks(log_path, since=since_dt))
    deny_ips = load_ufw_deny_ips()
    (
        total,
        ports,
        ports_blacklisted,
        ports_non_blacklisted,
        ips,
        pairs,
        hourly,
        protocols,
        tcp_flags,
        interfaces,
    ) = summarize(blocks, deny_ips)
    plot_paths = []

    print(f"Log file: {log_path}")
    if args.since_hours:
        print(f"Window: last {args.since_hours} hours")
    print(f"Total blocks: {total}")
    print(f"Unique source IPs: {len(ips)}")
    print(f"Unique destination ports: {len(ports)}")

    print_counter(ports, "Top destination ports", args.top_ports)
    print_counter(protocols, "Top protocols", args.top_protos)
    print_counter(ips, "Top source IPs", args.top_ips)
    if tcp_flags:
        print_counter(tcp_flags, "Top TCP flag patterns", args.top_flags)
    print_counter(interfaces, "Top inbound interfaces (IN)", args.top_interfaces)
    print_counter(pairs, "Top (source IP, destination port)", args.top_ips, fmt=lambda x: f"{x[0]} -> {x[1]}")

    print("\nBlocks per hour (UTC):")
    for hour, count in sorted(hourly.items()):
        print(f"  {hour}:00  {count}")

    if args.geo:
        print(f"\nGeolocation (max {args.geo_limit} IPs):")
        geo_rows = build_geo_rows(ips, geo_cache, args.geo_limit)
        location_counts = geo_location_counter(geo_rows)
        suspicious_rows = [r for r in geo_rows if r.get("assessment", {}).get("suspicious")]
        for row in geo_rows:
            info = _coerce_geo_record(row.get("info"))
            label = info.get("label", "lookup_failed")
            hint = row.get("network_hint", "No data")
            print(f"  {row.get('ip'):<15} {row.get('count'):<5} {label} [{hint}]")
            if info.get("lat") is not None and info.get("lon") is not None:
                geo_points.append(
                    {
                        "ip": row.get("ip"),
                        "count": row.get("count"),
                        "lat": info.get("lat"),
                        "lon": info.get("lon"),
                        "label": label,
                        "city": info.get("city"),
                        "country": info.get("country"),
                    }
                )
        if suspicious_rows:
            print("\nVPN/Proxy/Hosting suspicion (heuristic):")
            for row in suspicious_rows:
                print(f"  {row.get('ip'):<15} {row.get('count'):<5} {row.get('network_hint')}")

    if args.plots_dir:
        plots_dir = Path(args.plots_dir)
        ports_img = plot_stacked_ports(
            ports,
            ports_blacklisted,
            ports_non_blacklisted,
            plots_dir / "ufw_top_ports.jpg",
            "Top destination ports",
            "Port",
            args.top_ports,
        )
        locations_img = (
            plot_bar(
                location_counts,
                plots_dir / "ufw_top_locations.jpg",
                "Top source countries/cities",
                "Location",
                args.top_ips,
                horizontal=True,
            )
            if location_counts
            else None
        )
        hourly_img = plot_hourly(hourly, plots_dir / "ufw_hourly.jpg")
        geo_img = plot_geo_bubbles(geo_points, plots_dir / "ufw_geo_map.jpg") if geo_points else None
        for label, img in [
            ("Top destination ports", ports_img),
            ("Top source countries/cities", locations_img),
            ("Blocks per hour (UTC)", hourly_img),
            ("Block map", geo_img),
        ]:
            if img:
                plot_paths.append((label, Path(img)))
        if plot_paths:
            print("\nSaved charts:")
            for label, img in plot_paths:
                print(f"  {label}: {img}")

    if args.md_out:
        md_lines = ["# UFW Block Report", ""]
        md_lines.append(f"- Log: `{log_path}`")
        if args.since_hours:
            md_lines.append(f"- Window: last {args.since_hours} hours")
        md_lines.append(f"- Total blocks: {total}")
        md_lines.append(f"- Unique source IPs: {len(ips)}")
        md_lines.append(f"- Unique destination ports: {len(ports)}")
        md_lines.append("")

        md_lines.append("## Top destination ports")
        md_lines.append(md_table(ports, "Destination port", args.top_ports, fmt_item=lambda p: f"`{p}`"))

        md_lines.append("## Top protocols")
        md_lines.append(md_table(protocols, "Protocol", args.top_protos, fmt_item=lambda p: f"`{p}`"))

        md_lines.append("## Top source IPs")
        md_lines.append(md_table(ips, "Source IP", args.top_ips, fmt_item=lambda ip: f"`{ip}`"))

        if tcp_flags:
            md_lines.append("## Top TCP flag patterns")
            md_lines.append(md_table(tcp_flags, "Flags", args.top_flags, fmt_item=lambda f: f"`{f}`"))

        md_lines.append("## Top inbound interfaces (IN)")
        md_lines.append(md_table(interfaces, "Interface", args.top_interfaces, fmt_item=lambda i: f"`{i}`"))

        md_lines.append("## Top source IP -> destination port")
        md_lines.append(
            md_table(
                pairs,
                "Source IP -> port",
                args.top_ips,
                fmt_item=lambda x: f"`{x[0]}` -> `{x[1]}`",
            )
        )

        md_lines.append("## Blocks per hour (UTC)")
        md_lines.append(md_hourly_table(hourly))

        if args.geo:
            md_lines.append("## Top source countries/cities")
            md_lines.append(md_table(location_counts, "Location", args.top_ips))
            md_lines.append(f"## Geolocation (max {args.geo_limit} IPs)")
            md_lines.append(md_geo_table(geo_rows))
            if suspicious_rows:
                md_lines.append("## VPN/Proxy/Hosting suspicion (heuristic)")
                md_lines.append(md_suspicious_table(suspicious_rows))

        if plot_paths:
            md_lines.append("## Charts")
            md_dir = Path(args.md_out).parent
            for label, img in plot_paths:
                rel = os.path.relpath(img, md_dir)
                md_lines.append(f"![{label}]({rel})")
            md_lines.append("")

        Path(args.md_out).write_text("\n".join(md_lines))
        print(f"\nMarkdown report generated at: {args.md_out}")

    if geo_cache_path:
        save_geo_cache(geo_cache_path, geo_cache)


if __name__ == "__main__":
    main()
