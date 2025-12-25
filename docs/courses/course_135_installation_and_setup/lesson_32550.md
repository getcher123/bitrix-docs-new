# Конфигурация MariaDB

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32548 — Конфигурация Apache](lesson_32548.md)
- [Следующий: 32552 — Конфигурация PostgreSQL →](lesson_32552.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=32550

Если установили MariaDB, то для конфигурации настройте параметры:

- `transaction-isolation = READ-COMMITTED`,
- `innodb_flush_method = O_DIRECT` — рекомендованная, но необязательная настройка,
- `innodb_flush_log_at_trx_commit = 2` — рекомендованная, но необязательная настройка,
- `thread_cache_size = 4`.

Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/alt.zip). Конфигурационные файлы для MariaDB расположены в папке `/alt/my.cnf.d/`.

После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/alt.zip

unzip alt.zip

		, выполните команды:

```
su -
rsync -av /opt/alt/my.cnf.d/ /etc/my.cnf.d/
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

Получите доступ к оболочке БД. Создайте базу данных и пользователя:

```
create database portal;
CREATE USER 'bitrix'@'localhost' IDENTIFIED BY 'PASSWORD';
GRANT ALL PRIVILEGES ON portal.* to 'bitrix'@'localhost';
```

Замените `PASSWORD` на пароль, который будете использовать для доступа к БД.
