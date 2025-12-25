# Конфигурация Apache

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 31590 — Конфигурация PHP](lesson_31590.md)
- [Следующий: 31594 — Конфигурация MariaDB →](lesson_31594.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=31592

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




Основные действия для настройки конфигурации Apache:




- изменить каталог для сайта на /var/www/html/bx-site,
- изменить порт, который слушает сервис (так как в качестве внешнего сервиса используется Nginx),
- импортировать настройки для сайта из виртуальной машины 000-default.conf.




В дефолтной конфигурации /sites-enabled/000-default.conf — это ссылка на файл в каталоге /sites-available.




Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/astra.zip).  Конфигурационные файлы для Apache расположены в папке astra/apache2.





После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/astra.zip

unzip astra.zip

		, выполните команду:




```
rsync -av /opt/astra/apache2/ /etc/apache2/
```




В результате будут настроены следующие файлы:



- ports.conf — изменено значение порта `Listen` на 8090,
- sites-available/000-default.conf — заданы настройки сайта,
- mods-available/php.conf — выполнена конфигурация PHP модуля,
- apache2/apache2.conf - выключен AstraMode.




Отключите листинг каталогов в Apache:




```
a2dismod --force autoindex
```




Включите модуль `rewrite`:




```
a2enmod rewrite
```




Включите PHP модуль:




```
a2enmod php8.2
```




Запустите сервис:




```
systemctl --now enable apache2
```
