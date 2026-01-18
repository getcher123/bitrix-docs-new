# Amvera: деплой и управление проектом `rag-bitrix`

Этот документ — краткая шпаргалка по CLI Amvera для деплоя RAG‑сервиса и фронтенда.

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

## PostgreSQL (опционально)

Если решим использовать managed PostgreSQL вместо контейнера:

```bash
amvera create postgresql
amvera get psql
amvera describe postgresql --slug <psql-slug>
```

Бэкапы:

```bash
amvera psql backup list --slug <psql-slug>
amvera psql backup create --slug <psql-slug>
amvera psql backup delete --slug <psql-slug>
amvera psql restore --slug <psql-slug>
```

## Troubleshooting

- Если `amvera get projects` или `amvera describe project --slug rag-bitrix` возвращают `404`, значит:
  - slug отличается (нужно уточнить точное имя проекта), или
  - проект в другой организации/аккаунте.

В таком случае пришли **точный slug** или скрин списка проектов в Amvera.
