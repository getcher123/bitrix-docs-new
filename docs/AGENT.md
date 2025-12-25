# AGENT.md — как искать справку 1C‑Bitrix в этом Markdown‑vault

Этот репозиторий — офлайн‑копия документации 1C‑Bitrix в виде Markdown. Задача агента: быстро найти релевантные **локальные** страницы (класс/метод/событие/пример) и сослаться на них.

## Единая точка входа

- [MAIN_INDEX.md](./MAIN_INDEX.md) — стартовая навигация (роли/задачи)
- [INDEX.md](./INDEX.md) — справочная «карта» разделов (генерируется)

## Быстро определить «куда смотреть»

- **Классическое API**: классы вида `CUser`, `CIBlockElement`, `CSaleOrder` → `docs/<module>/...` и `docs/main/reference/...`
- **D7**: неймспейсы `Bitrix\\*` → `docs/d7/bitrix/...` (часто файлы `index.php.md`)
- **Bitrix24 REST**: REST‑методы → `docs/bitrix24_api/` (основной массив статей: `docs/bitrix24_api/b24-rest-docs/`)
- **Пользовательская справка**: интерфейс/настройки → `docs/user_help/`
- **Курсы**: уроки/обучение → `docs/courses/`

## Куда идти в первую очередь

1. [MAIN_INDEX.md](./MAIN_INDEX.md) — если запрос «по задаче» (что сделать).
2. [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) — если нужен быстрый рецепт/пример.
3. [MODULES.md](./MODULES.md) — если нужно понять, какой модуль отвечает за сущность.
4. `docs/<module>/index.md` — обзор модуля, ссылки на классы/события/функции.
5. Полнотекстовый поиск по vault (`rg`) — когда известны имена/термины.

## Навигация внутри папок (важно)

Многие `index.md` / `index.php.md` содержат автогенерируемый блок навигации по соседним файлам и подпапкам:

- `<!-- vault-nav:start -->` … `<!-- vault-nav:end -->`
- Заголовок: `## В этой папке`

Если на индексной странице нет «ручных» ссылок на соседние файлы, используйте этот блок — он всегда ведёт на **локальные** страницы.

## Шаблоны путей (эвристики)

### Классическое API (модули)

- Класс: `docs/<module>/classes/<class_slug>/index.md`
- Метод: `docs/<module>/classes/<class_slug>/<method_slug>.md`
- События: `docs/<module>/events/index.md` (и подкаталоги)
- Функции: `docs/<module>/functions/...`

`class_slug` и `method_slug` обычно в нижнем регистре (например `ciblockelement`, `getlist`).

### Классическое API (main/reference)

Часть базовых классов лежит в `docs/main/reference/...`, например:

- `docs/main/reference/cuser/index.md`
- `docs/main/reference/cdbresult/index.md`

### D7

- Обзор: `docs/d7/index.md`
- Дальше: `docs/d7/bitrix/<module>/.../index.php.md` (и соседние `.php.md`)

### Bitrix24 REST

- Точка входа: `docs/bitrix24_api/index.md`
- Официальный импорт (upstream): `docs/bitrix24_api/b24-rest-docs/index.md`
- Методы: `docs/bitrix24_api/b24-rest-docs/api-reference/`
- Туториалы: `docs/bitrix24_api/b24-rest-docs/tutorials/`

## Поиск (предпочтительно `rg`)

Если известен класс/метод/событие — начинайте с заголовков:

```bash
# Класс по заголовку (H1)
rg -n "^#\\s+CIBlockElement\\b" docs/

# Метод по заголовку (H1)
rg -n "^#\\s+GetList\\b" docs/

# Событие
rg -n "\\bOnAfterIBlockElementAdd\\b" docs/
```

Если известен модуль — сузьте область:

```bash
rg -n "^#\\s+CIBlockElement\\b" docs/iblock/
rg -n "\\bCSaleOrder\\b" docs/sale/
rg -n "Bitrix\\\\Main\\\\EventManager" docs/d7/
```

Если известны только слова/синонимы — используйте `-i` и альтернативы:

