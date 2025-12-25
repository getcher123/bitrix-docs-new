# Миграция на MySQL

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2496 — Пример работы с БД](lesson_2496.md)
- [Следующий: 7495 — Смена кодировки сайта →](lesson_7495.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=7843

**Внимание!** С 1 января 2017 года поддержка продуктов *«1С-Битрикс»* на **Oracle Database** и **MS SQL Server** стала ограниченной, заказчики не могут скачать обновления продукта платформы и воспользоваться возможностями новых релизов.

Задачу миграции Базы данных сайта с Oracle или MSSQL на MySQL можно с помощью [мигратора](http://dev.1c-bitrix.ru/docs/chm_files/migrator-1.0.27.1.zip). "Переезд" с его помощью возможен с Oracle или MSSQL только в одну сторону, на MySQL.

Мигратор работает на PHP не ниже версии 5.3.

Порядок действий при миграции:

1. Установите драйвера PHP для БД: [mysql](http://php.net/manual/en/mysql.php), [oracle](http://php.net/manual/en/book.oci8.php), [mssql](http://php.net/manual/en/book.sqlsrv.php).
2. Установите на БД MySQL редакцию 1С-Битрикс аналогичную используемой вами. Обновите её до той же версии, что и исходная установка.
3. В файле **config.php** укажите данные доступа к исходной и конечной базам данных.
  ## Пример файла config.php
  ```
  <?php
  /*
   * Config for Oracle/MSSQL => MySQL converter.
   *
   * @date 12/02/2016
   * @author Alexander Serbul
   * @copyright Bitrix
   */
  error_reporting(E_ALL);
  ini_set('memory_limit', '1024M');
  $config = array(
  	'logFile' => '/tmp/migrate_log.txt',//log file (important for diagnostics)
  	'logMigrateQueries' => false,//save queries as is to log file
  	'confirmTableDeletion' => true,//
  	'confirmTableCreation' => true,//
  	'skipCheckTruncation' => false,//skip checking of data truncation (slow)
  	'storeMigrationStatus' => false,//remember table migration status
  	'statusFolder' => '/tmp/mg_status',//where to save status about table migration
  	'encFrom' => 'UTF-8',//oracle data encoding
  	'encTo' => 'UTF-8',//mysql data encoding
  	'db' => array(
  		'oracle' => array(
  			'connectionString'	=> 'localhost/XE',
  			'user'				=> 'bitrix1',
  			'password'			=> '123456',
  			'database'			=> 'bitrix1',
  			'ignoreTables'		=> array(//which source tables to ignore
  				'B_FILE_ACTION',
  				'B_SALE_BIZVAL_CODE_1C',
  				'B_SALE_DELIVERY',
  				'B_SALE_DELIVERY_HANDLER',
  				'B_SALE_BIZVAL_PERSONTYPE'
  			)
  		),
  		'mssql' => array(
  			'serverName'		=> 'WIN-HO7VTHGJ7ED',
  			'connectionInfo'	=> array(
  				"UID"=>"sa",
  				"PWD"=>"123456",
  				"Database"=>"bitrix2",
  				//"CharacterSet" => "UTF-8",
  				'ReturnDatesAsStrings'=>true
  				//'ConnectionPooling' => false,
  				//'MultipleActiveResultSets' => false
  			),
  			'ignoreTables'		=> array(
  				'B_FILE_ACTION',
  				'B_SENDER_POSTING_LOCK',
  				'B_POSTING_LOCK',
  				'B_SALE_BIZVAL_CODE_1C',
  				'B_FAVORITE_LANG',
  				'B_LEARN_EXCEPTION_LOG',
  				'eshop_brand_reference_uf_intm',
  				'eshop_brand_reference_uf_tstringm'
  		)
  			),
  		'mysql' => array (
  			'host'		=> 'localhost',
  			'port'		=> 3306,
  			'user'		=> 'root',
  			'password'	=> '',
  			'database'	=> 'bitrix2',
  			'ignoreTables'		=> array()
  			)
  	)
  );
  ```
4. Запустите конверсию командой `"./converter.php convert oracle|mssql mysql"`.
5. Внимательно отслеживайте диагностику, думайте дважды перед подтверждением операций. Детали процесса можно изучить в лог-файле.
6. Если администратор не уверен в том с какими ключами нужно запускать конвертацию, то используйте команду `"./converter.php"` без параметров.
7. Вручную скопируйте файлы из старой установки на новую.
