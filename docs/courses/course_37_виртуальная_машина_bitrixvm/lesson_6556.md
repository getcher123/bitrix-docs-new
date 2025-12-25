# Настройка memcached

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 6555 — Корректное монтирование Windows-ресурсов](lesson_6555.md)
- [Следующий: 6557 — Настройка Postfix для отправки почты →](lesson_6557.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=6556

**Внимание!** Для операций, описанных в данном уроке, необходимы знания администрирования *nix-систем. Перед началом проведения данных операций рекомендуется сделать полный бекап «Виртуальной машины».






В случае, если в проекте планируется использовать **memcached**, необходимо произвести его настройку в соответствии с предполагаемой нагрузкой.




Для этого необходимо:



- в файле `/etc/sysconfig/memcached` задать следующие параметры:

  - `MAXCONN = "1024"` - количество одновременных подключений (по умолчанию 1024);
  - `CACHESIZE="1024"` - объем выделяемой памяти для кеша (по умолчанию 64MB);
  - `OPTIONS="t 8"` - количество потоков memcached (по умолчанию 4).
- После настройки memcaсhe необходимо перезапустить командой:
  ```
  service memcached restart
  ```
- Далее подключить его в `bitrix/php_intarface/dbconn.php`:
  ```
  define("BX_CACHE_TYPE", "memcache");
  define("BX_CACHE_SID", $_SERVER["DOCUMENT_ROOT"]."#01");
  define("BX_MEMCACHE_HOST", "127.0.0.1");
  define("BX_MEMCACHE_PORT", "11211");
  ```






В случае, если используется один сервер, то для улучшения производительности можно настроить работу с **memcache** через **сокет**:



- `USER="bitrix"` - пользователь, от которого будет запущен memcache;
- `OPTIONS="-t 8 -s /tmp/memcached.sock"` - количество потоков и путь к сокету.




После этого необходимо изменить настройки в `bitrix/php_interface/dbconn.php`:



```

define("BX_CACHE_TYPE", "memcache");
define("BX_CACHE_SID", $_SERVER["DOCUMENT_ROOT"]."#01");
define("BX_MEMCACHE_HOST", "unix:///tmp/memcached.sock");
define("BX_MEMCACHE_PORT", "0");
```
