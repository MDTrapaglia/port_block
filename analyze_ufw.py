#!/usr/bin/env python3
"""
Quick parser for UFW block logs.

Reads /var/log/ufw.log (or another file) and summarizes:
- total blocks, unique source IPs, destination ports
- top destination ports
- top source IPs (optionally with geolocation via ip-api.com)
- top (source IP, destination port) pairs
- hourly histogram
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import ipaddress
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.error import URLError
from urllib.request import urlopen


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize UFW block log entries.")
    parser.add_argument(
        "--log",
        default="/var/log/ufw.log",
        help="Ruta del log de UFW (default: /var/log/ufw.log)",
    )
    parser.add_argument(
        "--top-ports",
        type=int,
        default=10,
        help="Cantidad de puertos destino a mostrar (default: 10)",
    )
    parser.add_argument(
        "--top-ips",
        type=int,
        default=10,
        help="Cantidad de IP origen a mostrar (default: 10)",
    )
    parser.add_argument(
        "--since-hours",
        type=float,
        default=None,
        help="Solo procesar eventos de las últimas N horas (default: todo el log)",
    )
    parser.add_argument(
        "--geo",
        action="store_true",
        help="Añadir geolocalización para los IPs del top (usa ip-api.com)",
    )
    parser.add_argument(
        "--geo-limit",
        type=int,
        default=15,
        help="Máximo de IPs a geolocalizar (default: 15)",
    )
    parser.add_argument(
        "--md-out",
        help="Ruta de archivo Markdown para guardar el reporte (default: no genera archivo)",
    )
    parser.add_argument(
        "--plots-dir",
        help="Directorio donde guardar gráficos (jpg). Si no se pasa, no se generan gráficos.",
    )
    return parser.parse_args()


def parse_block_line(line: str) -> Optional[Dict[str, str]]:
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

    data: Dict[str, str] = {"timestamp": ts_raw}
    if timestamp:
        data["iso_ts"] = timestamp.isoformat()

    for token in parts:
        if "=" not in token:
            continue
        key, value = token.split("=", 1)
        data[key] = value
    return data


def iter_blocks(path: Path, since: Optional[dt.datetime] = None) -> Iterable[Dict[str, str]]:
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


def _coerce_geo_record(raw: object) -> GeoRecord:
    if isinstance(raw, dict):
        return {
            "label": raw.get("label") or raw.get("location") or "lookup_failed",
            "lat": raw.get("lat"),
            "lon": raw.get("lon"),
            "country": raw.get("country"),
            "city": raw.get("city"),
        }
    if isinstance(raw, str):
        return {"label": raw, "lat": None, "lon": None, "country": None, "city": None}
    return {"label": "lookup_failed", "lat": None, "lon": None, "country": None, "city": None}


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
        f"{ip}?fields=status,country,regionName,city,org,lat,lon,query"
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
    parts = [payload.get("country"), payload.get("regionName"), payload.get("city"), payload.get("org")]
    cache[ip] = {
        "label": " / ".join([p for p in parts if p]),
        "lat": payload.get("lat"),
        "lon": payload.get("lon"),
        "country": payload.get("country"),
        "city": payload.get("city"),
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


def summarize(blocks: Iterable[Dict[str, str]]):
    ports = collections.Counter()
    ips = collections.Counter()
    pairs = collections.Counter()
    hourly = collections.Counter()
    total = 0

    for b in blocks:
        total += 1
        dpt = b.get("DPT", "unknown")
        src = b.get("SRC", "unknown")
        ports[dpt] += 1
        ips[src] += 1
        pairs[(src, dpt)] += 1
        ts_str = b.get("timestamp")
        if ts_str:
            try:
                ts = dt.datetime.fromisoformat(ts_str)
                hour = ts.replace(minute=0, second=0, microsecond=0, tzinfo=None)
                hourly[hour] += 1
            except ValueError:
                pass
    return total, ports, ips, pairs, hourly


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
        return "_Sin datos_\n"
    total = sum(counter.values())
    lines = [
        f"| # | {header_label} | Conteo | % |",
        "| ---: | --- | ---: | ---: |",
    ]
    for idx, (item, count) in enumerate(counter.most_common(limit), start=1):
        pct = (count / total) * 100 if total else 0
        lines.append(f"| {idx} | {fmt_item(item)} | {count} | {pct:.1f}% |")
    return "\n".join(lines) + "\n"


def md_hourly_table(hourly: collections.Counter) -> str:
    if not hourly:
        return "_Sin datos_\n"
    total = sum(hourly.values())
    lines = [
        "| Hora (UTC) | Conteo | % |",
        "| :--- | ---: | ---: |",
    ]
    for hour, count in sorted(hourly.items()):
        pct = (count / total) * 100 if total else 0
        lines.append(f"| {hour}:00 | {count} | {pct:.1f}% |")
    return "\n".join(lines) + "\n"


def md_geo_table(ips: collections.Counter, cache: Dict[str, object], limit: int) -> str:
    if not ips:
        return "_Sin datos_\n"
    total = sum(ips.values())
    lines = [
        "| # | IP origen | Conteo | % | Ubicación |",
        "| ---: | --- | ---: | ---: | --- |",
    ]
    for idx, (ip, count) in enumerate(ips.most_common(limit), start=1):
        pct = (count / total) * 100 if total else 0
        info = geo_lookup(ip, cache)
        lines.append(f"| {idx} | `{ip}` | {count} | {pct:.1f}% | {info.get('label')} |")
    return "\n".join(lines) + "\n"


def _get_plt():
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    return plt


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
            with urlopen(url, timeout=8) as resp:
                data = resp.read()
            cache_path.write_bytes(data)
            return plt.imread(cache_path)
        except Exception:
            continue
    return None


def cluster_geo_points(points: List[Dict[str, object]], cell_size: float = 2.5) -> List[Dict[str, object]]:
    """
    Agrupa puntos cercanos en una grilla equirectangular simple para evitar
    superposición de burbujas. `cell_size` se expresa en grados.
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


