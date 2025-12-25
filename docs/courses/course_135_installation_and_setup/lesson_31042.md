# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 31040 — Установка и настройка ОС](lesson_31040.md)
- [Следующий: 31050 — Конфигурация Nginx →](lesson_31050.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=31042

Ниже приведен список всех пакетов, необходимых для установки коробочной версии Битрикс24. Для 1С-Битрикс: Управление сайтом список аналогичен, за исключением Push-сервера.

1. Apache — версия 2.4.62
  ```
  apt install apache2 -y
  ```
2. PHP — версия 8.2
  ```
  apt install php8.2 php8.2-cli php8.2-common php8.2-dev php8.2-gd php8.2-imap php8.2-ldap php8.2-mbstring php8.2-mysql php8.2-opcache php8.2-pspell php8.2-xml php8.2-zip php8.2-amqp php8.2-apcu php-pear -y
  ```
3. Nginx — версия 1.22
  ```
  apt install nginx -y
  ```
4. MariaDB-сервер — версия 10.11.6
  ```
  apt install mariadb-server mariadb-common -y
  ```
5. Node и NPM (Push-сервер) — версия 18.19.0
  ```
  apt install nodejs npm -y
  ```
6. Redis — 7.0.15:
  ```
  apt install redis-server -y
  ```

Перечисленные пакеты доступны и устанавливаются из дефолтного репозитория Debian 12. Если вам нужно установить другое ПО, например PHP версии 8.3, то следует подключить сторонний репозиторий.

Пример настройки репозитория от Яндекса:

```

cd /opt
wget https://mirror.yandex.ru/mirrors/packages.sury.org/php/apt.gpg
mv apt.gpg /etc/apt/trusted.gpg.d/php.gpg
echo "deb https://mirror.yandex.ru/mirrors/packages.sury.org/php/ bookworm main" | tee /etc/apt/sources.list.d/surry-mirror.list
apt update && apt upgrade
```
