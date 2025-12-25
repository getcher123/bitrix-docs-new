# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 15300 — Конфигурация Mariadb](lesson_15300.md)
- [Следующий: 15294 — Конфигурация Push-server →](lesson_15294.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=15278

Данный сервис необходим для организации работы Push-сервера.




Основные настройки, которые необходимо выполнить в конфигураторе:




- включить файловый сокет для работы;
- отключить сброс данных на диск (для работы Push-сервера эта возможность не нужна);
- установить группу пользователя.




Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/redos.zip). Конфигурационные файлы для Redis расположены в папке: `redos/redis`.




Разместите их в директории `/etc/redis/`:


```
su -
rsync -av redos/redis/ /etc/redis/
```




Выполните команды:




```
su -
usermod -g apache redis
chown root:apache /etc/redis/ /var/log/redis/
[[ ! -d /etc/systemd/system/redis.service.d ]] && mkdir /etc/systemd/system/redis.service.d
echo -e '[Service]\nGroup=apache' > /etc/systemd/system/redis.service.d/custom.conf
systemctl daemon-reload
```




Запустите сервис:




```
systemctl --now enable redis
```
