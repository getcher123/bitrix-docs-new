# Информация о версиях сервера очередей

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11759 — Как работает Push-сервер](lesson_11759.md)
- [Следующий: 2033 — Настройки модуля и сервера очередей →](lesson_2033.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=21636

### Общая информация




Сервер очередей Push and Pull служит для мгновенного взаимодействия между собой многих инструментов продуктов *Битрикс24* и *1С-Битрикс: Управление сайтом*. Он используется в Задачах, Календарях, ленте Новостей, Группах, RPA, мобильном приложении Битрикс24, Чатах, Генераторе документов, Телефонии, Центре продаж и других сервисах.




Мы рекомендуем вам заранее настроить сервер очередей — *облачный сервер «1С-Битрикс»* или локальный *Bitrix Push server 2.0*.


В виртуальной машине (

			BitrixVM версии 9.0 и выше

                    «1C-Битрикс: Виртуальная машина» — бесплатный программный продукт, готовый к немедленному использованию виртуальный сервер, полностью настроенный, протестированный и адаптированный для оптимальной работы как с продуктами «1С-Битрикс», так и с любыми PHP-приложениями.

Виртуальная машина сэкономит время и силы на правильное развертывание и администрирование сайта или внутреннего информационного ресурса на базе продуктов «1С-Битрикс».

[Подробнее в курсе Виртуальная машина](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&CHAPTER_ID=029228)

		) в качестве Push-сервера используется **NodeJS RTC Service**. По умолчанию он не запущен. Поэтому после установки виртуальной машины и создания пула, перейдите в меню по пути 6. Configure Push/RTC service for the pool &gt; 1. Install/Update NodeJS RTC Service и [запустите Push-сервер](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=29376).






#### Полезные материалы



- [Настройки модуля и сервера очередей Push and Pull](lesson_2033.md) (облачного и локального)
- [Установка отдельно стоящего сервера Bitrix Push server 2.0 на базе виртуальной машины](lesson_21594.md)
- [Установка БУС/КП на другие окружения](/learning/course/index.php?COURSE_ID=135&CHAPTER_ID=020866) (Debian 11, Astra 1.7, SLES 15, РЕД ОС 7.3, RedHat8, ALT 8 SP Server)






### Устаревшие версии BitrixVM




**Внимание!** Осенью 2021 года все старые версии модуля Push&Pull были признаны устаревшими, убраны из виртуальной машины BitrixVM и более не поддерживаются в продукте, например, чатами.

Настоятельно рекомендуем перейти на актуальные версии BitrixVM.




Для устаревших виртуальных машин используйте информацию из спойлеров.




## Работа модуля Push and Pull Битрикса на виртуальной машине до версии 7.5.5

В виртуальной машине (

			BitrixVM c версии 7.1 и выше

                    «1C-Битрикс: Виртуальная машина» — бесплатный программный продукт, готовый к немедленному использованию виртуальный сервер, полностью настроенный, протестированный и адаптированный для оптимальной работы как с продуктами «1С-Битрикс», так и с любыми PHP-приложениями.

Виртуальная машина сэкономит время и силы на правильное развертывание и администрирование сайта или внутреннего информационного ресурса на базе продуктов «1С-Битрикс».

[Подробнее в курсе Виртуальная машина](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&CHAPTER_ID=08809)

		) Push-сервер установлен по умолчанию.






Мы рекомендуем вам заранее настроить сервер очередей — *облачный сервер «1С-Битрикс»* или локальный *Bitrix Push server 2.0*.


**Внимание**: Поддержка старых версий локальных серверов очередей (*Nginx-PushStreamModule 0.3.4/0.4.0* и *Bitrix Push server 1.0*) прекращена  Осенью 2021 года.



Перейти на актуальную версию сервера (*Bitrix Push server 2.0*) вам помогут инструкции:

- [Переход c Bitrix Push server 1.0 на Bitrix Push server 2.0](lesson_21580.md);
- [Переход с Nginx-PushStreamModule на Bitrix Push server 2.0](lesson_21582.md);
- [Установка отдельно стоящего сервера Bitrix Push server 2.0 на базе вирт. машины](lesson_21594.md);
- [Настройки модуля и сервера очередей Push and Pull](lesson_2033.md) (облачного и локального);
- [Установка БУС/КП на другие окружения](/learning/course/index.php?COURSE_ID=135&CHAPTER_ID=020866) (Debian 11, Astra 1.7, SLES 15, РЕД ОС 7.3, RedHat8, ALT 8 SP Server).





## Работа модуля Push and Pull Битрикса на виртуальной машине до версии 5.0.

На серверной стороне поддержка мгновенных сообщений осуществляется модулем **NGINX**: [nginx-push-stream-module](https://github.com/wandenberg/nginx-push-stream-module). Данный модуль обеспечивает поддержку long-polling соединений с клиентами и доставку опубликованных им сообщений.




**Примечание**: *Bitrix Framework* и без модуля nginx-push-stream-module обеспечивает достаточно высокую скорость передачи сообщений: 60 секунд интервал, при наличии сообщений интервал между соединениями уменьшается до 10 секунд.




При открытии страницы клиент ajax-запросом, подключается к своему каналу на одном из портов NGINX: 8893 (http) или 8894 (https). (В случае использования виртуальной машины BitrixVM. При использовании собственной конфигурации сервера администратор волен использовать любые удобные ему порты.) С данного порта NGINX перенаправляет пользователя на внутренний сервер очередей (доступный только по 127.0.0.1:8895), где проверятся наличие канала пользователя и новых сообщений.  В случае если в канале нет сообщений, сервер не отдает ответ, а держит соединение в течение 40 сек.




Если в течение этого времени в канал пользователя придет новое сообщение, то сервер отправит его клиенту и закроет соединение. В случае если в канал пользователя не будет новых сообщений в течение 40 секунд, то сервер разорвет соединение и отправит ему заголовок: 304 Not Modified.




После получения ответа сервера и закрытия соединения клиент выполнит повторное подключение к каналу с новой датой последнего изменения.




![](../../../images/courses/41/dev.1c-bitrix.ru/images/admin_expert/pull/pull_12.png)




Сообщения в канал пользователя публикуются посредством вызова соответствующих [методов API](http://dev.1c-bitrix.ru/api_help/push_pull/index.php) модуля **Push and Pull**.




Для работы с мгновенными сообщениями рекомендуем использовать протокол https.




**Примечание**: Большое значение имеет правильная синхронизация времени сервера с глобальными серверами.




#### Настройка модуля




При использовании продуктов Bitrix Framework на базе виртуальной машины [BitrixVM](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37) с v. 5.0 необходимости в настройке модуля нет: всё работает "из коробки". Если проект используется не на штатных средствах установки Bitrix Framework, то необходимо произвести дополнительные настройки.




**Примечание**: Приведённые ниже образцы настроек даны для примера. Настройку под конкретный проект, при отказе от использования рекомендуемых BitrixVM или BitrixEnvironment, администратор должен произвести самостоятельно.




**Внимание!** Работа модуля **Push and Pull** поддерживается только до версии 0.5 **nginx-push-stream-module**. Более свежие версии не поддерживаются, так как для работы **Push and Pull** разрабатывается специальное решение от «1С-Битрикс».




- Соберите NGINX с поддержкой модуля nginx-push-stream-module;
  В качестве примеров можно использовать  файлы из нашей виртуальной машины:

  - `/etc/nginx/bx/site_enabled/push.conf` — настройки push and pull для публикации сообщений, а так же для работы мобильных;
  - `/etc/nginx/bx/conf/im_subscrider.conf` — настройки для получения сообщений (они подключаются к сайту непосредственно);
  - `/etc/nginx/bx/conf/im_settings.conf` — количество каналов, объём памяти и т.п.








## Настройка nginx-push-stream-module в версии 0.4.0

- Общие настройки (файл `/etc/nginx/bx/conf/im_settings.conf`):
  ```
  # Common settings for nginx-push-stream-module
  push_stream_shared_memory_size 256M;
  push_stream_max_messages_stored_per_channel 1000;
  push_stream_max_channel_id_length 32;
  push_stream_max_number_of_channels 200000;
  push_stream_message_ttl 86400;
  ```
- Настроить отдельные виртуальные сервера NGINX на портах 8893, 8894, 8895 (`/etc/nginx/bx/site_enabled/push.conf`):
  ```
  # поддержка мобильных платформ, для http запросов
  server {
      # nginx-push-stream-module server for push & pull
  listen 8893;
  server_name _;
  # Include error handlers
  include bx/conf/errors.conf;
  # Include im subscrider handlers
  include bx/conf/im_subscrider.conf;
  location ^~ / { deny all; }
  }
  # поддержка мобильных платформ, для https запросов
  # SSL enabled server for reading personal channels
  server {
      listen 8894;
  server_name _;
      include bx/conf/ssl.conf;
  # Include error handlers
  include bx/conf/errors.conf;
  # Include im subscrider handlers
  include bx/conf/im_subscrider.conf;
  location ^~ / { deny all; }
  }
  # для публикации сообщений
  # Server to push messages to user channels
  server {
      listen 127.0.0.1:8895;
  server_name _;
  location ^~ /bitrix/pub/ {
      push_stream_publisher admin;
      push_stream_channels_path $arg_CHANNEL_ID;
      push_stream_store_messages on;
      allow 127.0.0.0/8;
  deny all;
  }
  location ^~ / { deny all; }
  # Include error handlers
  include bx/conf/errors.conf;
  }
  ```
  Для получения сообщений через запрос на стандартный порт (80 для http, 443 для https) в файл `/etc/nginx/bx/conf/im_subscrider.conf` добавлено:
  ```
  # Include im subscrider handlers
  include bx/conf/im_subscrider.conf;
  ```
  Этот файл содержит:
  ```
  # Location for long-polling connections
  location ^~ /bitrix/sub {
  # we don't use callback and droppped it (XSS)
  if ( $arg_callback ) {
      return 400;
  }
      push_stream_subscriber            long-polling;
      push_stream_allowed_origins "*";
      push_stream_channels_path        $arg_CHANNEL_ID;
      push_stream_last_received_message_tag    $arg_tag;
      if ($arg_time) {
          push_stream_last_received_message_time "$arg_time";
      }
      push_stream_longpolling_connection_ttl    40;
      push_stream_authorized_channels_only    on;
      push_stream_message_template '#!NGINXNMS!#{"id":~id~,"channel":"~channel~","tag":"~tag~","time":"~time~","eventid":"~event-id~","text":~text~}#!NGINXNME!#';
  }
  # Location for websocet connections
  location ^~ /bitrix/subws/ {
      push_stream_subscriber websocket;
      push_stream_channels_path        $arg_CHANNEL_ID;
      push_stream_websocket_allow_publish    off;
      push_stream_ping_message_interval    40s;
      push_stream_authorized_channels_only     on;
      push_stream_last_received_message_tag    "$arg_tag";
      push_stream_last_received_message_time    "$arg_time";
      push_stream_message_template '#!NGINXNMS!#{"id":~id~,"channel":"~channel~","tag":"~tag~","time":"~time~","eventid":"~event-id~","text":~text~}#!NGINXNME!#';
  }
  ```










## Настройка nginx-push-stream-module в версии 0.3.4

- Общие настройки:
  ```
  # Common settings for nginx-push-stream-module
  push_stream_shared_memory_size			256M;
  push_stream_max_messages_stored_per_channel	1000;
  push_stream_max_channel_id_length		32;
  push_stream_max_number_of_channels		100000;
  push_stream_shared_memory_cleanup_objects_ttl	60;
  push_stream_message_ttl				86400;
  ```
- Настройки сервера мгновенных сообщений
  ```
  	# Nonsecure server for reading personal channels. Use secure server instead.
  	server {
  		# nginx-push-stream-module server for push & pull
  		listen	8893;
  		include	bx/node_host.conf;
  		# Include error handlers
  		include	bx/conf/errors.conf;
  		# Location for long-polling connections
  		location ^~ /bitrix/sub {
  			push_stream_subscriber			long-polling;
  			set $push_stream_channels_path		$arg_CHANNEL_ID;
  			push_stream_last_received_message_tag	$arg_tag;
  			push_stream_longpolling_connection_ttl	40;
  			push_stream_authorized_channels_only	on;
  			push_stream_content_type		"text/html; charset=utf-8";
  			push_stream_message_template "#!NGINXNMS!#{
                              \"id\":~id~,\"tag\":\"~tag~\",\"time\":\"~time~\",\"text\":~text~}#!NGINXNME!#";
  		}
  		# Location for websocet connections
  		location ^~ /bitrix/subws/ {
  			push_stream_websocket;
  			set $push_stream_channels_path		$arg_CHANNEL_ID;
  			push_stream_websocket_allow_publish	off;
  			push_stream_ping_message_interval	40s;
  			push_stream_authorized_channels_only on;
  			push_stream_message_template		"#!NGINXNMS!#{
                              \"id\":~id~,\"tag\":\"~tag~\",\"time\":\"~time~\",\"text\":~text~}#!NGINXNME!#";
  		}
  		location ^~ / 			{ deny all; }
  	}
  	# SSL enabled server for reading personal channels
  	server {
  		listen	8894;
  		include	bx/node_host.conf;
  		include	bx/conf/ssl.conf;
  		# Include error handlers
  		include	bx/conf/errors.conf;
  		add_header "Access-Control-Allow-Origin" "*";
  		add_header "Access-Control-Allow-Headers" "if-modified-since, origin, if-none-match";
  		# Location for long-polling connections
  		location ^~ /bitrix/sub {
  			push_stream_subscriber			long-polling;
  			set $push_stream_channels_path		$arg_CHANNEL_ID;
  			push_stream_last_received_message_tag	$arg_tag;
  			push_stream_longpolling_connection_ttl	40;
  			push_stream_authorized_channels_only	on;
  			push_stream_content_type		"text/html; charset=utf-8";
  			push_stream_message_template		"#!NGINXNMS!#{
                              \"id\":~id~,\"tag\":\"~tag~\",\"time\":\"~time~\",\"text\":~text~}#!NGINXNME!#";
  		}
  		# Location for web socket connections
  		location ^~ /bitrix/subws/ {
  			push_stream_websocket;
  			set $push_stream_channels_path		$arg_CHANNEL_ID;
  			push_stream_websocket_allow_publish	off;
  			push_stream_ping_message_interval	40s;
  			push_stream_authorized_channels_only	on;
  			push_stream_message_template		"#!NGINXNMS!#{
                               \"id\":~id~,\"tag\":\"~tag~\",\"time\":\"~time~\",\"text\":~text~}#!NGINXNME!#";
  		}
  		location ^~ / 			{ deny all; }
  	}
  	# Server to push messages to user channels
  	server {
  		listen 127.0.0.1:8895;
  		include	bx/node_host.conf;
  		location ^~ /bitrix/pub/ {
  			push_stream_publisher			admin;
  			set $push_stream_channel_id		$arg_CHANNEL_ID;
  			push_stream_store_messages		on;
  			push_stream_keepalive			off;
  			allow					127.0.0.0/8;
  			deny					all;
  		}
  		location ^~ /	{ deny all; }
  		# Include error handlers
  		include	bx/conf/errors.conf;
  	}
  ```




- Включите в настройках продукта  на странице Настройки &gt; Настройки продукта &gt; Настройки модулей &gt; Push and Pull опцию **На сервере установлен модуль nginx-push-stream-module**:
  Также необходимо выбрать версию используемой вами машины. Рекомендуется использовать Виртуальную машину в версии 4.4 и выше, так как в ней используется более совершенная версия модуля **nginx-push-stream-module** 0.4.0, позволяющая использовать технологию Веб-сокетов и отправление команд.
