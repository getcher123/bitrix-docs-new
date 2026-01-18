# Bitrix24 REST API

Раздел про REST API для Bitrix24 (облачная версия).

## Основная документация (офлайн‑копия)

- [Документация Bitrix24 REST API (b24-rest-docs)](./b24-rest-docs/index.md) — импорт официального репозитория.
- [Локальные интеграции (apidocs)](./local-integrations/index.md) — раздел про локальные интеграции (вебхуки/локальные приложения).

## Быстрый поиск по методам

```bash
# Пример: найти описание метода
rg -n \"\\bcrm\\.lead\\.add\\b\" docs/bitrix24_api/

# Пример: найти событие/вебхук
rg -n \"\\bOnAppInstall\\b|\\bOnAppUninstall\\b\" docs/bitrix24_api/
```

Если нужен поиск по конкретному методу в VS Code/Obsidian — используйте глобальный поиск по vault (`Ctrl+Shift+F`).

## Обновление снимка (опционально)

Если нужно подтянуть свежую версию из GitHub:

```bash
./scripts/update_b24_rest_docs.sh
python3 scripts/vault_maintenance.py --index-only
```

Текущий зафиксированный коммит upstream хранится в `docs/bitrix24_api/b24-rest-docs/UPSTREAM.md`.

<!-- vault-nav:start -->
## В этой папке

<details>
<summary>Показать файлы и папки</summary>

### Папки

- [Документация Bitrix24 REST API (b24-rest-docs)](b24-rest-docs/index.md)
- [Обзор инструментов для локальных интеграций](local-integrations/index.md)

</details>

<!-- vault-nav:end -->
