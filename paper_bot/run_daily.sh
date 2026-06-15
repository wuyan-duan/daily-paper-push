#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

python3 paper_bot/papers_cool_bot.py \
  --json-output paper_bot/reports/latest_agentic_rl.json
