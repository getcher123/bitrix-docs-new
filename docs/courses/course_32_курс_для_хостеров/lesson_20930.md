# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20928 — Конфигурация MariaDB](lesson_20928.md)
- [Следующий: 20932 — Конфигурация Push-server →](lesson_20932.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=20930

Данный сервис необходим для организации Push-сервера.




Основные настройки, которые необходимо выполнить в конфигураторе:




- включить файловый сокет для работы;
- отключить сброс данных на диск (для работы Push-сервера эта возможность не нужна);
- установить группу пользователя.




Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/redhat8.zip). Конфигурационные файлы для Nginx расположены в папке: `redhat8/redis`.




Разместите их в директории `/etc/redis/` и выполните команды:




```

su -
usermod -g apache redis
chown root:apache /etc/redis/ /var/log/redis/
mkdir /etc/systemd/system/redis.service.d
echo -e '[Service]\nGroup=apache' > /etc/systemd/system/redis.service.d/custom.conf
systemctl daemon-reload
```





Запустите сервис:




```

systemctl --now enable redis
```
