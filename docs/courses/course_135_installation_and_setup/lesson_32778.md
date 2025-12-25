# Конфигурация PHP

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32776 — Конфигурация Nginx](lesson_32776.md)
- [Следующий: 32780 — Конфигурация Apache →](lesson_32780.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=32778

В АЛЬТ 11 хранилище PHP конфигурации версии 8.3 расположено в папках:

- `/etc/php/8.3/cli/php.d/` — настройка CLI,
- `/etc/php/8.3/apache2-mod_php/php.d/` — настройки модуля Apache.

Минимальные настройки, которые необходимо добавить:

- для модуля opcache:
  ```
  opcache.max_accelerated_files = 100000
  opcache.revalidate_freq = 0
  ```
- настройки файла zx-bitrix.ini:
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

Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/alt.zip). Конфигурационные файлы для PHP расположены в папке `/alt/php.d/`.

После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/alt.zip

unzip alt.zip

		, выполните команды:

```
rsync -av /opt/alt/php.d/ /etc/php/8.3/apache2-mod_php/php.d/
```

Проверите, что PHP нашел все модули, и нет ошибок в конфигурации:

```
php -m
```

Создайте каталоги для сессий и загрузки файлов:

```
mkdir /tmp/php_upload /tmp/php_sessions
chown apache2:_webserver /tmp/php_upload /tmp/php_sessions -R
```

Каталоги в `/tmp/` находятся под управлением *tmpfiles*. Cделайте настройку для них:

```
vim /etc/tmpfiles.d/bitrix.conf
----
d /tmp/php_sessions 0770 apache2 _webserver -
d /tmp/php_upload 0770 apache2 _webserver -
----
```
