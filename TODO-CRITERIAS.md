# TODO by project criteria (DataTalksClub AI Dev Tools Zoomcamp)

Goal: close **all 12 criteria** (max points), based on the decisions made:

- Repository is public and includes full `docs/` (personal project). (Q1 updated)
- Deploy: **Amvera Cloud** (Dockerfile + `amvera.yml` + managed services; `docker compose` - local/CI). (Q2=A)
- Audience: **mixed** (admins + developers). (Q3=C)
- Public access **without auth** (but with technical protections). (Q4=C)
- DB: **Postgres (prod) + SQLite (dev/test)**; vectors in Postgres via **pgvector** (Qdrant optional). (Q5=A)
- Frontend: **React+Vite SPA** + tests. (Q6=A)
- OpenAPI: `openapi.yaml` - **contract**, client/types generated from it. (Q7=A)
- CI/CD: tests + deploy to Amvera. (Q8=A)
- MCP: **own MCP server** in repo. (Q9=A)
- Indexing: **incremental + full rebuild on demand**. (Q10=A)
- "No sources" policy: **explicitly say so and provide alternatives without links**. (Q11=A)
- Load: **A** (demo/small prod). (Q12=A)

Links to existing documentation:
- RAG plan: `docs/RAG/RAG_PLAN.md`
- Parameters: `docs/RAG/RAG_PARAMETERS.md`
- Acceptance: `docs/RAG/RAG_ACCEPTANCE.md`
- Risks: `docs/RAG/RAG_RISKS.md`
- Test set: `docs/RAG/RAG_TEST_SET.md`
- Project structure: `docs/RAG/RAG_PROJECT_STRUCTURE.md`

---

## Current infrastructure state (recorded)

**Amvera (project `rag-bitrix`)**
- ID: `119309`
- Status: `RUN_FAILED` (last error: `FileNotFoundError: /app/.rag/requests.log`)
- Instances: `requires=1`, `current=0`
- Tariff (current): `BEGINNER_PLUS` (0.5 CPU / 1 GB RAM / 7 GB SSD)
- Domain (internal): `amvera-getcher-run-rag-bitrix`
- Git clone/remote:
  - `git clone https://git.amvera.ru/getcher/rag-bitrix`
  - `git remote add amvera https://git.amvera.ru/getcher/rag-bitrix`
- Build log (last error):
  - `lstat /workspace/frontend/package.json: no such file or directory`

**Amvera Postgres (managed, pgvector)**
- Current DB: `ps-db2` (`PS-DB2`, `RUNNING`)
- Previous DB: `ps-db` (`PS-DB`, `STOPPED`)
- DB name: `PS-DB`
- Owner: `USER-DB`
- Superuser access: enabled
- Extension `vector` (pgvector): enabled (confirmed by user)
- INTERNAL domains: `amvera-getcher-cnpg-ps-db2-rw` (rw), `amvera-getcher-cnpg-ps-db2-ro` (ro)
- Limits (tariff): 0.5 CPU / 1 GB RAM / 25 GB SSD (`amvera tariff --slug ps-db2`)

**Frontend**
- Connected as submodule: `frontend/`
- Repo: `https://github.com/getcher123/bitrix-scribe.git` (branch `main`)
- Deploy via **GitHub Pages** (separate from backend).
- Needs adjustments to criteria (SPA + tests + unified API client + Ask/History/Eval screens).

---

## Stage 0 - "Repository hygiene" (required before public release)

- [x] Ensure secrets are not committed: `rag/.env`, ngrok tokens, OpenAI/DeepInfra keys.
- [x] Add/verify `.gitignore` for: `.env`, `.rag/`, `rag_data/`, `__pycache__/`, `.venv/`, `node_modules/`, `dist/`.
- [ ] Rotate compromised keys (if they ever appeared in git/logs/chat).
- [x] Document data policy: what is stored, where, how to delete (GDPR-like minimum).

---

## 1) Problem description (README) - 2/2

