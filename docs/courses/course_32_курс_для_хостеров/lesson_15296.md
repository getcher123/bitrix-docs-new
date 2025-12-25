# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 15270 — Установка и настройка ОС](lesson_15270.md)
- [Следующий: 16824 — Конфигурация NGINX →](lesson_16824.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=15296

Ниже приведен список всех пакетов, которые понадобятся для коробочной версии *«Битрикс24»*. Для *«1С-Битрикс: Управление сайтом»* список аналогичен (не нужно устанавливать только **push-server**).




1. **Apache** — версия 2.4 и **PHP** — версия 8.1:
  ```
  dnf install httpd
  dnf install php81-release
  dnf install php php-cli php-common php-devel \
      php-gd php-imap php-json php-ldap \
      php-mbstring php-mysqlnd php-opcache \
      php-pdo php-pear php-pear-DB php-pecl-apcu \
      php-pecl-mcrypt php-pecl-memcache \
      php-process php-pspell php-xml php-zipstream
  ```
2. **NGINX** — версия 1.25.4:
  ```
  dnf install nginx
  ```
3. **MariaDB** сервер — версия 10.11.6:
  ```
  dnf install mariadb-server mariadb
  ```
4. **Node** и **NPM** (push-server) — версия 18.20:
  ```
  dnf install nodejs npm
  ```
5. **Redis** — 7.0.15:
  ```
  dnf install redis
  ```
