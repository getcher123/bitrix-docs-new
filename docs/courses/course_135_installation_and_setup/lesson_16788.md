# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 16786 — Конфигурация MariaDB](lesson_16786.md)
- [Следующий: 2381 — Конфигурация push-server →](lesson_2381.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=16788

Данный сервис необходим для организации работы **push-server**.

Основное, что важно в конфиге:

- включение файлового сокета для работы;
- отключение сброса данных на диск (для работы push-server нам не нужна эта возможность);
- группа пользователя.

Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/astra.zip).  Конфигурационные файлы для **Redis** размещены в папке `astra/redis`

```
su -
rsync -av astra/redis/redis.conf /etc/redis/redis.conf
usermod -g www-data redis
chown root:www-data /etc/redis/ /var/log/redis/
[[ ! -d /etc/systemd/system/redis-server.service.d ]] && mkdir /etc/systemd/system/redis-server.service.d
echo -e '[Service]\nGroup=www-data' > /etc/systemd/system/redis-server.service.d/custom.conf
systemctl daemon-reload
```

Запустите сервис:

```
systemctl enable redis-server.service
systemctl restart redis-server.service
```
