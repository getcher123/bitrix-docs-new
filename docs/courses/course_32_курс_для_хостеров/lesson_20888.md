# Конфигурация Push-server

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20886 — Конфигурация Redis](lesson_20886.md)
- [Следующий: 4564 — Конфигурация сайта →](lesson_4564.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=20888

**Схема работы:**




```
 -----------------------                                   ---------------------------------------------------
| nginx: 0.0.0.0:80     | -> /bitrix/sub|/bitrix/subws -> | node server.js --config push-server-sub-80XX.json |
 -----------------------                                   ---------------------------------------------------

 -----------------------                     ---------------------------------------------------
| nginx: 127.0.0.1:8895 | -> /bitrix/pub -> | node server.js --config push-server-pub-90XX.json |
 -----------------------                     ---------------------------------------------------
```




Nginx проксирует запрос на push-сервис выбранного типа. Запросы получения сообщений (например, sub) - публичные и проксируются со стандартных портов 80/443. Запросы публикации (pub) доступны только с внутреннего адреса сервера.




Nodejs-процессы делятся на два типа:



1. Процессы, отвечающие за подключение пользователя к выбранному каналу и получение им сообщений. Слушают порты 8010-8015;
2. Процессы, отвечающие за отправку сообщения в канал. Слушают порты 9010-9011.




Для запуска Push-сервера нам понадобятся:

- nodejs & npm ;
- архив сервиса и его модулей.




Для установки понадобится **Python** и утилита **make**:



```
zypper install python3 make wget -y
```




Выполните действия:



1. Скачайте архив с репозитория repo.bitrix24.tech
  ```
  wget https://repo.bitrix24.tech/vm/push-server-0.2.2.tgz
  ```
   или с сайта [архив push-server-0.2.2.tgz](/docs/chm_files/push-server-0.2.2.tgz) и разместите его в директории `/opt`. Выполните установку:
  ```
  su -
  cd /opt
  npm install --production ./push-server-0.2.2.tgz
  ```
  Установка закончится строкой:
  ```
  + push-server@0.2.2
  added 65 packages from 78 contributors and audited 65 packages in 45.77s
  ```
2. Выполните (исключительно для удобства):
  ```
  su -
  ln -sf /opt/node_modules/push-server/logs /var/log/push-server
  ln -sf /opt/node_modules/push-server/etc/push-server /etc/push-server
  ```
3. Копируем файлы сервиса и основную конфигурацию:
  ```
  su -
  cd /opt/node_modules/push-server
  cp etc/init.d/push-server-multi /usr/local/bin/push-server-multi
  cp etc/sysconfig/push-server-multi  /etc/sysconfig/push-server-multi
  cp etc/push-server/push-server.service  /etc/systemd/system/
  ln -sf /opt/node_modules/push-server /opt/push-server
  ```
4. Создайте временный каталог:
  ```
  echo 'd /tmp/push-server 0770 wwwrun www -' > /etc/tmpfiles.d/push-server.conf
  systemd-tmpfiles --remove --create
  ```
  Отредактируйте конфигурационный файл `/etc/sysconfig/push-server-multi`. В нём нужно исправить/добавить параметры:
  - **USER/GROUP** - пользователь, под которым будет запущен сервис;
  - **SECURITY_KEY** - cекретный ключ для подписи соединения между клиентами и пуш-сервером;
    **Примечание:** Длина ключа не имеет значения. В ключе можно использовать только буквы латинского алфавита и цифры, спецсимволы запрещены. Но имейте в виду, что простой короткий ключ небезопасен. Можно генерировать его, например, таким образом:
    ```
    cat /dev/urandom |tr -dc A-Za-z0-9 | head -c 128
    ```
  - **RUN_DIR** - директория для хранения PID файлов процесса.
  Пример настроек параметров:
  ```
  GROUP=www
  USER=wwwrun
  SECURITY_KEY="SECURITYKEY123456"
  RUN_DIR=/tmp/push-server
  REDIS_SOCK=/var/run/redis/default.sock
  ```
5. Каждый nodejs процесс будет запущен как отдельный процесс. Сгенерируйте конфигурации:
  ```
  /usr/local/bin/push-server-multi configs pub
  /usr/local/bin/push-server-multi configs sub
  ```
  Сгенерированные конфигурации в формате
  			json
                      push-server-sub-80XX.json
  push-server-pub-90XX.json
  		 будут размещены в каталоге: `/etc/push-server/`.
6. Измените пользователя и путь к скрипту запуска в конфигурационном файле сервиса `/etc/systemd/system/push-server.service`:
  ```
  [Service]
  User=wwwrun
  Group=www
  ExecStart=/usr/local/bin/push-server-multi systemd_start
  ExecStop=/usr/local/bin/push-server-multi stop
  ...
  ```
7. Измените права доступа на каталог с логами:
  ```
  chown wwwrun:www /opt/node_modules/push-server/logs /tmp/push-server -RH
  ```
8. Переконфигурируйте:
  ```
  systemctl daemon-reload
  ```
9. Запустите сервис:
  ```
  systemctl --now enable push-server
  ```
10. Перейдите в конфигурацию push модуля (настройки сайта) и включите использование локального push-сервера (последняя версия).
  Дополнительно нужно будет указать секретный ключ SECURITY_KEY, который мы настраивали выше в файле `/etc/sysconfig/push-server-multi`.
