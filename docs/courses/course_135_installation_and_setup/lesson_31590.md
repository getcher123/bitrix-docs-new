# Конфигурация PHP

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 31588 — Конфигурация Nginx](lesson_31588.md)
- [Следующий: 31592 — Конфигурация Apache →](lesson_31592.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=31590

В данной версии централизованное хранилище PHP конфигурации — папка /etc/php/8.2 (для версии PHP 8.2):

```
/etc/php/8.2
|---- apache2
|       |-> conf.d/
|       |-> php.ini
|---- cli
|       |-> conf.d/
|       |-> php.ini
|---- mods-available
        |-> .ini
```

Минимальные настройки, которые необходимо добавить:

- для модуля opcache
  ```
  opcache.max_accelerated_files = 100000
  opcache.revalidate_freq = 0
  ```
- настройки zbx-bitrix.ini
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

Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/astra.zip). Конфигурационные файлы для PHP  расположены в папке astra/php.d.

После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/astra.zip

unzip astra.zip

		, выполните команды:

```

cd /opt/astra/php.d/
cat opcache.ini >> /etc/php/8.2/apache2/conf.d/bitrix.ini
cat zbx-bitrix.ini >> /etc/php/8.2/apache2/conf.d/bitrix.ini
mkdir /var/log/php
chown -R www-data:www-data /var/log/php
```
