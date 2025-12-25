# Конфигурация Apache

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20402 — Конфигурация PHP](lesson_20402.md)
- [Следующий: 20406 — Конфигурация MariaDB →](lesson_20406.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20404

По умолчанию Apache настроен на дефолтный сайт в каталоге `/var/www/html`.

Основное, что требуется сделать для настройки конфигурации Apache:

- изменить каталог для сайта на `var/www/html/bx-site`;
- изменить порт, который слушает сервис (так как в качестве внешнего сервиса используем nginx);
- импортировать настройки для сайта из виртуальной машины.

Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/alt8.zip). Конфигурационные файлы для Apache находятся в папке: `alt8/httpd2`.

Разместите их в директории `/etc/httpd2/`.

Настроить требуется три файла:

- `conf/ports-available/http.conf` - указать новый порт: **8090**;
- `conf/sites-available/default.conf` - заменить каталог в описании сайта на `var/www/html/bx-site`;
- `conf/httpd2.conf` - изменить группу пользователя на **_webserver**.

Отключите приватный Tmp каталог для сервиса httpd:

```
mkdir /etc/systemd/system/httpd2.service.d
echo -e "[Service]\nPrivateTmp=false\n" > /etc/systemd/system/httpd2.service.d/custom.conf
systemctl daemon-reload
```

После этого запустите сервис:

```
systemctl --now enable httpd2
```
