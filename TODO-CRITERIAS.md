# TODO по критериям проекта (DataTalksClub AI Dev Tools Zoomcamp)

Цель: закрыть **все 12 критериев** (максимальные баллы), с учетом принятых решений:

- Репозиторий публичный, **без полного vault**; в репо только код + **demo‑датасет** + скрипты импорта. (Q1=A)
- Деплой: **Amvera Cloud**, запуск всей системы через **docker compose**. (Q2=A)
- Аудитория: **смешанная** (админы + разработчики). (Q3=C)
- Публичный доступ **без авторизации** (но с тех. защитами). (Q4=C)
- DB: **Postgres (prod) + SQLite (dev/test)** + Qdrant. (Q5=A)
- Frontend: **React+Vite SPA** + тесты. (Q6=A)
- OpenAPI: `openapi.yaml` — **контракт**, из него генерируем клиент/типы. (Q7=A)
- CI/CD: тесты + деплой на Amvera. (Q8=A)
- MCP: **свой MCP server** в репо. (Q9=A)
- Индексация: **incremental + full rebuild по команде**. (Q10=A)
- Политика “нет источников”: **явно говорить и давать альтернативы без ссылок**. (Q11=A)
- Нагрузка: **A** (демо/малый прод). (Q12=A)

Ссылки на существующую документацию:
- План RAG: `docs/RAG/RAG_PLAN.md`
- Параметры: `docs/RAG/RAG_PARAMETERS.md`
- Критерии приемки: `docs/RAG/RAG_ACCEPTANCE.md`
- Риски: `docs/RAG/RAG_RISKS.md`
- Тест‑набор: `docs/RAG/RAG_TEST_SET.md`
- Структура проекта: `docs/RAG/RAG_PROJECT_STRUCTURE.md`

---

## Текущее состояние инфраструктуры (зафиксировано)

**Amvera (проект `rag-bitrix`)**
- ID: `119309`
- Status: `BUILD_FAILED` (сообщение: `Project failed to build`)
- Instances: `requires=1`, `current=0`
- Tariff (текущий): `BEGINNER_PLUS` (0.5 CPU / 1 GB RAM / 7 GB SSD)
- Domain (internal): `amvera-getcher-run-rag-bitrix`
- Git clone/remote:
  - `git clone https://git.amvera.ru/getcher/rag-bitrix`
  - `git remote add amvera https://git.amvera.ru/getcher/rag-bitrix`
- Build log (ключевая ошибка):
  - `error resolving dockerfile path: please provide a valid path to a Dockerfile within the build context with --dockerfile`

**Frontend**
- Подключен как submodule: `frontend/`
- Репозиторий: `git@github.com:getcher123/bitrix-scribe.git` (branch `main`)
- Участвует в деплое (Amvera) как frontend‑часть проекта.
- Требует доработки под критерии (SPA + тесты + единый API‑клиент + экраны Ask/History/Eval).

---

## Этап 0 — “Гигиена репозитория” (обязательное до публичного релиза)

- [ ] Убедиться, что секреты не закоммичены: `rag/.env`, токены ngrok, ключи OpenAI/DeepInfra.
- [ ] Добавить/проверить `.gitignore` для: `.env`, `.rag/`, `rag_data/`, `__pycache__/`, `.venv/`, `node_modules/`, `dist/`.
- [ ] Ротация скомпрометированных ключей (если когда-либо попадали в git/логи/чат).
- [ ] Описать политику данных: что хранится, где, как удалить (GDPR‑подобный минимум).

---

## 1) Problem description (README) — 2/2

- [ ] В корневом `README.md` описать: проблему, пользователей (админ+dev), ограничения (vault не публичный), expected behavior.
- [ ] Добавить “User stories” (5–8 штук): поиск по D7, по REST, по курсам, “нет данных в базе”, “с источниками/без”.
- [ ] Добавить схему high-level (1 картинка или ASCII): Frontend → API → Retrieval → (Qdrant/DB/LLM).
- [ ] Раздел “Demo”: ссылка на прод‑URL (Amvera) + как воспроизвести локально.

**Критерий готовности**
- README объясняет “что это” за 1 минуту чтения + есть ссылка на рабочий демо‑URL.

---

## 2) AI system development (tools, workflow, MCP) — 2/2

- [ ] В `AGENT.md` (и/или `docs/`) описать workflow разработки (инструменты, промпты, правила, как обновлять план).
- [ ] Добавить “How we used AI tools”: какие задачи, какие правила, какие ограничения.
- [ ] Реализовать **MCP server** в репо: `mcp/` (или `rag/mcp/`) с инструментами:
  - [ ] `search_docs(query, top_k, filters)`
  - [ ] `answer(query, mode?)`
  - [ ] `get_source(path)` (для выдачи конкретного чанка/страницы)
- [ ] Документация подключения MCP (VS Code / Claude Desktop / Codex): где конфиг, как запускать.
- [ ] Добавить минимальные тесты MCP (smoke): запуск, вызов 2–3 инструментов.

**Критерий готовности**
- В репо есть реальный MCP server + инструкции + демонстрация использования.

---

## 3) Technologies & architecture — 2/2

- [ ] В `README.md` или `docs/ARCHITECTURE.md` описать стек:
  - Frontend: React+Vite
  - Backend: FastAPI
  - Vector DB: Qdrant
  - DB: Postgres/SQLite (SQLAlchemy)
  - LLM: OpenAI (Responses API для `gpt-5.*`)
  - Embeddings/Rerank: выбранный провайдер (DeepInfra/Colab) и ограничения
  - Infra: docker compose + Amvera + CI/CD
