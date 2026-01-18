# RAG сервис для Bitrix Markdown‑vault

Этот каталог содержит код RAG‑системы для работы с локальным vault в `../docs/`.

Документация проекта:
- `../docs/RAG/RAG_PLAN.md`
- `../docs/RAG/RAG_PARAMETERS.md`
- `../docs/RAG/RAG_RISKS.md`
- `../docs/RAG/RAG_ACCEPTANCE.md`
- `../docs/RAG/RAG_TEST_SET.md`
- `../docs/RAG/RAG_QUESTIONNAIRE.md`

## Требования

- Python 3.10+
- Docker Desktop (для Qdrant) или локальный Qdrant binary
- Доступ к BGE endpoints (Colab/ngrok)
- OpenAI API key (для генерации ответа; без него будет extractive‑режим)

## Быстрый обзор

- Индексация: `bitrix-rag --env-file .env index`
- Поиск: `bitrix-rag --env-file .env search "запрос"`
- Ответ: `bitrix-rag --env-file .env answer "запрос"`
- API: `uvicorn bitrix_rag.api.main:app --host 0.0.0.0 --port 8000`
- Публичный API (ngrok): `./scripts/run_with_ngrok.sh run`

## Frontend

Продовый фронтенд подключен как git submodule в `../frontend/`.

Если после `git clone` папка `frontend/` пустая:

```bash
git submodule update --init --recursive
```

## Быстрый запуск (MVP)

1) Поднять Qdrant (если используем):

```bash
docker compose up -d
```

2) Заполнить `.env` по шаблону:

```bash
cp .env.example .env
```

3) Установить зависимости:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

4) Собрать индекс:

```bash
bitrix-rag --env-file .env index
```

5) Запустить API:

```bash
uvicorn bitrix_rag.api.main:app --host 0.0.0.0 --port 8000
```

Проверка:

```bash
curl -s http://localhost:8000/health
```

Опционально: запустить API с публичным ngrok‑endpoint:

```bash
chmod +x ./scripts/run_with_ngrok.sh
./scripts/run_with_ngrok.sh run
```

Дальше: индексация и API будут развиваться по плану в `../docs/RAG/RAG_PLAN.md`.

## Конфигурация (.env)

Файл `.env` не коммитится. Основные переменные:

- `VAULT_ROOT=docs` — путь к vault
- `RAG_DATA_DIR=.rag` — локальные артефакты индекса
- `DATABASE_URL=sqlite:///./.rag/app.db` (dev) или `postgresql+psycopg://...` (prod)
- `VECTOR_BACKEND=pgvector` (Postgres+pgvector) или `qdrant` (Qdrant), либо пусто (авто)
- `QDRANT_URL=http://localhost:6333`
- `QDRANT_COLLECTION=bitrix_docs`
- `BGE_PROVIDER=deepinfra` или `colab`
- DeepInfra:
  - `DEEPINFRA_BASE_URL=https://api.deepinfra.com/v1/inference`
  - `DEEPINFRA_EMBED_PATH=/BAAI/bge-m3`
  - `DEEPINFRA_RERANK_PATH=/Qwen/Qwen3-Reranker-0.6B`
  - `DEEPINFRA_KEY=...`
- Colab/ngrok:
  - `COLAB_BASE_URL=https://<ngrok>.app`
  - `COLAB_EMBED_PATH=/embed`
  - `COLAB_RERANK_PATH=/rerank`
  - `COLAB_API_KEY=...`
- `OPENAI_API_KEY=...`
- `OPENAI_MODEL=gpt-5.2`
- `OPENAI_TIMEOUT_S=20`
- `OPENAI_MAX_OUTPUT_TOKENS=800`
- `NGROK_AUTH_TOKEN=...` (для публичного API через ngrok)
- `RAG_EMBED_BATCH=4`
- `RAG_MAX_LATENCY_S=25`
- `RAG_FAST_REST=1` (быстрый режим для REST: без vector/rerank/LLM)

## Миграции (Alembic)

Для PostgreSQL (prod) применить миграции:

```bash
alembic -c alembic.ini upgrade head
```

Для SQLite (dev) таблицы создаются автоматически при старте API.

## История запросов

API сохраняет историю запросов/ответов в БД:
- `queries` — запрос, режим, латентность, ошибки
- `answers` — текст ответа, модель, sources JSON
- `feedback` — оценка/комментарий пользователя (позже подключим UI)

## API endpoints

- `GET /health` — состояние и конфиг
- `POST /search` — топ‑результаты
- `POST /answer` — ответ + источники
- `GET /openapi.json` — OpenAPI схема

Пример:

```bash
curl -s -X POST http://localhost:8000/answer \
  -H 'Content-Type: application/json' \
  -d '{"query":"Как получить список элементов инфоблока через CIBlockElement::GetList"}'
```

## OpenAPI и debug UI

- Статическая OpenAPI спецификация: `openapi.yaml`
- Фронт‑заглушка для отладки: `debug_frontend/index.html`

Запуск:

1) Запусти API (`uvicorn ...` или `./scripts/run_with_ngrok.sh run`).
2) Открой `http://localhost:8000/debug` (или `${ngrok_url}/debug`).
3) Проверь `POST /answer` или `POST /search`.

## Индексация

Индексация создаёт файлы в `.rag/`:
- `chunks.jsonl` — чанки и метаданные
- `bm25.json` — индекс BM25
- `embedding_cache.jsonl` — кеш эмбеддингов
- `index_manifest.json` — mtime/size для инкрементальных обновлений
- `index_version.json` — версия индекса (git commit + timestamp)

Qdrant коллекция: `bitrix_docs`.

Инкрементальная индексация:

```bash
bitrix-rag --env-file .env index --incremental --strategy auto
```

Стратегии: `auto` (git→mtime), `git`, `mtime`.

## Тестирование

Тест‑набор: `../docs/RAG/RAG_TEST_SET.md`  
Отчёт (пример): `../docs/RAG/RAG_TEST_REPORT_FULL.csv`

Оценка recall/MRR:

```bash
python3 scripts/eval_test_set.py --env-file .env --top-k 10 --out ../docs/RAG/RAG_EVAL_REPORT.csv
```

## Типичные проблемы

- Qdrant не доступен: проверь `docker compose up -d`, URL и порт `6333`.
- Rerank/Embed дают 4xx/5xx: проверь `BGE_BASE_URL` и ключ.
- LLM ошибки: проверь `OPENAI_MODEL` и `OPENAI_API_KEY`.
- Медленная индексация: уменьшай `RAG_EMBED_BATCH`.
- Логи запросов: `.rag/requests.log` (JSONL, включает timings).

## Остановка

```bash
docker compose down
```
