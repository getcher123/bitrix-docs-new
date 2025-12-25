# Объект Query

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5752 — Короткие вызовы](lesson_5752.md)
- [Следующий: 20656 — Предустановленные выборки →](lesson_20656.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=5751

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/orm/querying-data.html). В ней улучшена структура, описание, примеры.

Все параметры *getList*, *getRow* и другие передаются вместе, при этом сразу же выполняется запрос и возвращается результат: все происходит за один вызов. Но существует и альтернативный способ конфигурации запроса и контроля за его выполнением - это объект *Entity\Query*:

```
// получение данных через getList
$result = BookTable::getList(array(
	'select' => array('ISBN', 'TITLE', 'PUBLISH_DATE')
	'filter' => array('=ID' => 1)
));

// аналогично через Entity\Query
$q = new Entity\Query(BookTable::getEntity());
$q->setSelect(array('ISBN', 'TITLE', 'PUBLISH_DATE'));
$q->setFilter(array('=ID' => 1));
$result = $q->exec();
```

Такой подход может быть удобным, когда необходима гибкость в построении запроса. Например, если параметры запроса заранее неизвестны и формируются программно, можно вместо множества разных аргументов использовать один объект Query, накапливая в нем параметры запроса:

```
$query = new Entity\Query(BookTable::getEntity());
attachSelect($query);
attachOthers($query);
$result = $query->exec();

function attachSelect(Entity\Query $query)
{
	$query->addSelect('ID');

	if (...)
	{
		$query->addSelect('ISBN');
	}
}

function attachOthers(Entity\Query $query)
{
	if (...)
	{
		$query->setFilter(...);
	}

	if (...)
	{
		$query->setOrder(...);
	}
}
```

Также объект *Entity\Query* позволяет построить запрос, но не выполнять его. Это бывает полезным для выполнения подзапросов или же просто для получения текста запроса и последующего его использования:

```
$q = new Entity\Query(BookTable::getEntity());
$q->setSelect(array('ID'));
$q->setFilter(array('=PUBLISH_DATE' => new Type\Date('2014-12-13', 'Y-m-d')));
$sql = $q->getQuery();

file_put_contents('/tmp/today_books.sql', $sql);

// таким образом, запрос "SELECT ID FROM my_book WHERE PUBLISH_DATE='2014-12-31'" будет сохранен в файл, но не будет выполнен.
```

Полный список методов Entity\Query для реализации описанных выше возможностей:

***select, group***:



- *setSelect, setGroup* - устанавливает массив с именами полей
- *addSelect, addGroup* - добавляет имя поля
- *getSelect, getGroup* - возвращает массив с именами полей

***filter***:

- *setFilter* - устанавливает одно- или многомерный массив с описанием фильтра
- *addFilter* - добавляет один параметр фильтра со значением
- *getFilter* - возвращает текущее описание фильтра

***order***:

- *setOrder* - устанавливает массив с именами полей и порядком сортировки
- *addOrder* - добавляет одно поле с порядком сортировки
- *getOrder* - возвращает текущее описание сортировки

***limit/offset***:

- *setLimit, setOffset* - устанавливает значение
- *getLimit, getOffset* - возвращает текущее значение

***runtime fields***:

- *registerRuntimeField* - регистрирует новое временное поле для исходной сущности

Объект Query является основополагающим элементом при выборке данных, он же используется внутри стандартного *getList*. Именно поэтому эффективность переопределения методов getList сводится на нет: если при вызове соответствующего метода хак сработает, то при аналогичном запросе напрямую через Query уже нет.
