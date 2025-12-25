#!/usr/bin/env bash
set -euo pipefail

# Updates the imported Bitrix24 REST docs snapshot inside this vault.
#
# Source: https://github.com/bitrix-tools/b24-rest-docs
# Target: docs/bitrix24_api/b24-rest-docs/
#
# Notes:
# - This keeps the vault format (no `.git` in the target).
# - Run from the repo root (where `docs/` exists).

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="${TMPDIR:-/tmp}/b24-rest-docs"
TARGET_DIR="${ROOT_DIR}/docs/bitrix24_api/b24-rest-docs"

rm -rf "${TMP_DIR}"
git clone --depth 1 https://github.com/bitrix-tools/b24-rest-docs.git "${TMP_DIR}"

mkdir -p "${TARGET_DIR}"
rsync -a --exclude ".git" "${TMP_DIR}/" "${TARGET_DIR}/"

COMMIT="$(git -C "${TMP_DIR}" rev-parse HEAD)"
cat > "${TARGET_DIR}/UPSTREAM.md" <<EOF
# Upstream

- Repo: https://github.com/bitrix-tools/b24-rest-docs
- Commit: \`${COMMIT}\`

Этот каталог импортирован в vault без \`.git\` (как «снимок»), чтобы документация была доступна офлайн.
EOF

echo "[b24-rest-docs] updated to ${COMMIT}"

