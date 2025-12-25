# Проксирование запросов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 29424 — Настройка сервера](lesson_29424.md)
- [Следующий: 29430 — Провайдеры →](lesson_29430.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=29426

**Внимание!** Приведённые настройки выходят за рамки меню Виртуальной машины. Это означает, что информация — ознакомительная и применять её следует с чётким пониманием того что вы делаете и с собственной ответственностью за совершаемые действия. В нашей техподдержке рассматриваются только вопросы по работе пунктов меню ВМ.




Предположим, что в качестве внешнего прокси выступает nginx сервер.


При желании можно данные настройки адаптировать и для других прокси-сервисов.




### Push-server




Вне зависимости от того, как организована у вас работа балансера — единственная точка входа или он обслуживает только запросы клиентов из внешних сетей, а BitrixVM запросы внутренней сети — на него нужно перенести настройки Push-server.




Переносим настройки проксирования запросов push на балансер — можно взять конфигурационный файл виртуальной машины **/etc/nginx/bx/conf/im_subscrider.conf** за основу (можно прям его скопировать на балансер):




```

location ~* ^/bitrix/subws/ {
    access_log off;
    proxy_pass http://nodejs_sub;
    # 12h+0.5
    proxy_max_temp_file_size 0;
    proxy_read_timeout  43800;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $replace_upgrade;
    proxy_set_header Connection $connection_upgrade;
}

location ~* ^/bitrix/sub/ {
    access_log off;
    rewrite ^/bitrix/sub/(.*)$ /bitrix/subws/$1 break;
    proxy_pass http://nodejs_sub;
    proxy_max_temp_file_size 0;
    proxy_read_timeout  43800;
}

location ~* ^/bitrix/rest/ {
    access_log off;
    proxy_pass http://nodejs_pub;
    proxy_max_temp_file_size 0;
    proxy_read_timeout  43800;
}
```




Данный файл подключаем к серверу, на котором настроено проксирование запросов на виртуальную машину.






Верхний конфигурационный файл зависит от **/etc/nginx/bx/settings/rtc-im_settings.conf**, в котором определяются следующие параметры:


- передача заголовков `Upgrade` и `Connection` через переменные:
  ```
  # if connection ti not set
  map $http_upgrade $connection_upgrade {
    default upgrade;
    '' 'close';
  }
  map $http_upgrade  $replace_upgrade {
    default $http_upgrade;
    ''      "websocket";
  }
  ```
- upstream-server
  ```
  upstream nodejs_sub {
    ip_hash;
    keepalive 1024;
    server push:8010;
    server push:8011;
    server push:8012;
    server push:8013;
    server push:8014;
    server push:8015;
  }
  upstream nodejs_pub {
    ip_hash;
    keepalive 1024;
    server push:9010;
    server push:9011;
  }
  ```




Данный файл **/etc/nginx/bx/settings/rtc-im_settings.conf** тоже можно скопировать и подключить на уровне `http`-секции на балансере.




**Важно!** В файле **/etc/nginx/bx/settings/rtc-im_settings.conf** указано имя push-сервера, в рамках виртуальной машины BitrixVM все имена серверов пула прописаны в **/etc/hosts**. Внешний балансер об этом ничего не знает, поэтому нужно или прописать соответствие в hosts-файл балансера, или поменять настройку на IP-адрес push-сервера.






Далее на push-server необходимо открыть порты **8010-8015** и **9010-9011** для доступа с балансера.




**firewalld**:



```

firewall-cmd --permanent --add-port=8010-8015/tcp
firewall-cmd --permanent --add-port=9010-9011/tcp
firewall-cmd --reload
```






### HTTPS доступ




Предположим, мы проксируем http и https сайта **test.example.org** на **80** порт виртуальной машины BitrixVM.




Включим модуль **real_ip** в BitrixVM — создаем конфигурационный файл **bx/settings/real_ip.conf**:


```

set_real_ip_from BALANCER_IP;
real_ip_header X-Forwarded-For;
```




В качестве `real_ip_header` нужно указать заголовок балансера, который он передает на бэкенд (виртуальную машину BitrixVM). В `set_real_ip_from` — IP-адрес балансера.




Перезапускаем nginx.




```

systemctl restart nginx.service
```






Далее настраиваем передачу протокола, по которому клиент работает с сервером.





Нам нужно, чтобы балансер передавал на бэкенд-сервер информацию о протоколе:




```

proxy_set_header X-Forwarded-Proto $scheme;
```




На бэкенде (виртуальная машина BitrixVM) делаем конфигурацию для настройки переменных в файле **/etc/nginx/bx/settings/schema.conf**:


```

map $http_x_forwarded_proto $balancer_port {
   default 80;
   "https" 443;
}

map $http_x_forwarded_proto $balancer_https {
    default "NO";
    "https" "YES";
}
```




Тогда на бэкенде переменная `$http_x_forwarded_proto` будет содержать значение `http` или `https` в зависимости от протокола подключения.






Далее нам потребуется конфигурационный файл сайта:


сайт по умолчанию — **/etc/nginx/bx/site_enabled/s1.conf**

дополнительный сайт — **/etc/nginx/bx/site_enabled/bx_ext_test.example.org.conf**


В конфигурационном файле сайта нас интересует часть:



```

proxy_set_header Host $host:80;
```





Меняем указанную выше часть на:

```

proxy_set_header Host $host:$balancer_port;
proxy_set_header HTTPS $balancer_https;
```




Перезапускаем nginx:




```

systemctl restart nginx.service
```




Все готово.






### Телефония




Для настройки проксирования телефонии можно использовать правило:




```

location ~* ^/(pub/imconnector/|pub/imbot.php|services/telephony/info_receiver.php|bitrix/tools/voximplant/) {
proxy_ignore_client_abort on;
proxy_pass $proxyserver;
}
```




О других настройках локальной сети при использовании телефонии рассказывается в соответствующем [уроке](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=5017) курса Администратор сервиса Битрикс24.
