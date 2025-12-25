# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 29878 — Установка и настройка ОС](lesson_29878.md)
- [Следующий: 9227 — Конфигурация Nginx →](lesson_9227.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=29880

Ниже приведен список всех пакетов, необходимых для установки коробочной версии Битрикс24. Для 1С-Битрикс: Управление сайтом список аналогичен, за исключением Push-сервера.




1. Apache — версия 2.4.62
  ```
  dnf install httpd
  ```
2. PHP — версия 8.1.30
  ```
  dnf install php php-cli php-common php-devel \
      php-gd php-imap php-ldap \
      php-mbstring php-mysqlnd php-opcache \
      php-pdo php-pear php-pear-DB php-pecl-apcu \
      php-pecl-mcrypt php-pecl-memcache \
      php-process php-pspell php-xml php-zipstream
  ```
3. NGINX — версия 1.26.2
  ```
  dnf install nginx
  ```
4. MariaDB-сервер — версия 10.11.6
  ```
  dnf install mariadb-server mariadb
  ```
5. Node и NPM (Push-сервер) — версия 20.15.1
  ```
  dnf install nodejs npm
  ```
6. Redis — 7.2.6
  ```
  dnf install redis
  ```
