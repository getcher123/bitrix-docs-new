# Конфигурация push-server

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 16788 — Конфигурация Redis](lesson_16788.md)
- [Следующий: 6455 — Конфигурация сайта →](lesson_6455.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=2381

Схема работы:




```
 -----------------------                                   ---------------------------------------------------
| nginx: 0.0.0.0:80     | -> /bitrix/sub|/bitrix/subws -> | node server.js --config push-server-sub-80XX.json |
 -----------------------                                   ---------------------------------------------------

 -----------------------                     ---------------------------------------------------
| nginx: 127.0.0.1:8895 | -> /bitrix/pub -> | node server.js --config push-server-pub-90XX.json |
 -----------------------                     ---------------------------------------------------
```




Nginx проксирует запрос на push-сервис выбранного типа. Запросы получения сообщений (например, sub) - публичные и проксируются со стандартных портов 80/443, запросы публикации (pub) доступны только с внутреннего адреса сервера.





Процессы Nodejs делятся на два типа:




- Отвечающие за подключение пользователя к выбранному каналу и получение им сообщений. Они слушают порты 8010-8015
- Отвечающие за отправку сообщения в канал. Они слушают порты 9010-9011.




Для запуска push-server понадобится:



- nodejs и npm,
- архив сервиса и его модулей.




Скачайте архив:




```
su -
cd /opt
wget https://repo.bitrix24.tech/vm/push-server-0.3.0.tgz
npm install --production ./push-server-0.3.0.tgz
```




Установка закончится строкой:




```
added 1 package, and audited 145 packages in 13s

16 packages are looking for funding
  run `npm fund` for details
```




Для удобства можно использовать:




```
ln -sf /opt/node_modules/push-server/etc/push-server /etc/push-server
```




Скопируйте файлы сервиса и основной конфиг:




```
su -
cd /opt/node_modules/push-server
cp etc/init.d/push-server-multi /usr/local/bin/push-server-multi
mkdir /etc/sysconfig
cp etc/sysconfig/push-server-multi  /etc/sysconfig/push-server-multi
cp etc/push-server/push-server.service  /etc/systemd/system/
ln -sf /opt/node_modules/push-server /opt/push-server
```




Редактируйте конфигурационный файл `/etc/sysconfig/push-server-multi`. Нужно исправить/добавить параметры:




- SECURITY_KEY - cекретный ключ для подписи соединения между клиентом и пуш-сервером,
- RUN_DIR - используется для хранения pid файлов процесса,
- USER/GROUP - пользователь, под которым будет запущен сервис,
- REDIS_SOCK - сокет, который использует Redis сервис.




Пример




```
GROUP=www-data
SECURITY_KEY="PUTTHEPRIVATEKEYHERE"
RUN_DIR=/tmp/push-server
REDIS_SOCK=/var/run/redis/redis.sock
```




Создайте пользователя:




```
useradd -g www-data bitrix
```




Каждый nodejs процесс будет запущен как отдельный процесс. Сгенерируйте конфиги:




```
/usr/local/bin/push-server-multi configs pub
/usr/local/bin/push-server-multi configs sub
```




Создайте каталог через *tmpfiles.d*.




```
echo 'd /tmp/push-server 0770 bitrix www-data -' > /etc/tmpfiles.d/push-server.conf
systemd-tmpfiles --remove --create
```




Создайте каталог логов:




```
[[ ! -d /var/log/push-server ]] && mkdir /var/log/push-server
chown bitrix:www-data /var/log/push-server
```




Измените пользователя в конфигурационном файле сервиса `/etc/systemd/system/push-server.service`:




```
[Service]
User=bitrix
Group=www-data
ExecStart=/usr/local/bin/push-server-multi systemd_start
ExecStop=/usr/local/bin/push-server-multi stop
...
```




Переконфигурируйте




```
systemctl daemon-reload
```




и затем запустите сервис:




```
systemctl --now enable push-server
```




В

			настройках push модуля

                    Настройки производятся на странице http://_имя_сайта_/bitrix/admin/settings.php?lang=ru&mid=pull


![Нажмите на рисунок, чтобы увеличить](../../../images/courses/32/dev.1c-bitrix.ru/images/admin_start/install/other-environent/deb_push-server-settings_sm.png)


[Подробнее](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=2033)...

		 в административном разделе сайта включите использование

			локального пуш сервера (последняя версия)

                    ![Нажмите на рисунок, чтобы увеличить](../../../images/courses/41/dev.1c-bitrix.ru/images/admin_expert/pull/pnp_admin_localserver_sm.png).

		. Дополнительно нужно будет указать секретный ключ, который вы настраивали в файле `/etc/sysconfig/push-server`.
