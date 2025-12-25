# Настройка отправки Nagios-уведомлений в BitrixVM 5.1.3

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5504 — Корректное монтирование Windows-ресурсов](lesson_5504.md)
- [Следующий: 5507 — Выполнение всех агентов на Cron →](lesson_5507.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=9327

**Внимание!** Данный способ актуален для BitrixVM до версии **5.1.3**. В версии BitrixVM 5.1.4 и выше была добавлена возможность настроить email-уведомления для системы мониторинга Nagios. Данная настройка осуществляется в меню настройки мониторинга.




**Внимание!** Для отправки уведомлений Nagios-ом на email необходимо предварительно включить в меню BitrixVM [Мониторинг (Monitoring in pool)](lesson_6508.md).







Итак, чтобы получать уведомления Nagios-а о различных событиях сервера, нужно настроить контакты и шаблон уведомлений:




1. В `/etc/nagios/objects/contacts.cfg` указываем параметр `email` - email пользователя, кому будет отправляться нотификация:
  ```
  define contact{
  	contact_name	nagiosadmin		; Short name of user
  	use			generic-contact		; Inherit default values from generic-contact template (defined above)
  	alias		Nagios Admin		; Full name of user
  	email		email@myaddress.ru	; <<***** CHANGE THIS TO YOUR EMAIL ADDRESS ******
  	}
  ```
  **Примечание**: Можно создать новый контакт, но не забудьте прописать его в секции `CONTACT GROUPS` в этом же файле. Как это сделать см. [в документации Nagios](http://nagios.sourceforge.net/docs/3_0/objectdefinitions.html#contactgroup).
2. Далее в `/etc/nagios/objects/commands.cfg` меняем строки в секции `SAMPLE NOTIFICATION COMMANDS` запуска MTA на:
  ```
  # 'notify-host-by-email' command definition
  define command{
     command_name   notify-host-by-email
     command_line   /usr/bin/printf "%b" "Subject: ** $NOTIFICATIONTYPE$ Host Alert: $HOSTNAME$ is $HOSTSTATE$ **\n\n ***** Nagios *****\n\nNotification Type: $NOTIFICATIONTYPE$\nHost: $HOSTNAME$\nState: $HOSTSTATE$\nAddress: $HOSTADDRESS$\nInfo: $HOSTOUTPUT$\n\nDate/Time: $LONGDATETIME$\n" | /usr/bin/msmtp --host=hostname --port=number --user=username --passwordeval=eval --from=mailfrom@email.ru $CONTACTEMAIL$
     }
  # 'notify-service-by-email' command definition
  define command{
     command_name   notify-service-by-email
     command_line   /usr/bin/printf "%b" "Subject: ** $NOTIFICATIONTYPE$ Service Alert: $HOSTALIAS$/$SERVICEDESC$ is $SERVICESTATE$ **\n\n ***** Nagios *****\n\nNotification Type: $NOTIFICATIONTYPE$\n\nService: $SERVICEDESC$\nHost: $HOSTALIAS$\nAddress: $HOSTADDRESS$\nState: $SERVICESTATE$\n\nDate/Time: $LONGDATETIME$\n\nAdditional Info:\n\n$SERVICEOUTPUT$\n" | /usr/bin/msmtp --host=hostname --port=number --user=username --passwordeval=eval --from=mailfrom@email.ru $CONTACTEMAIL$
     }
  ```
  где:
  **Примечание**: Также можно настроить дополнительные ключи msmtp (TLS-опции и др.), список всех ключей msmtp можно посмотреть консольной  командой:
  `msmtp --help`.

  - `--host=hostname` - адрес smtp-сервера;
  - `--port=number` - порт smtp-сервера;
  - `--user=username` - логин для авторизации на smtp-сервере;
  - `--passwordeval=eval` - пароль для авторизации на smtp-сервере;
  - `--from=mailfrom@email.ru` -  от кого будет уходить письмо.
3. Обязательно сделать рестарт Nagios для применения настроек:
  ```
  service nagios restart
  ```






Т.е, по сути, в конфигурационном файле Nagios мы меняем MTA с **mail** на **msmtp** c ключами и немного модифицируем текст сообщения: т.к у **msmtp** нет ключа `Subject:` (Тема сообщения), то мы его включаем в тело письма, и оно при получении почтовым клиентом обработается корректно.






Проверить работу нотификаций можно, например, остановив МySQL:

```
service mysqld stop
```




По умолчанию Nagios будет записывать в лог 3 сообщения со статусом **CRITICAL\SOFT** каждую минуту, а 4-му сообщению даст статус **CRITICAL\HARD**. Далее будет инициирована команда **notify-service-by-email**, которая отправит текст сообщения через **msmtp** c ключами, настроенными выше. В итоге, в течение 4-5 минут сообщение примерно такого содержания должно уйти на почту:




```

Subject: ** PROBLEM Service Alert: test1/MySQL: connection to 3306 is CRITICAL **

 ***** Nagios *****

Notification Type: PROBLEM

Service: MySQL: connection to 3306
Host: server1
Address: 192.168.2.130
State: CRITICAL

Date/Time: Tue Jan 27 20:15:15 MSK 2015

Additional Info:

Connection refused

```




После запуска службы MySQL командой `# service mysqld start` должно прийти сообщение на почту:





```

Subject: ** RECOVERY Service Alert: server1/MySQL: connection to 3306 is OK **

 ***** Nagios *****

Notification Type: RECOVERY

Service: MySQL: connection to 3306
Host: server1
Address: 192.168.2.130
State: OK

Date/Time: Wed Jan 28 12:30:50 MSK 2015

Additional Info:

TCP OK - 0.001 second response time on port 3306
```






**Примечание**: Подробнее о email уведомлениях можно прочитать в [в документации Nagios](http://nagios.sourceforge.net/docs/3_0/notifications.html).
