#!/usr/bin/env bash
# Resumen rápido de bloqueos de UFW sin argumentos.
# Usa analyze_ufw.py con presets razonables; se pueden añadir flags extra.
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
OUT_FILE="${UFW_MD_OUT:-$PWD/ufw_report.md}"

python3 "${SCRIPT_DIR}/analyze_ufw.py" \
  --log /var/log/ufw.log \
  --since-hours 24 \
  --top-ports 15 \
  --top-ips 15 \
  --geo \
  --geo-limit 15 \
  --md-out "${OUT_FILE}" \
  "$@"