```bash
rg -ni "корзин|basket" docs/
```

Для REST‑методов удобно искать по полному имени:

```bash
rg -n "\\bcrm\\.lead\\.add\\b" docs/bitrix24_api/
rg -n "\\btasks\\.task\\.add\\b" docs/bitrix24_api/
```

## Рекомендуемый алгоритм ответа

1. Классифицировать запрос (classic/D7/REST/user_help/course).
2. Определить модуль (через `MODULES.md`, `INDEX.md` или поиск).
3. Найти страницу класса (или обзор раздела) и перейти к нужному методу/событию по локальным ссылкам.
4. Извлечь: назначение, параметры, возвращаемое значение, ограничения/версии, пример кода.
5. В ответе всегда указывать путь(и) к локальным файлам, откуда взята информация.

## Если локально «не находится»

- Проверьте альтернативы имён: `index.md` vs `index.php.md`, разные регистры, транслитерации.
- Ищите не только по имени сущности, но и по терминологии из описания/таблицы методов.
- На страницах D7/user_help часто встречается встроенный HTML (таблицы/списки/ссылки) и строка `Источник: ...` — используйте её как подсказку исходного URL.
- Если в тексте встречается исходная ссылка вида `/api_help/...` или `/api_d7/...`, найдите локальный эквивалент поиском; если страницы действительно нет — дайте внешнюю ссылку на `https://dev.1c-bitrix.ru/...` и явно отметьте это.

## Как парсить уроки (курсы) и поддерживать качество

Все команды ниже предполагают запуск из корня репозитория (там, где папки `docs/` и `scripts/`).

### Парсинг/обновление курсов (dev.1c-bitrix.ru/learning)

Скрипт парсинга сам:
- скачивает уроки,
- конвертирует HTML → Markdown,
- скачивает картинки в `images/courses/<COURSE_ID>/`,
- чинит внутренние ссылки уроков на локальные `lesson_<id>.md`,
- пересобирает `docs/courses/<course_...>/index.md` и общий `docs/courses/index.md`.

Команды:

```bash
# (Пере)спарсить курсы по COURSE_ID
python3 scripts/parse_courses.py --course-ids 48,57 --force

# (Пере)спарсить только выбранные уроки по LESSON_ID
python3 scripts/parse_courses.py --course-ids 57 --force --only-lessons 13640,20858
```

Если в уроках обнаружились внешние картинки (например после ручных правок), прогоните:

```bash
python3 scripts/normalize_courses_md.py
```

### Нормализация `*.php.md` (D7/user_help)

Типичный pipeline для «пустых/ломаных» страниц:

```bash
python3 scripts/refetch_empty_php_md.py --scopes d7,user_help
python3 scripts/normalize_php_md.py --scopes d7,user_help
```

### После любых массовых изменений

```bash
python3 scripts/vault_maintenance.py --index-only
python3 scripts/vault_maintenance.py --nav-only
```

Быстрые проверки:

```bash
# Внешние картинки (должно быть 0 для офлайн-vault)
rg -n "!\\[[^\\]]*\\]\\(https?://" docs/
```

## Как добавлять новые источники (общие правила)

1. **Определить формат источника**:
   - «Снимок репозитория» (как `b24-rest-docs`) → импорт в `docs/<section>/...` + `UPSTREAM.md` с commit/URL.
   - HTML‑сайт/раздел → написать/доработать скрипт в `scripts/`, который скачивает страницы и приводит к Markdown‑vault.
2. **Обязательные требования vault**:
   - Картинки: только локально в `images/` (никаких `![](http...)`).
   - Ссылки: относительные внутри `docs/`, без «мертвых» путей; на индексах — ссылки на соседние файлы/папки (в т.ч. через `vault-nav`).
   - Минимум «мусора» парсинга: без обрезков HTML‑шаблонов/скриптов, без навязанных баннеров/меню.
3. **После импорта/парсинга**: пересобрать `docs/INDEX.md` и навигационные блоки (`vault_maintenance.py`), затем проверить поиск по ключевым сущностям (`rg`).
