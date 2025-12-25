# Дополнительные настройки и отладка msmtp

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5503 — Подключение Swap-раздела](lesson_5503.md)
- [Следующий: 5504 — Корректное монтирование Windows-ресурсов →](lesson_5504.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=9325

Данная информация пригодится для ручной настройки и диагностики ошибок с почтой в *Виртуальная машина BitrixVM/BitrixEnv v.5.x*.





**Примечание:** Для *Виртуальная машины BitrixVM/BitrixEnv* **v7.x** никакой ручной настройки, как правило, не требуется. Нужно только [создать пул](/learning/course/?COURSE_ID=37&CHAPTER_ID=06511) и настроить почту с помощью [мастера настройки почты](lesson_6537.md) в меню виртуальной машины.




#### Изменения в конфигурационных файлах




В настройке используется пакет **msmtp** (он идет в стандартных зависимостях для пакета **bitrix-env**).
Из пакета приходят настройки php-модуля в файле `/etc/php.d/bitrixenv.ini`:


```

sendmail_path = msmtp -t -i
```




При конфигурации из веб-интерфейса или из консольного меню:



1. создается или обновляется конфигурационный файл **/home/bitrix/.msmtprc**:
  ```
  # smtp account configuration for default
  account default
  logfile /home/bitrix/msmtp_default.log
  host 192.168.0.25
  port 25
  from name@site.ru
  keepbcc on
  auth on
  user name@site.ru
  password XXXXXXXXXXXXXX
  tls on
  tls_certcheck off
  ```
2. Аккаунт с именем **default** используется по умолчанию для всех сайтов. Если настраивается почтовый ящик для сайта, отличного от **default**, то вносятся изменения в конфигурационный файл apache (конфигурационный файл сайта):
  ```
    <Directory /home/bitrix/www/>
          ...
          php_admin_value sendmail_path "msmtp -t -i -a <ИМЯ_САЙТА>"
   </Directory>
  ```
3. создается символическая ссылка с `/home/bitrix/.msmtprc` на `/etc/msmtprc` (данное действие необходимо для заданий отправки почты, которые выполняются через crontab).







#### Используемые скрипты




Данные рекомендации будут полезны для автоматизации тестирования.




Для создания из web или консоли используется скрипт `/opt/webdir/bin/bx-sites`.



При настройке почты он принимает следующие параметры:




```

 bx-sites -o json -a email --smtphost=smtp.yandex.ru \
  --smtpuser='ivan@yandex.ru' --password=XXXXXXXXXX \
  --email='ivan@yandex.ru' --smtptls -s alice
```



где:

- `-a email` - тип действия, которое мы выполняем для сайта (`-h` позволит получить весь доступный список);
- `--smtphost` - IP адрес или DNS имя хоста, через который будет отправляться почта;
- `--smtpuser` - логин пользователя (в случае, если не используется данный параметр, можно опустить);
- `--password` - пароль для авторизации на почтовом сервере;
- `--email` - поле **from** в письме;
- `--smtptls` - включает TLS при отправке почты;
- `-s|--site` - название сайта (по умолчанию будет использован **default**).







#### Проблемы и их решение




В разделе описаны найденные и решенные проблемы, а также способы отладки почтовых проблем.




1. **msmtp** ведет лог отправки уведомлений. Например, в логе можно найти информацию, почему письмо не ушло:




```

Сен 04 14:41:11 host=smtp.yandex.ru tls=on auth=on user=bx@ya.ru from=bx@ya.ru recipients=3458@mail.ru smtpstatus=554
smtpmsg='554 5.7.1 Message rejected under suspicion of SPAM adxPcTaXWc-fB4SvmKU' errormsg='the server did not accept the mail' exitcode=EX_UNAVAILABLE
```




**msmtp** не пишет информацию, если не смог запустится или конфигурация некорректна. Запускаем отправку из консоли (меняем адрес получателя на свой):


```

echo -e "test message" | /usr/bin/msmtp --debug -t -i name@site.ru
```



тут может быть ошибка, например, загрузки конфигурации:


```

ignoring system configuration file /etc/msmtprc: Нет такого файла или каталога
ignoring user configuration file /.msmtprc: Нет такого файла или каталога
falling back to default account
```




В данном случае, ни один из файлов конфигурации не был найден, поэтому отправка не удалась.





если в п.2 все хорошо и письма все еще не ходят:

- Поместить данный скрипт **test_email.sh** в каталог `/usr/bin/` и выставить права на исполнение:
  ```
  #!/bin/bash
  export HOME=/home/bitrix
  tmp_dir=/tmp/mail
  args=$@
  if [[ ! -d $tmp_dir ]]; then
          mkdir $tmp_dir
          chmod 777 $tmp_dir
  fi
  message_body=""
  while read line; do
    message_body="$message_body$line\n"
  done < /dev/stdin
  tmp_file=$(mktemp $tmp_dir/$(date +%Y%m%d_%H%M%S)_XXXXXXXXX)
  echo "=========================================" > $tmp_file
  echo "ARGV: /usr/bin/msmtp --debug -t -i $args" >> $tmp_file
  echo "=========================================" >> $tmp_file
  echo -e "BODY: $message_body" >> $tmp_file
  echo "=========================================" >> $tmp_file
  # send message
  echo -e "$message_body" | /usr/bin/msmtp --debug -t -i $args >> $tmp_file && 2>&1
  ```
- В конфигурации `/etc/php.d/bitrixenv.ini` изменить настройки почты:
  ```
  sendmail_path = /usr/bin/test_email.sh
  ```
- Перезапустить apache.
- Данный скрипт запускает **msmtp** с опцией **debug** и по каждому отправленному письму сохранит информацию о параметрах отправки, о теле письма, а также о результатах запуска команды.
  При создании письма из web-интерфейса вся информация сохраняется в каталоге `/tmp/mail`, каждое письмо будет сохранено в отдельном файле.









**Проблема**:

Не отправляются письма уведомлений о заказах с сайта, статистика за день в *BitrixVM* v5.0.44-5.0.45.



**Решение**:

Причина в том, что домашний каталог скриптов выставлен в `HOME=/`, поэтому письма, отправка которых происходит из задания в **Cron**, не отправляются.

Для решения необходимо:

- либо создать символическую ссылку с `/home/bitrix/.msmtprc` на `/etc/msmtprc` - конфигурационный файл `/etc/msmtprc` является системным файлом для утилиты и позволяет решить нахождение конфигурационного файла при таком параметре `HOME`.
- либо обновить *BitrixVM* до версии 5.0.46 и выше.







**Проблема**:

Не отправляется почта по **Cron**-у, хотя символическая ссылка с `/home/bitrix/.msmtprc` на `/etc/msmtprc` есть.



**Решение**:

Проблема может быть в том, что для **Cron** не установлено правильное значение переменной `PATH`.


Для решения необходимо:

1. Зайти по ssh под логином **bitrix** и в консоли выполнить команду:
  ```
  >echo $PATH
  ```
2. Получите ответ вида:
  ```
  /usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/bitrix/bin
  ```
3. Далее в файле **Cron** добавить первой строкой:
  ```
  PATH=/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/bitrix/bin
  ```
