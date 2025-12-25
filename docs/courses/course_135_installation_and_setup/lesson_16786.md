# Конфигурация MariaDB

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5407 — Конфигурация Apache](lesson_5407.md)
- [Следующий: 16788 — Конфигурация Redis →](lesson_16788.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=16786

Необходимые настройки:

- **transaction-isolation** измените в READ-COMMITTED.
- **innodb_flush_method** желательно должно быть равным O_DIRECT
- **innodb_flush_log_at_trx_commit** желательно должно быть равным 2.

Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/astra.zip).  Конфигурационные файлы для **MariaDB** размещены в папке `astra/my.cnf.d`

```
su -
rsync -av astra/mysql/ /etc/mysql/
```

Измените следующие файлы:

- **my.cnf** - добавьте загрузку настроек из каталога `/etc/mysql/my-bx.d/`;
- `my-bx.d/zbx-custom.cnf` - пропишите настройки, указанные выше.

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