def plot_bar(counter: collections.Counter, outfile: Path, title: str, xlabel: str, limit: int = 10):
    if not counter:
        return None
    plt = _get_plt()
    items = counter.most_common(limit)
    labels = [str(i[0]) for i in items]
    counts = [i[1] for i in items]
    outfile = Path(outfile)
    outfile.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.bar(range(len(labels)), counts, color="#1f77b4")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Conteo")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)
    fig.tight_layout()
    fig.savefig(outfile, dpi=150)
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
    ax.set_title("Bloqueos por hora (UTC)")
    ax.set_xlabel("Hora")
    ax.set_ylabel("Conteo")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.grid(True, linestyle="--", alpha=0.4)
    fig.tight_layout()
    fig.savefig(outfile, dpi=150)
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
    min_size = 40
    max_size = 360
    sizes = [
        min_size + (max_size - min_size) * (c / max_count) if max_count else min_size
        for c in counts
    ]

    fig, ax = plt.subplots(figsize=(12, 6))

    bg = _get_world_image(Path(".ufw_world_map.png"), plt)
    if bg is not None:
        ax.imshow(bg, extent=(-180, 180, -90, 90), zorder=0, alpha=0.9)
    else:
        ax.set_facecolor("#f2f6fa")

    ax.scatter(
        lons,
        lats,
        s=sizes,
        alpha=0.65,
        color="#1f78b4",
        edgecolor="white",
        linewidth=0.8,
        zorder=1,
    )

    for p in sorted(clustered, key=lambda x: x["count"], reverse=True)[:5]:
        ax.text(
            p["lon"],
            p["lat"],
            str(p.get("label", "")),
            fontsize=8,
            ha="center",
            va="center",
            color="#0b3558",
            weight="bold",
            zorder=2,
        )

    ax.set_xlim(-180, 180)
    ax.set_ylim(-90, 90)
    ax.set_xticks(range(-180, 181, 60))
    ax.set_yticks(range(-90, 91, 30))
    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    ax.set_title("Bloqueos por ubicación (círculos ~ conteo)")
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()
    fig.savefig(outfile, dpi=150)
    plt.close(fig)
    return outfile


