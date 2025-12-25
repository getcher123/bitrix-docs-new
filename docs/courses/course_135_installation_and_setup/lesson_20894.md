# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20892 — Установка и настройка ОС](lesson_20892.md)
- [Следующий: 20896 — Конфигурация Nginx →](lesson_20896.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20894

Ниже приведен список всех пакетов, которые понадобятся для *1С-Битрикс24 (коробочная версия)*. Для *1С-Битрикс: Управление сайтом* список аналогичен (не нужно устанавливать только **push-server**).

- **Apache 2.4** и **php 7.4**:
  ```
  # yum install httpd -y
  # yum -y install php php-cli php-common \
   php-devel php-gd \
   php-imap php-json php-ldap php-mbstring \
   php-mysqlnd php-opcache php-pdo \
   php-pear php-pear-DB php-pecl-apcu \
   php-pecl-apcu-bc php-pecl-geoip \
   php-pecl-mcrypt php-pecl-memcache  \
   php-pecl-ssh2 php-process php-pspell php-xml php-zipstream
  ```
  С 01.02.2023 ограничивается поддержка наших продуктов на PHP версии ниже 8.0. Рекомендуемая версия PHP - 8.1 и выше. Поэтому после установки необходимо обновить PHP до версии не ниже 8.0.
- **Nginx** (версия 1.18):
  ```
  yum install nginx -y
  ```
- **MariaDB** сервер (версия 10.5):
  ```
  yum -y install mariadb-server mariadb
  ```
- **Node** и **npm** (push-server), версия 16.13:
  ```
  yum install nodejs -y
  ```
- **Redis** (версия 6.2):
  ```
  yum install redis -y
  ```
