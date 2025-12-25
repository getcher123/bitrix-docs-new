# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 31056 — Конфигурация MariaDB](lesson_31056.md)
- [Следующий: 31060 — Конфигурация Push-server →](lesson_31060.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=31058

Работа Push-сервера невозможна без сервиса Redis. Для этого в конфигураторе следует:




- включить файловый сокет для работы,
- отключить сброс данных на диск, поскольку для работы Push-сервера это не требуется,
- установить группу пользователя.




Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/debian.zip). Файлы для Redis расположены в папке debian/redis.







После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/debian.zip

unzip debian.zip

		, выполните команду:





```
rsync -av /opt/debian/redis/redis.conf /etc/redis/redis.conf
```




Настройте права доступа:




```

usermod -g www-data redis
chown -R redis:www-data /etc/redis /var/log/redis /var/lib/redis
[[ ! -d /etc/systemd/system/redis.service.d ]] && mkdir /etc/systemd/system/redis.service.d
echo -e '[Service]\nGroup=www-data' > /etc/systemd/system/redis.service.d/custom.conf
systemctl daemon-reload
```




Запустите сервис Redis:




```
systemctl enable redis-server.service
systemctl restart redis-server.service
```
