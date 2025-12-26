# Документация 1C‑Bitrix (Markdown‑vault)

Это офлайн‑хранилище документации 1C‑Bitrix в виде обычных Markdown‑файлов для просмотра в VS Code/Obsidian (без сборщика сайта).

## Единая точка входа

Начинайте с **[docs/MAIN_INDEX.md](docs/MAIN_INDEX.md)** — это единая навигационная страница по ролям и задачам.

## Быстрый старт (2–3 минуты)

### Visual Studio Code (рекомендуется)

1. Откройте папку репозитория в VS Code
2. Откройте `docs/MAIN_INDEX.md`
3. Нажмите `Ctrl+Shift+V` (предпросмотр)
4. `Ctrl+Click` по ссылкам для навигации
5. `Ctrl+Shift+F` для поиска по vault

### Obsidian

1. `Open folder as vault` → выберите папку репозитория (или только `docs/`)
2. Откройте `docs/MAIN_INDEX.md` (или `MAIN_INDEX.md`, если vault = `docs/`)
3. Используйте глобальный поиск и граф ссылок

## Ключевые страницы (без дублирования навигации)

- `docs/MAIN_INDEX.md` — стартовая навигация (единая точка входа)
- `docs/INDEX.md` — индекс разделов (генерируется, пригоден как «карта»)
- `docs/MODULES.md` — список модулей классического API
- `docs/QUICK_REFERENCE.md` — быстрые ответы/сценарии
- `docs/bitrix24_api/index.md` — Bitrix24 REST API (включая импорт `b24-rest-docs`)
- `docs/AGENT.md` — как AI‑агенту искать справку
- `docs/RAG/` — документация по проекту RAG (план, параметры, риски, тесты)

## Быстрый поиск

```bash
# Поиск по всему хранилищу
rg "CIBlockElement" docs/

# Поиск по заголовкам (класс/метод)
rg "^#\\s+GetList\\b" docs/
```

## RAG‑сервис (опционально)

Код RAG‑системы находится в `rag/`. Инструкции запуска и конфигурации — в:
- `rag/README.md`
- `docs/RAG/RAG_PLAN.md`

## Источники

- https://dev.1c-bitrix.ru/docs/ (документация, классическое API)
- https://dev.1c-bitrix.ru/api_help/ (классическое API: справочник функций/классов)
- https://dev.1c-bitrix.ru/api_d7/ (D7 API)
- https://dev.1c-bitrix.ru/user_help/ (пользовательская документация)
- https://dev.1c-bitrix.ru/learning/ (учебные курсы)
- https://apidocs.bitrix24.ru/ (Bitrix24 REST API)
- https://github.com/bitrix-tools/b24-rest-docs (upstream-репозиторий Bitrix24 REST, импортирован в `docs/bitrix24_api/b24-rest-docs/`)
