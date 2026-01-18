# Структура проекта RAG (предлагаемая)

Цель — отделить:
- **vault‑контент** (в `docs/`, `images/`) от
- **кода RAG** (в `rag/`) и
- **runtime‑артефактов** (индексы/кеши в `.rag/` или `rag_data/`, не коммитятся).

## Где что лежит

- Документация по проекту RAG (в `docs/RAG/`):
  - `docs/RAG/RAG_PLAN.md` — план и чекбоксы прогресса
  - `docs/RAG/RAG_PARAMETERS.md` — параметры и стек (в т.ч. Colab endpoints)
  - `docs/RAG/RAG_RISKS.md` — риски и минимизация
  - `docs/RAG/RAG_ACCEPTANCE.md` — критерии тестирования/приемки
  - `docs/RAG/RAG_TEST_SET.md` — контрольные вопросы с эталонными ссылками
  - `docs/RAG/RAG_EVAL_REPORT.csv` — отчет по recall/MRR
  - `docs/RAG/RAG_EVAL_SUMMARY.md` — краткая сводка метрик
  - `docs/RAG/RAG_QUESTIONNAIRE.md` — ответы на вводные вопросы (настроечный “источник правды”)
  - `docs/RAG/RAG_PROJECT_STRUCTURE.md` — структура проекта RAG (куда класть код/данные)
  - `docs/RAG/RAG_UPDATE_PROCESS.md` — как обновлять индексы
  - `docs/RAG/RAG_REGRESSION_PLAN.md` — регресс‑план и проверки

- Код и инфраструктура RAG: `rag/`

## Дерево `rag/`

```
rag/
  README.md                 # как запустить/обновить (MVP)
  pyproject.toml            # зависимости и tooling
  .env.example              # шаблон переменных окружения
  docker-compose.yml        # локальная Qdrant (опционально)
  src/bitrix_rag/
    config.py               # конфигурация из env (BGE/OpenAI/Qdrant)
    ingest/                 # загрузка/очистка/чанкинг Markdown
    clients/                # клиенты к внешним сервисам (BGE endpoints, OpenAI)
    index/                  # построение/обновление индексов (vector + bm25)
    retrieval/              # роутинг, гибридный retrieval, rerank
    api/                    # FastAPI (/health, /search, /answer)
    cli.py                  # CLI для индексации и запросов (MVP)
```

## Runtime‑данные (не коммитятся)

- `.rag/` или `rag_data/` — кеш эмбеддингов, промежуточные jsonl, артефакты индексации.

Исключения уже добавлены в `.gitignore`.
