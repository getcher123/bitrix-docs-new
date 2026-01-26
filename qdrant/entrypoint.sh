#!/usr/bin/env sh
set -eu

STORAGE_DIR="/qdrant/storage"
SNAP_DIR="${QDRANT__STORAGE__SNAPSHOTS_PATH:-$STORAGE_DIR/snapshots}"
COLLECTION="${QDRANT_COLLECTION:-bitrix_docs}"
SNAPSHOT_BASE_URL="${SNAPSHOT_BASE_URL:-}"
SNAPSHOT_PARTS="${SNAPSHOT_PARTS:-}"
SNAPSHOT_FILENAME="${SNAPSHOT_FILENAME:-}"
AUTO_RECOVER="${SNAPSHOT_RECOVER_ON_STARTUP:-}"
FORCE_DOWNLOAD="${SNAPSHOT_FORCE_DOWNLOAD:-}"
CLEAN_STORAGE="${SNAPSHOT_CLEAN_STORAGE:-}"
VERIFY_TAR="${SNAPSHOT_VERIFY_TAR:-}"
EXPECTED_SHA="${SNAPSHOT_SHA256:-}"

log() {
  printf '%s %s\n' "$(date -u +"%Y-%m-%dT%H:%M:%SZ")" "$*"
}

mkdir -p "$SNAP_DIR"

clean_storage() {
  [ -n "$CLEAN_STORAGE" ] || return 0
  log "Cleaning storage for collection=$COLLECTION"
  rm -rf "$STORAGE_DIR/tmp" || true
  rm -rf "$STORAGE_DIR/collections/$COLLECTION" || true
  rm -f "$STORAGE_DIR/.qdrant-initialized" || true
  rm -f "$STORAGE_DIR/raft_state.json" || true
  rm -rf "$STORAGE_DIR/aliases" || true
}

download_parts() {
  [ -n "$SNAPSHOT_BASE_URL" ] || return 0
  [ -n "$SNAPSHOT_PARTS" ] || return 0
  log "Downloading snapshot parts from $SNAPSHOT_BASE_URL"
  log "SNAPSHOT_PARTS raw: $SNAPSHOT_PARTS"
  for part in $(echo "$SNAPSHOT_PARTS" | tr ',' ' '); do
    part="$(echo "$part" | xargs)"
    [ -n "$part" ] || continue
    if echo "$part" | grep -q '='; then
      log "Skipping invalid part entry (contains '='): $part"
      continue
    fi
    dest="$SNAP_DIR/$part"
    if [ -f "$dest" ] && [ -z "$FORCE_DOWNLOAD" ]; then
      log "Part already exists: $dest"
      continue
    fi
    if [ -f "$dest" ] && [ -n "$FORCE_DOWNLOAD" ]; then
      log "Removing existing part due to SNAPSHOT_FORCE_DOWNLOAD: $dest"
      rm -f "$dest"
    fi
    log "Downloading $part -> $dest"
    if ! curl -fL --retry 5 --retry-delay 2 --connect-timeout 10 \
      "$SNAPSHOT_BASE_URL/$part" -o "$dest"; then
      log "Download failed for $part (check SNAPSHOT_BASE_URL / SNAPSHOT_PARTS)"
      continue
    fi
  done
}

log_parts_status() {
  [ -n "$SNAPSHOT_PARTS" ] || return 0
  log "Snapshot parts status:"
  for part in $(echo "$SNAPSHOT_PARTS" | tr ',' ' '); do
    part="$(echo "$part" | xargs)"
    [ -n "$part" ] || continue
    path="$SNAP_DIR/$part"
    if [ -f "$path" ]; then
      size="$(wc -c < "$path" | tr -d ' ')"
      log "  - $part: $size bytes"
    else
      log "  - $part: MISSING"
    fi
  done
}

parts_ready() {
  [ -n "$SNAPSHOT_PARTS" ] || return 0
  for part in $(echo "$SNAPSHOT_PARTS" | tr ',' ' '); do
    part="$(echo "$part" | xargs)"
    [ -n "$part" ] || continue
    [ -f "$SNAP_DIR/$part" ] || return 1
  done
  return 0
}

