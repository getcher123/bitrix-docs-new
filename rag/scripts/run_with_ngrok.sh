#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAG_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
REPO_ROOT="$(cd "${RAG_ROOT}/.." && pwd)"
ENV_FILE="${RAG_ROOT}/.env"
CMD="${1:-run}"
FOREGROUND=false

case "${CMD}" in
  run|start|stop|restart)
    ;;
  *)
    echo "Usage: $0 [run|start|stop|restart]" >&2
    exit 1
    ;;
esac

if [[ ! -f "${ENV_FILE}" ]]; then
  echo "Missing .env at ${ENV_FILE}" >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
source "${ENV_FILE}"
set +a

if [[ -z "${NGROK_AUTH_TOKEN:-}" ]]; then
  echo "NGROK_AUTH_TOKEN is not set in ${ENV_FILE}" >&2
  exit 1
fi

if ! command -v ngrok >/dev/null 2>&1; then
  echo "ngrok not found. Install it first: https://ngrok.com/download" >&2
  exit 1
fi

UVICORN_BIN=""
if [[ -x "${RAG_ROOT}/.venv/bin/uvicorn" ]]; then
  UVICORN_BIN="${RAG_ROOT}/.venv/bin/uvicorn"
else
  UVICORN_BIN="$(command -v uvicorn || true)"
fi

if [[ -z "${UVICORN_BIN}" ]]; then
  echo "uvicorn not found. Activate venv and install deps (pip install -e .)." >&2
  exit 1
fi

PYTHON_BIN=""
if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
fi

if [[ -z "${PYTHON_BIN}" ]]; then
  echo "python not found. Install python3 to run the debug frontend and parse ngrok URLs." >&2
  exit 1
fi

RAG_DATA_DIR="${RAG_DATA_DIR:-.rag}"
if [[ "${RAG_DATA_DIR}" = /* ]]; then
  LOG_DIR="${RAG_DATA_DIR}"
else
  LOG_DIR="${REPO_ROOT}/${RAG_DATA_DIR}"
fi
mkdir -p "${LOG_DIR}"
PID_FILE="${LOG_DIR}/run_with_ngrok.pids"

cleanup() {
  if [[ -n "${API_PID:-}" ]]; then
    kill "${API_PID}" >/dev/null 2>&1 || true
  fi
  if [[ -n "${NGROK_PID:-}" ]]; then
    kill "${NGROK_PID}" >/dev/null 2>&1 || true
  fi
}

API_PORT="${API_PORT:-8000}"

ensure_port_free() {
  local port="$1"
  if command -v rg >/dev/null 2>&1; then
    if ss -ltnp 2>/dev/null | rg -q ":${port}\\b"; then
      echo "Port ${port} is already in use. Stop the existing process or change API_PORT." >&2
      return 1
    fi
    return 0
  fi
  if ss -ltnp 2>/dev/null | grep -Eq ":${port}[^0-9]"; then
    echo "Port ${port} is already in use. Stop the existing process or change API_PORT." >&2
    return 1
  fi
  return 0
}

write_pid_file() {
  cat >"${PID_FILE}" <<EOF
API_PID=${API_PID}
NGROK_PID=${NGROK_PID}
EOF
}

read_pid_file() {
  if [[ -f "${PID_FILE}" ]]; then
    # shellcheck disable=SC1090
    source "${PID_FILE}"
    return 0
  fi
  return 1
}

stop_running() {
  if ! read_pid_file; then
    echo "No pid file found at ${PID_FILE}." >&2
    return 0
  fi
  if [[ -n "${NGROK_PID:-}" ]] && ps -p "${NGROK_PID}" >/dev/null 2>&1; then
    kill "${NGROK_PID}" >/dev/null 2>&1 || true
  fi
  if [[ -n "${API_PID:-}" ]] && ps -p "${API_PID}" >/dev/null 2>&1; then
    kill "${API_PID}" >/dev/null 2>&1 || true
  fi
  rm -f "${PID_FILE}"
  echo "Stopped."
}

if [[ "${CMD}" == "stop" ]]; then
  stop_running
  exit 0
fi

if [[ "${CMD}" == "restart" ]]; then
  stop_running
  FOREGROUND=true
elif [[ "${CMD}" == "run" ]]; then
  FOREGROUND=true
fi

ensure_port_free "${API_PORT}"

PYTHONPATH="${RAG_ROOT}/src" \
  "${UVICORN_BIN}" bitrix_rag.api.main:app --host 0.0.0.0 --port "${API_PORT}" \
  >"${LOG_DIR}/api.log" 2>&1 &
API_PID=$!

ngrok config add-authtoken "${NGROK_AUTH_TOKEN}" >/dev/null 2>&1 || true
ngrok http "${API_PORT}" --log=stdout >"${LOG_DIR}/ngrok.log" 2>&1 &
NGROK_PID=$!

write_pid_file

for _ in $(seq 1 30); do
  if curl -s http://127.0.0.1:4040/api/tunnels >/dev/null 2>&1; then
    break
  fi
  sleep 1
done

API_PUBLIC_URL="$("${PYTHON_BIN}" - <<'PY'
import json
import sys
import urllib.request

try:
    with urllib.request.urlopen("http://127.0.0.1:4040/api/tunnels") as resp:
        data = json.load(resp)
    tunnels = data.get("tunnels") or []
    https = next((t for t in tunnels if t.get("proto") == "https"), None)
    if https:
        print(https.get("public_url", ""))
    elif tunnels:
        print(tunnels[0].get("public_url", ""))
except Exception:
    sys.exit(1)
PY
)"

if [[ -n "${API_PUBLIC_URL}" ]]; then
  echo "API Public URL: ${API_PUBLIC_URL}"
  echo "Health: ${API_PUBLIC_URL}/health"
  echo "Answer: ${API_PUBLIC_URL}/answer"
  echo "Frontend: ${API_PUBLIC_URL}/debug?ngrok-skip-browser-warning=1"
else
  echo "API ngrok tunnel not ready. Check ${LOG_DIR}/ngrok.log" >&2
fi

echo "Logs: ${LOG_DIR}/api.log, ${LOG_DIR}/ngrok.log"

if [[ "${FOREGROUND}" == "true" ]]; then
  trap cleanup EXIT
  echo "Press Ctrl+C to stop."
  wait
fi
