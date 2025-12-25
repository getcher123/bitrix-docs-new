# Конфигурация PHP

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 31050 — Конфигурация Nginx](lesson_31050.md)
- [Следующий: 31054 — Конфигурация Apache →](lesson_31054.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=31052

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






Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/debian.zip). Конфигурационные файлы для PHP расположены в папке debian/php.d.








После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/debian.zip

unzip debian.zip

		, выполните команды:




```

rsync -av /opt/debian/php.d/ /etc/php/8.2/mods-available/

ln -sf /etc/php/8.2/mods-available/zbx-bitrix.ini  /etc/php/8.2/apache2/conf.d/99-bitrix.ini
ln -sf /etc/php/8.2/mods-available/zbx-bitrix.ini  /etc/php/8.2/cli/conf.d/99-bitrix.ini

mkdir /var/log/php
chown -R www-data:www-data /var/log/php
```
