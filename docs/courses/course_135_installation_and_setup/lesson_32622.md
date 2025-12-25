# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32620 — Установка и настройка ОС](lesson_32620.md)
- [Следующий: 32624 — Конфигурация Nginx →](lesson_32624.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=32622

Ниже приведен список всех пакетов, необходимых для установки коробочной версии Битрикс24. Для 1С-Битрикс: Управление сайтом список аналогичен, за исключением Push-сервера.

1. Apache — версия 2.4.65
  ```
  dnf install httpd -y
  ```
2. PHP — версия 8.3.14
  ```
  dnf install -y php8-cli php8-devel php8-gd php8-imap php8-ldap php8-mbstring php8-mysqlnd php8-opcache php8-pdo php8-mysqli php8-pspell php8-xml php8-zip php-pear php-pear-DB php8-mcrypt php8-apcu apache-mod_php8 php8-memcached -y
  ```
  Список пакетов приведен с учетом того, что будет установлена MariaDB. Если вы будете устанавливать PostgreSQL, то для поддержки этой СУБД установите пакеты `php8-pgsql` и `php8-pdo_pgsql`:
  ```
  dnf install php8-pgsql php8-pdo_pgsql
  ```
3. Nginx — версия 1.26.2
  ```
  dnf install nginx -y
  ```
4. Выберите одну из СУБД:

5. PostgreSQL — версия 15. Подходит только для лицензии Энтерпрайз.
  ```
  dnf install postgresql15 postgresql15-contrib postgresql15-server postgresql15-docs -y
  ```
6. Node и NPM (Push-сервер) — версия 20.14
  ```
  dnf install nodejs npm -y
  ```
7. Redis — 7.2.5:
  ```
  dnf install redis -y
  ```
