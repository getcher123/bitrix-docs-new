# RAG сервис для Bitrix Markdown‑vault

Этот каталог содержит код RAG‑системы для работы с локальным vault в `../docs/`.

Документация проекта:
- `../docs/RAG_PLAN.md`
- `../docs/RAG_PARAMETERS.md`
- `../docs/RAG_RISKS.md`
- `../docs/RAG_ACCEPTANCE.md`
- `../docs/RAG_TEST_SET.md`
- `../docs/RAG_QUESTIONNAIRE.md`

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

Дальше: индексация и API будут добавляться по плану в `../docs/RAG_PLAN.md`.
