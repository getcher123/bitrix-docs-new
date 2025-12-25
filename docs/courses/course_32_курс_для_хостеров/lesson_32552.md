# Конфигурация PostgreSQL

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32550 — Конфигурация MariaDB](lesson_32550.md)
- [Следующий: 32554 — Конфигурация Redis →](lesson_32554.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=32552

Если выбрали PostgreSQL, выполните шаги по запуску и настройке.




1. Инициализируйте базу данных.
  ```
  /etc/init.d/postgresql initdb
  ```
2. Запустите сервис.
  ```
  systemctl restart postgresql.service && systemctl enable postgresql.service
  ```
3. Настройте доступ по паролю.
  ```
  psql -U postgres
  ALTER USER postgres WITH PASSWORD 'ваш_надежный_пароль';
  \q
  ```
4. Откройте на редактирование файл `/var/lib/pgsql/data/pg_hba.conf`.
  ```
  vim /var/lib/pgsql/data/pg_hba.conf
  ```
  Найдите строки, похожие на:
  ```
  local   all             all                                     trust
  host    all             all             127.0.0.1/32            trust
  ```
  Замените  `trust` на `password`.
  ```
  local   all             all                                     password
  host    all             all             127.0.0.1/32            password
  host    all             all             ::1/128                 password
  ```
5. Перегрузите конфигурацию
  ```
  systemctl restart postgresql.service
  ```
6. Создайте базу данных и пользователя.
  ```
  psql -U postgres
  CREATE USER bitrix WITH PASSWORD 'PASSWORD';
  CREATE DATABASE portal OWNER bitrix;
  GRANT ALL PRIVILEGES ON DATABASE portal TO bitrix;
  CREATE EXTENSION IF NOT EXISTS pgcrypto;
  ```
  Замените `PASSWORD` на пароль, который будете использовать для доступа к БД.
