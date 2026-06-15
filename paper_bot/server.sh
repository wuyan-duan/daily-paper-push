#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PORT="${PAPER_BOT_PORT:-8770}"
HOST="${PAPER_BOT_HOST:-127.0.0.1}"
PID_FILE="paper_bot/data/server.pid"
LOG_FILE="paper_bot/data/server.log"

mkdir -p paper_bot/data

is_running() {
  [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null
}

case "${1:-start}" in
  start)
    if is_running; then
      echo "Paper bot already running: pid=$(cat "$PID_FILE") http://${HOST}:${PORT}"
      exit 0
    fi
    nohup python3 paper_bot/platform.py serve --host "$HOST" --port "$PORT" > "$LOG_FILE" 2>&1 &
    echo $! > "$PID_FILE"
    sleep 1
    if is_running; then
      echo "Paper bot running: pid=$(cat "$PID_FILE") http://${HOST}:${PORT}"
    else
      echo "Paper bot failed to start. Log:" >&2
      tail -n 80 "$LOG_FILE" >&2 || true
      exit 1
    fi
    ;;
  stop)
    if is_running; then
      kill "$(cat "$PID_FILE")"
      rm -f "$PID_FILE"
      echo "Paper bot stopped."
    else
      rm -f "$PID_FILE"
      echo "Paper bot is not running."
    fi
    ;;
  restart)
    "$0" stop
    "$0" start
    ;;
  status)
    if is_running; then
      echo "Paper bot running: pid=$(cat "$PID_FILE") http://${HOST}:${PORT}"
    else
      echo "Paper bot is not running."
      exit 1
    fi
    ;;
  logs)
    tail -n "${2:-120}" "$LOG_FILE"
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|status|logs}" >&2
    exit 2
    ;;
esac
