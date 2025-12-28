#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAG_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
REPO_ROOT="$(cd "${RAG_ROOT}/.." && pwd)"
ENV_FILE="${RAG_ROOT}/.env"

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

RAG_DATA_DIR="${RAG_DATA_DIR:-.rag}"
if [[ "${RAG_DATA_DIR}" = /* ]]; then
  LOG_DIR="${RAG_DATA_DIR}"
else
  LOG_DIR="${REPO_ROOT}/${RAG_DATA_DIR}"
fi
mkdir -p "${LOG_DIR}"

cleanup() {
  if [[ -n "${API_PID:-}" ]]; then
    kill "${API_PID}" >/dev/null 2>&1 || true
  fi
  if [[ -n "${NGROK_PID:-}" ]]; then
    kill "${NGROK_PID}" >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

PYTHONPATH="${RAG_ROOT}/src" \
  "${UVICORN_BIN}" bitrix_rag.api.main:app --host 0.0.0.0 --port 8000 \
  >"${LOG_DIR}/api.log" 2>&1 &
API_PID=$!

ngrok config add-authtoken "${NGROK_AUTH_TOKEN}" >/dev/null 2>&1 || true
ngrok http 8000 --log=stdout >"${LOG_DIR}/ngrok.log" 2>&1 &
NGROK_PID=$!

for _ in $(seq 1 30); do
  if curl -s http://127.0.0.1:4040/api/tunnels >/dev/null 2>&1; then
    break
  fi
  sleep 1
done

PYTHON_BIN=""
if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
fi

if [[ -z "${PYTHON_BIN}" ]]; then
  echo "python not found. Install python3 to parse ngrok URL." >&2
  exit 1
fi

PUBLIC_URL="$("${PYTHON_BIN}" - <<'PY'
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

if [[ -n "${PUBLIC_URL}" ]]; then
  echo "Public URL: ${PUBLIC_URL}"
  echo "Health: ${PUBLIC_URL}/health"
  echo "Answer: ${PUBLIC_URL}/answer"
else
  echo "ngrok tunnel not ready. Check ${LOG_DIR}/ngrok.log" >&2
fi

echo "Logs: ${LOG_DIR}/api.log, ${LOG_DIR}/ngrok.log"
echo "Press Ctrl+C to stop."
wait
