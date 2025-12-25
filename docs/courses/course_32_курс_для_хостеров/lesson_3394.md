# Конфигурация PHP

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8455 — Конфигурация Nginx](lesson_8455.md)
- [Следующий: 4775 — Конфигурация Apache →](lesson_4775.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=3394

В данной версии централизованное хранилище PHP конфигурации — папка /etc/php/8.3 (для версии PHP 8.3):




```
/etc/php/8.3
|---- apache2
|       |-> conf.d/
|       |-> php.ini
|---- cli
|       |-> conf.d/
|       |-> php.ini
|---- mods-available
        |-> .ini
```




Файлы conf.d внутри каталогов /apache2 и /cli содержат ссылки на mods-available. То есть в дефолтной конфигурации и модуль apache2, и командная строка будут содержать одинаковый набор модулей с одинаковыми параметрами.




Минимальные настройки, которые необходимо добавить:




- для модуля opcache:
  ```
  opcache.max_accelerated_files = 100000
  opcache.revalidate_freq = 0
  ```
- настройки zbx-bitrix.ini:
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






Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/debian.zip). Конфигурационные файлы для PHP расположены в папке: debian/php.d.







Загрузите папку debian/php.d в корневую папку сервера и выполните команды:




```
su -
rsync -av debian/php.d/ /etc/php/8.3/mods-available/

ln -sf /etc/php/8.3/mods-available/zbx-bitrix.ini  /etc/php/8.3/apache2/conf.d/99-bitrix.ini
ln -sf /etc/php/8.3/mods-available/zbx-bitrix.ini  /etc/php/8.3/cli/conf.d/99-bitrix.ini
```
