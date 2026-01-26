#!/usr/bin/env sh
set -eu

STORAGE_DIR="/qdrant/storage"
SNAP_DIR="${QDRANT__STORAGE__SNAPSHOTS_PATH:-$STORAGE_DIR/snapshots}"
COLLECTION="${QDRANT_COLLECTION:-bitrix_docs}"
SNAPSHOT_BASE_URL="${SNAPSHOT_BASE_URL:-}"
SNAPSHOT_PARTS="${SNAPSHOT_PARTS:-}"
SNAPSHOT_FILENAME="${SNAPSHOT_FILENAME:-}"
AUTO_RECOVER="${SNAPSHOT_RECOVER_ON_STARTUP:-}"

log() {
  printf '%s %s\n' "$(date -u +"%Y-%m-%dT%H:%M:%SZ")" "$*"
}

mkdir -p "$SNAP_DIR"

download_parts() {
  [ -n "$SNAPSHOT_BASE_URL" ] || return 0
  [ -n "$SNAPSHOT_PARTS" ] || return 0
  log "Downloading snapshot parts from $SNAPSHOT_BASE_URL"
  IFS=',' read -r -a parts <<< "$SNAPSHOT_PARTS"
  for part in "${parts[@]}"; do
    part="$(echo "$part" | xargs)"
    [ -n "$part" ] || continue
    dest="$SNAP_DIR/$part"
    if [ -f "$dest" ]; then
      log "Part already exists: $dest"
      continue
    fi
    log "Downloading $part -> $dest"
    curl -fL --retry 5 --retry-delay 2 --connect-timeout 10 \
      "$SNAPSHOT_BASE_URL/$part" -o "$dest"
  done
}

reassemble_from_dir() {
  dir="$1"
  for part in "$dir"/*.snapshot.part-aa; do
    [ -e "$part" ] || break
    name="$(basename "$part")"
    base_name="${name%.part-aa}"
    target="$SNAP_DIR/$base_name"
    if [ -f "$target" ]; then
      log "Snapshot already present: $target"
      continue
    fi
    if [ "$dir" != "$SNAP_DIR" ]; then
      log "Moving snapshot parts from $dir to $SNAP_DIR for: $base_name"
      mv "$dir/$base_name".part-* "$SNAP_DIR/" 2>/dev/null || true
    fi
    log "Reassembling snapshot: $target"
    cat "$SNAP_DIR/$base_name".part-* > "$target"
  done
}

recover_snapshot() {
  [ -n "$SNAPSHOT_FILENAME" ] || return 0
  local snapshot_path="$SNAP_DIR/$SNAPSHOT_FILENAME"
  [ -f "$snapshot_path" ] || return 0
  local marker="$STORAGE_DIR/.snapshot_recovered_${SNAPSHOT_FILENAME}"
  if [ -f "$marker" ]; then
    log "Recovery already completed for $SNAPSHOT_FILENAME"
    return 0
  fi
  if [ -z "$AUTO_RECOVER" ]; then
    log "AUTO_RECOVER disabled; snapshot is ready at $snapshot_path"
    return 0
  fi

  log "Waiting for Qdrant API..."
  for i in $(seq 1 30); do
    if curl -fsS "http://127.0.0.1:6333/readyz" >/dev/null 2>&1; then
      break
    fi
    sleep 1
  done

  log "Triggering snapshot recover for collection=$COLLECTION"
  curl -fsS -X PUT "http://127.0.0.1:6333/collections/$COLLECTION/snapshots/recover" \
    -H "Content-Type: application/json" \
    -d "{\"location\":\"file://$snapshot_path\"}"
  touch "$marker"
  log "Recovery finished"
}

download_parts
reassemble_from_dir "$SNAP_DIR"
reassemble_from_dir "$STORAGE_DIR"

/qdrant/qdrant "$@" &
QDRANT_PID=$!

recover_snapshot

wait "$QDRANT_PID"
