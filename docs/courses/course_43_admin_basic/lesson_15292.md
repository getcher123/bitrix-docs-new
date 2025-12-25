# Установка PostgreSQL

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 15290 — Миграция сторонних модулей](lesson_15290.md)
- [Следующий: 3440 — Добавление кнопок на панель управления →](lesson_3440.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=15292

### Установка на CentOS 7 (BitrixVM)

[Инструкция на сайте PostgreSQL](https://www.postgresql.org/download/linux/redhat/)

1. Обновите BitrixVM
  ```
  yum -y update
  ```
2. В стандартном репозитории - старая версия PostgreSQL , поэтому запретите установку из нее. Для этого в файле `/etc/yum.repos.d/CentOS-Base.repo` в секции [base] добавьте:
  ```
  exclude=postgresql*
  ```
3. Добавьте в систему репозиторий PostgreSQL и уточните доступные версии:
  ```
  yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
  ```
  ```
  yum list -y postgre*-server*
  ```
  Отобразиться примерно такое:
  ```
  Available Packages
  postgresql-server.x86_64                           9.2.24-8.el7_9                            updates
  postgresql12-server.x86_64                         12.15-1PGDG.rhel7                         pgdg12
  postgresql13-server.x86_64                         13.11-1PGDG.rhel7                         pgdg13
  postgresql14-server.x86_64                         14.8-1PGDG.rhel7                          pgdg14
  postgresql15-server.x86_64                         15.3-1PGDG.rhel7                          pgdg15
  ```
4. Установите 12 версию БД и дополнения для него:
  ```
  yum -y install postgresql12-server
  ```
  ```
  yum -y install postgresql12-contrib
  ```
5. Инициализируйте БД:
  ```
  [root@pg ~]# /usr/pgsql-12/bin/postgresql-12-setup initdb
  Initializing database ... OK
  ```
  Будет создана папка `/var/lib/pgsql/12/data/` и файлы конфигурации в ней.
  Не ищите эти файлы в /etc/!
6. Активируйте запуск сервиса при загрузке системы и следом запустите службу:
  ```
  systemctl enable postgresql-12
  ```
  ```
  service postgresql-12 start
  ```
7. Установите расширение **pgsql** для PHP:
  ```
  yum -y install php-pgsql
  ```
8. Уберите лишнее расширение **pdo_pgsql** и перезапустите веб-сервер:
  ```
  mv /etc/php.d/30-pdo_pgsql.ini /etc/php.d/30-pdo_pgsql.ini.disabled
  ```
  ```
  service restart httpd
  ```

### Установка на MacOS

[Инструкция на сайте PostgreSQL](https://www.postgresql.org/download/macosx/)

1. Установите 11 или выше версию БД:
  ```
  brew install postgresql@11
  ```
2. Запустите сервис при загрузке системы:
  ```
  brew services start postgresql@11
  ```

### Конфигурация PostgreSQL

1. Добавьте пользователя:
  ```
  root@max:/# sudo -u postgres createuser www-data
  ```
  Для версии начиная с 15:
  ```
  root@max:/# sudo -u postgres psql
  postgres=> grant create on schema public to "www-data";
  ```
2. Добавьте базу данных:
  ```
  root@max:/# sudo -u postgres createdb www-data --owner www-data  --lc-ctype C.UTF-8 --template=template0
  ```
3. Добавьте расширение **pgcrypto**:
  ```
  root@max:/# sudo -u postgres psql -d www-data
  postgres=# CREATE EXTENSION IF NOT EXISTS pgcrypto;
  ```
4. Задайте пароль:
  ```
  root@max:/# sudo -u www-data psql --user www-data
  www-data=> ALTER USER "www-data" WITH PASSWORD 'passwd';
  ```
  Если вы при соединении из PHP получили ошибку типа **Ident authentication error...**, то нужно в конфигурационных файлах разрешить аутентификацию по паролю. Для этого в файле `/var/lib/pgsql/11/data/pg_hba.conf` измените строки, заменяя последнюю колонку на password.
  ```
  # IPv4 local connections:
  host    all             all             127.0.0.1/32            password
  # IPv6 local connections:
  host    all             all             ::1/128                 password
  ```
5. Перезапустите сервер.
