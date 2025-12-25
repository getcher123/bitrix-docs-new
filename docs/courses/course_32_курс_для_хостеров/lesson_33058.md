# Конфигурация PostgreSQL

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 33056 — Конфигурация MariaDB](lesson_33056.md)
- [Следующий: 33060 — Конфигурация Redis →](lesson_33060.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=33058

Если выбрали PostgreSQL, выполните шаги по запуску и настройке.




1. Инициализируйте базу данных и задайте пароль суперпользователя `postgres`.
  ```
  /etc/init.d/postgresql initdb
  ```
2. Запустите сервис.
  ```
  systemctl enable postgresql.service && systemctl restart postgresql.service
  ```
3. Откройте на редактирование файл `/var/lib/pgsql/data/pg_hba.conf`.
  ```
  vim /var/lib/pgsql/data/pg_hba.conf
  ```
  Найдите строки:
  ```
  local   all             all                                     scram-sha-256
  host    all             all             127.0.0.1/32            scram-sha-256
  host    all             all             ::1/128                 scram-sha-256
  ```
  Замените  `scram-sha-256` на `password`.
  ```
  local   all             all                                     password
  host    all             all             127.0.0.1/32            password
  host    all             all             ::1/128                 password
  ```
4. Перегрузите конфигурацию
  ```
  systemctl restart postgresql.service
  ```
5. Создайте базу данных и пользователя.
  ```
  psql -U postgres
  CREATE DATABASE portal lc_ctype='C.UTF-8' template template0;
  CREATE USER bitrix WITH PASSWORD 'PASSWORD';
  GRANT ALL PRIVILEGES ON DATABASE portal TO bitrix;
  ALTER DATABASE portal OWNER TO bitrix;
  GRANT CREATE ON schema public TO bitrix;
  \q
  ```
  Замените `PASSWORD` на пароль, который будете использовать для доступа к БД.
6. Подключите расширение `pgcrypto`.
  ```
  psql -U postgres -d portal -c "CREATE EXTENSION IF NOT EXISTS pgcrypto;"
  ```
