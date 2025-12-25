# Конфигурация MariaDB

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 4775 — Конфигурация Apache](lesson_4775.md)
- [Следующий: 2374 — Конфигурация Redis →](lesson_2374.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=5014

Для конфигурации MariaDB задайте настройки параметров:

- `transaction-isolation = READ-COMMITTED`,
- `innodb_flush_method = O_DIRECT` — рекомендованная, но необязательная настройка,
- `innodb_flush_log_at_trx_commit = 2` — рекомендованная, но необязательная настройка,
- `thread_cache_size = 4`.

Все конфигурационные файлы можно  [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/debian.zip). Конфигурационные файлы для MariaDB расположены в папке: debian/mysql.

Загрузите папку debian/mysql в корневую папку сервера и выполните команду:

```
su -
rsync -av debian/mysql/ /etc/mysql/
```

В результате:

- в файле my.cnf добавлена загрузка настроек из каталога `/etc/mysql/my-bx.d/`,
- настройки, указанные выше, прописаны в my-bx.d/zbx-custom.cnf.

Запустите сервис:

```
systemctl --now enable mariadb

systemctl restart mariadb
```

Настройте сервис через *mysql_secure_installation*.

```
mysql_secure_installation
...
Switch to unix_socket authentication [Y/n] n
 ... skipping.

Change the root password? [Y/n] y
New password:
Re-enter new password:
Password updated successfully!
Reloading privilege tables..
 ... Success!

Remove anonymous users? [Y/n] y
 ... Success!

Disallow root login remotely? [Y/n] y
 ... Success!
```
