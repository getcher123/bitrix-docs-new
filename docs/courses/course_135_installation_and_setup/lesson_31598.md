# Конфигурация Push-server

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 31596 — Конфигурация Redis](lesson_31596.md)
- [Следующий: 31600 — Конфигурация сайта →](lesson_31600.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=31598

Схема работы

```
 -----------------------                                   ---------------------------------------------------
| nginx: 0.0.0.0:80     | -> /bitrix/sub|/bitrix/subws -> | node server.js --config push-server-sub-80XX.json |
 -----------------------                                   ---------------------------------------------------

 -----------------------                     ---------------------------------------------------
| nginx: 127.0.0.1:8895 | -> /bitrix/pub -> | node server.js --config push-server-pub-90XX.json |
 -----------------------                     ---------------------------------------------------
```

Nginx проксирует запрос на Push-сервис выбранного типа. Запросы получения сообщений `sub` — публичные, проксируются со стандартных портов 80/443. Запросы публикации `pub` — доступны только с внутреннего адреса сервера.

Nodejs-процессы делятся на два типа.

1. Процессы, отвечающие за подключение пользователя к выбранному каналу и получение им сообщений. Слушают порты 8010-8015.
2. Процессы, отвечающие за отправку сообщения в канал. Слушают порты 9010-9011.

Для запуска Push-сервера необходимы:

- nodejs & npm,
- архив сервиса и его модулей.

Выполните следующие действия:

1. Скачайте и установите архив `push-server-0.4.0.tgz`:
  ```
  cd /opt
  wget https://repo.bitrix24.tech/vm/push-server-0.4.0.tgz
  npm install --omit=dev ./push-server-0.4.0.tgz
  ```
  Установка закончится строкой:
  ```
  added 1 package in 8s
  16 packages are looking for funding
    run `npm fund` for details
  ```
2. Для удобства дальнейшей работы выполните команду:
  ```
  ln -sf /opt/node_modules/push-server/etc/push-server /etc/push-server
  ```
3. Скопируйте файлы сервиса и основную конфигурацию:
  ```
  cd /opt/node_modules/push-server
  cp etc/init.d/push-server-multi /usr/local/bin/push-server-multi
  mkdir /etc/sysconfig
  cp etc/sysconfig/push-server-multi  /etc/sysconfig/push-server-multi
  cp etc/push-server/push-server.service  /etc/systemd/system/
  ln -sf /opt/node_modules/push-server /opt/push-server
  ```
4. В конфигурационном файле /etc/sysconfig/push-server-multi исправьте (или добавьте, если их нет) следующие параметры:
  Пример настроек параметров:
  ```
  GROUP=www-data
  SECURITY_KEY="PUTTHEPRIVATEKEYHERE"
  RUN_DIR=/tmp/push-server
  REDIS_SOCK=/var/run/redis/redis.sock
  ```

  - `SECURITY_KEY` — секретный ключ для подписи соединения между клиентом и Push-сервером,
    Длина ключа не имеет значения. В ключе можно использовать только буквы латинского алфавита и цифры, спецсимволы запрещены. Рекомендуем использовать длинный ключ — простой и короткий небезопасен. Вы можете сгенерировать его в консоли с помощью команды:
    ```
    cat /dev/urandom |tr -dc A-Za-z0-9 | head -c 128
    ```
  - `RUN_DIR` — директория для хранения PID файлов процесса,
  - `USER/GROUP` — пользователь, под которым будет запущен сервис,
  - `REDIS_SOCK` — сокет, который использует сервис Redis.
5. Создайте пользователя:
  ```
  useradd -g www-data bitrix
  ```
6. Создайте каталог логов:
  ```
  [[ ! -d /var/log/push-server ]] && mkdir /var/log/push-server
  chown bitrix:www-data /var/log/push-server
  ```
7. Каждый nodejs-процесс будет запущен как отдельный процесс. Сгенерируйте конфигурационные файлы:
  ```
  /usr/local/bin/push-server-multi configs pub
  /usr/local/bin/push-server-multi configs sub
  ```
8. Создайте каталог через tmpfiles.d.
  ```
  echo 'd /tmp/push-server 0770 bitrix www-data -' > /etc/tmpfiles.d/push-server.conf
  systemd-tmpfiles --remove --create
  ```
9. Измените пользователя и путь к скрипту запуска в конфигурационном файле сервиса /etc/systemd/system/push-server.service:
  ```
  [Service]
  User=bitrix
  Group=www-data
  ExecStart=/usr/local/bin/push-server-multi systemd_start
  ExecStop=/usr/local/bin/push-server-multi stop
  ...
  ```
10. Переконфигурируйте:
  ```
  systemctl daemon-reload
  ```
11. Запустите сервис:
  ```
  systemctl --now enable push-server
  ```
12. Выполните настройки Push-сервера, описанные [в следующем уроке](lesson_31600.md).
