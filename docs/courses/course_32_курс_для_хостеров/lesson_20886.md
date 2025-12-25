# Конфигурация Redis

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20884 — Конфигурация MariaDB](lesson_20884.md)
- [Следующий: 20888 — Конфигурация Push-server →](lesson_20888.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=20886

Данный сервис нам нужен для организации Push-сервера.



Основное, что нам важно установить в конфигурации:

- включить файловый сокет для работы;
- отключить сброс данных на диск (для работы Push-сервера нам не нужна эта возможность);
- группу пользователя.





Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/sles15.zip). Конфигурационные файлы для Redis расположены в папке: `sles15/redis`.




Разместите их в директории `/etc/redis/`.



```
su -
usermod -g www redis
chown -R redis:www /etc/redis/ /var/log/redis/ /var/lib/redis/
mkdir /etc/systemd/system/redis@.service.d
echo -e '[Service]\nGroup=www' > /etc/systemd/system/redis@.service.d/custom.conf
systemctl daemon-reload
```




Запустите сервис



```
systemctl --now enable redis@default
```
