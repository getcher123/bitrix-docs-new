# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 9859 — Конфигурация MariaDB](lesson_9859.md)
- [Следующий: 9673 — Конфигурация Push-server →](lesson_9673.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=9419

Работа Push-сервера невозможна без сервиса Redis. Для этого в конфигураторе следует:

- включить файловый сокет для работы,
- отключить сброс данных на диск, поскольку для работы Push-сервера это не требуется,
- установить группу пользователя.

Все конфигурационные файлы [скачайте в архиве](/docs/chm_files/redos.zip). Файлы для Redis расположены в папке: redos/redis.

Загрузите папку redos/redis в корневую папку сервера и выполните команду:

```
su -
rsync -av redos/redis/ /etc/redis/
```

Настройте права доступа:

```
su -
usermod -g apache redis
chown -R redis:apache /etc/redis /var/log/redis /var/lib/redis
[[ ! -d /etc/systemd/system/redis.service.d ]] && mkdir /etc/systemd/system/redis.service.d
echo -e '[Service]\nGroup=apache' > /etc/systemd/system/redis.service.d/custom.conf
systemctl daemon-reload
```

Запустите сервис Redis:

```
systemctl --now enable redis
```
