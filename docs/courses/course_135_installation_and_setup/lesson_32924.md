# Конфигурация MariaDB

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32922 — Конфигурация Apache](lesson_32922.md)
- [Следующий: 32926 — Конфигурация PostgreSQL →](lesson_32926.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=32924

Для конфигурации MariaDB задайте настройки параметров:

- `transaction-isolation = READ-COMMITTED`,
- `innodb_flush_method = O_DIRECT` — рекомендованная, но необязательная настройка,
- `innodb_flush_log_at_trx_commit = 2` — рекомендованная, но необязательная настройка,
- `thread_cache_size = 4`.

Все конфигурационные файлы можно  [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/debian.zip). Конфигурационные файлы для MariaDB расположены в папке: debian/mysql.

После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/debian.zip

unzip debian.zip

		, выполните команду:

```
rsync -av /opt/debian/mysql/ /etc/mysql/
```

В результате:

- в файле my.cnf добавлена загрузка настроек из каталога /etc/mysql/my-bx.d/,
- настройки, указанные выше, прописаны в my-bx.d/zbx-custom.cnf.

Запустите сервис:

```
systemctl --now enable mariadb

systemctl restart mariadb
```

Настройте сервис через *mariadb-secure-installation*.

```
NOTE: MariaDB is secure by default in Debian. Running this script is
      useless at best, and misleading at worst. This script will be
      removed in a future MariaDB release in Debian. Please read
      mariadb-server.README.Debian for details.

Enter root user password or leave blank:

Enter current password for root (enter for none):
OK, successfully used password, moving on...

Setting the root password or using the unix_socket ensures that nobody
can log into the MariaDB root user without the proper authorisation.

You already have your root account protected, so you can safely answer 'n'.

Switch to unix_socket authentication [Y/n] n
 ... skipping.

You already have your root account protected, so you can safely answer 'n'.

Change the root password? [Y/n] n
 ... skipping.

By default, a MariaDB installation has an anonymous user, allowing anyone
to log into MariaDB without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.

...

Cleaning up...

All done!  If you've completed all of the above steps, your MariaDB
installation should now be secure.

Thanks for using MariaDB!
```

Получите доступ к оболочке БД. Создайте базу данных и пользователя:

```
create database portal;
CREATE USER 'bitrix'@'localhost' IDENTIFIED BY 'PASSWORD';
GRANT ALL PRIVILEGES ON portal.* to 'bitrix'@'localhost';
```

Замените `PASSWORD` на пароль, который будете использовать для доступа к БД.
