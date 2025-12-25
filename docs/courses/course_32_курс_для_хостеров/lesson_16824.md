# Конфигурация NGINX

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 15296 — Установка пакетов](lesson_15296.md)
- [Следующий: 15276 — Конфигурация PHP →](lesson_15276.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=16824

Настройте конфигурацию Nginx:




- Рабочий каталог для сайта — `/var/www/html/bx-site`.
- Пользователь для web окружения — **nginx**, группа **apache**.






Конфигурация NGINX сервера:




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




Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/redos.zip). Конфигурационные файлы для Nginx расположены в папке: `redos/nginx`.




Загрузите папку `redos/nginx` в корневую папку сервера и выполните:




```
rsync -av redos/nginx/ /etc/nginx/
```




В сервисе используются имена для проксирования на определенные службы:




- **httpd** — проксирование запросов на apache
- **push** — проксирование запросов на push-server




Чтобы заработала конфигурация, необходимо прописать их в локальных адресах. Если сервисы расположены на другом хосте, указываем здесь правильный адрес:




```
echo "127.0.0.1 push httpd" >> /etc/hosts
```




Запускаем сервис:




```
systemctl --now enable nginx
```
