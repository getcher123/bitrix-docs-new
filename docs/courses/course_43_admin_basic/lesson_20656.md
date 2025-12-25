# Предустановленные выборки

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5751 — Объект Query](lesson_5751.md)
- [Следующий: 4766 — Выбор данных из хранимых процедур вместо таблиц →](lesson_4766.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=20656

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/orm/querying-data.html). В ней улучшена структура, описание, примеры.

### Глобальная область данных

При необходимости одну таблицу можно описать несколькими сущностями, разделив записи на сегменты:

```
class Element4Table extends \Bitrix\Iblock\ElementTable
{
	public static function getTableName()
		{
		return 'b_iblock_element';
		}

	public static function setDefaultScope(Query $query)
		{
		$query->where("IBLOCK_ID", 4);
		}

}

class Element5Table extends \Bitrix\Iblock\ElementTable
{
		public static function getTableName()
		{
		return 'b_iblock_element';
		}

	public static function setDefaultScope(Query $query)
		{
		$query->where("IBLOCK_ID", 5);
		}
}
```

Метод *setDefaultScope* будет выполняться при каждом запросе, пропуская через себя объект запроса. В нем можно задавать не только фильтр, но и любые другие параметры запроса.

### Локальная область данных

Начиная с версии **20.5.500** появилась возможность задать предустановленные выборки – методы *with**. Это аналог *setDefaultScope*, но не на глобальном уровне, а на пользовательском – вызов при необходимости. После описания метода в сущности можно вызывать его в конструкторе запросов:

```

class UserTable
{
	public static function withActive(Query $query)
		{
		$query->where('ACTIVE', true);
		}
}

$activeUsers = UserTable::query()
	->withActive()
	->fetchCollection();

// WHERE `ACTIVE`='Y'
```

В качестве аргумента используется объект *Bitrix\Main\ORM\Query\Query*, поэтому можно задавать не только фильтр, но и любые другие параметры запроса. Кроме того, можно дополнить метод своими аргументами, которые также будут переданы при вызове из конструктора запросов:

```

class UserTable
{
	public static function withActive(Query $query, $value)
	{
	$query
		->addSelect('LOGIN')
		->where('ACTIVE', $value);
	}
}

$activeUsers = UserTable::query()
	->withActive(false)
	->fetchCollection();

// SELECT `LOGIN` ... WHERE `ACTIVE`='N'
```
