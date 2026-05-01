#!/usr/bin/env python3
import re
import ipaddress
from datetime import datetime, timezone, timedelta
from collections import Counter
import subprocess
from pathlib import Path

LOG = "/var/log/ufw.log"
SINCE_HOURS = 24
THRESHOLD = 20
REPORT_DIR = Path("/home/mtrapaglia/projects/status_page")

WHITELIST = [
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("192.168.1.0/24"),
    ipaddress.ip_network("192.168.100.0/24"),
    ipaddress.ip_network("::1/128"),
]

SRC_RE = re.compile(r"\bSRC=([0-9a-fA-F:.]+)")
TS_RE = re.compile(r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}[+-]\d{2}:\d{2})")


def is_whitelisted(ip_str: str) -> bool:
    try:
        ip_obj = ipaddress.ip_address(ip_str)
    except ValueError:
        return True
    return any(ip_obj in net for net in WHITELIST)


def collect_candidates():
    since = datetime.now(timezone.utc) - timedelta(hours=SINCE_HOURS)
    counts = Counter()
    with open(LOG, "r", errors="ignore") as fh:
        for line in fh:
            if "[UFW BLOCK]" not in line:
                continue
            m_ts = TS_RE.search(line)
            if m_ts:
                try:
                    ts = datetime.fromisoformat(m_ts.group(1))
                    if ts.tzinfo is None:
                        ts = ts.replace(tzinfo=timezone.utc)
                    if ts < since:
                        continue
                except Exception:
                    pass
            m = SRC_RE.search(line)
            if not m:
                continue
            ip_str = m.group(1)
            if is_whitelisted(ip_str):
                continue
            counts[ip_str] += 1
    return [(ip, c) for ip, c in counts.items() if c >= THRESHOLD]


def get_existing_denies() -> set[str]:
    existing = set()
    try:
        result = subprocess.run(
            ["sudo", "-n", "/usr/sbin/ufw", "status"],
            check=True,
            capture_output=True,
            text=True,
        )
        for line in result.stdout.splitlines():
            if "DENY" not in line:
                continue
            # Normalize line like: "1.2.3.4 Anywhere DENY"
            parts = line.split()
            if parts:
                ip = parts[0]
                existing.add(ip)
    except subprocess.CalledProcessError:
        pass
    return existing


def apply_blocks(candidates):
    applied = []
    existing = get_existing_denies()
    for ip, count in sorted(candidates, key=lambda x: x[1], reverse=True):
        if ip in existing:
            applied.append((ip, count, True, "SKIPPED (already denied)"))
            continue
        try:
            subprocess.run(
                ["sudo", "-n", "/usr/sbin/ufw", "deny", "from", ip, "to", "any"],
                check=True,
                capture_output=True,
                text=True,
            )
            applied.append((ip, count, True, ""))
        except subprocess.CalledProcessError as exc:
            applied.append((ip, count, False, exc.stderr.strip() or exc.stdout.strip()))
    return applied


def write_report(candidates, applied):
    ts = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    date_tag = datetime.now().astimezone().strftime("%Y-%m-%d")
    report_path = REPORT_DIR / f"port_block_report_{date_tag}.md"

    lines = [
        f"# Port-block report ({date_tag})",
        "",
        f"Generated: {ts}",
        "",
        "## Policy",
        f"- Window: last {SINCE_HOURS} hours",
        f"- Threshold: >= {THRESHOLD} blocked attempts per IP",
        "- Block type: deny by IP (all ports)",
        "- Whitelist: 127.0.0.0/8, ::1/128, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 192.168.1.0/24, 192.168.100.0/24",
        "",
        "## Candidates",
    ]
    if not candidates:
        lines.append("- _No candidates found_\n")
    else:
        for ip, count in sorted(candidates, key=lambda x: x[1], reverse=True):
            lines.append(f"- {ip} ({count})")
        lines.append("")

    lines.append("## Applied rules")
    if not applied:
        lines.append("- _No rules applied_\n")
    else:
        for ip, count, ok, err in applied:
            status = "OK" if ok else f"FAILED ({err})"
            lines.append(f"- {ip} ({count}) → {status}")
        lines.append("")

    report_path.write_text("\n".join(lines))
    return report_path


def main():
    candidates = collect_candidates()
    applied = apply_blocks(candidates)
    report = write_report(candidates, applied)
    print(report)


if __name__ == "__main__":
    main()
