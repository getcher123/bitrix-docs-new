# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32490 — Установка и настройка ОС](lesson_32490.md)
- [Следующий: 32494 — Конфигурация Nginx →](lesson_32494.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=32492

Ниже приведен список всех пакетов, необходимых для установки коробочной версии Битрикс24. Для 1С-Битрикс: Управление сайтом список аналогичен, за исключением Push-сервера.

1. Apache — версия 2.4.65
  ```
  apt-get install apache2-mods apache2-htcacheclean apache2-cgi-bin-test-cgi apache2-htpasswd apache2-httpd-prefork apache2-mod_php8.2 apache2-mod_cache_disk apache2 apache2-datadirs apache2-cgi-bin-printenv apache2-htcacheclean-control apache2-html apache2-ab apache2-base apache2-httpd-worker apache2-cgi-bin apache2-icons -y
  ```
2. PHP — версия 8.2.28
  ```
  apt-get install php8.2-mcrypt php8.2-imap php8.2 php8.2-xsl php8.2-gd php8.2-memcache php8.2-exif php8.2-zip php8.2-mbstring php8.2-fileinfo apache2-mod_php8.2 php8.2-libs php8.2-dom php8.2-xmlrpc php8.2-dba php8.2-curl php8.2-mysqli php8.2-openssl php8.2-opcache php8.2-ldap -y
  ```
  Список пакетов приведен с учетом того, что будет установлена MariaDB. Если вы будете устанавливать PostgreSQL, то для поддержки этой СУБД установите пакет php8.2-pgsql:
  ```
  apt-get install php8.2-pgsql
  ```
3. Nginx — версия 1.26.3
  ```
  apt-get install nginx -y
  ```
4. Выберите одну из СУБД:

  - MariaDB — версия 10.6.23. Подходит для всех лицензий.
    ```
    apt-get install mariadb-server mariadb-client -y
    ```
  - PostgreSQL — версия 15. Подходит только для лицензии Энтерпрайз.
    ```
    apt-get install postgresql15 postgresql15-contrib postgresql15-server postgresql15-docs -y
    ```
5. Node и NPM (Push-сервер) — версия 16.20.3
  ```
  apt-get install node npm -y
  ```
6. Redis — 6.2.17:
  ```
  apt-get install redis -y
  ```
