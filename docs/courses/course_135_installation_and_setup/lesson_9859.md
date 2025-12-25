# Конфигурация MariaDB

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 9861 — Конфигурация Apache](lesson_9861.md)
- [Следующий: 9419 — Конфигурация Redis →](lesson_9419.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=9859

Для конфигурации MariaDB задайте настройки параметров:

- `transaction-isolation = READ-COMMITTED`,
- `innodb_flush_method = O_DIRECT` — рекомендованная, но необязательная настройка,
- `innodb_flush_log_at_trx_commit = 2` — рекомендованная, но необязательная настройка,
- `thread_cache_size = 4`.

Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/redos.zip). Конфигурационные файлы для MariaDB расположены в папке: redos/my.cnf.d.

Загрузите папку redos/my.cnf.d в корневую папку сервера и выполните команду:

```
su -
rsync -av redos/my.cnf.d/ /etc/my.cnf.d/
```

Запустите сервис:

```

systemctl --now enable mariadb
```

Настройте сервис через `mysql_secure_installation`.

```
mysql_secure_installation
.....

By default, a MariaDB installation has an anonymous user, allowing anyone
to log into MariaDB without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.

Remove anonymous users? [Y/n] y
 ... Success!

Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.

Disallow root login remotely? [Y/n] y
 ...
```
