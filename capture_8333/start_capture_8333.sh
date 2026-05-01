#!/usr/bin/env bash
set -euo pipefail

# Launch tcpdump capture for TCP port 8333 via the Python helper.
# Requires tcpdump (and typically sudo/root). Environment overrides:
#   IFACE=any PORT=8333 DURATION=0 PACKETS=0 SNAPLEN=256

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
OUT_DIR="${SCRIPT_DIR}/captures"
PY_PID_FILE="${SCRIPT_DIR}/capture_8333.pid"
TCP_PID_FILE="${SCRIPT_DIR}/tcpdump_8333.pid"
LOG_FILE="${SCRIPT_DIR}/capture_8333.out.log"

if [[ -f "$PY_PID_FILE" ]] && kill -0 "$(cat "$PY_PID_FILE")" 2>/dev/null; then
  echo "Capture already running (python PID $(cat "$PY_PID_FILE")). Stop it first." >&2
  exit 1
fi

mkdir -p "$OUT_DIR"

IFACE="${IFACE:-any}"
PORT="${PORT:-8333}"
DURATION="${DURATION:-}"
PACKETS="${PACKETS:-}"
SNAPLEN="${SNAPLEN:-256}"

cmd=(python3 "$SCRIPT_DIR/capture_8333.py" --iface "$IFACE" --out-dir "$OUT_DIR" --pid-file "$TCP_PID_FILE" --port "$PORT" --snaplen "$SNAPLEN")
if [[ -n "$PACKETS" ]]; then
  cmd+=(--packet-count "$PACKETS")
fi
if [[ -n "$DURATION" ]]; then
  cmd+=(--duration "$DURATION")
fi

nohup "${cmd[@]}" >"$LOG_FILE" 2>&1 &
echo $! >"$PY_PID_FILE"
echo "Capture started (python PID $(cat "$PY_PID_FILE")); tcpdump PID stored in $TCP_PID_FILE"
echo "PCAPs in $OUT_DIR; live log: $LOG_FILE"
