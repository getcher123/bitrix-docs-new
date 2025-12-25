# Конфигурация Push-server

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20408 — Конфигурация Redis](lesson_20408.md)
- [Следующий: 5408 — Конфигурация сайта →](lesson_5408.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20410

**Схема работы:**

```
 -----------------------                                   ---------------------------------------------------
| nginx: 0.0.0.0:80     | -> /bitrix/sub|/bitrix/subws -> | node server.js --config push-server-sub-80XX.json |
 -----------------------                                   ---------------------------------------------------

 -----------------------                     ---------------------------------------------------
| nginx: 127.0.0.1:8895 | -> /bitrix/pub -> | node server.js --config push-server-pub-90XX.json |
 -----------------------                     ---------------------------------------------------
```

Nginx проксирует запрос на push-сервис выбранного типа. Публикация сообщений ограничена для локальной ноды.

Nodejs-процессы делятся на два типа:

1. Процессы, отвечающие за подключение пользователя к выбранному каналу и получение им сообщений. Слушают порты 8010-8015;
2. Процессы, отвечающие за отправку сообщения в канал. Слушают порты 9010-9011.

Для запуска Push-сервера нам понадобятся:

- nodejs & npm ;
- архив сервиса и его модулей.

Выполните действия:

1. Скачайте архив с репозитория repo.bitrix24.tech
  ```
  wget https://repo.bitrix24.tech/vm/push-server-0.3.0.tgz
  ```
   и разместите его в директории `/opt`. Выполните установку:
  ```
  su -
  cd /opt
  npm install --production ./push-server-0.3.0.tgz
  ```
  Установка закончится строкой:
  ```
  + push-server@0.3.0
  added 144 packages from 151 contributors and audited 144 packages in 10.388s
  ```
2. Выполните (исключительно для удобства):
  ```
  su -
  ln -sf /opt/node_modules/push-server/etc/push-server /etc/push-server
  ```
3. Скопируйте файлы сервиса и основную конфигурацию:
  ```
  su -
  cd /opt/node_modules/push-server
  cp etc/init.d/push-server-multi /usr/local/bin/push-server-multi
  cp etc/sysconfig/push-server-multi  /etc/sysconfig/push-server-multi
  cp etc/push-server/push-server.service  /etc/systemd/system/
  ln -sf /opt/node_modules/push-server /opt/push-server
  ```
4. Отредактируйте конфигурационный файл `/etc/sysconfig/push-server-multi`. В нём нужно исправить/добавить параметры:
  Пример настроек параметров:
  ```
  USER=apache2
  GROUP=_webserver
  SECURITY_KEY="SECURITYKEY123456"
  RUN_DIR=/tmp/push-server
  ```

  - **USER/GROUP** - пользователь, под которым будет запущен сервис;
  - **SECURITY_KEY** - cекретный ключ для подписи соединения между клиентами и пуш-сервером;


  - **RUN_DIR** - директория для хранения PID файлов процесса.
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
6. Создайте каталог через **tmpfiles.d**:
  ```
  echo 'd /tmp/push-server 0770 apache2 _webserver -' > /etc/tmpfiles.d/push-server.conf
  systemd-tmpfiles --remove --create
  ```
7. Создайте каталог логов:
  ```
  mkdir /var/log/push-server
  chown apache2:_webserver /var/log/push-server
  ```
8. Измените пользователя в конфигурационном файле сервиса: `/etc/systemd/system/push-server.service`
  ```
  [Service]
  User=apache2
  Group=_webserver
  ExecStart=/usr/local/bin/push-server-multi systemd_start
  ExecStop=/usr/local/bin/push-server-multi stop
  ....
  ```
9. Переконфигурируйте:
  ```
  systemctl daemon-reload
  ```
10. Запустите сервис:
  ```
  systemctl --now enable push-server
  ```
11. Перейдите в конфигурацию push модуля (настройки сайта) и включите использование локального push-сервера (последняя версия).
  Дополнительно нужно будет указать секретный ключ SECURITY_KEY, который мы настраивали выше в файле `/etc/sysconfig/push-server-multi`.
