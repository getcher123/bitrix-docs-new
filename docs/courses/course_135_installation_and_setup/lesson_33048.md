# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 33046 — Установка и настройка ОС](lesson_33046.md)
- [Следующий: 33050 — Конфигурация Nginx →](lesson_33050.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=33048

Ниже приведен список всех пакетов, необходимых для установки коробочной версии Битрикс24. Для 1С-Битрикс: Управление сайтом список аналогичен, за исключением Push-сервера.

1. Apache — версия 2.4.65
  ```
  apt-get install apache2-mods apache2-htcacheclean apache2-cgi-bin-test-cgi apache2-htpasswd apache2-httpd-prefork apache2-mod_php8.3 apache2-mod_cache_disk apache2 apache2-datadirs apache2-cgi-bin-printenv apache2-htcacheclean-control apache2-html apache2-ab apache2-base apache2-httpd-worker apache2-cgi-bin apache2-icons -y
  ```
2. PHP — версия 8.3.24
  ```
  apt-get install php8.3 php8.3-curl php8.3-dba php8.3-exif php8.3-fileinfo php8.3-gd php8.3-imap php8.3-ldap php8.3-libs php8.3-mbstring php8.3-mcrypt php8.3-memcache php8.3-mysqlnd-mysqli php8.3-openssl php8.3-opcache php8.3-xmlrpc php8.3-xsl php8.3-zip php8.3-pdo php8.3-mysqlnd -y
  ```
  Список пакетов приведен с учетом того, что будет установлена MariaDB. Если вы будете устанавливать PostgreSQL, то для поддержки этой СУБД установите пакет php8.3-pdo_pgsql и php8.3-pgsql:
  ```
  apt-get install php8.3-pdo_pgsql php8.3-pgsql
  ```
3. Nginx — версия 1.28.0
  ```
  apt-get install nginx -y
  ```
4. Выберите одну из СУБД:

  - MariaDB — версия 10.6.22. Подходит для всех лицензий.
    ```
    apt-get install mariadb-server mariadb-client mariadb-common -y
    ```
  - PostgreSQL — версия 16. Подходит только для лицензии Энтерпрайз.
    ```
    apt-get install postgresql16 postgresql16-contrib postgresql16-server postgresql16-docs -y
    ```
5. Node и NPM (Push-сервер) — версия 16.20.3
  ```
  apt-get install node npm -y
  ```
6. Redis — 7.2.11:
  ```
  apt-get install redis -y
  ```
