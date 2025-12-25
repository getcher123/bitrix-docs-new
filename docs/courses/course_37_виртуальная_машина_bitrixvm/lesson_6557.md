# Настройка Postfix для отправки почты

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 6556 — Настройка memcached](lesson_6556.md)
- [Следующий: 6558 — Выполнение всех агентов на Cron →](lesson_6558.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=6557

**Внимание!** Для операций, описанных в данном уроке, необходимы знания администрирования *nix-систем. Перед началом проведения данных операций рекомендуется сделать полный бекап виртуальной машины.






По умолчанию в *BitrixEnv* и *BitrixVM* используется **msmtp** для отправки почтовых сообщений.




**Преимуществом** данного решения является простота его настройки. К **недостатком** можно отнести медленную отправку почтовых сообщений через внешние сервисы (Google, Yandex).




В большинстве случаев, это не приводит к каким-либо проблемам, так как почтовые события отрабатывают из-под cron-a, но в ряде случаев может создать проблему - например, если почтовые события исполняются на хите (задан параметр немедленной доставки) или разработчик напрямую использует функцию `mail()`.






Рассмотрим настройку отправки почтовых сообщений **postfix**-ом через Яндекс:



1. Устанавливаем дополнительные пакеты:
  ```
  yum install cyrus-sasl-plain
  ```
2. Добавляем в файл `/etc/postfix/main.cf`:
  ```
  smtp_sasl_auth_enable = yes
  smtp_sasl_password_maps = hash:/etc/postfix/mailpasswd
  smtp_sasl_security_options = noanonymous
  smtp_sasl_type = cyrus
  smtp_sasl_mechanism_filter = login
  smtp_sender_dependent_authentication = yes
  sender_dependent_relayhost_maps = hash:/etc/postfix/sender_relay
  sender_canonical_maps = hash:/etc/postfix/canonical
  smtp_generic_maps = hash:/etc/postfix/generic
  ```
3. В `/etc/postfix/mailpasswd` указываем логин и пароль:
  ```
  [smtp.yandex.ru]      www@some.ru:password
  ```
4. В `/etc/postfix/sender_relay` указываем привязку доменов и конкретных отправителей к внешним службам:
  ```
  @some.ru [smtp.yandex.ru]
  www@some.ru [smtp.yandex.ru]
  ```
5. В `/etc/postfix/canonical` добавляем для домена указание через какой аккаунт отправлять почту:
  ```
  @some.ru   www@some.ru
  ```
   В `/etc/postfix/generic` добавляем отправку почты админу:
  ```
  root@localhost admin@mail.xx
  bitrix@localhost admin@mail.xx
  ```
  И выполняем команду `postmap` для `/etc/postfix/generic`, `/etc/postfix/canonical`, `/etc/postfix/sender_relay`, `/etc/postfix/mailpasswd`:
  ```
  postmap /etc/postfix/generic
  postmap /etc/postfix/canonical
  postmap /etc/postfix/sender_relay
  postmap /etc/postfix/mailpasswd
  ```
  Изменяем настройки в **php.ini**:
  ```
  sendmail_path = sendmail -t -i -f www@some.ru          ;bitrix-env
  ```
  Запускаем все необходимые службы:
  ```
  chkconfig saslauthd on
  service saslauthd restart
  chkconfig postfix on
  service postfix restart
  service zend-server restart
  ```



Скорость отправки сообщений php-скриптами значительно возрастет, а всю работу по доставке писем до внешнего сервера возьмет на себя **postfix**. При этом не нужно настраивать полноценный почтовый сервер.
