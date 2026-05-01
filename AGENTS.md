# Repository Guidelines

## Project Structure & Module Organization
- Root contains `analyze_ufw.py`, the CLI that parses `/var/log/ufw.log`, summarizes blocks, and optionally adds geolocation plus plots. Small, pure helpers live alongside parsing/formatting code; keep related functions co-located.
- `ufw_report.sh` wraps the CLI with 24h defaults and writes `ufw_report.md` plus charts under `ufw_plots/`. Treat these outputs as generated artifacts.
- Cache files such as `.ufw_geo_cache.json`, `.ufw_world_geo.json`, and `.ufw_world_map.png` are created on demand to reduce repeat lookups; they can be deleted and rebuilt safely.

## Build, Test, and Development Commands
- Prereqs: Python 3.10+; plotting requires `matplotlib` (`pip install matplotlib`). `--geo` and world map downloads need network access.
- Quick daily snapshot with defaults: `bash ufw_report.sh`.
- Custom run with report + plots:  
  `python3 analyze_ufw.py --log /var/log/ufw.log --since-hours 24 --top-ports 15 --top-ips 15 --geo --geo-limit 15 --md-out ufw_report.md --plots-dir ufw_plots`
- Console-only summary (no network/files): `python3 analyze_ufw.py --log sample.log --top-ports 10 --top-ips 10`

## Coding Style & Naming Conventions
- Use 4-space indentation, type hints, and snake_case for functions/variables to match the existing module.
- Prefer small helpers with early returns for parsing and aggregation; reuse `Path` for filesystem access and avoid hardcoded paths beyond sensible defaults.
- Keep generated reports/plots/caches out of commits unless intentionally sharing examples.

## Testing Guidelines
- There is no automated test suite; validate changes by running the CLI against a small log excerpt and confirming totals, rankings, and tables look reasonable.
- When modifying geo or plotting logic, run with `--geo --plots-dir ufw_plots` and inspect regenerated images. Use `--geo-limit` to avoid excessive ip-api.com requests.

## Commit & Pull Request Guidelines
- Match the current history with concise, imperative subjects (e.g., `Add location breakdown and dark-themed UFW charts`).
- Commit after each successful, self-contained change; avoid bundling unrelated adjustments.
- PRs should summarize behavior changes, new flags, and dependencies, and include sample commands/output for reviewers. Call out any impact on network usage or cache files.

## Security & Configuration Tips
- UFW logs and generated reports contain real IPs/locations; scrub or truncate before sharing externally and avoid committing `.ufw_geo_cache.json` or real `ufw_report.md`.
- Geolocation and map downloads are optional; omit `--geo` to stay offline and keep processing deterministic.
