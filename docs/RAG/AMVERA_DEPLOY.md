# Amvera: деплой и управление проектом `rag-bitrix`

Этот документ — краткая шпаргалка по CLI Amvera для деплоя RAG‑сервиса и фронтенда.

Сейчас деплой в Amvera настроен **только для backend**. Frontend будет добавлен отдельно.

## Установка CLI

Рекомендуемый способ (официальный скрипт):

```bash
curl -sSL https://raw.githubusercontent.com/amvera-cloud/cli/master/amvera-install.sh | bash -s -- v1.0.5
```

Если в системе нет `unzip` (WSL/Ubuntu), можно поставить:

```bash
sudo apt-get update && sudo apt-get install -y unzip
```

Альтернатива без `unzip` (python):

```bash
version=v1.0.5
url="https://github.com/amvera-cloud/cli/releases/download/${version}/amvera-linux.zip"
tmpdir=$(mktemp -d)
curl -sSL -o "$tmpdir/amvera.zip" "$url"
python3 - <<PY
import zipfile, os
zip_path = r"$tmpdir/amvera.zip"
out_dir = r"$tmpdir/extract"
os.makedirs(out_dir, exist_ok=True)
with zipfile.ZipFile(zip_path, "r") as zf:
    zf.extractall(out_dir)
PY
install -m 755 "$tmpdir/extract/amvera" "$HOME/.local/bin/amvera"
```

Проверка версии:

```bash
amvera --version
```

## Логин

```bash
amvera login
amvera whoami
```

## Проекты и описание

Список проектов:

```bash
amvera get projects
```

Описание конкретного проекта:

```bash
amvera describe project --slug rag-bitrix
```

## Текущее состояние проекта `rag-bitrix` (снято через amvera CLI)

- ID: `119309`
- Name: `RAG-Bitrix`
- Slug: `rag-bitrix`
- Status: `BUILD_FAILED` (сообщение: `Project failed to build`)
- Instances: `requires=1`, `current=0`
- Tariff: `BEGINNER_PLUS` (0.5 CPU / 1.0 GB RAM / 7 GB SSD)
- Git clone:
  - `git clone https://git.amvera.ru/getcher/rag-bitrix`
  - `git remote add amvera https://git.amvera.ru/getcher/rag-bitrix`
- Домены:
  - `amvera-getcher-run-rag-bitrix` (INTERNAL, HTTP, active, default)
- Переменные окружения: список пуст (env list не вернул значений)

### Диагностика build failure (последние логи)

Из `amvera logs build --slug rag-bitrix --last 200`:

```
Error: error resolving dockerfile path: please provide a valid path to a Dockerfile within the build context with --dockerfile
```

Вероятная причина: в репозитории нет `Dockerfile` в корне или в Amvera не указан путь к Dockerfile/контекст сборки.
Нужна проверка настроек build‑контекста и расположения Dockerfile.

## Домен и публичный URL

```bash
amvera domain --slug rag-bitrix
```

## GitHub интеграция (webhook)

Если проект разворачивается из GitHub (без `git.amvera.ru`):

1) В Amvera UI откройте раздел интеграции GitHub и включите событие `Push`.
2) Укажите ветку, например `main`.
3) Скопируйте `URL` и `Secret` из Amvera UI.
4) В GitHub: `Settings → Webhooks → Add webhook`:
   - Payload URL: `URL` из Amvera
   - Content type: `application/json`
   - Secret: `Secret` из Amvera
   - Events: `Just the push event`
5) В поле `Token` в Amvera UI вставьте GitHub PAT с доступом **read** к репозиторию
   (и ко всем submodule, если используются).

Если build не стартует — проверьте Deliveries в GitHub Webhooks и логи Amvera.
Если frontend подключен как submodule и не скачан, билд соберется с заглушкой
(`Frontend bundle not found`). В этом случае проверьте доступ PAT к репозиторию submodule
и опцию загрузки submodules в Amvera (если доступна).

## Переменные окружения

Список:

```bash
amvera env --slug rag-bitrix
```

Добавление/обновление (CLI попросит ввести имя и значение):

```bash
amvera env add --slug rag-bitrix
amvera env update --slug rag-bitrix
amvera env delete --slug rag-bitrix
```

## Логи

Логи билда:

```bash
amvera logs build --slug rag-bitrix --last 120
```

Логи запуска:

```bash
amvera logs run --slug rag-bitrix --last 120
```

## Управление процессом

