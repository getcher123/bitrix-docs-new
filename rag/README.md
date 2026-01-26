# RAG service for the Bitrix Markdown vault

This directory contains the RAG system code for the local vault in `../docs/`.

Project documentation:

- `../docs/RAG/RAG_PLAN.md`
- `../docs/RAG/RAG_PARAMETERS.md`
- `../docs/RAG/RAG_RISKS.md`
- `../docs/RAG/RAG_ACCEPTANCE.md`
- `../docs/RAG/RAG_TEST_SET.md`
- `../docs/RAG/RAG_QUESTIONNAIRE.md`

## Requirements

- Python 3.10+
- Docker Desktop (for Qdrant) or local Qdrant binary
- Access to BGE endpoints (Colab/ngrok)
- OpenAI-compatible API key (for answer generation; without it the system uses extractive mode)

## Quick overview

- Index: `bitrix-rag --env-file .env index`
- Search: `bitrix-rag --env-file .env search "query"`
- Answer: `bitrix-rag --env-file .env answer "query"`
- API: `uvicorn bitrix_rag.api.main:app --host 0.0.0.0 --port 8000`
- Public API (ngrok): `./scripts/run_with_ngrok.sh run`

## Problem and behavior

**Problem:** in a large Bitrix vault it is hard to quickly find exact answers, examples and source links.  
**Users:** Bitrix24 / 1C-Bitrix admins and developers.  
**Constraints:** data is a local `docs/` Markdown vault, no external indexing.  
**Expected behavior:** answers must cite sources and explicitly say when data is missing.

### User stories (example)

- As a developer, I want to find a D7 class example and get the source link.
- As a developer, I want to understand a REST method and where it is documented.
- As an admin, I want to find configuration steps for a feature (smart processes / CRM).
- As a user, I want to navigate to the exact lesson from the answer.
- As a user, I want to see sources right after statements.
- As a user, I want an honest "no data" answer with a helpful alternative.

### Architecture (high-level)

```
Frontend (SPA) -> FastAPI /answer
                     |
                     +-> BM25 (rag_data)
                     +-> Vector Search (Postgres+pgvector / Qdrant)
                     +-> Rerank + LLM (OpenAI)
                     +-> Answer + links
                     +-> Query history (Postgres/SQLite)
```

## SLA and response format

**Timeouts/SLA (via env):**

- `RAG_MAX_LATENCY_S` - total response budget (default 25s).
- `OPENAI_TIMEOUT_S` - LLM timeout (default 20s).
- `BGE_TIMEOUT_S` - embed/rerank timeout (default 30s).

**API response format:**

- `answer` - answer text without inline `sources:`.
- `sources` - array of source paths.
- If data is missing, the answer must explicitly say so and provide alternatives **without links**.

## Frontend

The production frontend is a git submodule at `../frontend/`.

If `frontend/` is empty after `git clone`:

```bash
git submodule update --init --recursive
```

## Single entry point

Start with **[docs/MAIN_INDEX.md](docs/MAIN_INDEX.md)** - the single navigation page by roles and tasks.

## Quick start (2-3 minutes)

### Visual Studio Code (recommended)

1. Open the repo folder in VS Code
2. Open `docs/MAIN_INDEX.md`
3. Press `Ctrl+Shift+V` (preview)
4. `Ctrl+Click` links to navigate
5. `Ctrl+Shift+F` to search the vault

### Obsidian

1. `Open folder as vault` -> select repo folder (or only `docs/`)
2. Open `docs/MAIN_INDEX.md` (or `MAIN_INDEX.md` if vault = `docs/`)
3. Use global search and graph view

## Key pages (no duplicate navigation)

- `docs/MAIN_INDEX.md` - start navigation (single entry point)
- `docs/INDEX.md` - section index (generated, map-like)
- `docs/MODULES.md` - classic API modules list
- `docs/QUICK_REFERENCE.md` - quick answers/scenarios
- `docs/bitrix24_api/index.md` - Bitrix24 REST API (incl. `b24-rest-docs` import)
- `docs/AGENT.md` - how AI agents search the docs
- `docs/RAG/` - project documentation (plan, params, risks, tests)
- `docs/ARCHITECTURE.md` - RAG architecture (stack/data flow)

## Quick search

```bash
# Search the entire repository
rg "CIBlockElement" docs/

# Search by headings (class/method)
rg "^#\\s+GetList\\b" docs/
```

## RAG service (optional)

RAG code lives in `rag/`. Full description, architecture, SLA and response format:

- `rag/README.md`
- `docs/RAG/RAG_PLAN.md`

## Quick start (MVP)

1. Start Qdrant (if used):

```bash
docker compose up -d
```

2. Fill `.env` from template:

```bash
cp .env.example .env
```

3. Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

4. Build index:

```bash
bitrix-rag --env-file .env index
```

5. Start API:

```bash
uvicorn bitrix_rag.api.main:app --host 0.0.0.0 --port 8000
```

