# Конфигурация Nginx

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 32492 — Установка пакетов](lesson_32492.md)
- [Следующий: 32546 — Конфигурация PHP →](lesson_32546.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=32494

Настройте конфигурацию Nginx:

- рабочий каталог для сайта — `/var/www/html/bx-site`,
- пользователь для web-окружения — `_nginx`, группа — `_webserver`.

Конфигурация сервера Nginx:

```
/etc/nginx/nginx.conf                                       # основной конфигурационный файл
            |_conf.d/upstreams.conf                         # конфигурация для upstream серверов: apache && push-server
            |_conf.d/maps-composite_settings.conf           # переменные используемые для кеша
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

Все конфигурационные файлы можно [скачать в архиве](https://dev.1c-bitrix.ru/docs/chm_files/alt.zip). Конфигурационные файлы для Nginx расположены в папке `/alt/nginx/`.

Чтобы скачать и распаковать на сервере файлы конфигурации, можно выполнить команды:

```
cd /opt
wget https://dev.1c-bitrix.ru/docs/chm_files/alt.zip
unzip alt.zip
```

Скопируйте файлы конфигурации в папку `/etc/nginx/`.

```

 rsync -av /opt/alt/nginx/ /etc/nginx/
```

В сервисе используются имена для проксирования:

- `httpd` — проксирование запросов на Apache,
- `push` — проксирование запросов на Push-сервер.

Чтобы заработала конфигурация, пропишите имена в локальных адресах:

```
echo "127.0.0.1 push httpd" >> /etc/hosts
```

Если сервисы расположены на другом хосте, укажите правильный IP-адрес.

Запустите Nginx:

```
systemctl --now enable nginx
```
