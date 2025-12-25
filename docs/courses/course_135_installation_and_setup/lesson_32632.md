# Конфигурация PostgreSQL

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32630 — Конфигурация MariaDB](lesson_32630.md)
- [Следующий: 32634 — Конфигурация Redis →](lesson_32634.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=32632

Если выбрали PostgreSQL, выполните шаги по запуску и настройке.

1. Запустите сервис.
  ```
  systemctl enable postgresql15.service
  systemctl restart postgresql15.service
  ```
2. Настройте доступ по паролю.
  ```
  psql -U postgres
  ALTER USER postgres WITH PASSWORD 'ваш_надежный_пароль';
  \q
  ```
3. Откройте на редактирование файл `/var/lib/pgsql/data/pg_hba.conf`.
  ```
  nano /var/lib/pgsql/data/pg_hba.conf
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
4. Перегрузите конфигурацию
  ```
  systemctl restart postgresql15.service
  ```
5. Создайте базу данных и пользователя.
  ```
  psql -U postgres
  CREATE USER bitrix WITH PASSWORD 'PASSWORD';
  CREATE DATABASE portal OWNER bitrix;
  GRANT ALL PRIVILEGES ON DATABASE portal TO bitrix;
  \q
  ```
  Замените `PASSWORD` на пароль, который будете использовать для доступа к БД.
6. Подключите расширение `pgcrypto`.
  ```
  psql -U postgres -d portal -c "CREATE EXTENSION IF NOT EXISTS pgcrypto;"
  ```
