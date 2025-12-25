# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 33058 — Конфигурация PostgreSQL](lesson_33058.md)
- [Следующий: 33062 — Конфигурация Push-server →](lesson_33062.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=33060

Работа Push-сервера невозможна без сервиса Redis. Для этого в конфигураторе следует:

- включить файловый сокет для работы,
- отключить сброс данных на диск, поскольку для работы Push-сервера это не требуется,
- установить группу пользователя.

Все конфигурационные файлы [скачайте в архиве](/docs/chm_files/alt.zip). Файлы для Redis расположены в папке `/alt/redis/`.

После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/alt.zip

unzip alt.zip

		, выполните команды:

```
su -
rsync -av /opt/alt/redis/ /etc/redis/
```

Настройте права доступа:

```
su -
usermod -g apache2 _redis
chown -R _redis:apache2 /etc/redis /var/log/redis /var/lib/redis
[[ ! -d /etc/systemd/system/redis.service.d ]] && mkdir /etc/systemd/system/redis.service.d
echo -e '[Service]\nGroup=apache2' > /etc/systemd/system/redis.service.d/custom.conf
systemctl daemon-reload
```

Запустите сервис Redis:

```
systemctl --now enable redis
```
