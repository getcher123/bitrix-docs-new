# Настройка Front-end NGINX

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3366 — Пример: число процессов веб-сервера](lesson_3366.md)
- [Следующий: 3368 — Отдача графики напрямую NGINX →](lesson_3368.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=3367

### Конфигурационный файл




Каталог с конфигурацией NGINX - `/etc/nginx`. Рассмотрим его конфигурационный файл `/etc/nginx/nginx.conf`:



```

        user    bitrix;  #пользователь, под которым работает nginx. Желательно совпадение с пользователем apache
        worker_processes  8; #8 одновременных процессов
        error_log  /var/log/nginx/error.log warn;
        pid        /var/run/nginx.pid;
        worker_rlimit_nofile 10240;  #максимальное число открытых файлов

        events {
                use epoll;
                worker_connections  10240; #максимальное число соединений с одним процессом. Система может одновременно работать с max_clients = worker_processes * worker_connections, т.е. с 81920 соединений, в том числе статических файлов
        }

        http {
                include       /etc/nginx/mime.types;
                default_type  application/octet-stream;
#формат логов
                log_format  main  '$remote_addr - $remote_user [$time_local] $status'
                                '"$request" $body_bytes_sent "$http_referer" '
                                '"$http_user_agent" "$http_x_forwarded_for"';
                log_format      common  '$remote_addr - - [$time_local] "$request" $status $bytes_sent "$http_referer" "$http_user_agent" $msec';

                access_log  /var/log/nginx/access.log  common;
                sendfile        on;
                tcp_nopush     on;
                tcp_nodelay    on;
                client_max_body_size       10m; # максимально допустимый размер тела запроса клиента, указываемый в строке "Content-Length" в заголовке запроса
                client_body_buffer_size    128k;
                proxy_connect_timeout      300; #время на ожидание соединения
                proxy_send_timeout         300;
                proxy_read_timeout         300;
                proxy_buffer_size          64k;
                proxy_buffers              8 64k;
                proxy_busy_buffers_size    64k;
                proxy_temp_file_write_size 10m;
                gzip on; #сжимать передаваемые данные
                gzip_proxied any;
                gzip_types application/x-javascript text/css;

        server { #виртуальный хост
                listen 80; #порт 80
                server_name bitrix; #адрес узла. Если узел всего один – можно написать любой
                server_name_in_redirect off; #лучше поставить в ON – передавать запрошенное имя сайту
                access_log /var/log/nginx/access.log common;
                index index.php;
                error_page 500 502 503 504 /500.html;
                error_page 404 = /404.php;
#установить дополнительные заголовки для определения адреса клиента в статистике сайта
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $host:80;
                client_max_body_size 1024M; #максимальный размер передаваемого файла
                client_body_buffer_size 4M;
                root /var/www; #корневая папка сайта

#включить https режим при нахождении в корне сайта файла .htsecure
                if (-f /home/bitrix/www/.htsecure) {
                        rewrite ^(.*)$ https://$host$1 permanent;
                }

#выбрать, какие данные пересылать backend серверу, а какие – показывать напрямую
#в данной конфигурации все пересылается backend серверу
#обилие вариантов потребовалось компании Битрикс для того, чтобы при добавлении в конфигурацию отдачу статических файлов напрямую через NGINX динамические запросы на псевдостатические файлы все-таки перенаправлялись на backend
                location / { expires 3d;
                                if ($request_method = OPTIONS ) {
                                        proxy_pass http://127.0.0.1:8888;
                                        }
                                if ($request_method = PROPFIND ) {
                                        proxy_pass http://127.0.0.1:8888;
                                        }
                                if ($request_method = PROPPATCH ) {
                                        proxy_pass http://127.0.0.1:8888;
                                        }
                                if ($request_method = MKCOL ) {
                                        proxy_pass http://127.0.0.1:8888;
                                        }
                                if ($request_method = COPY ) {
                                        proxy_pass http://127.0.0.1:8888;
                                        }
                                if ($request_method = MOVE ) {
                                        proxy_pass http://127.0.0.1:8888;
                                        }
                                if ($request_method = LOCK ) {
                                        proxy_pass http://127.0.0.1:8888;
                                        }
                                if ($request_method = UNLOCK ) {
                                        proxy_pass http://127.0.0.1:8888;
                                        }
                        }

                location ~ ^(/extranet/docs|/docs|/workgroups|/company/profile|/bitrix/tools|/company/personal/user).*/$ {
                        proxy_pass         http://127.0.0.1:8888;
                        }

                location ~ ^(/extranet/docs|/docs|/workgroups|/company/profile|/bitrix/tools|/company/personal/user) {
                        if (-d $request_filename) {
                            rewrite  ^(.*)(/*)$  $1/  last;
                        }
                        proxy_pass         http://127.0.0.1:8888;
                        }

                location ~ ^(/bitrix/html_pages)
                        {
                        root /var/www;
                        index index@.html;
                        if (!-f $request_filename)
                                {
                                rewrite ^/bitrix/html_pages(.*)@(.*)\.html$ $1.php?$2 break;
                                rewrite ^/bitrix/html_pages(.*)\.html$ $1\.php break;
                                proxy_pass http://127.0.0.1:8888;
                                }
                        }

                location ~ \.php$ {
                                root        /var/www;
                                if ($request_method = POST ) {
                                        break;
                                        proxy_pass http://127.0.0.1:8888;
                                        }
                                if ($http_cookie !~ "PHPSESSID=" ) {
                                        rewrite ^(.*)\.php$ /bitrix/html_pages$1@$args.html? last;
                                        }
                                proxy_pass http://127.0.0.1:8888;
                                }

                location ~ /$ {
                                root        /var/www;
                                if ($request_method = POST ) {
                                        break;
                                        proxy_pass http://127.0.0.1:8888;
                                        }
                                if ($http_cookie !~ "PHPSESSID=" ) {
                                        rewrite ^(.*)/$ /bitrix/html_pages$1/index@$args.html? last;
                                        }
                                proxy_pass http://127.0.0.1:8888;
                                }

                location ~ (/|\.php|\.asmx|/rest.*)$ {
                        proxy_pass         http://127.0.0.1:8888;
                        }
                location ~ /\.ht {
                        deny  all;
                        }
                location ~ /favicon.ico {
                        proxy_pass         http://127.0.0.1:8888;
                        }

                location ~ ^(/bitrixsetup\.php)$ {
                    proxy_pass         http://127.0.0.1:8888;
                    proxy_buffering off;
                }

        }
#аналогичная конфигурация для https (удалена)
}
```



В данной конфигурации настройка NGINX проведена так, что все обращения к серверу будут перенаправляться на **Back-end** сервер. Однако, можно избранные файлы отдавать через NGINX. В этом случае будет достигнуто дополнительное увеличение производительности.






### Некоторые нюансы настройки






```
# cat /proc/cpuinfo | grep "processor" | wc -l
worker_processes 8;
```




Регулируем размер очереди, который мы можем обрабатывать **worker_processes**. Разработчики NGINX рекомендуют устанавливать количество рабочих процессов равным количеству процессоров или ядер в системе. Например, если система имеет 2 физических процессора по 4 ядра каждый — рекомендуется указать `worker_processes 8;`.




```
# max_clients = worker_processes * worker_connections
events {
        use epoll;
        worker_connections  10240;
}
```




**worker_connections** - сколько запросов одновременно может обрабатывать один процесс. NGINX легкий и надёжный. Он способен выдержать такое число. В результате общее число коннектов, которые будут обрабатываться - это значение **worker_processes** умноженное на значение **worker_connections**.




```
# больше - больше памяти, меньше - чаще пишем на диск
client_body_buffer_size 4m;
```




**client_body_buffer_size** отвечающий за то как часто будет производиться запись на диск (а не держать из в памяти) при загрузке пользователями каких-то данных на сервер. При достаточно большой памяти можно установить это значение побольше, чтобы реже писать на диск и слегка разгрузить систему.




```
# максимально быстро получаем ответ от бэкенда
proxy_buffering on;
```




Включение **proxy_buffering** позволяет облегчить работу с клиентами с медленными каналами. Такие клиенты будут медленно соединяться с NGINX, медленно от него получать данные. Но сам frontend данные с backend'а получает быстро и не загружает веб-сервер.




```
gzip            on;
gzip_proxied    any;
gzip_static     on;
gzip_types      application/x-javascript text/css;
gzip_min_length 1100;
```




Обязательно включайте сжатие статики, что также ускорит отдачу данных.





Дополнительную информацию по настройке NGINX вы можете получить на сайте [www.nginx.ru](http://www.nginx.ru) и [wiki.nginx.org](http://wiki.nginx.org).
