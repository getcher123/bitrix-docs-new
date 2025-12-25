# Конфигурация PHP

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20400 — Конфигурация Nginx](lesson_20400.md)
- [Следующий: 20404 — Конфигурация Apache →](lesson_20404.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20402

В данной версии установки два местоположения для конфигов:

- `/etc/php/7.2/cli/php.d/` настройка CLI;
- `/etc/php/7.2/apache2-mod_php/php.d/` настройки модуля Apache.

Минимально необходимо добавить настройки для модуля Apache:

- для модуля OPCache (файл opcache.ini) укажите:
  ```
  opcache.max_accelerated_files = 100000
  opcache.revalidate_freq = 0
  ```
- и добавьте файл настроек zx-bitrix.ini

Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/alt8.zip). Конфигурационные файлы для PHP находятся в папке: `alt8/php.d`.

Разместите их в директории `/etc/php/7.2/apache2-mod_php/php.d/`.

Можно проверить, что php нашел все модули без проблем и нет ошибок в конфигурации:

```
php -m
```

Создайте каталоги для сессий и загрузки файлов:

```
mkdir /tmp/php_upload /tmp/php_sessions
chown apache2:_webserver /tmp/php_upload /tmp/php_sessions -R
```

Каталоги в `/tmp` находятся под управлением *tmpfiles*, делаем настройку для них:

```
vim /etc/tmpfiles.d/bitrix.conf
----
d /tmp/php_sessions 0770 apache2 _webserver -
d /tmp/php_upload 0770 apache2 _webserver -
----
```
