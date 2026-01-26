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

Deploy docs: `docs/RAG/AMVERA_DEPLOY.md`

---

## 11) CI/CD

CI workflow: `.github/workflows/ci.yml`  
CD workflow: `.github/workflows/cd.yml`  
Secrets:
- `AMVERA_USERNAME`
- `AMVERA_PASSWORD`
- `AMVERA_HEALTH_URL`

The CI smoke job starts API only (no migrations/indexing):
`RUN_MIGRATIONS=0`, `MIGRATE_QDRANT_ON_STARTUP=0`.

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
