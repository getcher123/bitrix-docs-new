# Миграция сторонних модулей

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 15288 — Миграция через командную строку](lesson_15288.md)
- [Следующий: 15292 — Установка PostgreSQL →](lesson_15292.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=15290

**Внимание.** Встроенный мигратор предназначен только для основного продукта. Он не работает со сторонними решениями.
Если сторонний модуль не поддерживает PostgreSQL, мастер миграции отключит его автоматически.



### Миграция сторонних модулей

**Модули из [Битрикс24.Маркет](https://www.bitrix24.ru/apps/)**.  Все модули работают корректно. Они используют REST и не обращаются напрямую к базе данных.

**Модули из [Маркетплейс 1С-Битрикс](https://marketplace.1c-bitrix.ru/about/)**. Работоспособность зависит от способа разработки модуля:

- Модуль на ядре D7 и использует [Bitrix ORM](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=05748) — работает без доработок.
  Модуль не на ядре D7 — с высокой вероятностью работать не будет.
  Модуль на ядре D7 с прямыми запросами к СУБД или специфичными функциями — не работает. Рекомендуем обратиться к разработчикам модуля для внесения изменений в код.

### Адаптация модуля

#### Схема данных

Для квотирования идентификаторов в Postgres используются двойные кавычки.

Все неквотированные идентификаторы сначала преобразуются к НИЖНЕМУ регистру, а потом ищутся в метаданных базы.

Для совместимости к кодом «1С-Битрикс: Управление сайтом» в методе **fetch** ВСЕ колонки преобразуются к верхнему регистру.

Поэтому, если создана табличка:

```
create table test (ID int)
```

то по факту будет создана табличка test с колонкой **id** в нижнем регистре.

При выборке «из 1С-Битрикс: Управление сайтом»:

```
$rs = $DB->Query('SELECT ID from test');
```

Неквотированный ID будет сначала преобразован в нижний регистр, найден в метаданных и запрос выполнится.

Вот пример неправильного запроса:

```
$rs = $DB->Query('SELECT "ID" from test');
```

При выборке данных:

```
$ar = $rs->Fetch();
```

Метод **Fetch** автоматически преобразует колонку **id** в **ID**.

Если идентификатор нужно квотировать, то воспользуйтесь методом **quote** ([SqlHelper](https://dev.1c-bitrix.ru/api_d7/bitrix/main/db/sqlhelper/quote.php) или **CDatabase**). Для MySQL с регистром ничего делаться не будет, а вот для PostgresSQL идентификатор сначала будет приведён к нижнему регистру, а потом обрамлён двойными кавычками. Например:

Код

```
$sql = 'SELECT ' . $DB->quote('ID') . ' from ' . $DB->quote('test');
```

для MySql сформирует строку:

```
SELECT `ID` from `test`
```

а для Postgres:

```
SELECT "id" from "test"
```

Это будет рабочим кодом для обеих баз данных.

#### Типы колонок

| \| **Типы колонок** \|  \|<br>\| --- \| --- \|<br>\| **timestamp** \| Замените на datetime с переделкой логики на PHP. \|<br>\| **enum** \| Замените на char т.к. в PostgreSQL будет создаваться лишний тип для колонки. \|<br>\| unsigned \| В PostgreSQL отсутствует такой модификатор типа поэтому для него будет увеличено количество разрядов хранения.
<br>
<br>Примеры соответствия типов:<br>
<br>
<br>\\| MySql \\| PostgreSQL \\|<br>\\| --- \\| --- \\|<br>\\| smallint \\| smallint \\|<br>\\| unsigned smallint \\| int \\|<br>\\| int \\| int \\|<br>\\| unsigned int \\| int8 \\|<br>
<br>
<br>unsigned чаще всего используется не для ограничения хранения только положительных чисел (например результат ip2long), а как «дешёвый» способ удвоить диапазон хранимых данных. В таких случаях для упрощения поддержки и унификации типов в разных базах откажитесь от использования unsigned в MySql (с возможным увеличением разрядности хранения). \|<br>\| char \| Учтите, что PostgreSQL возвращает значение дополненное пробелами справа до указанной длины поля. Для char(1) это не составляет проблемы, однако если в char колонке вы храните данные переменной длины, то необходимо изменить тип хранения на varchar. \| |
| --- |

#### Имена индексов

В MySql имена индексов «локальные» по отношению к таблице и вполне возможна ситуация когда разные индексы у разных таблиц называются одинаково.

```

CREATE TABLE author (id int, name varchar(50), primary key (id), key ix_search(name));
CREATE TABLE book (id int, title varchar(50), primary key (id), key ix_search(title));
```

В PostgreSQL имена индексов должны быть уникальны в рамках схемы данных. Поэтому рекомендуется «составлять» имена индексов для удобства последующих манипуляций из:

- префикса (ux_ - для уникальных, tx_ - для полнотекстовых и ix_ для остальных),
- далее имя таблицы и разделитель «_»
- далее имена столбцов разделённых «_»

**Примечание**: Надо учитывать, что максимальная длина имени индекса в PostgreSQL - 63 символа. Для таких случаев необходимо обрезать имя индекса и если оно будет конфликтовать с другим, то добавить числовой суффикс через «_».

#### Конвертация install.sql

```

$cd mymodule
$mkdir install/db/pgsql
$cp install/mysql/uninstall.sql install/pgsql/uninstall.sql
$php -f ../perfmon/tools/mysql_to_pgsql.php -- install/mysql/install.sql > install/pgsql/install.sql
```

#### Использование специфичного квотирования

Использование обратных кавычек для экранирования идентификаторов в MySql не подходит для PostgreSQL.

Такие использования необходимо переписать с использованием методов `CDatabase::quote` или `SqlHelper::quote` или убрать как ненужное/избыточное. При этом необходимо помнить, что названия таблиц всегда в нижнем регистре, а названия столбцов в верхнем.

#### Строковые литералы

В отличие от MySql в PostgresQL не допускается использование двойных кавычек для строковых литералов. Необходимо заменить их на одиночные кавычки.

Также MySql и PostgreSQL имеют различие в интерпретации обратных слешей в строковых литералах.

Например, запрос:

```

select '\Bitrix'
```

в MySql вернет `"Bitrix"`, а в PostgreSQL —  `"\Bitrix"`.

А запрос:

```

select '\\Bitrix'
```

в MySql вернет `"\Bitrix"`, а в PostgreSQL —  `"\\Bitrix"`.

Чтобы избежать этого, используйте функцию *ForSql* ([SqlHelper](https://dev.1c-bitrix.ru/api_d7/bitrix/main/db/sqlhelper/quote.php) или *CDatabase*):

```

$rs = $DB->Query("SELECT '" . $DB->ForSql("\\Bitrix") . "'")
```

Для обеих баз данных запрос вернет `"\Bitrix"`.

#### Функции

| \| **Функции** \|  \|<br>\| --- \| --- \|<br>\| `ifnull()` \| Замените на coalesce. Например:
<br>
<br>```<br>SELECT ID,ifnull(NAME, '') AS NAME FROM b_user<br>```<br>
<br>
<br>Замените на:<br>
<br>
<br>```<br>SELECT ID,coalesce(NAME, '') AS NAME FROM b_user<br>``` \|<br>\| `mid()` \| Замените на substr. \|<br>\| `if()` \| Замените на оператор case when. Например:
<br>
<br>```<br>SELECT ID, if(TIMESTAMP_X > now() , 'red', 'green') AS STATUS FROM b_user<br>```<br>
<br>
<br>Замените на:<br>
<br>
<br>```<br>SELECT ID, case when TIMESTAMP_X > now() then 'red' else 'green' end AS STATUS FROM b_user<br>``` \|<br>\| `YEAR(), MONTH(), DAY()` \| Замените на extract(... from ...). Например:
<br>
<br>```<br>SELECT ID, YEAR(TIMESTAMP_X) AS A_YEAR FROM b_user<br>```<br>
<br>
<br>Замените на<br>
<br>
<br>```<br>SELECT ID, extract(YEAR FROM TIMESTAMP_X) AS A_YEAR FROM b_user<br>``` \|<br>\| `LOCATE()` \| Замените на position(... in ...). Например:
<br>
<br>```<br>SELECT ID, LOCATE(',',NAME) AS A_POS FROM b_user<br>```<br>
<br>
<br>Замените на<br>
<br>
<br>```<br>SELECT ID, POSITION(',' IN NAME) AS A_POS FROM b_user<br>``` \|<br>\| `get_lock()` и `release_lock()` \| Перепишите с прямых запросов на методы DatabaseConnection
<br>
<br>```<br>$lockName = 'mylock';
<br>$connection = \Bitrix\Main\Application::getConnection();
<br>if ($connection->lock($lockName))
<br>{
<br>	//....
<br>	$connection->unlock($lockName);
<br>}<br>``` \|<br>\| `date_add()` и `date_sub()` \| Перепишите с прямых запросов на методы [SqlHelper](https://dev.1c-bitrix.ru/api_d7/bitrix/main/db/sqlhelper/index.php)
<br>
<br>
<br>```<br>$sql = 'SELECT ID, date_add(TIMESTAMP_X, interval 60 second) AS EXPIRATION_TIME FROM b_user';<br>```<br>
<br>
<br>Меняем на:<br>
<br>
<br>
<br>```<br>$connection = \Bitrix\Main\Application::getConnection();
<br>$helper = $connection->getSqlHelper();
<br>
<br>$sql = 'SELECT ID, ' . $helper->addSecondsToDateTime(60, 'TIMESTAMP_X') . ' AS EXPIRATION_TIME FROM b_user';
<br>```<br>
<br>
<br>Для `date_sub` вызовите с отрицательным значением.
<br>
<br>Для `date_add(..., interval day)` используйте метод **addDaysToDateTime**. \|<br>\| `date_format()` \| Перепишите с использованием метода **formatDate** из `\Bitrix\Main\Application::getConnection()->getSqlHelper()`. \|<br>\| `concat()` \| Перепишите с использованием метода **getConcatFunction** из `\Bitrix\Main\Application::getConnection()->getSqlHelper()`. \|<br>\| `date()` \| Перепишите с использованием метода **getCurrentDateFunction** из `\Bitrix\Main\Application::getConnection()->getSqlHelper()`. \|<br>\| `rand()` \| Перепишите с использованием метода **getRandomFunction** из `\Bitrix\Main\Application::getConnection()->getSqlHelper()`. \|<br>\| `sha1()` \| Перепишите с использованием метода **getSha1Function** из `\Bitrix\Main\Application::getConnection()->getSqlHelper()`. \|<br>\| `group_concat()` \| Избавьтесь от использования этой функции так как она потенциально может вернуть <br>«битые» данные<br>&gt;The result is truncated to the maximum length that is given by the group_concat_max_len system variable, which has a default value of 1024.<br>[Подробнее](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_group-concat)...<br>. \| |
| --- |

#### Запросы

INSERT IGNORE

Перепишите с прямых запросов на методы [SqlHelper](https://dev.1c-bitrix.ru/api_d7/bitrix/main/db/sqlhelper/index.php).

```

$sql = 'INSERT IGNORE INTO b_user_group (USER_ID, GROUP_ID, DATE_ACTIVE_FROM, DATE_ACTIVE_TO) VALUES (...)';
$sql = 'INSERT IGNORE INTO b_user_access_check (USER_ID, PROVIDER_ID) SELECT ...';
```

Замените на:

```
$connection = \Bitrix\Main\Application::getConnection();
$helper = $connection->getSqlHelper();

$sql = $helper->getInsertIgnore("b_user_group", "(USER_ID, GROUP_ID, DATE_ACTIVE_FROM, DATE_ACTIVE_TO)", "VALUES (...)");
$sql = $helper->getInsertIgnore("b_user_access_check", "(USER_ID, PROVIDER_ID)", "SELECT ...");
```

[Различия в CDatabase::PrepareInsert и SqlHelper::prepareInsert](#CDatabase)

UPDATE IGNORE

Аналогичного по логике выполнения запроса в PostgreSQL нет. В принципе идея обновления значений первичного или альтернативного ключа не очень хорошая. Но запрос можно заменить на два. Это не вполне соответствует исходной логике, но обе БД будут вести себя одинаково.

```

INSERT IGNORE INTO ... SELECT ... WHERE
DELETE FROM ... WHERE
```

REPLACE INTO

Перепишите с прямых запросов на методы SqlHelper

```
$sql = 'REPLACE INTO b_module_table (KEY_ID, DATA) VALUES (...)';
```

Измените на:

```

$connection = \Bitrix\Main\Application::getConnection();
$helper = $connection->getSqlHelper();

$update = [
    'KEY_ID' => 1,
    'DATA' => 'a',
];
$merge = $helper->prepareMerge('b_module_table', ['KEY_ID'], $update, $update);
if ($merge[0])
{
    $connection->query($merge[0]);
}
//or another helper method
//$update - is a row in a rows array
foreach ($helper->prepareMergeMultiple('b_module_table', ['KEY_ID'], [$update]) as $sql)
{
    $connection->query($sql);
}
```

[Различия в CDatabase::PrepareInsert и SqlHelper::prepareInsert](#CDatabase)

DELETE ... LIMIT

Перепишите с прямых запросов на методы SqlHelper:

```

$sql = 'DELETE FROM b_test WHERE ACTIVE = 'N' ORDER BY TIMESTAMP_X ASC LIMIT 50';
```

Измените на:

```

$connection = \Bitrix\Main\Application::getConnection();
$helper = $connection->getSqlHelper();

$sql = $helper->prepareDeleteLimit('b_test', ['ID'], "ACTIVE = 'N'", ['TIMESTAMP_X' => 'ASC'], 50);
```

- Коррелированный UPDATE
- Коррелированный DELETE

С этими запросами нужно быть осторожными, они очень специфичны. Рекомендуется их переписать.

#### Использование классов

- MysqlCommonConnection
- MssqlConnection
- OracleConnection

Код, использующий эти классы, также требует внимания.



#### Некоторые особенности

`CDatabase::Add` в табличку без автоинкремента:

```

$DB->Add("b_iblock_fields", $arAdd, array("DEFAULT_VALUE"));
```

Перепишите на прямой запрос:

```

$arInsert = $DB->PrepareInsert("b_iblock_fields", $arAdd);
$DB->Query("INSERT INTO b_iblock_fields (".$arInsert[0].") VALUES (".$arInsert[1].")");
```

#### Различия в CDatabase::PrepareInsert и SqlHelper::prepareInsert (и update тоже).

- По разному обрабатываются поля типа дата/время.
- **CDatabase** учитывает настройку часовых поясов, а **SqlHelper** - нет

Поэтому в методы хеспера передавайте объект даты/времени созданный методом [\Bitrix\Main\Type\DateTime::createFromUserTime](https://dev.1c-bitrix.ru/api_d7/bitrix/main/type/datetime/createfromusertime.php). Например:

```
$fields = [
	'DATE_REGISTER' => '01.01.2023 00:00:00',
];
print_r($DB->PrepareInsert('b_user', $fields));

$fields = [
	'DATE_REGISTER' => new \Bitrix\Main\Type\DateTime('01.01.2023 00:00:00'),
];
print_r(\Bitrix\Main\Application::getConnection()->getSqlHelper()->prepareInsert('b_user', $fields));

$fields = [
	'DATE_REGISTER' => \Bitrix\Main\Type\DateTime::createFromUserTime('01.01.2023 00:00:00'),
];
print_r(\Bitrix\Main\Application::getConnection()->getSqlHelper()->prepareInsert('b_user', $fields));
```

Выведет

```
Array
(
    [0] => `DATE_REGISTER`
    [1] => DATE_ADD('2023-01-01 00:00:00', INTERVAL 3600 SECOND)
)
Array
(
    [0] => `DATE_REGISTER`
    [1] => '2023-01-01 00:00:00'
    [2] => Array
        (
        )
)
Array
(
    [0] => `DATE_REGISTER`
    [1] => '2023-01-01 01:00:00'
    [2] => Array
        (
        )
+
−)
```

#### Использование двойных кавычек

В PostgreSQL не допускается для строковых литералов. Необходимо менять на одинарные кавычки.
