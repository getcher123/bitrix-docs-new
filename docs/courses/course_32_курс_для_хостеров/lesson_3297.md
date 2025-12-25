# Ошибки запросов к БД

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3296 — Ошибки подключения к БД](lesson_3296.md)
- [Следующий: 3379 — 500 - Internal Server Error →](lesson_3379.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=3297

<!-- -&lt;p&gt;При возникновении ошибок запросов к базе данных на экран выдается сообщение вида:&lt;/p&gt;

&lt;p&gt;&lt;img src="/images/admin_start/install/additional/db_query_error.png"/&gt;&lt;/p&gt;

&lt;p&gt;Стандартный вид данного сообщения определяется в файле &lt;code&gt;/bitrix/php_interface/dbquery_error.php&lt;/code&gt;. &lt;/p&gt;- -->



Иногда возникает ситуация, когда сайт перестает отвечать, и посетителям отображается пустая страница. В этом случае рекомендуется открыть файл `bitrix/php_interface/dbconn.php` и установить значение параметра **$DBDebug = true;**




```
<?
define("DBPersistent", true);
$DBType = "mysql";
$DBHost = "localhost:31006";
$DBLogin = "root";
$DBPassword = "";
$DBName = "bsm_demo";
$DBDebug = true;
$DBDebugToFile = false;

set_time_limit(60);

define("BX_FILE_PERMISSIONS", 0644);
define("BX_DIR_PERMISSIONS", 0755);
@ini_set("memory_limit", "64M");
?>
```




В результате будет получен код ошибки, содержащий, как правило, названия поврежденных таблиц базы данных.




![](../../../images/courses/32/dev.1c-bitrix.ru/images/admin_start/install/additional/db_query_error_ext.png)




Запуск утилиты **perror.exe** с кодом ошибки (файл **perror.exe** хранится в каталоге **mysql/bin**) позволяет получить описание ошибки по ее коду:




![](../../../images/courses/32/dev.1c-bitrix.ru/images/admin_start/install/additional/error_code.png)




**Примечание**: Для ошибки с кодом **28** выводится следующее описание:

![](../../../images/courses/32/dev.1c-bitrix.ru/images/admin_start/install/additional/error_code_examp.png)


Данное сообщение означает, что на диске, где установлена база данных, недостаточно места для ее работы.




Если речь идет о повреждении базы данных, то рекомендуется воспользоваться встроенным инструментом системы для проверки и восстановления базы данных. Использование скрипта проверки и восстановления базы данных позволит оперативно восстановить работу сайта.




**Обратите внимание на следующее:**

- Скрипт проверки и восстановления базы данных может быть использован только для **MySQL** с типом таблиц
  			**MyISAM**
                      Для таблиц типа InnoDB неактуальна сама проблема поломки таблиц, поэтому для них нет инструмента.
  		.
- Скрипт проверки запускается из административного раздела сайта Настройки -&gt; Инструменты -&gt; Проверка БД:
  ![](../../../images/courses/32/dev.1c-bitrix.ru/images/admin_start/install/additional/repair_db_page.png)
  В случае, если повреждены таблицы статистики и нет возможности перейти в административный раздел, сбор статистики может быть временно отключен с помощью параметра `?no_keep_statistic_LICENSE-KEY=Y`. В параметре указывается лицензионный ключ сайта.
- Существует возможность использования скрипта проверки и восстановления базы данных без перехода в административный раздел.
      Для этого при обращении к странице восстановления необходимо указать два параметра: **имя** (login) и **пароль** (password) на доступ к базе данных. Например: http://www.mysite.ru/bitrix/admin/repair_db.php?login=DB_Login&password=DB_Password. По умолчанию значения данных параметров хранятся в файле `/bitrix/php_interface/dbconn.php`.




**Проблема:**




На экран выводится ошибка:




| \| MySQL Query Error: ….. [Out of memory restart server and try again (needed 65528 bytes)] \|<br>\| --- \| |
| --- |




**Решение:**




Необходимо увеличить объем памяти в настройках **MySQL**.




Рекомендуется использовать следующие параметры **MySQL**, задавая их в конфигурационном файле MySQL **my.cnf**:




```
key_buffer = 128K
max_allowed_packet = 16M
table_cache = 4
sort_buffer_size = 128K
read_buffer_size = 128K
read_rnd_buffer_size = 128K
net_buffer_length = 128K
thread_stack = 128K
```




После изменения параметров необходимо будет перезагрузить MySQL.
