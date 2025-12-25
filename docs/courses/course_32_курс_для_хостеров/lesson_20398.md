# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20396 — Установка и настройка ОС](lesson_20396.md)
- [Следующий: 20400 — Конфигурация Nginx →](lesson_20400.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=20398

Ниже приведен весь список пакетов, который нам понадобится для *1С-Битрикс24 коробочная версия*. Для *1С-Битрикс: Управление сайтом* из этого набора не нужен только **push-server**.




Установка по шагам:



1. **Apache 2.4** и **php 7.2** уже будут установлены на сервере, если Вы выбрали **web-сервер** на этапе установки дистрибутива.
  Если Вы выбрали минимальную установку (а не **web-сервер**), то просто поставьте все пакеты из списка ниже:
  ```
  su -
  apt-get install apache2-mods apache2-htcacheclean \
      apache2-cgi-bin-test-cgi apache2-htpasswd \
      apache2-httpd-prefork apache2-mod_php7 \
      apache2-mod_cache_disk apache2 \
      apache2-datadirs apache2-cgi-bin-printenv \
      apache2-htcacheclean-control apache2-html \
      apache2-ab apache2-base apache2-httpd-worker apache2-cgi-bin apache2-icons
  apt-get install php7-mcrypt php7-imap \
      php7 php7-xsl php7-gd php7-memcache \
      php7-exif php7-zip php7-mbstring \
      php7-fileinfo apache2-mod_php7 \
      php7-libs php7-dom php7-xmlrpc php7-dba php7-curl \
      php7-mysqli php7-openssl php7-opcache
  ```
  С 01.02.2023 ограничивается поддержка наших продуктов на PHP версии ниже 8.0. Рекомендуемая версия PHP – 8.1 и выше. Поэтому после установки необходимо обновить PHP до версии не ниже 8.0.
  Установите **Nginx** (версия 1.20.1):
  ```
  su -
  apt-get install nginx
  ```
  Установите **MariaDB** сервер (версия 10.4.20):
  ```
  su -
  apt-get install mariadb-server mariadb-client
  ```
  Установите **Node** и **npm** (push-server) (версия 14.3.0):
  ```
  su -
  apt-get install node npm
  ```
  Установите **Redis** (версия 5.0.4):
  ```
  su -
  apt-get install redis
  ```