- [ ] Описать поток данных: ingestion → chunking → embed → upsert → retrieval → rerank → prompt → answer.
- [ ] Описать observability: логи, метрики латентности, трассировка шагов.

---

## 4) Front-end — 3/3

- [ ] Создать `frontend/` (React+Vite) с единой точкой общения с API (client module):
  - [ ] Экран “Ask”: вопрос → ответ + источники (только после утверждений).
  - [ ] Экран “History”: последние запросы/ответы (из DB).
  - [ ] Экран “Eval/Smoke”: прогон тест‑набора + таблица результатов.
- [ ] Добавить настройки в UI: base URL (локально/прод), таймаут, режим (llm/extractive/auto).
- [ ] Добавить unit‑тесты фронта (Vitest): клиент API, парсинг sources, отображение ошибок.
- [ ] Добавить e2e (Playwright): “задал вопрос → получил ответ → вижу источники”.

---

## 5) API contract (OpenAPI) — 2/2

- [ ] Привести `rag/openapi.yaml` к фактическому API (или наоборот — привести API к контракту).
- [ ] Генерация клиента для фронта из OpenAPI (например, `openapi-typescript` + fetch wrapper).
- [ ] Добавить CI-проверку: OpenAPI не “сломали” (lint/validate).
- [ ] Документировать версии API (semver/changes).

---

## 6) Back-end — 3/3

- [ ] Привести структуру `rag/src/bitrix_rag` к чистым слоям: `api/`, `retrieval/`, `clients/`, `db/`, `ingest/`, `eval/`.
- [ ] Добавить тесты backend:
  - [ ] unit: роутер/фильтры/форматирование sources/citations
  - [ ] unit: OpenAI client (mock)
  - [ ] unit: embed/rerank clients (mock)
  - [ ] integration: FastAPI endpoint `/answer` (TestClient) + sqlite/postgres
- [ ] Гарантировать SLA по таймаутам: `RAG_MAX_LATENCY_S`, `OPENAI_TIMEOUT_S`, per-step timeouts.
- [ ] Единый формат ответа: `answer` без “sources:” текста внутри; источники — в `sources` (и/или отдельный `citations` массив).

---

## 7) Database integration — 2/2

- [ ] Добавить слой DB (SQLAlchemy):
  - [ ] таблица `queries` (query, mode, latency_ms, error, created_at)
  - [ ] таблица `answers` (answer_text, model, tokens, sources_json)
  - [ ] таблица `feedback` (rating, comment)
- [ ] Конфиг окружений:
  - [ ] `DATABASE_URL=sqlite:///...` для dev/test
  - [ ] `DATABASE_URL=postgresql+psycopg://...` для prod
- [ ] Миграции (Alembic) + команда “init/upgrade”.
- [ ] Документация: где посмотреть историю, как чистить.

---

## 8) Containerization — 2/2

- [ ] `docker-compose.yml` для полного стека: `api`, `qdrant`, `postgres`, `frontend` (nginx).
- [ ] `Dockerfile` backend (multi-stage, non-root).
- [ ] `Dockerfile` frontend (build → nginx serve).
- [ ] `make up/down/logs/test` (или `justfile`) для удобства.
- [ ] Локальный запуск “одной командой” согласно README.

---

## 9) Integration testing — 2/2

- [ ] Отдельный набор integration tests (pytest marker `integration`):
  - [ ] поднимает docker compose (qdrant+postgres+api) или использует testcontainers
  - [ ] выполняет 3–5 ключевых сценариев: answer, search, history, eval
- [ ] Отчет по прогону (CSV/JSON) с latency и flags (answer_has_sources, exact/whitelist).
- [ ] Документация: как запускать локально и в CI.

---

## 10) Deployment — 2/2

- [ ] Описать “как деплоим на Amvera” (infra-as-doc):
  - [ ] переменные окружения
  - [ ] volume для Qdrant/DB
  - [ ] healthchecks
  - [ ] домен/URL
- [ ] Дать рабочий прод‑URL (в README) + доказательство (скрин/лог deploy).
- [ ] Smoke endpoint: `/health` + версия сборки (git sha).

---

## 11) CI/CD — 2/2

- [ ] GitHub Actions CI:
  - [ ] lint (python + frontend)
  - [ ] unit tests (backend+frontend)
  - [ ] integration tests (docker compose)
  - [ ] OpenAPI validation
- [ ] CD:
  - [ ] deploy job на Amvera (авто или manual approval)
  - [ ] после деплоя — smoke check `/health`
- [ ] Badge в README (CI status).

---

## 12) Reproducibility — 2/2

- [ ] “One-command” локальный старт: `make up` или `docker compose up -d`.
- [ ] “One-command” тесты: `make test` (unit) и `make test-integration`.
- [ ] “One-command” ingestion (demo vault): `make ingest-demo`.
- [ ] `docs/DEMO_VAULT.md`: что в demo‑датасете, как его обновлять.
- [ ] Отдельный “public demo dataset”: `demo_vault/` (20–50 файлов) без лиценз. рисков.

---

## Рекомендуемый минимальный тариф (из предложенных)

Для выбранной архитектуры (API + Qdrant + Postgres + frontend в одном окружении) и нагрузки A:

- [ ] Выбрать тариф **“Стандартный — 1 CPU, 2.5GB RAM, 15GB SSD”** как минимум.

---

## Порядок выполнения (предлагаемый)

1) Этап 0 (секреты/чистота) → 2) Docker-compose full stack → 3) DB слой + миграции → 4) Frontend SPA + OpenAPI client → 5) CI (unit) → 6) Integration tests → 7) CD deploy Amvera → 8) MCP server + docs → 9) Финальная полировка README/Architecture.
