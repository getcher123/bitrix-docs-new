# Настройка почты на VMBitrix

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 6552 — Изменение стандартных настроек BitrixVM без отключения автоподстройки](lesson_6552.md)
- [Следующий: 6553 — Увеличение дискового пространства BitrixVM →](lesson_6553.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=2946

Запустите виртуальную машину.




В первом окне нажмите **Login**, войдите под **root** (это обязательно). Отобразится меню настройки:




![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vmplayer3_sm.png)


Нажмите **1**, потом - **Enter** и пройдите шаги базового мастера настройки почты.




В большинстве случаев этот мастер может сразу решить проблему настройки, достаточно указать адрес почтового сервера, порт, требуется ли авторизация для отправки писем, и, если да, то логин и пароль.




Однако этот мастер не учитывает много нюансов относительно шифрования, специфических алгоритмов аутентификации.




- Для проверки результата параллельно настройке откройте ваш *Bitrix Framework*.
- Перейдите на страницу Настройки &gt; Инструменты &gt; Командная PHP строка и выполняйте скрипт после каждой манипуляции с настройками:
  ```
  if(mail("email@example.ru", "TEST SUBJECT", "TEST BODY"))
  echo "Почтовая система работает!";
  else
  echo "Неудача, почтовая система не работает, попробуйте еще!";
  ```
  Если после прохождения мастера почтовая система не заработала, то:
- Зайдите под **root** в консольный режим.
- Перейдите в папку `/home/bitrix/`.



В этой папке мастер создает файл конфигурации **.msmtprc** - в нем хранится конфиг. Также, после того, как мы через функцию **mail** попробовали отправить письмо и получили ошибку, должен создаться файл **.msmtp.log** - с указанием ошибки отправки, которую вернул почтовый сервер. Его также необходимо изучить.




Примерное содержимое файла .msmtprc:



```
account default
logfile /home/bitrix/.msmtp.log
host mail-001.bitrix24.ru
port 25
from user@email.ru
auth off
```





Указан хост, порт и то, что авторизация не требуется. Если при таком конфиге в файле **.msmtp.log** ошибка вида:



```
cannot use a secure authentication method
```



то, значит, надо включать авторизацию:



```
account default
logfile /home/bitrix/.msmtp.log
host mail-001.bitrix24.ru
port 25
from user@email.ru
auth on
user user_name
password user_password
```




Значения **user_name** и **user_password** и **user@email.ru** - меняем на свои, их надо запросить у администратора почтового сервера, если они вам неизвестны.




Если ошибка не пропала, значит схема авторизации немного другая и надо пробовать другой конфиг. (После каждого изменения необходимо сохранить файл и без перезагрузки веб-сервера пробовать отправить почту скриптом, описанным выше.)




```
account default
logfile /home/bitrix/.msmtp.log
host mail-001.bitrix24.ru
port 25
from user@email.ru
auth on
login user_name
password user_password
```




или такой:




```

account default
logfile /home/bitrix/.msmtp.log
host mail-001.bitrix24.ru
port 25
from user@email.ru
auth login
user user_name
password user_password
```




Видны небольшие изменения в названии директив. Один из этих вариантов должен сработать, если нет - возможен другой, специфический механизм, это надо также уточнить у администратора почтового сервера.




Перечисленные выше варианты работают для почтовой системы без шифрования. Если на вашем почтовом сервере обязательно требуется шифрование для отправки письма, то тут надо запросить новый номер порта, обычно это 465, и конфиг меняется на такой:




```
account default
logfile /home/bitrix/.msmtp.log
host mail-001.bitrix24.ru
port 465
tls on
tls_starttls off
tls_certcheck off
from user@email.ru
auth on
login user_name
password user_password
```




Этот конфиг должен работать с шифрованым соединением. Также иногда возможны совмещения шифрования с вариантами авторизации, описанными выше, и надо пробовать разные конфиги, например:



```
account default
logfile /home/bitrix/.msmtp.log
host mail-001.bitrix24.ru
port 465
tls on
tls_starttls off
tls_certcheck off
from user@email.ru
auth login
user user_name
password user_password
```



или:

```
account default
logfile /home/bitrix/.msmtp.log
host mail-001.bitrix24.ru
port 465
tls on
tls_starttls off
tls_certcheck off
from user@email.ru
auth on
login user_name
password user_password
```




На этом настройка почты должна успешно завершиться.
