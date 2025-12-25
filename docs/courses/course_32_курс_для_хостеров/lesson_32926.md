# Конфигурация PostgreSQL

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32924 — Конфигурация MariaDB](lesson_32924.md)
- [Следующий: 32944 — Конфигурация Redis →](lesson_32944.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=32926

Если выбрали PostgreSQL, выполните шаги по настройке.




По умолчанию кластер `main` создается и запускается автоматически при установке пакетов PostgreSQL.




1. Задайте пароль суперпользователя `postgres`.
  ```
  su - postgres -c psql
  ALTER USER postgres PASSWORD 'ваш_надежный_пароль';
  \q
  ```
2. Откройте на редактирование файл `/etc/postgresql/17/main/pg_hba.conf`.
  ```
  nano /etc/postgresql/17/main/pg_hba.conf
  ```
  Найдите строки:
  ```
  local   all             postgres                                peer
  local   all             all                                     peer
  local   all             all                                     scram-sha-256
  host    all             all             127.0.0.1/32            scram-sha-256
  ```
  Замените  `peer` и `scram-sha-256` на `password`.
  ```
  local   all             postgres                                password
  local   all             all                                     password
  host    all             all             127.0.0.1/32            password
  host    all             all             ::1/128                 password
  ```
3. Перегрузите конфигурацию. Команда для PostgreSQL версии 17.6:
  ```
  systemctl reload postgresql@17-main.service
  ```
4. Создайте базу данных и пользователя.
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
5. Подключите расширение `pgcrypto`.
  ```
  psql -U postgres -d portal -c "CREATE EXTENSION IF NOT EXISTS pgcrypto;"
  ```
