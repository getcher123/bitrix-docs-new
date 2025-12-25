# Смена кодировки сайта

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 7843 — Миграция на MySQL](lesson_7843.md)
- [Следующий: 15284 — Порядок действий для миграции →](lesson_15284.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=7495

С версии main 24.0.0 продукты 1С-Битрикс полностью перешли на кодировку UTF-8. Однобайтовые установки более не поддерживаются.

Сменить кодировку поможет **Мастер конвертации сайта в UTF-8**. Или вы можете выполнить её вручную с помощью инструкции в уроке.



**Внимание!** Прежде чем приступить к конвертации сайта обязательно сделайте [резервную копию сайта и базы данных](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&CHAPTER_ID=04833&LESSON_PATH=3906.4833). Настоятельно рекомендуем предварительно потренироваться выполнять конвертацию на отдельной копии сайта. Конвертация сайта сложная операция и каждый случай индивидуален. При её выполнении высока вероятность потерять важные данные, если что-то пойдет не так!

### Общий порядок действий

Редактировать файлы и вносить правки на сервере можно подключаясь по **SSH**.

Рассмотрим общий порядок конвертации сайта с кодировки cp1251 в UTF-8:

1.
   В региональных настройках Настройки &gt; Настройки продукта &gt; Языковые параметры &gt; Региональные настройки сменитe кодировку на **UTF-8** для всех языков;
2. ## mbstring.func_overload до версии 20.100.0 модуля main
  До версии 20.100.0 требуется добавить в файл `/.htaccess` строки:
  ```
  php_value mbstring.func_overload 2
  php_value mbstring.internal_encoding UTF-8
  ```
  С версии **20.100.0** Главного модуля (**main**) требуется удаление настройки PHP [mbstring.func_overload](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=30130). Эта опция более не требуется и не поддерживается платформой.
3. Установите в файле настроек **php.ini** значение `default_charset = "utf-8"`;
  Расположение файла настроек php.ini можно посмотреть заранее в административном разделе на странице
  			Настройки PHP
                      Страница **Настройки PHP** (Настройки &gt; Инструменты &gt; Диагностика &gt; Настройки PHP) служит для отображения информации о текущих настройках PHP.
  Подробнее в курсе [Администратор. Базовый](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=2027&LESSON_PATH=3906.4493.4506.2027)
  		 (Loaded Configuration File) или с помощью PHP функции [phpinfo()](https://www.php.net/manual/ru/function.phpinfo.php).
  Если сайт размещен на Хостинге, возможно понадобится обратиться к хостинг провайдеру для внесения этих настроек.
4. Добавьте в `/bitrix/php_interface/dbconn.php`
  ```
  define("BX_UTF", true);
  ```
  В этом же файле удалите строки, относящиеся к кодировке cp1251:
  ```
  setlocale(LC_ALL, 'ru_RU.CP1251');
  mb_internal_encoding("Windows-1251");
  ```
5. Установите значение **'value' =&gt; true** для utf_mode в файле `/bitrix/.settings.php`:
  ```
  utf_mode =>
  	array(
  		'value' => true,
  		'readonly' => true,
  	),
  ```
6. Перекодируйте всю базу данных в UTF-8. Вероятнее всего придётся обращаться за помощью к администратору сервера.
  Установите в файле `/bitrix/php_interface/after_connect.php`
  ```
  $DB->Query("SET NAMES 'utf8'");
  $DB->Query('SET collation_connection = "utf8_unicode_ci"');
  ```
  и в файле `/bitrix/php_interface/after_connect_d7.php`
  ```
  $this->queryExecute("SET NAMES 'utf8'");
  $this->queryExecute('SET collation_connection = "utf8_unicode_ci"');
  //До версии main 22.0 вместо $this использовалась переменная $connection.
  ```
  Установите в `/.htaccess`:
  ```
  php_value default_charset utf-8
  ```
  Перекодируйте все файлы сайта в UTF-8.
  Сбросьте весь кеш;
  Выйдите и зайдите заново на сайт чтобы обновить данные сессии.

### База данных

Для конвертации базы (БД) потребуется сменить кодировку самой базы, всех её таблиц и всех текстовых полей таблиц. **НЕ** выполняйте конвертацию БД из административной части. Используйте для этого другие доступные средства.

В простом случае (без сериализованных данных) перекодировать базу данных и все таблицы можно следующим образом:

- Изменить кодировку самой базы данных сайта:
  ```
  ALTER DATABASE имя_базы_данных charset=utf8;
  ```
- Изменить кодировку соединения с базой данных:
  ```
  SET NAMES 'utf8'
  ```
  ```
  ALTER DATABASE database_name CHARACTER SET utf8 COLLATE utf8_unicode_ci;
  ```
- Выполним запрос, который позволит найти все таблицы базы данных и сформировать запрос на смену кодировки для каждой:
  ```
  SELECT CONCAT('ALTER   TABLE `', t.`TABLE_SCHEMA`, '`.`', t.`TABLE_NAME`, '` CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;') as sqlcode
  FROM `information_schema`.`TABLES` t
  WHERE 1
  AND t.`TABLE_SCHEMA` = 'имя_базы_данных'
  ORDER BY 1
  ;
  ```
- В качестве ответа получим список запросов вида:
  ```
  ALTER TABLE `имя_базы_данных`.`имя_таблицы` CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
  ```
- Выполните все запросы. База данных и таблицы перекодированы.

**Внимание:** Если в базе данных хранятся сериализованные данные, то приведенный выше метод конвертации для них не подойдет. Используйте специальные методы / средства для конвертации таких данных.

### Файлы

В простом варианте, когда все файлы сайта в кодировке cp1251, перекодировать их в UTF-8 можно выполнив такую команду в **корневой папке сайта** (для UNIX систем):

```

// переходим в корневую папку сайта. Например:
cd /var/www/html/

// выполняем команду для перекодирования файлов
find . -name '*.php' -type f -exec iconv -fcp1251 -tutf8 -o /tmp/tmp_file {} \; -exec mv /tmp/tmp_file {} \;
```

**Важно:**

1. Способ не подходит для сайтов на нескольких языках, т.к. в таком случае в структуре будут присутствовать файлы в различных кодировках.
2. Учитывайте особенности используемого вами Unix. Указанный выше пример может не сработать. В этом случае его надо адаптировать под вашу ОС. Например:
  ```
  // выполняем команду для перекодирования файлов
  find ./ -type f -name "*.php" -exec bash -c 'file="$1"; iconv -f cp1251 -t utf8 "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"' _ {} \;
  ```

#### Использование внешних программ или конвертация файлов вручную

Часто при использовании внешних программ для конвертации в файлы добавляется специальная последовательность символов, так называемый **BOM**. Эти символы должны находиться только вначале файла, а поскольку итоговая страница является составной из нескольких php файлов, то спецсимволы появляются в теле страницы. Если делаете конвертацию файлов вручную - не сохраняйте с BOM!

### Бизнес-процессы

Шаблоны бизнес-процессов с переменными, константами и параметрами хранятся в сериализованном и запакованном виде в таблице **b_bp_workflow_template**, поэтому смена кодировки БД не повлияет на них. Чтобы привести их к нужной кодировке требуется выполнить дополнительные действия.

Сначала обязательно сделайте копию таблиц шаблонов b_bp_workflow_template одним из приведенных ниже способов:

1. копированием с помощью [SQL-запросов](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=2029#sql):
  ```
  //создаём новую таблицу, аналогичную оригинальной
  CREATE TABLE b_bp_workflow_template_bak LIKE b_bp_workflow_template;
  // копируем данные в созданную таблицу
  INSERT INTO b_bp_workflow_template_bak SELECT * FROM b_bp_workflow_template;
  ```
2. созданием полной [резервной копии базы данных](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=5330#parameters).

Следующим шагом выполните скрипт в командной [PHP-строке](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=2029#php), который изменит кодировку данных:

```
cmodule::includemodule("bizproc");
$connection = \Bitrix\Main\Application::getConnection();

$sql_select = "select * from b_bp_workflow_template";
$process = $connection->query($sql_select);

while ($r = $process->fetch())
{
	$gztemp = $r['TEMPLATE'];
	$gzvar = $r['VARIABLES'];
	$gzconst = $r['CONSTANTS'];
	$gzpar = $r['PARAMETERS'];

	// Распаковываем данные по БП.
	$serializedTemplate = @gzuncompress($gztemp);
	$serializedVariables = @gzuncompress($gzvar);
	$serializedConstants = @gzuncompress($gzconst);
	$serializedParameters = @gzuncompress($gzpar);

	// Рассериализуем данные по БП.
	$serializedTemplate = @unserialize($serializedTemplate);
	$serializedVariables = @unserialize($serializedVariables);
	$serializedConstants = @unserialize($serializedConstants);
	$serializedParameters = @unserialize($serializedParameters);

	if ($serializedTemplate === false) continue;

	// Меняем кодировку данных.
	$serializedTemplate = $APPLICATION->ConvertCharsetArray(
		$serializedTemplate,
		'windows-1251',
		'utf-8'
	);
	$serializedVariables = $APPLICATION->ConvertCharsetArray(
		$serializedVariables,
		'windows-1251',
		'utf-8'
	);
	$serializedConstants = $APPLICATION->ConvertCharsetArray(
		$serializedConstants,
		'windows-1251',
		'utf-8'
	);
	$serializedParameters = $APPLICATION->ConvertCharsetArray(
		$serializedParameters,
		'windows-1251',
		'utf-8'
	);

	$r["TEMPLATE"] = $serializedTemplate;
	$r["VARIABLES"] = $serializedVariables;
	$r["CONSTANTS"] = $serializedConstants;
	$r["PARAMETERS"] = $serializedParameters;

	// Сохраняем обновленную информацию.
	CBPWorkflowTemplateLoader::update(
		$r["ID"],
		[
			'TEMPLATE' => $r['TEMPLATE'],
			'VARIABLES' => $r['VARIABLES'],
			'CONSTANTS' => $r['CONSTANTS'],
			'PARAMETERS' => $r['PARAMETERS']
		],
		$r,
		false,
		false
	);
}
```

### Советы и ссылки

Основные шаги по конвертации сайта выполнены. Если после конвертации возникают ошибки при открытии сайта, включите режим отладки `'debug' => true` в файле `/bitrix/.settings.php`. Это позволит видеть где и какие возникают ошибки.

Обязательно выполните

			проверку системы

                    Форма **Проверка системы** (Настройки &gt; Инструменты &gt; Проверка системы) предназначена для всесторонней проверки соответствия параметров системы, на которой осуществляется функционирование проекта, минимальным и рекомендуемым техническим требованиям продукта.

Подробнее в курсе [Администратор. Базовый](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=14020).

		. По результатам проверки будет видно, что ещё нужно исправить. Пользуйтесь подсказками под знаками вопроса справа.

Если возникли ошибки с таблицами базы данных (последняя строка проверки), можно посмотреть

			логи в журнале

                    ![](../../../images/courses/43/dev.1c-bitrix.ru/images/admin_start/admin_base/tools/test_info_11_sm.png)

		. В конце файла логов будут указаны запросы, с помощью которых можно исправить эти ошибки. Перед началом исправления рекомендуется сделать копию базы данных.

**Внимание!** С версии **23.200.0** появился альтернативный путь смены кодировки - Мастер конвертации сайта в UTF-8. Он находится на странице списка мастеров `/bitrix/admin/wizard_list.php?lang=ru`. Все шаги его работы сопровождаются необходимыми пояснениями.

#### Список ссылок по теме:

- [Конвертация сайта из cp1251 в UTF-8](http://dev.1c-bitrix.ru/community/blogs/howto/1466.php) (блог разработчиков);
- [Выбор кодировки сайта](lesson_2919.md);
  [Настройка параметров ядра](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=02795);
  [Проверка системы](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=14020) в курсе Администратор. Базовый.
  [Как изменить кодировку базы данных MySQL?](https://handyhost.ru/help/hosting/bazyi-dannyix/kak-izmenit-kodirovku-tabliczyi-mysql.html).
