# Выполнение всех агентов на Cron

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 6557 — Настройка Postfix для отправки почты](lesson_6557.md)
- [Следующий: 6559 — Опции монтирования →](lesson_6559.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=6558

На больших и не очень проектах часто возникает вопрос с переносом исполнения некоторых особо тяжелых агентов на **Cron**.




- Для начала полностью отключим выполнение агентов на хите. Для этого необходимо выполнить команду в php-консоли административного меню продукта «1С-Битрикс» /bitrix/admin/php_command_line.php?lang=ru:
  ```
  COption::SetOptionString("main", "agents_use_crontab", "N");
  echo COption::GetOptionString("main", "agents_use_crontab", "N");
  COption::SetOptionString("main", "check_agents", "N");
  echo COption::GetOptionString("main", "check_agents", "Y");
  ```
  В результате выполнения должно быть `NN`.
- Убираем из файла `/bitrix/php_interface/dbconn.php` определение следующих констант:
  ```
  define("BX_CRONTAB_SUPPORT", true);
  define("BX_CRONTAB", true);
  ```
  И добавляем:
  ```
  if(!(defined("CHK_EVENT") && CHK_EVENT===true))
     define("BX_CRONTAB_SUPPORT", true);
  ```
- Далее создаем файл проверки агентов и рассылки системных сообщений `/bitrix/php_intarface/cron_events.php`:
  ```
  <?
  $_SERVER["DOCUMENT_ROOT"] = realpath(dirname(__FILE__)."/../..");
  $DOCUMENT_ROOT = $_SERVER["DOCUMENT_ROOT"];
  define("NO_KEEP_STATISTIC", true);
  define("NOT_CHECK_PERMISSIONS",true);
  define('CHK_EVENT', true);
  require($_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/main/include/prolog_before.php");
  @set_time_limit(0);
  @ignore_user_abort(true);
  CAgent::CheckAgents();
  define("BX_CRONTAB_SUPPORT", true);
  define("BX_CRONTAB", true);
  CEvent::CheckEvents();
  ?>
  ```
- И добавляем данный скрипт в **Cron**:
  ```
   */5 * * * * /usr/bin/php -f /home/bitrix/www/bitrix/php_interface/cron_events.php
  ```



После этого все агенты и отправка системных событий будут обрабатывается из-под **cron**, раз в 5 минут.






Чтобы не увеличивалась очередь отправки почтовых сообщений, нужно изменить параметр, отвечающий за количество почтовых обрабатываемых за раз событий. Для этого выполняем в php-консоли следующую команду:



```

COption::SetOptionString("main", "mail_event_bulk", "20");
echo COption::GetOptionString("main", "mail_event_bulk", "5");
```
