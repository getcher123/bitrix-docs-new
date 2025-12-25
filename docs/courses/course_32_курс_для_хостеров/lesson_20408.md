# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20406 — Конфигурация MariaDB](lesson_20406.md)
- [Следующий: 20410 — Конфигурация Push-server →](lesson_20410.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=20408

Данный сервис нам нужен для организации Push-сервера.



Основное, что нам важно установить в конфигурации:

- включить файловый сокет для работы;
- отключить сброс данных на диск (для работы Push-сервера нам не нужна эта возможность);
- установить группу пользователя.




Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/alt8.zip). Конфигурационные файлы для Redis находятся в папке: `alt8/redis`.




Разместите их в директории `/etc/redis/` и выполните:




```
su -
usermod -g apache2 \_redis
chown root:apache2 /etc/redis/ /var/log/redis/
mkdir /etc/systemd/system/redis.service.d
echo -e '[Service]\nGroup=apache2' > /etc/systemd/system/redis.service.d/custom.conf
systemctl daemon-reload
```





Запустите сервис:



```
systemctl --now enable redis
```
