# Выполнение всех агентов на Cron

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 29402 — Ручная настройка memcached](lesson_29402.md)
- [Следующий: 29412 — Опции монтирования →](lesson_29412.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=29410

**Внимание!** Приведённые настройки выходят за рамки меню Виртуальной машины. Это означает, что информация - ознакомительная и применять её следует с чётким пониманием того что вы делаете и с собственной ответственностью за совершаемые действия. В нашей техподдержке рассматриваются только вопросы по работе пунктов меню ВМ.





### Перенос агентов на cron




На больших и не очень проектах часто возникает вопрос с переносом исполнения некоторых особо тяжелых агентов на **Cron**. Агент считается "тяжёлым", если время его выполнения более 10 минут.




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
- В скрипте /home/bitrix/www/bitrix/php_interface/cron_events.php используйте код:
  ```
  <?php
  $_SERVER["DOCUMENT_ROOT"] = realpath(dirname(__FILE__)."/../..");
  $DOCUMENT_ROOT = $_SERVER["DOCUMENT_ROOT"];
  define("NO_KEEP_STATISTIC", true);
  define("NOT_CHECK_PERMISSIONS",true);
  define('BX_NO_ACCELERATOR_RESET', true);
  define('CHK_EVENT', true);
  define('BX_WITH_ON_AFTER_EPILOG', true);
  require($_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/main/include/prolog_before.php");
  @set_time_limit(0);
  @ignore_user_abort(true);
  CAgent::CheckAgents();
  define("BX_CRONTAB_SUPPORT", true);
  define("BX_CRONTAB", true);
  if(CModule::IncludeModule('sender'))
  {
      \Bitrix\Sender\MailingManager::checkPeriod(false);
      \Bitrix\Sender\MailingManager::checkSend();
  }
  require($_SERVER['DOCUMENT_ROOT']."/bitrix/modules/main/tools/backup.php");
  CMain::FinalActions();
  ?>
  ```
  Замените `/home/bitrix/www/` на свой путь к корню сайта.
- Далее добавляем запуск скрипта в **Cron**:
  ```
  */1 * * * * /usr/bin/php -f /home/bitrix/www/bitrix/php_interface/cron_events.php
  ```



После этого все агенты и отправка системных событий будут обрабатывается из-под **cron**, раз в 1 минуту.




**Примечание**: Если после выполнения команды cron не заработал, то, значит, у вас ошибки в проекте. Эти ошибки, скорее всего, не связаны с агентами. Надо смотреть  в логах PHP. Включить расширенный вывод ошибок можно в файле настроек [.settings.php](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=02795).






### Очередь отправки почтовых сообщений



Чтобы не увеличивалась очередь отправки почтовых сообщений, нужно изменить параметр, отвечающий за количество почтовых обрабатываемых за раз событий. Для этого выполняем в php-консоли следующую команду:



```

COption::SetOptionString("main", "mail_event_bulk", "20");
echo COption::GetOptionString("main", "mail_event_bulk", "5");
```




Если очередной запуск **cron_events.php** произошёл до завершения работы ранее запущенного скрипта, то запуска агентов не произойдет и скрипт завершит свою работу (т.к. агенты блокируются на время выполнения). В данном случае обработка ничем не отличается от обработки на хите, новый хит может произойти в тот момент, когда еще не отработали агенты на предыдущем.




Как правило, скрипты, выполненные из под **cron**, не имеют ограничения на время исполнения. Но если в скриптах используются методы для работы с БД, то можно столкнуться с ошибкой выполнения вложенных скриптов. Для избежания этой ошибки можно подправить значение в `/bitrix/php_interface/dbconn.php`:




```
// если скрипт выполняется кроном, то лимит подключения к БД - 600 секунд, иначе - 60
@set_time_limit(php_sapi_name() == "cli" ? 600 : 60);
```
