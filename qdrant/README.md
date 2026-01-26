# Qdrant (Amvera) — отдельное приложение

В этом репозитории основной `amvera.yaml` относится к backend‑API, поэтому для Qdrant вынесен отдельный конфиг: `qdrant/amvera.yaml`.

## Деплой в Amvera

Рекомендуемый вариант: создать **отдельный репозиторий** для Qdrant (или отдельную ветку), куда положить:
- `qdrant/amvera.yaml` как `amvera.yaml` в корень
- `qdrant/Dockerfile` как `Dockerfile` в корень

И запустить новый проект в Amvera из этого репозитория.

Если Amvera UI позволяет указать путь до Dockerfile/конфига в текущем репозитории, используйте:
- Dockerfile: `qdrant/Dockerfile`
- Config: `qdrant/amvera.yaml` (или перенесите/скопируйте в корень репозитория, который деплоите)

## Данные

Для персистентности используется mount в `/qdrant/storage` (см. `persistenceMount`).
Снапшоты складываются в `/qdrant/storage/snapshots` (см. `QDRANT__STORAGE__SNAPSHOTS_PATH` в Dockerfile),
чтобы они тоже попадали в persistent storage.

## Снапшоты > 200MB (ограничение загрузки)

Если платформа ограничивает размер загрузки (например 200MB), снапшот можно порезать на части.

### Нарезка (локально)

```bash
split -b 190m bitrix_docs.snapshot bitrix_docs.snapshot.part-
```

### Куда положить на сервер

Загрузить части в persistent каталог снапшотов (**рекомендуется**):

`/qdrant/storage/snapshots/`

Также допускается загрузить части прямо в корень persistent storage:

`/qdrant/storage/`

Например:

```
/qdrant/storage/snapshots/bitrix_docs-20260123-193108.snapshot.part-aa
/qdrant/storage/snapshots/bitrix_docs-20260123-193108.snapshot.part-ab
...
```

### Автосборка

В образе используется `qdrant/entrypoint.sh`: при старте контейнера он автоматически собирает
`*.snapshot.part-*` в итоговый `*.snapshot` (если его ещё нет) в каталоге снапшотов.
Если части загружены в `/qdrant/storage/`, entrypoint переместит их в каталог снапшотов и затем соберёт.

## Автоскачивание и авто‑recover (опционально)

Если нужно, контейнер умеет **сам скачать** части снапшота по HTTP и **выполнить recover**.

Переменные окружения:
- `SNAPSHOT_BASE_URL` — базовый URL (например, `https://.../qdrant`)
- `SNAPSHOT_PARTS` — список частей через запятую
- `SNAPSHOT_FILENAME` — итоговый файл снапшота
- `QDRANT_COLLECTION` — имя коллекции (по умолчанию `bitrix_docs`)
- `SNAPSHOT_RECOVER_ON_STARTUP=1` — включить авто‑recover

Пример:

```
SNAPSHOT_BASE_URL=https://<ngrok-host>.ngrok-free.app
SNAPSHOT_PARTS=bitrix_docs-20260123-193108.snapshot.part-aa,bitrix_docs-20260123-193108.snapshot.part-ab,bitrix_docs-20260123-193108.snapshot.part-ac,bitrix_docs-20260123-193108.snapshot.part-ad
SNAPSHOT_FILENAME=bitrix_docs-20260123-193108.snapshot
QDRANT_COLLECTION=bitrix_docs
SNAPSHOT_RECOVER_ON_STARTUP=1
```

Логи: при старте контейнера будет подробный вывод о скачивании, сборке и recover.
