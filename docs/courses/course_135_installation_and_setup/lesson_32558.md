# Конфигурация сайта

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32556 — Конфигурация Push-server](lesson_32556.md)
- [Следующий: 32772 — Установка и настройка ОС →](lesson_32772.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=32558

### Сайт

Выбор дистрибутива продукта зависит от СУБД на сервере: MariaDB или PostgreSQL.

#### MariaDB

Создайте рабочий каталог и загрузите скрипт BitrixSetup:

```
mkdir /var/www/html/bx-site
cd /var/www/html/bx-site
wget https://www.1c-bitrix.ru/download/scripts/bitrixsetup.php
chown apache2:_webserver /var/www/html/bx-site -R
```

Аналогичным образом можно скачать дистрибутив с сайта компании 1С-Битрикс и распаковать его в каталог `/var/www/html/bx-site`.

#### PostgreSQL

- Создайте рабочий каталог.
- Скачайте дистрибутив продукта с сайта компании 1С-Битрикс, например, [«1С-Битрикс24» - Энтерпрайз для Постгрес](https://www.1c-bitrix.ru/download/portal/bitrix24_enterprise_postgresql_encode.zip).
- Распакуйте его в каталог `/var/www/html/bx-site`.

```
mkdir /var/www/html/bx-site
cd /var/www/html/bx-site
wget https://www.1c-bitrix.ru/download/portal/bitrix24_enterprise_postgresql_encode.zip
unzip bitrix24_enterprise_postgresql_encode.zip
chown apache2:_webserver /var/www/html/bx-site -R
```

#### Установка продукта

Выполните установку продукта, как описано в главе [Установка продуктов «1С-Битрикс»](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&CHAPTER_ID=04888). На этапе создания базы данных укажите ваши параметры подключения к базе.

![](../../../images/courses/135/dev.1c-bitrix.ru/images/admin_start/install/install_db.png)

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

Параметр `signature_key` должен содержать тот же ключ, который вы указали в `/etc/sysconfig/push-server-multi` в соответствующем параметре. Если все хорошо, то после перезапуска httpd:

```
systemctl restart httpd2
```

Вы увидите запросы к Push-серверу:

```
Request URL: ws://sitename/bitrix/subws/?CHANNEL_ID=....
Request Method: GET
Status Code: 101 Switching Protocols
```
