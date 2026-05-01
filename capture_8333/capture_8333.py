#!/usr/bin/env python3
"""
Capture and summarize TCP traffic to a port (default: 8333) using tcpdump.

Produces a pcap plus a small text summary (flag patterns, top source IPs).
Requires tcpdump and usually root privileges. UFW/iptables drops are still
visible because tcpdump hooks before the firewall decision.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import signal
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Iterable, Tuple


TCP_FLAG_MAP = {
    "S": "SYN",
    ".": "ACK",
    "F": "FIN",
    "R": "RST",
    "P": "PSH",
    "U": "URG",
    "E": "ECE",
    "W": "CWR",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Capture and summarize traffic to TCP port 8333.")
    parser.add_argument("--port", type=int, default=8333, help="Destination TCP port to filter (default: 8333)")
    parser.add_argument("--iface", default="any", help='Interface to sniff (default: "any")')
    parser.add_argument(
        "--out-dir",
        default=Path(__file__).resolve().parent / "captures",
        help="Directory to store pcap and summary files (default: capture_8333/captures)",
    )
    parser.add_argument("--snaplen", type=int, default=256, help="Snap length for tcpdump (default: 256 bytes)")
    parser.add_argument(
        "--packet-count",
        type=int,
        default=0,
        help="Stop after N packets (0 means unlimited until interrupted)",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=0,
        help="Stop after N seconds (0 means run until interrupted)",
    )
    parser.add_argument(
        "--pid-file",
        type=Path,
        default=Path(__file__).resolve().parent / "tcpdump_8333.pid",
        help="Path to write the tcpdump PID (for stop script)",
    )
    parser.add_argument(
        "--no-summary",
        action="store_true",
        help="Skip parsing the pcap after capture (just capture packets).",
    )
    return parser.parse_args()


def write_pid_file(pid_file: Path, pid: int) -> None:
    try:
        pid_file.parent.mkdir(parents=True, exist_ok=True)
        pid_file.write_text(str(pid))
    except Exception:
        pass


def remove_pid_file(pid_file: Path) -> None:
    try:
        pid_file.unlink()
    except FileNotFoundError:
        pass
    except Exception:
        pass


def normalize_flags(raw: str) -> str:
    flags = [TCP_FLAG_MAP.get(ch, ch) for ch in raw]
    uniq = []
    for f in flags:
        if f not in uniq:
            uniq.append(f)
    return "+".join(uniq) if uniq else "unknown"


def split_host_port(token: str) -> Tuple[str, str]:
    token = token.rstrip(":")
    if token and token.split(".")[-1].isdigit():
        host, port = token.rsplit(".", 1)
        return host, port
    return token, ""


def analyze_pcap(pcap_path: Path) -> Path:
    summary_path = pcap_path.with_suffix(pcap_path.suffix + ".summary.txt")
    cmd = ["tcpdump", "-nn", "-tttt", "-r", str(pcap_path)]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    if result.returncode not in (0, 1):
        summary_path.write_text(f"tcpdump failed to read pcap (code {result.returncode}): {result.stderr}\n")
        return summary_path

    lines = result.stdout.splitlines()
    total = 0
    flags_counter: Counter[str] = Counter()
    src_counter: Counter[str] = Counter()
    dst_counter: Counter[str] = Counter()
    flag_pattern = re.compile(r"Flags\s+\[([^\]]+)\]")

    for line in lines:
        if " > " not in line:
            continue
        parts = line.split()
        try:
            ip_idx = parts.index("IP")
        except ValueError:
            continue
        total += 1
        src_token = parts[ip_idx + 1]
        dst_token = parts[ip_idx + 3]
        src_host, _ = split_host_port(src_token)
        dst_host, _ = split_host_port(dst_token)
        src_counter[src_host] += 1
        dst_counter[dst_host] += 1
        match = flag_pattern.search(line)
        if match:
            flags_counter[normalize_flags(match.group(1))] += 1

    lines_out = [
        f"Capture file: {pcap_path}",
        f"Total packets: {total}",
        "",
        "Top source IPs:",
    ]
    for ip, count in src_counter.most_common(10):
        lines_out.append(f"  {ip:<20} {count}")
    lines_out.append("")
    lines_out.append("Top destination IPs:")
    for ip, count in dst_counter.most_common(10):
        lines_out.append(f"  {ip:<20} {count}")
    lines_out.append("")
    lines_out.append("TCP flag patterns:")
    for flag, count in flags_counter.most_common():
        lines_out.append(f"  {flag:<15} {count}")
    lines_out.append("")
    if result.stderr.strip():
        lines_out.append("tcpdump stderr:")
        lines_out.append(result.stderr.strip())
        lines_out.append("")

    summary_path.write_text("\n".join(lines_out))
    return summary_path


def run_capture(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    pcap_path = out_dir / f"port{args.port}_{timestamp}.pcap"

    cmd = [
        "tcpdump",
        "-i",
        args.iface,
        "-n",
        "-s",
        str(args.snaplen),
        "-w",
        str(pcap_path),
    ]
    if args.packet_count > 0:
        cmd.extend(["-c", str(args.packet_count)])
    cmd.extend(["tcp", "port", str(args.port)])

    print(f"Starting tcpdump: {' '.join(cmd)}")
    print(f"Writing to: {pcap_path}")
    try:
        proc = subprocess.Popen(cmd)
    except FileNotFoundError:
        print("tcpdump not found in PATH. Install it and re-run (sudo apt install tcpdump).", file=sys.stderr)
        return 1
    write_pid_file(Path(args.pid_file), proc.pid)

    deadline = time.time() + args.duration if args.duration > 0 else None
    try:
        while True:
            try:
                proc.wait(timeout=1.0)
                break
            except subprocess.TimeoutExpired:
                if deadline and time.time() >= deadline:
                    print("Stopping capture (duration reached).")
                    proc.send_signal(signal.SIGINT)
                    proc.wait(timeout=5)
                    break
                continue
    except KeyboardInterrupt:
        print("Stopping capture (keyboard interrupt).")
        proc.send_signal(signal.SIGINT)
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
    finally:
        remove_pid_file(Path(args.pid_file))

    ret = proc.returncode or 0
    if ret not in (0, 130):  # 130 = interrupted
        print(f"tcpdump exited with code {ret}", file=sys.stderr)
    if not args.no_summary:
        summary_path = analyze_pcap(pcap_path)
        print(f"Summary written to: {summary_path}")
    return ret


def main() -> None:
    args = parse_args()
    sys.exit(run_capture(args))


if __name__ == "__main__":
    main()
