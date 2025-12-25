# Фильтр ORM

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3269 — Взаимосвязи между сущностями (устаревший вариант)](lesson_3269.md)
- [Следующий: 2410 — Автоматическая генерация ORM-классов →](lesson_2410.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3030

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/orm/querying-data.html). В ней улучшена структура, описание, примеры.

В обновлении main 17.5.2 в ORM появился новый фильтр.

#### Одиночные условия

Пример простейшего запроса:

```
\Bitrix\Main\UserTable::query()
	->where("ID", 1)
	->exec();

// WHERE `main_user`.`ID` = 1
```

Если нужен другой оператор сравнения, то он указывается явно:

```
\Bitrix\Main\UserTable::query()
	->where("ID", "<", 10)
	->exec();

// WHERE `main_user`.`ID` < 10
```

Пример с использованием IS NULL:

```
\Bitrix\Main\UserTable::query()
	->whereNull("ID")
	->exec();

// WHERE `main_user`.`ID` IS NULL
```

Для всех **where*** методов есть **whereNot*** аналоги. Пример:

```
\Bitrix\Main\UserTable::query()
	->whereNotNull("ID")
	->exec();

// WHERE `main_user`.`ID` IS NOT NULL
```

Помимо общего **where**, можно использовать следующие операторные методы:

```
whereNull($column) / whereNotNull($column)

whereIn($column, $values|Query|SqlExpression) / whereNotIn($column, $values|Query|SqlExpression)

whereBetween($column, $valueMin, $valueMax) / whereNotBetween($column, $valueMin, $valueMax)

whereLike($column, $value) / whereNotLike($column, $value)

whereExists($query|SqlExpression) / whereNotExists($query|SqlExpression)
```

Для произвольного выражения с привязкой к полям сущности следует использовать метод

			**whereExpr**

                    Доступно с версии **20.400.0** модуля **main**.

		:

```
\Bitrix\Main\UserTable::query()
	->whereExpr('JSON_CONTAINS(%s, 4)', ['SOME_JSON_FIELD'])
	->exec();

// WHERE JSON_CONTAINS(`main_user`.`SOME_JSON_FIELD`, 4)
```

Аргументы выражения и составных полей аналогичны конструктору поля `ExpressionField` и подставляются через функцию

			sprintf

                    **sprintf** — Возвращает отформатированную строку.
