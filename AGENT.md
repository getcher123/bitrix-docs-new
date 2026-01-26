# AGENT.md - guidelines for autonomous development (Zoomcamp project)

This document is for the agent/developer implementing tasks from `TODO-CRITERIAS.md`.

## Sources of truth

- Criteria plan: `TODO-CRITERIAS.md` (main progress checklist)
- RAG docs: `docs/RAG/` (parameters, risks, acceptance, test set, Amvera deploy)
- Bitrix vault search guide: `docs/AGENT.md`
- Backend (API/RAG): `rag/`
- Frontend (submodule): `frontend/` (repo `bitrix-scribe`)

## Mandatory autonomy rule (important)

If a step requires user actions/answers (access, tokens, Amvera/GitHub settings, UI choices, etc.):

1) **Do not stop** all work - continue with other independent tasks.
2) Mark the blocked step in `TODO-CRITERIAS.md` as: **"waiting for user"**.
3) Return to it after receiving the required info.

Recommended marker format:

```md
- [ ] (waiting for user) <step description> - need: <what exactly is needed>
```

## Minimum tools (must-have)

- `git` (submodules required)
- Python **3.10+** + `pip` (backend)
- Node.js **18+** + package manager (`npm`/`pnpm`/`bun`) (frontend)
- Docker + Docker Compose (local run / CI integration tests)
- Amvera CLI (`amvera`) for deploy (see `docs/RAG/AMVERA_DEPLOY.md`)

Optional (speeds up work): `rg` (ripgrep) for vault search.

## Code change rules

- Follow the contract: `rag/openapi.yaml` is the **source of truth** for the API.
- Do not commit secrets: `.env`, tokens, API keys. Check `.gitignore`.
- Keep changes minimal and focused (one logical change at a time).
- After changes, run local checks at minimum:
  - backend: unit tests / lint (if available)
  - frontend: `lint` + smoke (dev build)
- Always update `TODO-CRITERIAS.md` checkboxes after completion.

## Workflow

- Before a task: check `TODO-CRITERIAS.md` and current blockers.
- During a task: make small patches, do not mix topics.
- After a task: update checkboxes, add notes about risks/blockers.
- If a step needs external actions - mark it as **"waiting for user"**.

## How we used AI tools

- Search code/docs (rg/CLI) to understand structure.
- Generate drafts (README/architecture/instructions) with manual review.
- Diagnose build/deploy errors from logs.
- Constraints: do not expose secrets, do not invent sources, verify facts.

## Submodule `frontend/` (important for deploy)

- After `git clone` run:

```bash
git submodule update --init --recursive
```

- Frontend changes are **committed inside** `frontend/` as a separate repo. Then the main repo commits the updated submodule pointer.

## Deploy to Amvera (short)

- Amvera project: `rag-bitrix`
- Current state and commands: `docs/RAG/AMVERA_DEPLOY.md`

Amvera has no native docker-compose: deploy via `Dockerfile` + `amvera.yml` and managed services (e.g., Postgres). `docker compose` is used locally and in CI for integration tests.