def main():
    args = parse_args()
    log_path = Path(args.log)
    if not log_path.exists():
        sys.exit(f"Log no encontrado: {log_path}")
    geo_cache_path = Path(".ufw_geo_cache.json") if args.geo else None
    geo_cache = load_geo_cache(geo_cache_path) if geo_cache_path else {}
    geo_points: List[Dict[str, object]] = []

    since_dt = None
    if args.since_hours:
        since_dt = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=args.since_hours)

    blocks = list(iter_blocks(log_path, since=since_dt))
    total, ports, ips, pairs, hourly = summarize(blocks)
    plot_paths = []

    print(f"Archivo: {log_path}")
    if args.since_hours:
        print(f"Ventana: últimas {args.since_hours} horas")
    print(f"Total de bloqueos: {total}")
    print(f"IPs de origen únicas: {len(ips)}")
    print(f"Puertos destino únicos: {len(ports)}")

    print_counter(ports, "Top puertos destino", args.top_ports)
    print_counter(ips, "Top IPs origen", args.top_ips)
    print_counter(pairs, "Top (IP origen, puerto destino)", args.top_ips, fmt=lambda x: f"{x[0]} -> {x[1]}")

    print("\nBloqueos por hora (UTC):")
    for hour, count in sorted(hourly.items()):
        print(f"  {hour}:00  {count}")

    if args.geo:
        print(f"\nGeolocalización (máx {args.geo_limit} IPs):")
        for ip, count in ips.most_common(args.geo_limit):
            info = geo_lookup(ip, geo_cache)
            label = info.get("label", "lookup_failed")
            print(f"  {ip:<15} {count:<5} {label}")
            if info.get("lat") is not None and info.get("lon") is not None:
                geo_points.append(
                    {
                        "ip": ip,
                        "count": count,
                        "lat": info.get("lat"),
                        "lon": info.get("lon"),
                        "label": label,
                        "city": info.get("city"),
                        "country": info.get("country"),
                    }
                )

    if args.plots_dir:
        plots_dir = Path(args.plots_dir)
        ports_img = plot_bar(ports, plots_dir / "ufw_top_ports.jpg", "Top puertos destino", "Puerto", args.top_ports)
        ips_img = plot_bar(ips, plots_dir / "ufw_top_ips.jpg", "Top IPs origen", "IP", args.top_ips)
        hourly_img = plot_hourly(hourly, plots_dir / "ufw_hourly.jpg")
        geo_img = plot_geo_bubbles(geo_points, plots_dir / "ufw_geo_map.jpg") if geo_points else None
        for label, img in [
            ("Top puertos destino", ports_img),
            ("Top IPs origen", ips_img),
            ("Bloqueos por hora (UTC)", hourly_img),
            ("Mapa de bloqueos", geo_img),
        ]:
            if img:
                plot_paths.append((label, Path(img)))
        if plot_paths:
            print("\nGráficos guardados:")
            for label, img in plot_paths:
                print(f"  {label}: {img}")

    if args.md_out:
        md_lines = ["# UFW Block Report", ""]
        md_lines.append(f"- Log: `{log_path}`")
        if args.since_hours:
            md_lines.append(f"- Ventana: últimas {args.since_hours} horas")
        md_lines.append(f"- Total de bloqueos: {total}")
        md_lines.append(f"- IPs de origen únicas: {len(ips)}")
        md_lines.append(f"- Puertos destino únicos: {len(ports)}")
        md_lines.append("")

        md_lines.append("## Top puertos destino")
        md_lines.append(md_table(ports, "Puerto destino", args.top_ports, fmt_item=lambda p: f"`{p}`"))

        md_lines.append("## Top IPs origen")
        md_lines.append(md_table(ips, "IP origen", args.top_ips, fmt_item=lambda ip: f"`{ip}`"))

        md_lines.append("## Top IP origen -> puerto destino")
        md_lines.append(
            md_table(
                pairs,
                "IP origen -> puerto",
                args.top_ips,
                fmt_item=lambda x: f"`{x[0]}` -> `{x[1]}`",
            )
        )

        md_lines.append("## Bloqueos por hora (UTC)")
        md_lines.append(md_hourly_table(hourly))

        if args.geo:
            md_lines.append(f"## Geolocalización (máx {args.geo_limit} IPs)")
            md_lines.append(md_geo_table(ips, geo_cache, args.geo_limit))

        if plot_paths:
            md_lines.append("## Gráficos")
            md_dir = Path(args.md_out).parent
            for label, img in plot_paths:
                rel = os.path.relpath(img, md_dir)
                md_lines.append(f"![{label}]({rel})")
            md_lines.append("")

        Path(args.md_out).write_text("\n".join(md_lines))
        print(f"\nReporte Markdown generado en: {args.md_out}")

    if geo_cache_path:
        save_geo_cache(geo_cache_path, geo_cache)


if __name__ == "__main__":
    main()
