# Конфигурация Apache

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3730 — Конфигурация PHP](lesson_3730.md)
- [Следующий: 16786 — Конфигурация MariaDB →](lesson_16786.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=5407

По умолчанию конфигурация Apache устроена следующим образом:




```
#   /etc/apache2/
#   |-- apache2.conf
#   |   `--  ports.conf
#   |-- mods-enabled
#   |   |-- *.load
#   |   `-- *.conf
#   |-- conf-enabled
#   |   `-- *.conf
#   `-- sites-enabled
#       |-- 000-default.conf
#       `-- *.conf
```




Основное, что нужно изменить:




- каталог для сайта `/var/www/html/bx-site`,
- порт, который слушает сервис (так как в качестве внешнего сервиса используем nginx),
- для сайта импортируем настройки из виртуальной машины **000-default.conf**. Замечание: В дефолтной конфигурации `sites-enabled/000-default.conf` - это ссылка на файл в каталоге `/sites-available`.




Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/astra.zip).  Конфигурационные файлы для **Apache** размещены в папке `astra/apache2`





```
rsync -av astra/apache2/ /etc/apache2/
```




Настройте следующие файлы:




- **ports.conf** - смена Listen на 8090
- `sites-available/000-default.conf` - настройки сайта
- `mods-available/php.conf` - конфгурация php модуля
- `apache2/apache2.conf` - выключаем AstraMode




Отключите листинг каталогов в Apache:




```
a2dismod --force autoindex
```




Включите модуль rewrite:




```
a2enmod rewrite
```




Включите php модуль:




```
a2enmod php
```




Запустите сервис:




```
systemctl --now enable apache2
```
