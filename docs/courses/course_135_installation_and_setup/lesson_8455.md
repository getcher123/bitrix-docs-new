# Конфигурация Nginx

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5321 — Установка пакетов](lesson_5321.md)
- [Следующий: 3394 — Конфигурация PHP →](lesson_3394.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=8455

Настройте конфигурацию Nginx:

- рабочий каталог для сайта — /var/www/html/bx-site,
- пользователь для web-окружения — www-data, группа — www-data.

Конфигурация сервера Nginx:

```
/etc/nginx/nginx.conf                                       # основной конфигурационный файл
            |_conf.d/upstreams.conf                         # конфигурация для upstream серверов: apache && push-server
            |_conf.d/maps-composite_settings.conf           # параменные используемые для кеша
            |_conf.d/maps.conf                              # дополнительные переменные
            |_conf.d/http-add_header.conf                   # CORS заголовки
            |_sites-available/*.conf                        # подключаем сайты
                              |_default.conf                # сайт по умолчанию (настраиваем только 80 порт)
                                    |_conf.d/bx_temp.conf   # конфигурация BX_TEMPORARY_FILES_DIRECTORY
                                    |_conf.d/bitrix.conf    # дефолтная конфигурация сайта
                              |_rtc.conf                    # проксирование запросов на push-server (публикация)
```

Дефолтная конфигурация сайта:

```
conf.d/bitrix.conf                                          # основный блоки со включенным по умолчанию кешем в файлах
        |_conf.d/bitrix_general.conf                        # отдача статики, быстрая отдача для внешних хранилищ и прочее
                |_conf.d/errors.conf                        # обработка ошибок
                |_conf.d/im_subscrider.conf                 # проксирование запросов на push-server (получение)
                |_conf.d/bitrix_block.conf                  # блокировки по умолчанию
```

Конфигурация взята из виртуальной машины и может показаться избыточной, но фактически поддерживает все возможности, что и виртуальная машина.

Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/debian.zip). Конфигурационные файлы для Nginx расположены в папке: debian/nginx.

Загрузите папку debian/nginx в корневую папку сервера и выполните команду:

```
su -
rsync -av debian/nginx/ /etc/nginx/
```

В сервисе используются имена для проксирования:

- `httpd` — проксирование запросов на Apache,
- `push` — проксирование запросов на Push-сервер.

Чтобы заработала конфигурация, пропишите имена в локальных адресах:

```
echo "127.0.0.1 push httpd" >> /etc/hosts
```

Если сервисы расположены на другом хосте, укажите правильный IP-адрес.

По умолчанию в Debian сервер Apache использует 80 порт и поставлен на автозапуск. Поэтому перед запуском сервера Nginx на время выключите Apache (на данный момент он еще не настроен). Остановите Apache:

```
systemctl stop apache2
```

Запустите Nginx:

```
systemctl --now enable nginx
```