```bash
amvera start --slug rag-bitrix
amvera stop --slug rag-bitrix
amvera restart --slug rag-bitrix
amvera rebuild --slug rag-bitrix
```

## Масштабирование

```bash
amvera scale --slug rag-bitrix --replicas 2
```

## Тариф

```bash
amvera tariff --slug rag-bitrix
amvera tariff update --slug rag-bitrix
```

## PostgreSQL (managed) — текущая БД для проекта

Текущий кластер (создан пользователем):

- Slug: `ps-db2` (name: `PS-DB2`)
- Status: `RUNNING`
- DB name: `PS-DB`
- DB owner: `USER-DB`
- Superuser access: включен
- Лимиты (tariff): 0.5 CPU / 1 GB RAM / 25 GB SSD (`amvera tariff --slug ps-db2`)
- Postgres image (из UI): `harbor.amvera.ru/cnpg/extensions:17.5`
- INTERNAL домены:
  - RW: `amvera-getcher-cnpg-ps-db2-rw`
  - RO: `amvera-getcher-cnpg-ps-db2-ro`

Проверить наличие кластера:

```bash
amvera get psql
amvera describe postgresql --slug ps-db2
```

Бэкапы:

```bash
amvera psql backup list --slug ps-db2
amvera psql backup create --slug ps-db2
amvera psql backup delete --slug ps-db2
amvera psql restore --slug ps-db2
```

### Подключение из `rag-bitrix`

В Amvera сервисы видят друг друга по INTERNAL DNS. Для backend достаточно выставить `DATABASE_URL`
на rw‑endpoint (пароль хранить только в Amvera env, не в git):

```text
DATABASE_URL=postgresql+psycopg://USER-DB:<PASSWORD>@amvera-getcher-cnpg-ps-db2-rw:5432/PS-DB
VECTOR_BACKEND=pgvector
```

Примечание: INTERNAL домены (`...-rw`, `...-ro`) не резолвятся из локальной машины/интернета.
Проверки подключения и расширений выполняйте:
- внутри приложения (например, через `/health`), или
- из контейнера/окружения, запущенного в Amvera.

### Миграции (Alembic)

Перед индексацией и запуском сервиса в prod (Postgres) нужно применить миграции:

```bash
alembic -c rag/alembic.ini upgrade head
```

### pgvector (расширение `vector`)

Расширение `vector` включено пользователем. Для самопроверки в рантайме (или при отладке),
выполнить:

```sql
SELECT extname FROM pg_extension WHERE extname = 'vector';
```

Если нужно включить:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

## Qdrant (опционально): минимальные требования и выбор тарифа

Qdrant не имеет “жёсткого” минимума по CPU/RAM — ресурсы зависят от:
кол-ва векторов, размерности (у нас `1024`), payload, индексов (HNSW), репликации и квантования.

Базовые требования:
- 64‑битная система (x86_64/arm64)
- персистентное хранилище с **POSIX‑совместимой** файловой системой (не NFS/S3)

Практический ориентир по нашему текущему индексу (локально):
- размер вектора: `1024`
- число чанков/векторов: ~`4.4k`
- размер qdrant storage: ~`0.6 GB`

Для отдельного проекта Qdrant в Amvera минимум:
- `0.5 CPU / 1 GB RAM / 7 GB SSD` (на малом индексе)

Рекомендуемый минимум “на рост” (полный `docs/` и HNSW при >10k векторов):
- `1 CPU / 2.5 GB RAM / 15 GB SSD`

## Альтернатива: Postgres + pgvector вместо Qdrant

Если хотим не поднимать отдельный проект Qdrant, можно хранить вектора в managed PostgreSQL
через расширение `pgvector` и делать поиск по косинусной близости из Postgres.

Важно: наличие `pgvector` в managed Postgres нужно **проверить**. Для `ps-db2` — включено пользователем.

Проверка (любой клиент Postgres, где есть доступ к `DATABASE_URL`):

```sql
CREATE EXTENSION IF NOT EXISTS vector;
SELECT extname FROM pg_extension WHERE extname = 'vector';
```

Если `CREATE EXTENSION vector` недоступен — остаёмся на Qdrant.

## Troubleshooting

- Если `amvera get projects` или `amvera describe project --slug rag-bitrix` возвращают `404`, значит:
  - slug отличается (нужно уточнить точное имя проекта), или
  - проект в другой организации/аккаунте.

В таком случае пришли **точный slug** или скрин списка проектов в Amvera.
