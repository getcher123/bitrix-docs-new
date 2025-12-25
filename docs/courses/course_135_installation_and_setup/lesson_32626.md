# Конфигурация PHP

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32624 — Конфигурация Nginx](lesson_32624.md)
- [Следующий: 32628 — Конфигурация Apache →](lesson_32628.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=32626

В ОС РОСА централизованное хранилище PHP конфигурации — папка `/etc/php8`.

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

Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/cfg.zip). Конфигурационные файлы для PHP расположены в папке `/cfg/php8/`.

После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/cfg.zip

unzip cfg.zip

		, выполните команду:

```
rsync -av /opt/cfg/php8/ /etc/php8/
```
