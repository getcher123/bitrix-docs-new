# Конфигурация Apache

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 9229 — Конфигурация PHP](lesson_9229.md)
- [Следующий: 9859 — Конфигурация MariaDB →](lesson_9859.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=9861

По умолчанию Apache настроен на дефолтный сайт в каталоге /var/www/html.

Основные действия для настройки конфигурации Apache:

- изменить каталог для сайта на /var/www/html/bx-site,
- изменить порт, который слушает сервис (так как в качестве внешнего сервиса будет использоваться Nginx),
- импортировать настройки для сайта из виртуальной машины.



Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/redos.zip). Конфигурационные файлы для Apache расположены в папке: redos/httpd2.

Загрузите папку redos/httpd2 в корневую папку сервера и выполните команду:

```
su -
rsync -av redos/httpd2/ /etc/httpd/
```

В результате будет настроено три файла:

- conf.d/default.conf — в описании сайта заменен каталог на var/www/html/bx-site,
- conf/httpd.conf — изменено значение порта `Listen` на порт 8090,
- conf.modules.d/00-mpm.conf — заменен `mpm event` на `prefork`.

Запустите Apache:

```
systemctl --now enable httpd
```
