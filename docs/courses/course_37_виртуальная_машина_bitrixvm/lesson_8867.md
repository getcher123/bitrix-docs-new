# Конфигурационный файл сайта

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8865 — Условия работы композитного кеша](lesson_8865.md)
- [Следующий: 9357 — 1. Настроить параметр proxy_ignore_client_abort (1. Configure proxy_ignore_client_abort for site) →](lesson_9357.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=8867

Проверки для включения технологии на стороне NGINX  используются в конфигурационном файле сайта, который в виртуальном окружении находится в каталоге `/etc/nginx/bx/site_enabled`. В случае стандартной конфигурации, файл обычно содержит следующие настройки:




```
    # Include parameters common to all websites
    include bx/conf/bitrix.conf;
```




При включенной технологии Композитный сайт, настройки зависят от выбранного хранилища.





Указанные в этом подразделе настройки производить не нужно. Здесь для ознакомления дано описание того, что происходит при включении настроек NGINX на технологию Композитный сайт в *BitrixVM*.




### Хранение в файлах




1. В файле `/bitrix/html_pages/.config.php` опция **STORAGE** содержит значение `files`.
2. В конфигурационном файле сайта, который в виртуальном окружении находится в каталоге `/etc/nginx/bx/site_enabled`, должно быть прописано:
  ```
    # определяем ключ композита и файл на диске
    set $composite_cache    "bitrix/html_pages/${host}${composite_key}/index@${args}.html";
    set $composite_file     "${docroot}/${composite_cache}";
    # файл, который определяет включен ли композит на сайте или нет
    set $composite_enabled  "${docroot}/bitrix/html_pages/.enabled";
    # переменная, которая используется для композитной проверки
    set $use_composite_cache "";
    # если переменная глобальных условий содержит 1, добавляем признак в  use_composite_cache
    if ($is_global_composite  = 1) {set $use_composite_cache "A";}
    # если переменная персональных условий сайта содержит 1, добавляем признак use_composite_cache
    if ($is_site_composite_02 = 1) {set $use_composite_cache "${use_composite_cache}B";}
    # Подключаем конфиг, который содержит наши стандартные настройки, без  location по умолчанию
    include bx/conf/bitrix_general.conf;
    # Основной location
    location / {
      # если файл включения композита существует, добавляем признак в use_composite_cache
      if (-f $composite_enabled)     { set $use_composite_cache "${use_composite_cache}C"; }
      # если файл кеша существует, добавляем признак в use_composite_cache
      if (-f $composite_file)  { set $use_composite_cache "${use_composite_cache}D"; }
      # если все четыре условия выполняются, отправляем запрос в location c кешем
      if ($use_composite_cache = "ABCD") { rewrite .* /$composite_cache last; }
       # по дефолту отправляем в apache
      proxy_pass $proxyserver;
    }
  ```






### Хранение в memcached





1. В файле `/bitrix/html_pages/.config.php` опция **STORAGE** содержит значение `memcached` или `memcached_cluster`.
  В конфигурационном файле сайта, который в виртуальном окружении находится в каталоге `/etc/nginx/bx/site_enabled`, должно быть прописано:
  ```
  # устанавливаем параметры подключения для memcached
    memcached_connect_timeout 1s;
    memcached_read_timeout 1s;
    memcached_send_timeout 1s;
    memcached_gzip_flag 65536;
    # ключ поиска
    set $memcached_key "/${host}${composite_key}/index@${args}.html";
    # включен ли композитный кеш
    set $composite_enabled  "${docroot}/bitrix/html_pages/.enabled";
    # переменная, которая используется для проверки работы с композитом при запросе пользователя
    set $use_composite_cache "";
    # учитываем глобальные условия
    if ($is_global_composite  = 1) {set $use_composite_cache "A";}
    # учитываем персональные условия
    if ($is_site_composite_02 = 1) {set $use_composite_cache "${use_composite_cache}B";}
    # подключаем общие параметры для bitrix окружения, без использования  default location
    include bx/conf/bitrix_general.conf;
    # основной location
    location / {
       # если данные не найдены в кеше проксируем запрос на apache
      error_page 404 405 412 502 504 = @apache;
      # учитываем наличие .enabled файла
      if (-f $composite_enabled)     { set $use_composite_cache "${use_composite_cache}C"; }
      default_type text/html;
      # если все совпало, отправляем запрос в memcached
      if ($use_composite_cache = "ABC") {
        add_header X-Bitrix-Composite "Nginx (memcached)";
        memcached_pass localhost:11211;
      }
      proxy_pass $proxyserver;
    }
    location @apache {
      proxy_pass $proxyserver;
    }
  ```






### PHP или NGINX?





После завершения настроек NGINX возникает вопрос: как проверить, через что отдаются страницы - через PHP или NGINX при использовании *BitrixVM*? Для такой проверки просмотрите заголовки ответа сервера.




Заголовки при использовании Композита в *BitrixVM* могут быть такие:



- `X-Bitrix-Composite:Nginx (file)` - отдача страниц - **NGINX**, хранение - **файлы**;
- `X-Bitrix-Composite:Nginx (memcached)` - отдача страниц - **NGINX**, хранение - **memcached**;
- `X-Bitrix-Composite:Cache (200)` - отдача страниц - **PHP**, хранение - **файлы**.