- [x] In root `README.md` describe: problem, users (admin+dev), constraints (vault not public), expected behavior.
- [x] Add "User stories" (5-8): D7 search, REST search, courses, "no data", "with sources/without".
- [x] Add high-level diagram (1 image or ASCII): Frontend -> API -> Retrieval -> (Postgres+pgvector/DB/LLM).
- [x] "Demo" section: prod URL (Amvera) + how to reproduce locally.
  - URL: `https://rag-bitrix-getcher.amvera.io/`

**Readiness criteria**
- README explains "what it is" in 1 minute of reading + includes a working demo URL.

---

## 2) AI system development (tools, workflow, MCP) - 2/2

- [x] In `AGENT.md` (and/or `docs/`) describe dev workflow (tools, prompts, rules, how to update plan).
- [x] Add "How we used AI tools": what tasks, what rules, what limitations.
- [x] Implement **MCP server** in repo: `mcp/` (or `rag/mcp/`) with tools:
  - [x] `search_docs(query, top_k, filters)`
  - [x] `answer(query, mode?)`
  - [x] `get_source(path)` (return a specific chunk/page)
- [x] MCP connection docs (VS Code / Claude Desktop / Codex): where config lives, how to run.
- [x] Add minimal MCP tests (smoke): run + call 2-3 tools.

**Readiness criteria**
- Repo contains a real MCP server + instructions + usage demo.

---

## 3) Technologies & architecture - 2/2

- [x] In `README.md` or `docs/ARCHITECTURE.md` describe stack:
  - Frontend: React+Vite
  - Backend: FastAPI
  - Vector DB: Postgres + pgvector (prod), Qdrant (optional)
  - DB: Postgres/SQLite (SQLAlchemy)
  - LLM: OpenAI (Responses API for `gpt-5.*`)
  - Embeddings/Rerank: provider (DeepInfra/Colab) and limitations
  - Infra: docker compose + Amvera + CI/CD
- [x] Describe data flow: ingestion -> chunking -> embed -> upsert -> retrieval -> rerank -> prompt -> answer.
- [x] Describe observability: logs, latency metrics, step tracing.

---

## 4) Front-end - 3/3

- [x] Create `frontend/` (React+Vite) with a single API client module:
  - [x] "Ask" screen: question -> answer + sources (only after statements).
  - [x] "History" screen: latest queries/answers (from DB).
  - [x] "Eval/Smoke" screen: run test set + results table.
- [x] Add UI settings: base URL (local/prod), timeout, mode (llm/extractive/auto).
- [x] Add frontend unit tests (Vitest): API client, sources parsing, error display.
- [x] Add e2e (Playwright): "ask -> answer -> sources".

---

## 5) API contract (OpenAPI) - 2/2

- [x] Align `rag/openapi.yaml` to actual API (or vice versa).
- [x] Generate frontend client from OpenAPI (e.g., `openapi-typescript` + fetch wrapper).
- [x] Add CI check: OpenAPI not broken (lint/validate).
- [x] Document API versioning (semver/changes).

---

## 6) Back-end - 3/3

- [x] Align `rag/src/bitrix_rag` to clean layers: `api/`, `retrieval/`, `clients/`, `db/`, `ingest/`, `eval/`.
- [x] Add backend tests:
  - [x] unit: router/filters/sources formatting
  - [x] unit: OpenAI client (mock)
  - [x] unit: embed/rerank clients (mock)
  - [x] integration: FastAPI `/answer` (TestClient) + sqlite/postgres
- [x] Enforce SLA/timeouts: `RAG_MAX_LATENCY_S`, `OPENAI_TIMEOUT_S`, per-step timeouts.
- [x] Single response format: `answer` without "sources:" text; sources in `sources` array (and/or `citations`).

---

## 7) Database integration - 2/2

- [x] Add DB layer (SQLAlchemy):
  - [x] table `queries` (query, mode, latency_ms, error, created_at)
  - [x] table `answers` (answer_text, model, tokens, sources_json)
  - [x] table `feedback` (rating, comment)
