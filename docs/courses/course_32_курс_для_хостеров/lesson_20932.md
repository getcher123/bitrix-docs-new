# Конфигурация Push-server

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20930 — Конфигурация Redis](lesson_20930.md)
- [Следующий: 5253 — Конфигурация сайта →](lesson_5253.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=20932

**Схема работы:**




```

 -----------------------                                   ---------------------------------------------------
| nginx: 0.0.0.0:80     | -> /bitrix/sub|/bitrix/subws -> | node server.js --config push-server-sub-80XX.json |
 -----------------------                                   ---------------------------------------------------

 -----------------------                     ---------------------------------------------------
| nginx: 127.0.0.1:8895 | -> /bitrix/pub -> | node server.js --config push-server-pub-90XX.json |
 -----------------------                     ---------------------------------------------------
```




Nginx проксирует запрос на push-сервис выбранного типа. Запросы получения сообщений (например, sub) – публичные, проксируются со стандартных портов 80/443. Запросы публикации (pub) – доступны только с внутреннего адреса сервера.





Nodejs-процессы делятся на два типа:



1. Процессы, отвечающие за подключение пользователя к выбранному каналу и получение им сообщений. Слушают порты 8010-8015;
2. Процессы, отвечающие за отправку сообщения в канал. Слушают порты 9010-9011.




Для запуска Push-сервера необходимы:

- nodejs & npm;
- архив сервиса и его модулей.




Для установки понадобится **Python** и утилита **make**:




```

dnf install python3 make -y
```




Выполните следующие действия:




1. Скачайте и установите архив **push-server-0.3.0.tgz**:
  ```
  su -
  cd /opt
  wget https://repo.bitrix24.tech/vm/push-server-0.3.0.tgz
  npm install --production ./push-server-0.3.0.tgz
  ```
  **Примечание**: Если репозиторий [repo.bitrix24.tech](https://repo.bitrix24.tech/vm/) недоступен, [скачайте архив push-server-0.3.0.tgz](/docs/chm_files/push-server-0.3.0.tgz) и разместите его в директории `/opt`. Далее выполните установку:
  ```
  su -
  cd /opt
  npm install --production ./push-server-0.3.0.tgz
  ```
  Установка закончится строкой:
  ```
  + push-server@0.3.0
  added 65 packages in 46.522s
  ```
2. Для удобства дальнейшей работы выполните команды:
  ```
  su -
  ln -sf /opt/node_modules/push-server/logs /var/log/push-server
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
4. Создайте временный каталог:
  ```
  echo 'd /tmp/push-server 0770 apache apache -' > /etc/tmpfiles.d/push-server.conf
  systemd-tmpfiles --remove --create
  ```
  Отредактируйте конфигурационный файл `/etc/sysconfig/push-server-multi`. В нём нужно исправить/добавить параметры:
  - **SECURITY_KEY** - cекретный ключ для подписи соединения между клиентами и пуш-сервером;
    **Примечание:** Длина ключа не имеет значения. В ключе можно использовать только буквы латинского алфавита и цифры, спецсимволы запрещены. Но имейте в виду, что простой короткий ключ небезопасен. Можно генерировать его, например, таким образом:
    ```
    cat /dev/urandom |tr -dc A-Za-z0-9 | head -c 128
    ```
  - **RUN_DIR** - директория для хранения PID файлов процесса;
  - **USER/GROUP** - пользователь, под которым будет запущен сервис.
  Пример настроек параметров:
  ```
  GROUP=apache
  SECURITY_KEY="SECURITYKEY123456"
  RUN_DIR=/tmp/push-server
  ```
5. Каждый nodejs-процесс будет запущен как отдельный процесс. Сгенерируйте конфигурации:
  ```
  /usr/local/bin/push-server-multi configs pub
  /usr/local/bin/push-server-multi configs sub
  ```
  Сгенерированные конфигурации в формате
  			json
                      push-server-sub-80XX.json
  push-server-pub-90XX.json
  		 будут размещены в каталоге: `/etc/push-server/`.
6. В конфигурационном файле сервиса `/etc/systemd/system/push-server.service` измените пользователя:
  ```
  [Service]
  User=apache
  Group=apache
  ExecStart=/usr/local/bin/push-server-multi systemd_start
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
10. Перейдите в конфигурацию Push-модуля (настройки сайта) и включите использование локального Push-сервера (последняя версия). Укажите секретный ключ, который настраивали ранее в файле `/etc/sysconfig/push-server-multi`.
