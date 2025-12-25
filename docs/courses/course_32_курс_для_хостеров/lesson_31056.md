# Конфигурация MariaDB

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 31054 — Конфигурация Apache](lesson_31054.md)
- [Следующий: 31058 — Конфигурация Redis →](lesson_31058.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=31056

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
