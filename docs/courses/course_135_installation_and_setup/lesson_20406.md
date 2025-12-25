# Конфигурация MariaDB

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20404 — Конфигурация Apache](lesson_20404.md)
- [Следующий: 20408 — Конфигурация Redis →](lesson_20408.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20406

Для конфигурации MariaDB требуется выполнить такие настройки:

- **transaction-isolation** изменить на `READ-COMMITTED`;
- **innodb_flush_method** установить равным `O_DIRECT` (желательная, но не обязательная настройка);
- **innodb_flush_log_at_trx_commit** установить равным **2** (желательная, но не обязательная настройка).

Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/alt8.zip). Конфигурационные файлы для MariaDB находятся в папке: `alt8/my.cnf.d`.

Разместите их в директории `/etc/my.cnf.d/`.

Запустите сервис:

```
systemctl --now enable mariadb
```

Настройте пароль для доступа к серверу и прочие опции безопасности через скрипт:

```
mysql_secure_installation
.....

Set root password? [Y/n] y
New password:
Re-enter new password:
Password updated successfully!
Reloading privilege tables..
 ... Success!

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
