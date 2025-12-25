# Выбор данных из хранимых процедур вместо таблиц

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20656 — Предустановленные выборки](lesson_20656.md)
- [Следующий: 3250 — Выборки в отношениях 1:N и N:M →](lesson_3250.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=4766

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/orm/querying-data.html). В ней улучшена структура, описание, примеры.

ORM подходит даже для таких экзотических запросов, как выборка данных не из таблицы, а из хранимых процедур. Такие процедуры могут быть созданы в MSSQL-базе данных.

Укажем название функции в методе *getTableName*:

```
public static function getTableName()
{
	// return "foo_table_name"
	return "foo_table_procedure()";
}
```

В этом виде такой код работать не будет. Дело в том, что при использовании подключения [Bitrix\Main\DB\MssqlConnection](http://dev.1c-bitrix.ru/api_d7/bitrix/main/db/mssqlconnection/index.php) все вхождения имен таблиц проходят через экранирование. Попытка сразу выполнить такой запрос приведет к выбрасыванию исключения:

```
MS Sql query error: Invalid object name 'foo_table_procedure()'. (400)

SELECT

[base].[bar] AS [BAR],

[base].[baz] AS [BAZ],

FROM [foo_table_procedure()] [base]
```

Получению нужного результата мешают только знаки **[** и **]**, которыми [MssqlSqlHelper](http://dev.1c-bitrix.ru/api_d7/bitrix/main/db/mssqlsqlhelper/index.php) защитил имя "таблицы". Проблема решается созданием собственного подключения **Connection** и **SqlHelper**.

Вариант решения: на сервер установите расширение mssql и реализуйте следующую архитектуру:

```
class MssqlSqlHelper extends Bitrix\Main\DB\SqlHelper
{
	public function quote($identifier)
	{
		if (self::isKnowFunctionalCall($identifier))
		{
			return $identifier
		}
			else
		{
			return parent::quote($identifier);
		}
	}
}
```

Где *self::isKnownFunctionCall* - метод проверки, который возвращает *true*, если в **$identifier** находится `“foo_table_procedure()”`.

**Примечание**: Пример разработан компанией [Интерволга](http://www.intervolga.ru).