Подробнее в [документации по PHP](https://www.php.net/manual/ru/function.sprintf.php).

		.

Список операторов находится в `\Bitrix\Main\ORM\Query\Filter\Operator::$operators` (см. ключи массива):

= , &lt;&gt; , != , &lt; , &lt;= , &gt; , &gt;= , in , between , like , exists

#### Сравнение с другим полем

Отдельный метод *whereColumn* упрощает сравнение полей друг с другом:

```
\Bitrix\Main\UserTable::query()
	->whereColumn('NAME', 'LOGIN')
	->exec();

// WHERE `main_user`.`NAME` = `main_user`.`LOGIN`
```

Этот метод мало чем отличается от *where*, и формально это тот же самый вызов с небольшой оберткой:

```
\Bitrix\Main\UserTable::query()
	->where('NAME', new Query\Filter\Expression\Column('LOGIN'))
	->exec();

// WHERE `main_user`.`NAME` = `main_user`.`LOGIN`
```

*whereColumn* обеспечивает особую гибкость использования колонок в фильтре, например:

```
\Bitrix\Main\UserTable::query()
	->whereIn('LOGIN', [
		new Column('NAME'),
		new Column('LAST_NAME')
	])
	->exec();

// WHERE `main_user`.`LOGIN` IN (`main_user`.`NAME`, `main_user`.`LAST_NAME`)
```

Колонки можно использовать в любом операторе. И они будут восприняты именно как поля конкретных сущностей, а не просто произвольное SQL выражение.

#### Множественные условия

Для нескольких условий предполагается такая запись:

```
\Bitrix\Main\UserTable::query()
	->where('ID', '>', 1)
	->where('ACTIVE', true)
	->whereNotNull('PERSONAL_BIRTHDAY')
	->whereLike('NAME', 'A%')
	->exec();

// WHERE `main_user`.`ID` > 1 AND `main_user`.`ACTIVE` = 'Y' AND `main_user`.`PERSONAL_BIRTHDAY` IS NOT NULL AND `main_user`.`NAME` LIKE 'A%'
```

**Примечание**: для boolean полей со значениями Y/N, 1/0 и т.п. можно использовать true и false.

Если необходимо указать несколько условий в одном вызове, то использовать такой формат: (операторные методы можно заменять кодами операторов)

```
\Bitrix\Main\UserTable::query()
	->where([
		['ID', '>', 1],
		['ACTIVE', true],
		['PERSONAL_BIRTHDAY', '<>', null],
		['NAME', 'like', 'A%']
	])
	->exec();

// WHERE `main_user`.`ID` > 1 AND `main_user`.`ACTIVE` = 'Y' AND `main_user`.`PERSONAL_BIRTHDAY` IS NOT NULL AND `main_user`.`NAME` LIKE 'A%'
```

#### OR и вложенные фильтры

Для хранения всех условий фильтра в Query используется контейнер условий `\Bitrix\Main\Entity\Query\Filter\ConditionTree`. Помимо стандартных условий, в него допускается добавление других экземпляров *ConditionTree*, таким образом создавая любой уровень ветвления и вложенности.

Все приведенные выше вызовы *where* - проксирование к базовому контейнеру. Следующие два вызова приведут к совершенно одинаковому результату:

```
\Bitrix\Main\UserTable::query()
	->where([
		['ID', '>', 1],
		['ACTIVE', true]
	])
	->exec();

\Bitrix\Main\UserTable::query()
	->where(Query::filter()->where([
		["ID", '>', 1],
		['ACTIVE', true]
	]))->exec();

// WHERE `main_user`.`ID` > 1 AND `main_user`.`ACTIVE` = 'Y'
```

Вместо массива использовался объект фильтра. Это позволяет создавать субфильтры и менять логику с AND на OR:

```
\Bitrix\Main\UserTable::query()
	->where('ACTIVE', true)
	->where(Query::filter()
		->logic('or')
		->where([
			['ID', 1],
			['LOGIN', 'admin']
		])
	)->exec();

// WHERE `main_user`.`ACTIVE` = 'Y' AND (`main_user`.`ID` = 1 OR `main_user`.`LOGIN` = 'admin')
```

Допускается использование цепочки вызовов:

```
\Bitrix\Main\UserTable::query()
	->where('ACTIVE', true)
	->where(Query::filter()
		->logic('or')
		->where('ID', 1)
		->where('LOGIN', 'admin')
	)
	->exec();

// WHERE `main_user`.`ACTIVE` = 'Y' AND (`main_user`.`ID` = 1 OR `main_user`.`LOGIN` = 'admin')
```

#### Выражения

В фильтре в качестве имен полей допустимо задание [ExpressionField](lesson_2244.md#ExpressionField), которые автоматически регистрируются как **runtime** поля сущности.

```
\Bitrix\Main\UserTable::query()
	->where(new ExpressionField('LNG', 'LENGTH(%s)', 'LAST_NAME'), '>', 10)
	->exec();

// WHERE LENGTH(`main_user`.`LAST_NAME`) > '10'
```

Для упрощения подобных конструкций добавлен хелпер, строящий вычисляемые поля:

```
\Bitrix\Main\UserTable::query()
	->where(Query::expr()->length("LAST_NAME"), '>', 10)
	->exec();

// WHERE LENGTH(`main_user`.`LAST_NAME`) > '10'

\Bitrix\Main\UserTable::query()
	->addSelect(Query::expr()->count("ID"), 'CNT')
	->exec();

// SELECT COUNT(`main_user`.`ID`) AS `CNT` FROM `b_user` `main_user`
```

В хелпере заложены наиболее популярные SQL выражения:

- count
- countDistinct
- sum
- min
- avg
- max
- length
- lower
- upper
- concat

#### Совместимость с getList

Если вместо цепочки вызовов Query использовать [getList](lesson_5753.md), то фильтр вставляется в него вместо массива:

```
\Bitrix\Main\UserTable::getList([
	'filter' => ['=ID' => 1]
]);

\Bitrix\Main\UserTable::getList([
	'filter' => Query::filter()
		->where('ID', 1)
]);

// WHERE `main_user`.`ID` = 1
```

#### Условия JOIN

Описания референсов представлено в таком формате:

```
new Entity\ReferenceField('GROUP', GroupTable::class,
	Join::on('this.GROUP_ID', 'ref.ID')
)
```

Метод *`on`* - короткая и более семантически уместная запись `Query::filter()` с предустановленным условием по колонкам. Возвращает инстанс фильтра, и можно строить какие угодно условия JOIN:

```
new Entity\ReferenceField('GROUP', GroupTable::class,
	Join::on('this.GROUP_ID', 'ref.ID')
		->where('ref.TYPE', 'admin')
		->whereIn('ref.OPTION', [
			new Column('this.OPTION1'),
			new Column('this.OPTION2'),
			new Column('this.OPTION3')
		]
)
```

Везде, где указывается имя поля, подразумевается, что можно указать любую цепочку переходов:

```
->whereColumn('this.AUTHOR.UserGroup:USER.GROUP.OWNER.ID', 'ref.ID');
```

#### Формат массива

Для использования фильтра в виде массива существует метод конвертации из массива в объект `\Bitrix\Main\ORM\Query\Filter\ConditionTree::createFromArray`. Формат массива имеет общий вид:

```
$filter = [
	['FIELD', '>', 2],
	[
		'logic' => 'or',
		['FIELD', '<', 8],
		['SOME', 9]
	],
	['FIELD', 'in', [5, 7, 11]],
	['FIELD', '=', ['column' => 'FIELD2']],
	['FIELD', 'in', [
		['column' => 'FIELD1'],
		['value' => 'FIELD2'],
		['FIELD3']
	],
	[
		'negative' => true,
		['FIELD', '>', 19]
	],
 ];
```

При обычном сравнении значение передается либо непосредственно:

```
['FIELD', '>', 2]
```

либо в виде массива с ключом `value`:

```
['FIELD', '>', ['value' => 2]]
```

При сравнении с колонкой следует использовать массив с ключом `column`:

```
['FIELD1', '>', ['column' => 'FIELD2']]
```

Вложенные фильтры передаются в качестве аналогичных вложенных массивов. В качестве замены методов объекта для отрицания `negative()` и изменения логики `logic()` используются одноименные ключи:

```
$filter = [
	['FIELD', '>', 2],
	[
		'logic' => 'or',
		['FIELD', '<', 8],
		['SOME', 9]
	],
	[
		'negative' => true,
		['FIELD', '>', 19]
	]
]
```

Остальные методы `where*` заменяются соответствующими операторами сравнения `in`, `between`, `like` и т.д.

```
['FIELD', 'in', [5, 7, 11]]
```

**Внимание:** Будьте внимательны при использовании массивов. Не подставляйте сырые, переданные пользователем, данные в качестве фильтра, так как в них могут содержаться опасные условия для раскрытия данных БД. Проверяйте все входящие условия через белый список полей.
