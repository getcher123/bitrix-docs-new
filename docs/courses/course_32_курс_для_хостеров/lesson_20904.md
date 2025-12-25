# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20902 — Конфигурация MariaDB](lesson_20902.md)
- [Следующий: 20906 — Конфигурация Push-server →](lesson_20906.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=20904

Данный сервис необходим для организации Push-сервера.




Основные настройки, которые необходимо выполнить в конфигураторе:




- включить файловый сокет для работы;
- отключить сброс данных на диск (для работы Push-сервера эта возможность не нужна);
- установить группу пользователя.




Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/redos.zip). Конфигурационные файлы для Nginx расположены в папке: `redos/redis`.




Разместите их в директории `/etc/redis/` и выполните команды:




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
