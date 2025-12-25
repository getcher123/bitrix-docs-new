# Конфигурация Apache

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3394 — Конфигурация PHP](lesson_3394.md)
- [Следующий: 5014 — Конфигурация MariaDB →](lesson_5014.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=4775

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
- изменить порт, который слушает сервис  (так как в качестве внешнего сервиса используется Nginx),
- импортировать настройки для сайта из виртуальной машины **000-default.conf**.

В дефолтной конфигурации /sites-enabled/000-default.conf — это ссылка на файл в каталоге /sites-available.

Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/debian.zip). Конфигурационные файлы для Apache расположены в папке: debian/apache2.

Загрузите папку debian/apache2 в корневую папку сервера и выполните команду:

```
su -
rsync -av debian/apache2/ /etc/apache2/
```

В результате будут настроены следующие файлы:

- ports.conf — изменено значение порта `Listen` на 8090,
- sites-available/000-default.conf — заданы настройки сайта.

Отключите листинг каталогов в Apache:

```
a2dismod --force autoindex
```

Включите модуль `rewrite`:

```
a2enmod rewrite
```

Запустите сервис:

```
systemctl --now enable apache2
```
