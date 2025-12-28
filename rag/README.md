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
- Публичный API (ngrok): `./scripts/run_with_ngrok.sh`

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
./scripts/run_with_ngrok.sh
```

Дальше: индексация и API будут развиваться по плану в `../docs/RAG/RAG_PLAN.md`.

## Конфигурация (.env)

Файл `.env` не коммитится. Основные переменные:

- `VAULT_ROOT=docs` — путь к vault
- `RAG_DATA_DIR=.rag` — локальные артефакты индекса
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
- `NGROK_AUTH_TOKEN=...` (для публичного API через ngrok)
- `RAG_EMBED_BATCH=4`
- `RAG_MAX_LATENCY_S=25`
- `RAG_FAST_REST=1` (быстрый режим для REST: без vector/rerank/LLM)

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

## Индексация

Индексация создаёт файлы в `.rag/`:
- `chunks.jsonl` — чанки и метаданные
- `bm25.json` — индекс BM25
- `embedding_cache.jsonl` — кеш эмбеддингов

Qdrant коллекция: `bitrix_docs`.

## Тестирование

Тест‑набор: `../docs/RAG/RAG_TEST_SET.md`  
Отчёт (пример): `../docs/RAG/RAG_TEST_REPORT_FULL.csv`

## Типичные проблемы

- Qdrant не доступен: проверь `docker compose up -d`, URL и порт `6333`.
- Rerank/Embed дают 4xx/5xx: проверь `BGE_BASE_URL` и ключ.
- LLM ошибки: проверь `OPENAI_MODEL` и `OPENAI_API_KEY`.
- Медленная индексация: уменьшай `RAG_EMBED_BATCH`.

## Остановка

```bash
docker compose down
```
