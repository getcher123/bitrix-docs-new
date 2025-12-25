# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32914 — Установка и настройка ОС](lesson_32914.md)
- [Следующий: 32918 — Конфигурация Nginx →](lesson_32918.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=32916

Ниже приведен список всех пакетов, необходимых для установки коробочной версии Битрикс24. Для 1С-Битрикс: Управление сайтом список аналогичен, за исключением Push-сервера.

1. Apache — версия 2.4.65
  ```
  apt install apache2 -y
  ```
2. PHP — версия 8.4
  ```
  apt install php8.4 php8.4-cli php8.4-common php8.4-dev php8.4-gd php8.4-ldap php8.4-mbstring php8.4-mysql php8.4-opcache php8.4-pspell php8.4-xml php8.4-zip php8.4-amqp php8.4-apcu php-pear -y
  ```
  Список пакетов приведен с учетом того, что будет установлена MariaDB. Если вы будете устанавливать PostgreSQL, то для поддержки этой СУБД установите пакет `php8.4-pgsql`:
  ```
  apt install php8.4-pgsql -y
  ```
3. Nginx — версия 1.26.3
  ```
  apt install nginx -y
  ```
4. Выберите одну из СУБД:

  - MariaDB — версия 11.8.3. Подходит для всех лицензий продуктов компании 1С-Битрикс.
    ```
    apt install mariadb-server mariadb-common -y
    ```
  - PostgreSQL — версия 17.6. Подходит только для лицензии Энтерпрайз.
    ```
    apt install postgresql postgresql-client postgresql-doc -y
    ```
5. Node и NPM (Push-сервер) — версия 20.19.2
  ```
  apt install nodejs npm -y
  ```
6. Redis — 8.0.2
  ```
  apt install redis-server -y
  ```
