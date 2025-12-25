# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 31594 — Конфигурация MariaDB](lesson_31594.md)
- [Следующий: 31598 — Конфигурация Push-server →](lesson_31598.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=31596

Работа Push-сервера невозможна без сервиса Redis. Для этого в конфигураторе следует:

- включить файловый сокет для работы,
- отключить сброс данных на диск, поскольку для работы Push-сервера это не требуется,
- установить группу пользователя.

Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/astra.zip). Конфигурационные файлы для Redis расположены в папке astra/redis.

После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/astra.zip

unzip astra.zip

		, выполните команду:

```
rsync -av /opt/astra/redis/redis.conf /etc/redis/redis.conf
```

Настройте права доступа:

```

usermod -g www-data redis
chown -R redis:www-data /etc/redis /var/log/redis /var/lib/redis

[[ ! -d /etc/systemd/system/redis-server.service.d ]] && mkdir /etc/systemd/system/redis-server.service.d
echo -e '[Service]\nGroup=www-data' > /etc/systemd/system/redis-server.service.d/custom.conf
systemctl daemon-reload
```

Запустите сервис Redis:

```
systemctl enable redis-server.service
systemctl restart redis-server.service
```
