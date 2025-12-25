# N:M

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11739 — 1:1](lesson_11739.md)
- [Следующий: 11733 — Аннотации классов →](lesson_11733.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11741

#### Примитивные отношения без вспомогательных данных

У книги может быть несколько авторов, у автора может быть несколько книг. В таких случаях создается отдельная таблица с двумя полями `AUTHOR_ID` и `BOOK_ID`. В **ORM** не придется оформлять ее отдельной сущностью, достаточно описать отношение специальным полем *ManyToMany*:

```
//Файл bitrix/modules/main/lib/test/typography/booktable.php

namespace Bitrix\Main\Test\Typography;

use Bitrix\Main\ORM\Fields\Relations\ManyToMany;

class BookTable extends \Bitrix\Main\ORM\Data\DataManager
{
	public static function getMap()
	{
		return [
			// ...

			(new ManyToMany('AUTHORS', AuthorTable::class))
				->configureTableName('b_book_author')
		];
	}
}
```

```
//Файл bitrix/modules/main/lib/test/typography/authortable.php

namespace Bitrix\Main\Test\Typography;

use Bitrix\Main\ORM\Fields\Relations\ManyToMany;

class AuthorTable extends \Bitrix\Main\ORM\Data\DataManager
{
	public static function getMap()
	{
		return [
			// ...

			(new ManyToMany('BOOKS', BookTable::class))
				->configureTableName('b_book_author')
		];
	}
}
```

**Необязательно описывать поле в обеих сущностях** - можно только в одной, но тогда и доступ к данным будет осуществляться только через нее.

В конструктор передаются название поля и класс партнерской сущности. В случае примитивных отношений достаточно вызвать метод *configureTableName* с указанием имени таблицы, где хранятся связующие данные. Более сложный случай будет рассмотрен ниже, в примере отношений **Книг** с **Магазинами**.

В данном же случае в памяти автоматически создается временная сущность для работы с промежуточной таблицей. Фактически вы нигде не увидите ее следов, но для понимания происходящего и возможных дополнительных настроек приоткроем внутренности. Системная сущность промежуточной таблицы имеет примерно такой вид:

```
class ... extends \Bitrix\Main\ORM\Data\DataManager
{
	public static function getTableName()
	{
		return 'b_book_author';
	}

	public static function getMap()
	{
		return [
			(new IntegerField('BOOK_ID'))
				->configurePrimary(true),

			(new Reference('BOOK', BookTable::class,
				Join::on('this.BOOK_ID', 'ref.ID')))
				->configureJoinType('inner'),

			(new IntegerField('AUTHOR_ID'))
				->configurePrimary(true),

			(new Reference('AUTHOR', AuthorTable::class,
				Join::on('this.AUTHOR_ID', 'ref.ID')))
				->configureJoinType('inner'),
		];
	}
}
```

Это не более чем типовая сущность с референсами (направленными отношениями 1:N) к исходным сущностям-партнерам. Имена полей формируются на основе имен сущностей и имен их первичных ключей:

```
new IntegerField('BOOK_ID') - snake_case от Book + primary поле ID
new Reference('BOOK') - snake_case от Book
new IntegerField('AUTHOR_ID') - snake_case от Author + primary поле ID
new Reference('AUTHOR') - snake_case от Author
```

Чтобы задать имена полей явно, особенно это актуально в сущностях с составными первичными ключами для избегания путаницы, используются конфигурирующие методы:

```
//Файл bitrix/modules/main/lib/test/typography/booktable.php

namespace Bitrix\Main\Test\Typography;

use Bitrix\Main\ORM\Fields\Relations\ManyToMany;

class BookTable extends \Bitrix\Main\ORM\Data\DataManager
{
	public static function getMap()
	{
		return [
			// ...

			(new ManyToMany('AUTHORS', AuthorTable::class))
				->configureTableName('b_book_author')
				->configureLocalPrimary('ID', 'MY_BOOK_ID')
				->configureLocalReference('MY_BOOK')
				->configureRemotePrimary('ID', 'MY_AUTHOR_ID')
				->configureRemoteReference('MY_AUTHOR')
		];
	}
}
```

```
//Файл bitrix/modules/main/lib/test/typography/authortable.php

namespace Bitrix\Main\Test\Typography;

use Bitrix\Main\ORM\Fields\Relations\ManyToMany;

class AuthorTable extends \Bitrix\Main\ORM\Data\DataManager
{
	public static function getMap()
	{
		return [
			// ...

			(new ManyToMany('BOOKS', BookTable::class))
				->configureTableName('b_book_author')
				->configureLocalPrimary('ID', 'MY_AUTHOR_ID')
				->configureLocalReference('MY_AUTHOR'),
				->configureRemotePrimary('ID', 'MY_BOOK_ID')
				->configureRemoteReference('MY_BOOK')
		];
	}
}
```

Метод *configureLocalPrimary* указывает, как будет называться привязка к полю из первичного ключа текущей сущности, аналогично *configureRemotePrimary* задает соответствие полей первичного ключа сущности-партнера. Методы *configureLocalReference* и *configureRemoteReference* задают имена референсов к исходным сущностям. При описанной выше конфигурации системная сущность отношений будет иметь примерно такой вид:

```
class ... extends \Bitrix\Main\ORM\Data\DataManager
{
	public static function getTableName()
	{
		return 'b_book_author';
	}

	public static function getMap()
	{
		return [
			(new IntegerField('MY_BOOK_ID'))
				->configurePrimary(true),

			(new Reference('MY_BOOK', BookTable::class,
				Join::on('this.MY_BOOK_ID', 'ref.ID')))
				->configureJoinType('inner'),

			(new IntegerField('MY_AUTHOR_ID'))
				->configurePrimary(true),

			(new Reference('MY_AUTHOR', AuthorTable::class,
				Join::on('this.MY_AUTHOR_ID', 'ref.ID')))
				->configureJoinType('inner'),
		];
	}
}
```

Как и в случае *Reference* с *OneToMany*, здесь тоже можно переопределить тип джойна методом *configureJoinType* (значение по умолчанию - "left"):

```
(new ManyToMany('AUTHORS', AuthorTable::class))
	->configureTableName('b_book_author')
	->configureJoinType('inner')
```

Чтение данных работает аналогично отношениям 1:N:

```
// выборка со стороны авторов
$author = \Bitrix\Main\Test\Typography\AuthorTable::getByPrimary(18, [
	'select' => ['*', 'BOOKS']
])->fetchObject();

foreach ($author->getBooks() as $book)
{
	echo $book->getTitle();
}
// цикл выведет "Title 1" и "Title 2"

// выборка со сороны книг
$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(2, [
	'select' => ['*', 'AUTHORS']
])->fetchObject();

foreach ($book->getAuthors() as $author)
{
	echo $author->getLastName();
}
// цикл выведет "Last name 17" и "Last name 18"
```

Выборка объектов вместо массивов вновь выгодно отличается тем, что не происходит "двоения" данных, как это происходит с массивами:

```
$author = \Bitrix\Main\Test\Typography\AuthorTable::getByPrimary(18, [
	'select' => ['*', 'BOOK_' => 'BOOKS']
])->fetchAll();

// вернет
Array (
	[0] => Array
		[ID] => 18
		[NAME] => Name 18
		[LAST_NAME] => Last name 18
		[BOOK_ID] => 1
		[BOOK_TITLE] => Title 1
		[BOOK_PUBLISHER_ID] => 253
		[BOOK_ISBN] => 978-3-16-148410-0
		[BOOK_IS_ARCHIVED] => Y
	)
	[1] => Array (
		[ID] => 18
		[NAME] => Name 18
		[LAST_NAME] => Last name 18
		[BOOK_ID] => 2
		[BOOK_TITLE] => Title 2
		[BOOK_PUBLISHER_ID] => 253
		[BOOK_ISBN] => 456-1-05-586920-1
		[BOOK_IS_ARCHIVED] => N
	)
)
```

Создание связи между объектами двух сущностей происходит так же, как в случае с отношениями 1:N:

```
// со стороны авторов
$author = \Bitrix\Main\Test\Typography\AuthorTable::getByPrimary(17)
	->fetchObject();

$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
	->fetchObject();

$author->addToBooks($book);

$author->save();

// со стороны книг
$author = \Bitrix\Main\Test\Typography\AuthorTable::getByPrimary(17)
	->fetchObject();

$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
	->fetchObject();

$book->addToAuthors($author);

$book->save();
```

Методы *removeFrom* и *removeAll* работают тоже аналогично.

Для массивов подобных конструкций не предусмотрено. Как связывать сущности, используя массивы - смотрите ниже в примере отношений **Книг** с **Магазинами**.

#### Отношения со вспомогательными данными

| \| **STORE_ID** \| **BOOK_ID** \| **QUANTITY** \|<br>\| --- \| --- \| --- \|<br>\| 33 \| 1 \| 4 \|<br>\| 33 \| 2 \| 0 \|<br>\| 43 \| 2 \| 9 \| |
| --- |

Когда есть дополнительные данные (количество книг в наличие), а не только первичные ключи исходных сущностей, такое отношение следует описать отдельной сущностью:

```
namespace Bitrix\Main\Test\Typography;

use Bitrix\Main\ORM\Data\DataManager;
use Bitrix\Main\ORM\Fields\IntegerField;
use Bitrix\Main\ORM\Fields\Relations\Reference;
use Bitrix\Main\ORM\Query\Join;

class StoreBookTable extends DataManager
{
	public static function getTableName()
	{
		return 'b_store_book';
	}

	public static function getMap()
	{
		return [
			(new IntegerField('STORE_ID'))
				->configurePrimary(true),

			(new Reference('STORE', StoreTable::class,
				Join::on('this.STORE_ID', 'ref.ID')))
				->configureJoinType('inner'),

			(new IntegerField('BOOK_ID'))
				->configurePrimary(true),

			(new Reference('BOOK', BookTable::class,
				Join::on('this.BOOK_ID', 'ref.ID')))
				->configureJoinType('inner'),

			(new IntegerField('QUANTITY'))
				->configureDefaultValue(0)
		];
	}
}
```

Если для простых отношений без вспомогательных данных использовались поля *ManyToMany*, здесь их использование будет сильно ограничено. Можно будет создавать и удалять связи, но не будет доступа к вспомогательному полю `QUANTITY`. С помощью removeFrom*() можно будет удалить связь, с помощью addTo*() можно будет добавить связь со значением `QUANTITY` только по умолчанию, и не будет возможности обновить значение `QUANTITY`. Поэтому в таких случаях более гибким будет использование непосредственно сущности-посредника:

```
// объект книги
$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
	->fetchObject();

// объект магазина
$store = \Bitrix\Main\Test\Typography\StoreTable::getByPrimary(34)
	->fetchObject();

// новый объект связи книги с магазином
$item = \Bitrix\Main\Test\Typography\StoreBookTable::createObject()
	->setBook($book)
	->setStore($store)
	->setQuantity(5);

// сохранение
$item->save();
```

Обновление количества книг:

```
// объект существующей связи
$item = \Bitrix\Main\Test\Typography\StoreBookTable::getByPrimary([
	'STORE_ID' => 33, 'BOOK_ID' => 2
])->fetchObject();

// обновление количества
$item->setQuantity(12);

// сохранение
$item->save();
```

Удаление связи:

```
// объект существующей связи
$item = \Bitrix\Main\Test\Typography\StoreBookTable::getByPrimary([
	'STORE_ID' => 33, 'BOOK_ID' => 2
])->fetchObject();

// удаление
$item->delete();
```

То есть, работа с объектом связи ведется как с объектом любой другой сущности. Для массивов тоже следует использовать стандартные подходы по работе с данными:

```
// добавление
\Bitrix\Main\Test\Typography\StoreBookTable::add([
	'STORE_ID' => 34, 'BOOK_ID' => 1, 'QUANTITY' => 5
]);

// обновление
\Bitrix\Main\Test\Typography\StoreBookTable::update(
	['STORE_ID' => 34, 'BOOK_ID' => 1],
	['QUANTITY' => 12]
);

// удаление
\Bitrix\Main\Test\Typography\StoreBookTable::delete(
	['STORE_ID' => 34, 'BOOK_ID' => 1]
);
```

Выше было упомянуто, что использовать поле *ManyToMany* в случае со вспомогательными данными - непродуктивно. Правильнее будет использовать тип *OneToMany*:

```
//Файл bitrix/modules/main/lib/test/typography/booktable.php

namespace Bitrix\Main\Test\Typography;

use Bitrix\Main\ORM\Fields\Relations\OneToMany;

class BookTable extends \Bitrix\Main\ORM\Data\DataManager
{
	public static function getMap()
	{
		return [
			// ...

			(new OneToMany('STORE_ITEMS', StoreBookTable::class, 'BOOK'))
		];
	}
}
```

```
//Файл bitrix/modules/main/lib/test/typography/storetable.php

namespace Bitrix\Main\Test\Typography;

use Bitrix\Main\ORM\Fields\Relations\OneToMany;

class StoreTable extends \Bitrix\Main\ORM\Data\DataManager
{
	public static function getMap()
	{
		return [
			// ...

			(new OneToMany('BOOK_ITEMS', StoreBookTable::class, 'STORE'))
		];
	}
}
```

В таком случае выборка ничем не будет отличаться от отношений 1:N, только в этот раз будут возвращаться объекты отношения *StoreBook*, а не сущности-партнера:

```
$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1, [
	'select' => ['*', 'STORE_ITEMS']
])->fetchObject();

foreach ($book->getStoreItems() as $storeItem)
{
	printf(
		'store "%s" has %s of book "%s"',
		$storeItem->getStoreId(), $storeItem->getQuantity(), $storeItem->getBookId()
	);
	// выведет store "33" has 4 of book "1"
}
```