Check:

```bash
curl -s http://localhost:8000/health
```

Optional: run API with a public ngrok endpoint:

```bash
chmod +x ./scripts/run_with_ngrok.sh
./scripts/run_with_ngrok.sh run
```

Indexing and API will continue to evolve per `../docs/RAG/RAG_PLAN.md`.

## Dev stand (Docker + MCP)

Dev stand brings up API + Postgres + MCP and uses `rag/.env`:

```bash
docker compose -f ../docker-compose.yml -f ../docker-compose.dev.yml up -d db api mcp
```

Checks:

```bash
curl -s http://localhost:8000/health
python ../mcp/smoke.py
```

Public access via ngrok (if needed):

```bash
ngrok http 8000
```

## Configuration (.env)

`.env` is not committed. Key variables:

- `VAULT_ROOT=docs` - vault path
- `RAG_DATA_DIR=.rag` - local index artifacts
- `DATABASE_URL=sqlite:///./.rag/app.db` (dev) or `postgresql+psycopg://...` (prod)
- `VECTOR_BACKEND=pgvector` (Postgres+pgvector) or `qdrant` (Qdrant), or empty (auto)
- `BGE_PROVIDER=deepinfra` or `colab`
- `NGROK_AUTH_TOKEN=...` (for public API via ngrok)
- `RAG_FAST_REST=1` (fast mode for REST: no vector/rerank/LLM)

### LLM via DeepInfra (OpenAI-compatible API)

Example:

```
OPENAI_BASE_URL=https://api.deepinfra.com/v1/openai
OPENAI_API_KEY=<DEEPINFRA_KEY>
OPENAI_MODEL=Qwen/Qwen3-Next-80B-A3B-Instruct
OPENAI_TIMEOUT_S=60
OPENAI_MAX_OUTPUT_TOKENS=1600
```

## Migrations (Alembic)

For PostgreSQL (prod), apply migrations:

```bash
alembic upgrade head
```

For SQLite (dev), tables are created automatically on API startup.

## Query history

API stores query/answer history in DB:

- `queries` - query, mode, latency, errors
- `answers` - answer text, model, sources JSON
- `feedback` - rating/comment (planned UI)

## API endpoints

- `GET /health` - status and config
- `POST /search` - top results
- `POST /answer` - answer + sources (`mode`: auto/llm/extractive)
- `GET /history` - latest queries/answers
- `GET /openapi.json` - OpenAPI schema

Example:

```bash
curl -s http://localhost:8000/answer \
  -H 'Content-Type: application/json' \
  -d '{"query":"How to get a list of iblock elements via CIBlockElement::GetList"}'
```

## OpenAPI and debug UI

- Static OpenAPI spec: `openapi.yaml`
- Debug UI stub: `debug_frontend/index.html`

Run:

1. Start API (`uvicorn ...` or `./scripts/run_with_ngrok.sh run`).
2. Open `http://localhost:8000/debug` (or `${ngrok_url}/debug`).
3. Test `POST /answer` or `POST /search`.

## Frontend (separate)

In Amvera prod container we deploy **backend only**.  
Frontend is planned as a separate deployment (Amvera as a second service or GitHub Pages).

## Indexing

Indexing creates files in `.rag/`:

- `chunks.jsonl` - chunks + metadata
- `bm25.json` - BM25 index
- `embedding_cache.jsonl` - embedding cache
- `index_manifest.json` - mtime/size for incremental updates
- `index_version.json` - index version (git commit + timestamp)

Qdrant collection: `bitrix_docs`.

Incremental indexing:

```bash
bitrix-rag --env-file .env index --strategy auto
```

Strategies: `auto` (git->mtime), `git`, `mtime`.

## Testing

Test set: `../docs/RAG/RAG_TEST_SET.md`  
Report example: `../docs/RAG/RAG_TEST_REPORT_FULL.csv`

Recall/MRR evaluation:

```bash
python3 rag/scripts/eval_test_set.py
```

Local tests:

```bash
make test
make test-integration
```

## Common issues

- Qdrant not reachable: check `docker compose up -d`, URL and port `6333`.
- Rerank/Embed return 4xx/5xx: check `BGE_BASE_URL` and key.
- LLM errors: check `OPENAI_MODEL` and `OPENAI_API_KEY`.
- Slow indexing: reduce `RAG_EMBED_BATCH`.
- Request logs: `.rag/requests.log` (JSONL with timings).

## Stop

```bash
docker compose down
```

## Sources

- https://dev.1c-bitrix.ru/docs/ (documentation, classic API)
- https://dev.1c-bitrix.ru/api_help/ (classic API: functions/classes)
- https://dev.1c-bitrix.ru/user_help/ (user docs)
- https://dev.1c-bitrix.ru/learning/ (courses)
- https://github.com/bitrix-tools/b24-rest-docs (upstream Bitrix24 REST docs, imported into `docs/bitrix24_api/b24-rest-docs/`)
