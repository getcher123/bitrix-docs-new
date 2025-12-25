# Конфигурация PHP

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5335 — Конфигурация Nginx](lesson_5335.md)
- [Следующий: 5407 — Конфигурация Apache →](lesson_5407.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=3730

В данной версии установки централизованное хранилище конфигов (для версии php 8.0):

```
/etc/php/8.0
|       |-> php.ini
```

Как минимум, нам нужно добавить настройки для следующих опций:

- для модуля **opcache**
  ```
  opcache.max_accelerated_files = 100000
  opcache.revalidate_freq = 0
  ```
- добавляем настройки **bitrexenv.ini**
  ```
  display_errors = Off
  error_reporting = E_ALL
  error_log = '/var/log/php/error.log'
  ; Set some more PHP parameters
  enable_dl = Off
  short_open_tag = On
  allow_url_fopen = On
  # Security headers
  mail.add_x_header = Off
  expose_php = Off
  ...
  ```

Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/astra.zip).  Конфигурационные файлы для **PHP** размещены в папке `astra/php.d`

```
su -
cd bx-os/astra

# добавляем конфиг для opcache
cat ./php.d/opcache.ini  >> /etc/php/8.0/php.ini

# остальные настройки
cat ./php.d/zbx-bitrix.ini  >> /etc/php/8.0/php.ini

# создаем каталог для логов
mkdir /var/log/php
chown www-data:www-data /var/log/php
```
