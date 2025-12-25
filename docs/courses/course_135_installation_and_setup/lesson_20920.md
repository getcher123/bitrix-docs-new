# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20918 — Установка и настройка ОС](lesson_20918.md)
- [Следующий: 20922 — Конфигурация Nginx →](lesson_20922.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20920

Ниже приведен весь список пакетов, который нам понадобится для *1С-Битрикс24 коробочная версия*. Для *1С-Битрикс: Управление сайтом* не нужен только **push-server**.

1. Установите **apache 2.4** и  **php 7.2**:
  ```
  dnf -y install httpd
  dnf -y install php php php-cli php-common \
      php-devel php-gd php-json php-mbstring \
      php-mysqlnd php-opcache php-pdo php-pear \
      php-pecl-apcu php-pecl-zip php-process php-xml php-ldap
  ```
  С 01.02.2023 ограничивается поддержка наших продуктов на PHP версии ниже 8.0. Рекомендуемая версия PHP – 8.1 и выше. Поэтому после установки необходимо обновить PHP до версии не ниже 8.0.
2. Установите **nginx** (1.14 версия):
  ```
  dnf install nginx -y
  ```
3. Установите **MariaDB** сервер (10.1 версия):
  ```
  dnf install mariadb -y
  ```
4. Установите **node** и **npm** (push-server):
  ```
  dnf install nodejs -y
  ```
5. Установите **redis**:
  ```
  dnf install redis -y
  ```
