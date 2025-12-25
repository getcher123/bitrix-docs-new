# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5014 — Конфигурация MariaDB](lesson_5014.md)
- [Следующий: 2376 — Конфигурация Push-server →](lesson_2376.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=2374

Работа Push-сервера невозможна без сервиса Redis. Для этого в конфигураторе следует:

- включить файловый сокет для работы,
- отключить сброс данных на диск, поскольку для работы Push-сервера это не требуется,
- установить группу пользователя.

Все конфигурационные файлы [скачайте в архиве](https://dev.1c-bitrix.ru/docs/chm_files/debian.zip). Файлы для Redis расположены в папке: debian/redis.

Загрузите папку debian/redis в корневую папку сервера и выполните команду:

```
su -
rsync -av debian/redis/redis.conf /etc/redis/redis.conf
```

Настройте права доступа:

```

usermod -g www-data redis
chown root:www-data /etc/redis/ /var/log/redis/
[[ ! -d /etc/systemd/system/redis.service.d ]] && mkdir /etc/systemd/system/redis.service.d
echo -e '[Service]\nGroup=www-data' > /etc/systemd/system/redis.service.d/custom.conf
systemctl daemon-reload
```

Запустите сервис Redis:

```
systemctl enable redis-server.service
systemctl restart redis-server.service
```
