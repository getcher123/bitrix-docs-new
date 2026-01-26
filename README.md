# Bitrix Docs Vault + RAG (Zoomcamp Project)

[![CI](https://github.com/getcher123/bitrix-docs-new/actions/workflows/ci.yml/badge.svg)](https://github.com/getcher123/bitrix-docs-new/actions/workflows/ci.yml)

This README presents the project **against Zoomcamp criteria** (DataTalksClub AI Dev Tools) and links to the detailed documentation.

---

## 1) Problem description

**Problem:** in a large Bitrix vault it is hard to quickly find exact answers, examples, and links to the source of truth.  
**Users:** Bitrix24 / 1C-Bitrix administrators and developers.  
**Constraints:** data is a local `docs/` Markdown vault, without external indexing.

User stories (short):
- Find a D7 class example and get the original source link.
- Find a REST method and its documentation.
- Find configuration steps for a feature (smart processes / CRM).
- See sources immediately after each statement.
- Get an honest "no data" answer with alternatives (no links).

---

## 2) Data & policy

**We store:** `docs/`, indexes (`.rag/`, `.rag_demo/`), and query/answer history in DB.  
**We do not store:** passwords/keys in the repository; secrets live only in env.  
**Deletion:** remove `.rag/`/`.rag_demo/`; clear DB tables `queries`, `answers`, `feedback`, `embeddings`.

---

## 3) Architecture & tech stack

Stack:
- Frontend: React + Vite (SPA)
- Backend: FastAPI
- Vector: Qdrant (prod), pgvector (optional)
- DB: Postgres (prod) / SQLite (dev)
- LLM: OpenAI (Responses API)
- Embeddings/Rerank: DeepInfra/Colab
- Infra: Docker, Amvera, GitHub Actions

High-level flow:
```
Frontend -> FastAPI /answer
   -> BM25 + Vector Search (pgvector/Qdrant)
   -> Rerank + LLM
   -> Answer + sources + History
```

---

## 4) AI tools / MCP

This repo includes an MCP server with tools:
- `search_docs(query, top_k, filters)`
- `answer(query, mode?)`
- `get_source(path)`

Documentation: `docs/AGENT.md` and `mcp/`.

---

## 5) API contract (OpenAPI)

Contract: `rag/openapi.yaml`  
Frontend type generation:
```bash
cd frontend
npm run gen:api
```

API versioning: semver in `info.version` (OpenAPI).

---

## 6) Backend

Code: `rag/src/bitrix_rag/`  
Layers: `api/`, `retrieval/`, `clients/`, `db/`, `ingest/`, `eval/`.

SLA/timeouts via env:
`RAG_MAX_LATENCY_S`, `OPENAI_TIMEOUT_S`, `BGE_TIMEOUT_S`.

Response format:
- `answer` contains no `sources:` text
- `sources` is a separate array
- if no data - honest answer + alternatives without links

---

## 7) Frontend

Submodule: `frontend/` -> `https://github.com/getcher123/bitrix-scribe`  
Screens: Ask / History / Eval.  
Tests: unit (Vitest) + e2e (Playwright).
Deploy: GitHub Pages from the frontend repo (workflow `.github/workflows/pages.yml`).  
Build script: `npm run build` (Vite) publishes `dist/`.

---

## 8) Database & Vector store

Postgres + pgvector (optional):
- tables `queries`, `answers`, `feedback`, `embeddings`
- Alembic migrations
- `/health` shows DB and pgvector status

---

## 9) Evaluation & tests

Unit + integration tests, CI report:
- `docs/RAG/RAG_INTEGRATION_REPORT.json`
- `docs/RAG/RAG_INTEGRATION_REPORT.csv`

Generate locally:
```bash
python3 rag/scripts/generate_integration_report.py
```

---

## 10) Deployment (Amvera)

Prod: `https://rag-bitrix-getcher.amvera.io/`  
Smoke: `https://rag-bitrix-getcher.amvera.io/health`

Frontend (GitHub Pages): `https://getcher123.github.io/bitrix-scribe/`  
OpenAPI JSON: `https://rag-bitrix-getcher.amvera.io/openapi.json`  
Swagger UI: `https://rag-bitrix-getcher.amvera.io/docs`

Deploy docs: `docs/RAG/AMVERA_DEPLOY.md`

---

## 11) CI/CD

CI workflow: `.github/workflows/ci.yml`  
CD workflow: `.github/workflows/cd.yml`

### CI (tests + build)
- Trigger: `push` to `main` and all `pull_request`s
- Checkout with submodules
- Backend:
  - Install deps: `pip install -e 'rag[dev]'` + `ruff`
  - Lint: `ruff check rag/src --select E9,F63,F7,F82`
  - Unit tests: `make test`
  - Integration tests (TestClient + sqlite): `make test-integration`
- OpenAPI:
  - Validate spec: `npx @apidevtools/swagger-cli validate rag/openapi.yaml`
- Frontend (if `frontend/package.json` exists):
  - `npm ci`
  - `npm run lint`
  - `npm run test`
  - `npm run build`
- Smoke job (after tests):
  - `docker compose up -d api`
  - `/health` check (20 tries)
  - No migrations / no reindex:
    - `RUN_MIGRATIONS=0`
    - `MIGRATE_QDRANT_ON_STARTUP=0`
  - Dummy BGE env for startup:
    - `BGE_BASE_URL=http://localhost:9999`

### CD (Amvera)
- Trigger: manual (`workflow_dispatch`) or `push` to `main`
- Uses Amvera CLI (v1.0.6)
- Deploys project: `rag-bitrix`
- Runs `/health` smoke check after rebuild
- Retries rebuild on 409 (build already in progress) and skips after max attempts

### Required secrets (GitHub Actions)
- `AMVERA_USERNAME`
- `AMVERA_PASSWORD`
- `AMVERA_HEALTH_URL`

---

## 12) Reproducibility

Local run:
```bash
make up
make ingest
```

Demo ingest (manual, for debugging):
```bash
make ingest-demo
```

---

## Additional

Full RAG documentation:
- `rag/README.md`
- `docs/RAG/` (plan, parameters, tests, risks)

Single entry point for Bitrix documentation:
- `docs/MAIN_INDEX.md`

---
