# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5363 — Установка и настройка ОС](lesson_5363.md)
- [Следующий: 8455 — Конфигурация Nginx →](lesson_8455.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=5321

### Настройка репозитория

В дефолтном репозитории Debian 11 отсутствует PHP 8.1 и выше. Есть сторонние репозитории, которые позволяют поставить необходимое ПО.

Выполните установку пакетов:

```
apt install lsb-release ca-certificates curl
```

Настройте репозиторий, симпортируйте ключ репозитория, обновите список пакетов:

```

curl -sSLo /tmp/debsuryorg-archive-keyring.deb https://packages.sury.org/debsuryorg-archive-keyring.deb
dpkg -i /tmp/debsuryorg-archive-keyring.deb
sh -c 'echo "deb [signed-by=/usr/share/keyrings/deb.sury.org-php.gpg] https://ftp.mpi-inf.mpg.de/mirrors/linux/mirror/deb.sury.org/repositories/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list'
apt update && apt upgrade
```

При недоступности указанного зеркала следует использовать альтернативное зеркало из [списка](https://www.debian.org/mirror/list.ru.html).

### Установка пакетов

Ниже приведен список всех пакетов, необходимых для установки коробочной версии Битрикс24. Для 1С-Битрикс: Управление сайтом список аналогичен, за исключением Push-сервера.

1. Apache — версия 2.4.62
  ```
  apt install apache2 -y
  ```
2. PHP — версия 8.3
  ```
  apt install php8.3 php8.3-cli php8.3-common php8.3-gd php8.3-ldap php8.3-mbstring php8.3-mysql php8.3-opcache php-pear php8.3-apcu php-geoip php8.3-mcrypt php8.3-memcache php8.3-zip php8.3-pspell php8.3-xml -y
  ```
3. Nginx — версия 1.18.0
  ```
  apt install nginx -y
  ```
4. MariaDB-сервер — версия 10.5.26
  ```
  apt -y install mariadb-server mariadb-common
  ```
5. Node и NPM (Push-сервер) — версия 12.22
  ```
  apt install nodejs npm -y
  ```
6. Redis — 6.0.16:
  ```
  apt install redis -y
  ```
