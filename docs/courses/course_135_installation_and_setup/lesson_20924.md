# Конфигурация PHP

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20922 — Конфигурация Nginx](lesson_20922.md)
- [Следующий: 20926 — Конфигурация Apache →](lesson_20926.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20924

В данной версии установки централизованное хранилище конфигов: `/etc/php.d`.

Минимальные настройки, которые необходимо добавить:

- для модуля **opcache**:
  ```
  opcache.max_accelerated_files = 100000
  opcache.revalidate_freq = 0
  ```
- добавьте настройки **bitrexenv.ini**:
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

Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/redhat8.zip). Конфигурационные файлы для Nginx расположены в папке: `redhat8/php.d`.

Разместите их в директории `/etc/php.d/`.
