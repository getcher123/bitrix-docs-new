# Технические параметры RAG‑системы (рекомендуемые)

Ниже базовый профиль для текущего Markdown‑vault. Значения можно менять после замеров.

## Стек

- Векторная БД: Qdrant 1.x (локально) или pgvector (если нужен один PostgreSQL).
- Поиск BM25: rank‑bm25 или Elasticsearch (при большом числе запросов).
- Embeddings: `bge-m3` (локально) или `text-embedding-3-large` (облако).
- Reranker: `bge-reranker-v2-m3` (локально) или `cohere-rerank` (облако).
- Эндпоинты моделей для индексации: `bge-m3` и `bge-reranker-v2-m3`, развернутые в Google Colab (см. `notebooks/bge_endpoints_colab.ipynb`).
- API: FastAPI + Uvicorn.
- Хранилище метаданных: SQLite/JSONL (для инкрементального индекса).

## Индексация и чанкинг

| Параметр | Значение | Примечание |
| --- | --- | --- |
| Корпус | `docs/**/*.md` | Исключить `scripts/`, `images/`, `.git/`, `docs/RAG/**` |
| Очистка | удалять `vault-nav` блоки | `<!-- vault-nav:start -->…<!-- vault-nav:end -->` |
| Chunk size | 900 токенов | Допустимо 800–1200 |
| Overlap | 150 токенов | Допустимо 120–200 |
| Min chunk | 200 токенов | Мелкие чанки склеивать |
| Разделители | H1 → H2 → H3 | Не разрывать код/таблицы |
| Нормализация | whitespace, невидимые символы | Без изменения смысла |

Примечание по длине чанков при rerank: большинство reranker‑моделей ограничены `max_length` (обычно ~512 токенов). Если чанки существенно длиннее — rerank будет работать по усеченному тексту. Для качества лучше либо уменьшить `Chunk size` (например до 400–500), либо формировать «snippet» для rerank.

## Эмбеддинги

| Параметр | Значение | Примечание |
| --- | --- | --- |
| Модель | `bge-m3` | Русский/английский, технические тексты |
| Размерность | 1024 | Для `bge-m3` |
| Нормализация | `true` | L2‑нормализация векторов |
| Batch size | 16–32 | По памяти |
| Кеш | `sha256(chunk)` → vector | Для инкрементальных обновлений |

## Эндпоинты моделей (Google Colab)

Эндпоинты используются для:
- генерации эмбеддингов при индексации,
- генерации эмбеддингов для запросов,
- rerank top‑k кандидатов.

Рекомендуемая конфигурация через переменные окружения:

| Переменная | Пример | Примечание |
| --- | --- | --- |
| `BGE_BASE_URL` | `https://cc2bb1b6c3b0.ngrok-free.app` | Без завершающего `/` |
| `BGE_EMBED_PATH` | `/embed` | По умолчанию `/embed` |
| `BGE_RERANK_PATH` | `/rerank` | По умолчанию `/rerank` |
| `BGE_HEALTH_PATH` | `/health` | По умолчанию `/health` |
| `BGE_API_KEY` | `<YOUR_KEY>` | Опционально (если включите защиту); не коммитить |
| `BGE_TIMEOUT_S` | `30` | Таймаут HTTP на запрос |
| `BGE_RETRIES` | `3` | Повторы при временных сбоях |

Контракт:

- `POST {BGE_BASE_URL}{BGE_EMBED_PATH}`  
  Request: `{"texts": ["text1", "text2"]}`  
  Response: `{"embeddings": [[...], [...]]}`

- `POST {BGE_BASE_URL}{BGE_RERANK_PATH}`  
  Request: `{"query": "q", "documents": ["d1", "d2"]}`  
  Response: `{"scores": [0.12, 0.87]}`

- `GET {BGE_BASE_URL}{BGE_HEALTH_PATH}`  
  Response (пример): `{"status":"ok","embed_model":"BAAI/bge-m3","rerank_model":"BAAI/bge-reranker-v2-m3","device":"cuda"}`

Если включена защита ключом — использовать заголовок `X-API-Key: <BGE_API_KEY>`.

### Быстрая проверка эндпоинтов

Python (requests):

```python
import requests

url = "https://cc2bb1b6c3b0.ngrok-free.app/embed"
headers = {"X-API-Key": "<BGE_API_KEY>"}
payload = {"texts": ["Hello world"]}
print(requests.post(url, json=payload, headers=headers).json())
```

cURL:

```bash
curl -X POST https://cc2bb1b6c3b0.ngrok-free.app/embed \
  -H 'X-API-Key: <BGE_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{"texts": ["Hello world"]}'
```

## Векторная БД (Qdrant)

| Параметр | Значение | Примечание |
| --- | --- | --- |
| Index | HNSW | По умолчанию |
| M | 16 | Баланс память/качество |
| efConstruction | 200 | Качество индекса |
| efSearch | 64 | Скорость/качество |
| Payload index | `section`, `module`, `course_id`, `lesson_id` | Для фильтрации |

## Гибридный retrieval

| Параметр | Значение | Примечание |
| --- | --- | --- |
| BM25 top‑k | 40 | Лексический поиск |
| Vector top‑k | 40 | Семантический поиск |
| Fusion | RRF | Стандартный merge |
| RRF k | 60 | Стабильность ранжирования |
| Rerank top‑k | 10 | Финальный список |

## Генерация ответа

| Параметр | Значение | Примечание |
| --- | --- | --- |
| Контекст | 6–10 чанков | По важности после rerank |
| Макс. ответ | 500–800 токенов | Для читаемого ответа |
| Temperature | 0.2 | Стабильность |
| Top‑p | 0.9 | Без креативности |
| Цитирование | пути `docs/.../file.md` | Обязательно в ответе |

## Маршрутизация

- `Bitrix\\` → `docs/d7/`
- `crm.`/`tasks.`/`im.` → `docs/bitrix24_api/`
- `урок`, `курс` → `docs/courses/`
- `настройки`, `интерфейс` → `docs/user_help/`

## Инкрементальная индексация

- Источник изменений: `git diff --name-only` или `mtime`.
- Пересчет только изменённых файлов и их чанков.
- Версия индекса: `git rev-parse HEAD`.
