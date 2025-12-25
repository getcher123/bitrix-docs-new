# Миграция через командную строку

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 15286 — Миграция через мастер](lesson_15286.md)
- [Следующий: 15290 — Миграция сторонних модулей →](lesson_15290.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=15288

1. Создайте пользователя и базу PostgreSQL
  ```
  root@cp:/var/www/html# sudo -u postgres createuser bitrix
  root@cp:/var/www/html# sudo -u postgres psql -c 'grant create on schema public to "bitrix"'
  GRANT
  root@cp:/var/www/html# sudo -u postgres createdb portaldb --owner bitrix --lc-ctype C.UTF-8 --template=template0
  root@cp:/var/www/html# sudo -u postgres psql -d portaldb -c 'CREATE EXTENSION IF NOT EXISTS pgcrypto'
  CREATE EXTENSION
  root@cp:/var/www/html# sudo -u postgres psql -d portaldb -c 'ALTER USER "bitrix" WITH PASSWORD '\''passwd'\'''
  ALTER ROLE
  ```
2. Остановите cron и веб-сервер, чтобы избежать модификации данных во время переноса.
  ```
  root@cp:/var/www/html# systemctl stop cron
  root@cp:/var/www/html# systemctl stop apache2
  root@cp:/var/www/html# systemctl stop php-fpm
  root@cp:/var/www/html# systemctl stop nginx
  ```
3. Сделайте дамп базы данных MySQL
  ```
  root@cp:/var/www/html# mysqldump --opt --skip-extended-insert --hex-blob -u root portaldb > /tmp/mysql_dump.sql
  ```
4. Сконвертируйте его в PostgreSQL
  ```
  root@cp:/var/www/html# php -f bitrix/modules/perfmon/tools/mysql_to_pgsql.php -- --mysqldump=/tmp/mysql_dump.sql > /tmp/pgsql_dump.sql
  ```
5. Убедитесь, что всё получилось
  ```
  root@cp:/var/www/html# less /tmp/pgsql_dump.sql
  ```
6. Добавьте дамп в PostgreSQL
  ```
  root@cp:/var/www/html# sudo -u www-data psql -b -q --user bitrix -d portaldb -f /tmp/pgsql_dump.sql
  ```
7. Добавьте дополнительные функции в PostgreSQL
  ```
  root@cp:/var/www/html# grep -v 'ALTER TABLE b_group' bitrix/modules/main/install/pgsql/install_add.sql | sudo -u www-data psql -b -q --user bitrix -d portaldb
  ```
8. Отредактируйте файл [.settings.php](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=02795)
  ```
  root@cp:/var/www/html# vi bitrix/.settings.php
  'connections' =>
  	array (
  		'value' =>
  		array (
  			'default' =>
  			array (
  				'className' => '\\Bitrix\\Main\\DB\\PgsqlConnection',
  				'host' => 'localhost',
  				'database' => 'portaldb',
  				'login' => 'bitrix',
  				'password' => 'passwd',
  				'options' => 2,
  				'charset' => 'utf-8',
  				'include_after_connected' => '',
  			),
  		),
  ```
9. Удалите модули без поддержки PostgreSQL
  ```
  root@cp:/home/max/sites/php74cp1251.cp/html# for mysql in `ls bitrix/modules/*/install/mysql/install.sql bitrix/modules/*/install/db/mysql/install.sql`;
  do
  pgsql=`echo $mysql|sed 's#/mysql/#/pgsql/#'`;
  test -e $pgsql || sudo -u postgres psql -d portaldb -a -c "delete from b_module where id='`echo $pgsql|cut -d '/' -f 3`'";
  done
  delete from b_module where id='abtest'
  DELETE 0
  delete from b_module where id='advertising'
  DELETE 0
  delete from b_module where id='b24connector'
  DELETE 0
  delete from b_module where id='biconnector'
  DELETE 0
  ........
  ```
10. Запустите сервисы
