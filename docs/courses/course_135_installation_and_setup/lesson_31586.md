# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 31584 — Установка и настройка ОС](lesson_31584.md)
- [Следующий: 31588 — Конфигурация Nginx →](lesson_31588.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=31586

Ниже приведен список всех пакетов, необходимых для установки коробочной версии Битрикс24. Для 1С-Битрикс: Управление сайтом список аналогичен, за исключением Push-сервера.

1. Apache — версия 2.4.57
  ```
  apt install apache2 apache2-dev -y
  ```
2. PHP — версия 8.2
  ```
  apt install php php-cli php-common php-dev php-gd php-imap php-ldap php-mbstring php-mysql php-opcache php-pspell php-xml php-zip php-amqp php-apcu php-pear -y
  ```
3. Nginx — версия 1.22
  ```
  apt install nginx -y
  ```
4. MariaDB-сервер — версия 10.11.6
  ```
  apt -y install mariadb-server mariadb-client
  ```
5. Node и NPM (Push-сервер) — версия 18.19.0
  ```
  apt install nodejs npm -y
  ```
6. Redis — 7.0.15
  ```
  apt install redis -y
  ```
