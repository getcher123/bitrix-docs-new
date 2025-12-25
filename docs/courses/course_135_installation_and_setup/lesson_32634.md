# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32632 — Конфигурация PostgreSQL](lesson_32632.md)
- [Следующий: 32636 — Конфигурация Push-server →](lesson_32636.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=32634

Работа Push-сервера невозможна без сервиса Redis. Для этого в конфигураторе следует:

- включить файловый сокет для работы,
- отключить сброс данных на диск, поскольку для работы Push-сервера это не требуется,
- установить группу пользователя.

Все конфигурационные файлы [скачайте в архиве](/docs/chm_files/cfg.zip). Файл для Redis `redis.conf`расположен в папке `/cfg/`.

После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/cfg.zip

unzip cfg.zip

		, выполните команду:

```
cp -v /opt/cfg/redis.conf /etc/
```

Настройте права доступа:

```
usermod -g apache redis
chown -R redis:apache /etc/redis.conf /var/log/redis /var/lib/redis
[[ ! -d /etc/systemd/system/redis.service.d ]] && mkdir /etc/systemd/system/redis.service.d
echo -e '[Service]\nGroup=apache' > /etc/systemd/system/redis.service.d/custom.conf
systemctl daemon-reload
```

Запустите сервис Redis:

```
systemctl --now enable redis
```
