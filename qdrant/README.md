# Qdrant (Amvera) - separate application

In this repository the main `amvera.yaml` belongs to the backend API, so Qdrant has its own config: `qdrant/amvera.yaml`.

## Deploy to Amvera

Recommended: create a **separate repository** for Qdrant (or a separate branch) and place:
- `qdrant/amvera.yaml` as `amvera.yaml` in the repo root
- `qdrant/Dockerfile` as `Dockerfile` in the repo root

Then create a new Amvera project from that repository.

If Amvera UI allows selecting a Dockerfile/config path within the current repo, use:
- Dockerfile: `qdrant/Dockerfile`
- Config: `qdrant/amvera.yaml` (or copy it to the root of the repo you deploy)

## Data

Persistence uses a mount at `/qdrant/storage` (see `persistenceMount`).
Snapshots are stored in `/qdrant/storage/snapshots` (see `QDRANT__STORAGE__SNAPSHOTS_PATH` in Dockerfile),
so they are also persisted.

## Snapshots > 200MB (upload limit)

If the platform limits upload size (e.g. 200MB), the snapshot can be split into parts.

### Split (locally)

```bash
split -b 190m bitrix_docs.snapshot bitrix_docs.snapshot.part-
```

### Where to upload on the server

Upload parts into the persistent snapshots directory (**recommended**):

`/qdrant/storage/snapshots/`

You can also upload parts into the root of the persistent storage:

`/qdrant/storage/`

Example:

```
/qdrant/storage/snapshots/bitrix_docs-20260123-193108.snapshot.part-aa
/qdrant/storage/snapshots/bitrix_docs-20260123-193108.snapshot.part-ab
...
```

### Auto-reassembly

The image uses `qdrant/entrypoint.sh`: at container start it assembles `*.snapshot.part-*`
into a final `*.snapshot` (if it does not exist) in the snapshots directory.
If parts are uploaded into `/qdrant/storage/`, the entrypoint moves them into the snapshots directory and assembles.
If `SNAPSHOT_FILENAME` is set, the script **only assembles that snapshot** and ignores other parts.

## Auto-download and auto-recover (optional)

If needed, the container can **download** snapshot parts over HTTP and **run recover** automatically.

Environment variables:
- `SNAPSHOT_BASE_URL` - base URL (e.g. `https://.../qdrant`)
- `SNAPSHOT_PARTS` - comma-separated list of parts
- `SNAPSHOT_FILENAME` - final snapshot file name
- `QDRANT_COLLECTION` - collection name (default `bitrix_docs`)
- `SNAPSHOT_RECOVER_ON_STARTUP=1` - enable auto-recover
- `SNAPSHOT_FORCE_DOWNLOAD=1` - re-download parts and reassemble even if files exist
- `SNAPSHOT_CLEAN_STORAGE=1` - clean old collection/temp before recover
- `SNAPSHOT_VERIFY_TAR=1` - verify that `config.json` exists inside the snapshot
- `SNAPSHOT_SHA256` - expected sha256 for the assembled snapshot (protects from corrupted downloads)

Example:

```
SNAPSHOT_BASE_URL=https://<ngrok-host>.ngrok-free.app
SNAPSHOT_PARTS=bitrix_docs-2026-01-26.snapshot.part-aa,bitrix_docs-2026-01-26.snapshot.part-ab,bitrix_docs-2026-01-26.snapshot.part-ac,bitrix_docs-2026-01-26.snapshot.part-ad
SNAPSHOT_FILENAME=bitrix_docs-2026-01-26.snapshot
QDRANT_COLLECTION=bitrix_docs
SNAPSHOT_RECOVER_ON_STARTUP=1
SNAPSHOT_VERIFY_TAR=1
SNAPSHOT_SHA256=71efca728583ede30294e400d42e0903c085dabf8ab17ffbb58ce59c3a13b0e8
```

Important: `SNAPSHOT_PARTS` must contain **only file names**, without `SNAPSHOT_FILENAME=...` and without spaces. Otherwise downloads will fail with 404.

Logs: on container start, detailed logs will show download, assembly and recovery status.
