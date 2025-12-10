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
import sys
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple
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


def geo_lookup(ip: str, cache: Dict[str, str]) -> str:
    if ip in cache:
        return cache[ip]
    if is_private_ip(ip):
        cache[ip] = "private"
        return cache[ip]
    url = f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,org,query"
    try:
        with urlopen(url, timeout=4) as resp:
            payload = json.load(resp)
    except (URLError, TimeoutError, ValueError):
        cache[ip] = "lookup_failed"
        return cache[ip]
    if payload.get("status") != "success":
        cache[ip] = "lookup_failed"
        return cache[ip]
    parts = [payload.get("country"), payload.get("regionName"), payload.get("city"), payload.get("org")]
    cache[ip] = " / ".join([p for p in parts if p])
    return cache[ip]


def load_geo_cache(cache_path: Path) -> Dict[str, str]:
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


def main():
    args = parse_args()
    log_path = Path(args.log)
    if not log_path.exists():
        sys.exit(f"Log no encontrado: {log_path}")

    since_dt = None
    if args.since_hours:
        since_dt = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=args.since_hours)

    blocks = list(iter_blocks(log_path, since=since_dt))
    total, ports, ips, pairs, hourly = summarize(blocks)

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
        cache_path = Path(".ufw_geo_cache.json")
        cache = load_geo_cache(cache_path)
        print(f"\nGeolocalización (máx {args.geo_limit} IPs):")
        for ip, count in ips.most_common(args.geo_limit):
            location = geo_lookup(ip, cache)
            print(f"  {ip:<15} {count:<5} {location}")
        save_geo_cache(cache_path, cache)


if __name__ == "__main__":
    main()
