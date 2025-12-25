# Конфигурация Apache

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32778 — Конфигурация PHP](lesson_32778.md)
- [Следующий: 32782 — Конфигурация MariaDB →](lesson_32782.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=32780

По умолчанию Apache настроен на дефолтный сайт в каталоге `/var/www/html`.




Основные действия для настройки конфигурации Apache:




- изменить каталог для сайта на `/var/www/html/bx-site`,
- изменить порт, который слушает сервис (так как в качестве внешнего сервиса будет использоваться Nginx),
- импортировать настройки для сайта из виртуальной машины.





Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/alt.zip). Конфигурационные файлы для Apache расположены в папке `/alt/httpd2/`.




После того, как файлы конфигурации

			загружены на сервер

                    cd /opt

wget https://dev.1c-bitrix.ru/docs/chm_files/alt.zip

unzip alt.zip

		, выполните команды:




```
rsync -av /opt/alt/httpd2/ /etc/httpd2/
```




В результате будет настроено три файла:




- `conf/sites-available/default.conf` — в описании сайта заменен каталог на `var/www/html/bx-site`,
- `conf/ports-available/http.conf` — изменено значение порта `Listen` на порт 8090,
- `conf/httpd2.conf` — изменена группа пользователя на `_webserver`.




Включите модуль `rewrite`:




```
a2enmod rewrite
```




Отключите приватный Tmp каталог для сервиса:




```
mkdir /etc/systemd/system/httpd2.service.d
echo -e "[Service]\nPrivateTmp=false\n" > /etc/systemd/system/httpd2.service.d/custom.conf
systemctl daemon-reload
```




Запустите Apache:




```
systemctl --now enable httpd2
```
