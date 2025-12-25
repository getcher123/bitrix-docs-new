# Конфигурация сайта

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 9673 — Конфигурация Push-server](lesson_9673.md)
- [Следующий: 15270 — Установка и настройка ОС →](lesson_15270.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=9467

### Сайт




Создайте рабочий каталог и загрузите скрипт BitrixSetup:




```
mkdir /var/www/html/bx-site
cd /var/www/html/bx-site
wget https://www.1c-bitrix.ru/download/scripts/bitrixsetup.php
chown apache:apache /var/www/html/bx-site -R
```




Аналогичным образом можно скачать нужный дистрибутив и установить его в каталог /var/www/html/bx-site.




Получите доступ к оболочке БД. Создайте базу данных и пользователя:




```
create database portal;
CREATE USER 'bitrix'@'localhost' IDENTIFIED BY 'PASSWORD';
GRANT ALL PRIVILEGES ON portal.* to 'bitrix'@'localhost';
```




Замените `PASSWORD` на пароль, который будете использовать для доступа к БД.




Выполните [установку](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&CHAPTER_ID=04888) продукта.





### Push-server




Для работы портала необходимо настроить push-server. Сервис запущен, необходимо сделать настройки.




Настройки могут быть выполнены через

			административный раздел портала

                    Настройки производятся на странице http://имя_сайта/bitrix/admin/settings.php?lang=ru&mid=pull



[Подробнее](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=2033)...

		 или с помощью конфигурационного файла. Покажем, как это делается вторым способом.




Исправьте [конфигурационный файл](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=02795) /var/www/html/bx-site/bitrix/.settings.php, добавив следующую секцию:




```
return array (
'pull' => Array(
    'value' =>  array(
        'path_to_listener' => 'http://#DOMAIN#/bitrix/sub/',
        'path_to_listener_secure' => 'https://#DOMAIN#/bitrix/sub/',
        'path_to_modern_listener' => 'http://#DOMAIN#/bitrix/sub/',
        'path_to_modern_listener_secure' => 'https://#DOMAIN#/bitrix/sub/',
        'path_to_mobile_listener' => 'http://#DOMAIN#:8893/bitrix/sub/',
        'path_to_mobile_listener_secure' => 'https://#DOMAIN#:8894/bitrix/sub/',
        'path_to_websocket' => 'ws://#DOMAIN#/bitrix/subws/',
        'path_to_websocket_secure' => 'wss://#DOMAIN#/bitrix/subws/',
	'path_to_publish' => 'http://localhost:8895/bitrix/pub/',
        'path_to_publish_web' => 'http://#DOMAIN#/bitrix/rest/',
        'path_to_publish_web_secure' => 'https://#DOMAIN#/bitrix/rest/',
        'nginx_version' => '4',
        'nginx_command_per_hit' => '100',
        'nginx' => 'Y',
        'nginx_headers' => 'N',
        'push' => 'Y',
        'websocket' => 'Y',
        'signature_key' => 'PUTTHEPRIVATEKEYHERE',
        'signature_algo' => 'sha1',
        'guest' => 'N',
    ),
),
...
```




Параметр `signature_key` должен содержать тот же ключ, который вы указали в /etc/sysconfig/push-server-multi в соответствующем параметре. Если все хорошо, то после перезапуска httpd:


```
systemctl restart httpd
```




Вы увидите запросы к Push-серверу:




```
Request URL: ws://sitename/bitrix/subws/?CHANNEL_ID=....
Request Method: GET
Status Code: 101 Switching Protocols
```