reassemble_from_dir() {
  dir="$1"
  for part in "$dir"/*.snapshot.part-aa; do
    [ -e "$part" ] || break
    name="$(basename "$part")"
    base_name="${name%.part-aa}"
    if [ -n "$SNAPSHOT_FILENAME" ] && [ "$base_name" != "$SNAPSHOT_FILENAME" ]; then
      log "Skipping snapshot parts for $base_name (expecting $SNAPSHOT_FILENAME)"
      continue
    fi
    target="$SNAP_DIR/$base_name"
    if [ -f "$target" ] && [ -z "$FORCE_DOWNLOAD" ]; then
      log "Snapshot already present: $target"
      continue
    fi
    if [ -f "$target" ] && [ -n "$FORCE_DOWNLOAD" ]; then
      log "Removing existing snapshot due to SNAPSHOT_FORCE_DOWNLOAD: $target"
      rm -f "$target"
    fi
    if [ -n "$SNAPSHOT_PARTS" ] && ! parts_ready; then
      log "Snapshot parts missing; skipping reassembly for $base_name"
      continue
    fi
    if [ "$dir" != "$SNAP_DIR" ]; then
      log "Moving snapshot parts from $dir to $SNAP_DIR for: $base_name"
      mv "$dir/$base_name".part-* "$SNAP_DIR/" 2>/dev/null || true
    fi
    log "Reassembling snapshot: $target"
    cat "$SNAP_DIR/$base_name".part-* > "$target"
    size="$(wc -c < "$target" | tr -d ' ')"
    log "Snapshot size: $size bytes"
  done
}

verify_snapshot() {
  [ -n "$SNAPSHOT_FILENAME" ] || return 1
  snapshot_path="$SNAP_DIR/$SNAPSHOT_FILENAME"
  [ -f "$snapshot_path" ] || return 1

  if [ -n "$EXPECTED_SHA" ]; then
    if command -v sha256sum >/dev/null 2>&1; then
      actual_sha="$(sha256sum "$snapshot_path" | awk '{print $1}')"
      log "Snapshot sha256: $actual_sha"
      if [ "$actual_sha" != "$EXPECTED_SHA" ]; then
        log "Snapshot checksum mismatch; expected $EXPECTED_SHA"
        return 1
      fi
    else
      log "sha256sum not available; skipping checksum verification"
    fi
  fi

  if [ -n "$VERIFY_TAR" ]; then
    if command -v tar >/dev/null 2>&1; then
      if tar -tf "$snapshot_path" | grep -q '^config.json$'; then
        log "Snapshot verified: config.json present"
      else
        log "Snapshot invalid: config.json missing"
        return 1
      fi
    else
      log "tar not available; skipping tar verification"
    fi
  fi

  return 0
}

recover_snapshot() {
  [ -n "$SNAPSHOT_FILENAME" ] || return 0
  snapshot_path="$SNAP_DIR/$SNAPSHOT_FILENAME"
  [ -f "$snapshot_path" ] || return 0
  marker="$STORAGE_DIR/.snapshot_recovered_${SNAPSHOT_FILENAME}"
  if [ -f "$marker" ]; then
    log "Recovery already completed for $SNAPSHOT_FILENAME"
    return 0
  fi
  if [ -z "$AUTO_RECOVER" ]; then
    log "AUTO_RECOVER disabled; snapshot is ready at $snapshot_path"
    return 0
  fi

  if ! verify_snapshot; then
    log "Snapshot verification failed; skipping recover"
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
  if ! curl -fsS -X PUT "http://127.0.0.1:6333/collections/$COLLECTION/snapshots/recover" \
    -H "Content-Type: application/json" \
    -d "{\"location\":\"file://$snapshot_path\"}"; then
    log "Recovery failed; see Qdrant logs for details"
    return 0
  fi
  touch "$marker"
  log "Recovery finished"
}

clean_storage
download_parts
log_parts_status
reassemble_from_dir "$SNAP_DIR"
reassemble_from_dir "$STORAGE_DIR"

/qdrant/qdrant "$@" &
QDRANT_PID=$!

recover_snapshot

wait "$QDRANT_PID"