- [x] Add vector store in Postgres (pgvector):
  - [x] `CREATE EXTENSION IF NOT EXISTS vector;`
  - [x] table `embeddings` (`chunk_id`, `path`, `section`, `embedding vector(1024)`, ...)
  - [x] vector index (HNSW/IVFFLAT) + update strategy
- [x] `/health` check: DB accessible, pgvector enabled.
- [x] Env config:
  - [x] `DATABASE_URL=sqlite:///...` for dev/test
  - [x] `DATABASE_URL=postgresql+psycopg://...` for prod
- [x] Migrations (Alembic) + init/upgrade.
- [x] Docs: where to view history, how to clean.

---

## 8) Containerization - 2/2

- [x] `docker-compose.yml` for local full stack: `api`, `postgres(+pgvector)`, `frontend` (nginx).
- [x] `amvera.yml` for Amvera deploy (Dockerfile + managed services).
- [ ] (waiting for user) `Dockerfile` (prod) - build backend + embed frontend (or separate container if Amvera supports). Currently backend-only deploy.
- [x] `make up/down/logs/test` (or `justfile`) for convenience.
- [x] One-command local run per README.

---

## 9) Integration testing - 2/2

- [x] Separate integration tests (pytest marker `integration`):
  - [x] use FastAPI TestClient + sqlite (no docker)
  - [x] cover answer, search, history
- [x] Run report (CSV/JSON) with latency and flags (answer_has_sources, exact/whitelist).
- [x] Docs: how to run locally and in CI.

---

## 10) Deployment - 2/2

- [x] "How we deploy on Amvera" (infra-as-doc):
  - [x] env variables
  - [x] managed Postgres (pgvector): rw/ro + `DATABASE_URL`
  - [x] healthchecks
  - [x] external domain/public URL (for demo/peer-review)
- [ ] (optional) Run Qdrant as a separate Amvera project/service and connect via internal network (`QDRANT_URL`) if pgvector is not sufficient.
- [x] Provide working prod URL (README) + proof (deploy log/screenshot).
- [x] Smoke endpoint: `/health` + build git sha.

---

## 11) CI/CD - 2/2

- [x] CI: unit/integration tests, OpenAPI validation.
- [x] CD: deploy job to Amvera (GitHub Actions), then `/health` smoke.
- [x] Badges in README.

---

## 12) Reproducibility - 2/2

- [x] One-command local start: `make up` or `docker compose up -d`.
- [x] One-command tests: `make test` (unit) and `make test-integration`.
- [x] One-command ingestion: `make ingest` (for `docs/`).
- [x] Optional for faster CI: `demo_vault/` (20-50 files) + `make ingest-demo`.

---

## Recommended minimum tariff (from provided plans)

For chosen architecture (API + Postgres/pgvector + frontend; embeddings/rerank external) and load A:

- [ ] (waiting for user) Tariff decision: **do not upgrade** (stay on `BEGINNER_PLUS`).

---

## Suggested execution order

1) Stage 0 (secrets/cleanliness) -> 2) Docker-compose full stack -> 3) DB layer + migrations -> 4) Frontend SPA + OpenAPI client -> 5) CI (unit) -> 6) Integration tests -> 7) CD deploy Amvera -> 8) MCP server + docs -> 9) Final README/Architecture polish.

---

## Survey results (Amvera/Deploy)

- Deploy format (Amvera): single project (Dockerfile) = **backend**; frontend - **GitHub Pages**.
- Frontend submodule: `bitrix-scribe` is public and used via HTTPS URL in `.gitmodules`.
- Demo/peer-review: external URL `https://rag-bitrix-getcher.amvera.io/`.
- Data: publish full `docs/` (no separate demo dataset).
- Embeddings/rerank (prod): cloud provider (DeepInfra) + keys in Amvera env.
- CD: GitHub Actions pushes to Amvera git remote and triggers build/deploy.
