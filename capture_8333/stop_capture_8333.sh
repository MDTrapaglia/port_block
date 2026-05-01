#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PY_PID_FILE="${SCRIPT_DIR}/capture_8333.pid"
TCP_PID_FILE="${SCRIPT_DIR}/tcpdump_8333.pid"

stop_pid_file() {
  local file="$1"
  if [[ ! -f "$file" ]]; then
    return 1
  fi
  local pid
  pid="$(cat "$file")"
  if kill -0 "$pid" 2>/dev/null; then
    kill -INT "$pid" 2>/dev/null || true
    echo "Sent SIGINT to PID $pid (from $file)"
    return 0
  fi
  rm -f "$file"
  return 1
}

stopped=false
if stop_pid_file "$PY_PID_FILE"; then
  stopped=true
fi
if stop_pid_file "$TCP_PID_FILE"; then
  stopped=true
fi

rm -f "$PY_PID_FILE" "$TCP_PID_FILE"

if [[ "$stopped" == "false" ]]; then
  echo "No running capture found."
  exit 1
fi

echo "Capture stop requested. If tcpdump was busy, give it a few seconds to exit."
