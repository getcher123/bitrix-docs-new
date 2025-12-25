# Конфигурация PHP

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 16824 — Конфигурация NGINX](lesson_16824.md)
- [Следующий: 15298 — Конфигурация Apache →](lesson_15298.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=15276

В данной версии установки централизованное хранилище конфигов: `/etc/php.d`.

Минимальные настройки, которые необходимо добавить:

- для модуля **opcache**:
  ```
  opcache.max_accelerated_files = 100000
  opcache.revalidate_freq = 0
  ```
- Настройки файла **zx-bitrix.ini**:
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

Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/redos.zip). Конфигурационные файлы для PHP расположены в папке: `redos/php.d`. Загрузите папку на сервер и выполните:

```
su -
rsync -av redos/php.d/ /etc/php.d/
```
