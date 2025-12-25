# 1:N

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11751 — Восстановление коллекции](lesson_11751.md)
- [Следующий: 11739 — 1:1 →](lesson_11739.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11737

В нашей тестовой вселенной книга может принадлежать и издаваться строго в одном издательстве. Получаем отношение "1 издательство - N книг".

#### Книга и издательство

В таких случаях в таблицу **Книги** следует добавить поле **PUBLISHER_ID**, значение которого будет указывать на **Издательство**.

```
namespace Bitrix\Main\Test\Typography;

use Bitrix\Main\ORM\Fields\IntegerField;

class BookTable extends \Bitrix\Main\ORM\Data\DataManager
{
	public static function getMap()
	{
		return [
			// ...
			(new IntegerField('PUBLISHER_ID'))
		];
	}
}
```

Но для ORM одного этого поля недостаточно для понимания связи между сущностями *Book* и *Publisher*. Чтобы такое понимание возникло, используются поля множества *Bitrix\Main\ORM\Fields\Relations*, в данном случае для указания направленной связи "много к одному" нужно поле типа *Reference*:

```
namespace Bitrix\Main\Test\Typography;

use Bitrix\Main\ORM\Fields\IntegerField;
use Bitrix\Main\ORM\Fields\Relations\Reference;
use Bitrix\Main\ORM\Query\Join;

class BookTable extends \Bitrix\Main\ORM\Data\DataManager
{
	public static function getMap()
	{
		return [
			// ...
			(new IntegerField('PUBLISHER_ID')),

			(new Reference(
					'PUBLISHER',
					PublisherTable::class,
					Join::on('this.PUBLISHER_ID', 'ref.ID')
				))
				->configureJoinType('inner')
		];
	}
}
```

Параметры конструктора *Reference*:

| \| **Параметр** \| **Описание** \|<br>\| --- \| --- \|<br>\| $name \| Имя поля. \|<br>\| $referenceEntity \| Класс связываемой сущности. \|<br>\| $referenceFilter \| Условия "джойна". Ожидается объект [фильтра](lesson_3030.md). В отличие от регулярного использования фильтра, здесь к именам колонок нужно добавлять префиксы "this." и "ref.", чтобы обозначить принадлежность к текущей и связываемой сущности соответственно.
<br>
<br>Для читаемости создан класс *Bitrix\Main\ORM\Query\Join*, единственный метод которого *on* возвращает объект фильтра *Bitrix\Main\ORM\Query\Filter\ConditionTree*, задавая перед этим наиболее популярное условие *whereColumn*. \| |
| --- |

Дополнительно можно сконфигурировать [тип "джойна"](https://stackoverflow.com/questions/6294778/mysql-quick-breakdown-of-the-types-of-joins). По умолчанию это *left join*, в примере выше задается *inner join*.

Теперь можно воспользоваться описанным отношением при выборке данных:

```
$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1, [
	'select' => ['*', 'PUBLISHER']
])->fetchObject();

echo $book->getPublisher()->getTitle();
// выведет Publisher Title 253
```

Доступ к объекту сущности *Publisher* реализуется через "геттер" *getPublisher()*. Таким образом, можно подключать более глубокие цепочки отношений, и так же по цепочкам "геттеров" добираться до конечных объектов.

Чтобы установить связь, достаточно передать объект сущности *Publisher* в соответствующий "сеттер":

```
// инициализация издателя
$publisher = \Bitrix\Main\Test\Typography\PublisherTable::wakeUpObject(253);

// инициализация книги
$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
	->fetchObject();

// установка значения объекта
$book->setPublisher($publisher);

// сохранение
$book->save();
```

Значение поля **PUBLISHER_ID** будет заполнено автоматически из переданного объекта.

С массивами результат выглядит не так лаконично:

```
$result = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1, [
	'select' => ['*', 'PUBLISHER']
]);

print_r($result->fetch());
/* выведет
Array (
	[ID] => 1
	[TITLE] => Title 1
	[PUBLISHER_ID] => 253
	[ISBN] => 978-3-16-148410-0
	[IS_ARCHIVED] => Y
	[MAIN_TEST_TYPOGRAPHY_BOOK_PUBLISHER_ID] => 253
	[MAIN_TEST_TYPOGRAPHY_BOOK_PUBLISHER_TITLE] => Publisher Title 253
)
*/
```

Полям связанной сущности присваиваются уникальные имена, основанные на пространстве имен и имени класса. Можно воспользоваться механизмом "алиасов" для получения более коротких и практичных имен:

```
$result = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1, [
	'select' => ['*', 'PUB_' => 'PUBLISHER']
]);

print_r($result->fetch());
/* выведет
Array (
	[ID] => 1
	[TITLE] => Title 1
	[PUBLISHER_ID] => 253
	[ISBN] => 978-3-16-148410-0
	[IS_ARCHIVED] => Y
	[PUB_ID] => 253
	[PUB_TITLE] => Publisher Title 253
)
*/
```

#### Издательство и книги

Пока что доступ к отношению работает только по направлению "Книга" -&gt; "Издатель". Чтобы сделать его двунаправленным, понадобится описать отношение на стороне сущности *Publisher*:

```
namespace Bitrix\Main\Test\Typography;

use Bitrix\Main\ORM\Data\DataManager;
use Bitrix\Main\ORM\Fields\Relations\OneToMany;

class PublisherTable extends DataManager
{
	public static function getMap()
	{
		return [
			// ...

			(new OneToMany('BOOKS', BookTable::class, 'PUBLISHER'))->configureJoinType('inner')
		];
	}
}
```

Параметры конструктора *OneToMany*:

| \| **Параметр** \| **Описание** \|<br>\| --- \| --- \|<br>\| $name \| Имя поля. \|<br>\| $referenceEntity \| Класс связываемой сущности. \|<br>\| $referenceFilter \| Имя поля `Reference` в сущности-партнере, через которое осуществляется связь. \| |
| --- |

Дополнительно можно переопределить [тип джойна](https://stackoverflow.com/questions/6294778/mysql-quick-breakdown-of-the-types-of-joins). По умолчанию используется тип, заданный в *Reference* поле связываемой сущности.

Теперь можно воспользоваться описанным отношением при выборке данных:

```
$publisher = \Bitrix\Main\Test\Typography\PublisherTable::getByPrimary(253, [
	'select' => ['*', 'BOOKS']
])->fetchObject();

foreach ($publisher->getBooks() as $book)
{
	echo $book->getTitle();
}

// цикл выведет "Title 1" и "Title 2"
```

В примере выше видно принципиальное преимущество объектной модели перед массивами. Несмотря на то, что фактически выбрано две записи (для одного **Издателя** нашлось две книги), по факту из результата получается только один объект. Система самостоятельно распознала этот случай и склеила все книги издателя в одну [Коллекцию](/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=011743).

Если запросить из результата массив, будет классическая структура данных с двоением данных **Издателя**:

```
$data = \Bitrix\Main\Test\Typography\PublisherTable::getByPrimary(253, [
	'select' => ['*', 'BOOK_' => 'BOOKS']
])->fetchAll();

// вернет
Array (
	[0] => Array (
		[ID] => 253
		[TITLE] => Publisher Title 253
		[BOOK_ID] => 2
		[BOOK_TITLE] => Title 2
		[BOOK_PUBLISHER_ID] => 253
		[BOOK_ISBN] => 456-1-05-586920-1
		[BOOK_IS_ARCHIVED] => N
	)
	[1] => Array (
		[ID] => 253
		[TITLE] => Publisher Title 253
		[BOOK_ID] => 1
		[BOOK_TITLE] => Title 1
		[BOOK_PUBLISHER_ID] => 253
		[BOOK_ISBN] => 978-3-16-148410-0
		[BOOK_IS_ARCHIVED] => Y
	)
)
```

Чтобы добавить новую **Книгу** **Издателю**, используется именованный "сеттер" *addTo*:

```
// инициализация издателя
$publisher = \Bitrix\Main\Test\Typography\PublisherTable::getByPrimary(253)
	->fetchObject();

// инициализация книги
$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(2)
	->fetchObject();

// добавление книги в коллекцию отношения
$publisher->addToBooks($book);

// сохранение
$publisher->save();
```

Для удаления связи со стороны книги достаточно установить *setPublisher()* другого издателя или *null*. А чтобы сделать это со стороны **Издателя**, существуют специализированные "сеттеры" *removeFrom()* и *removeAll()*:

```
// инициализация книги
$book = \Bitrix\Main\Test\Typography\Book::wakeUp(2);

// инициализация издателя
$publisher = \Bitrix\Main\Test\Typography\PublisherTable::getByPrimary(253, [
	'select' => ['*', 'BOOKS']
])->fetchObject();

// удаление одной конкретной книги издателя
$publisher->removeFromBooks($book);

// или удаление всех книг издателя
$publisher->removeAllBooks();

// во время сохранения поле PUBLISHER_ID в Книгах будет обновлено на пустое значение
// сами книги удалены не будут, удаляется именно связь
$publisher->save();
```

**Важно обратить внимание, что** для корректной работы поле отношения должно быть заполнено - в примере выше оно указано при выборке данных. Если вы не выбирали значения из базы данных или не уверены в их заполненности у конкретного объекта, необходимо предварительно вызвать метод *fill*:

```
// инициализация книги
$book = \Bitrix\Main\Test\Typography\BookTable::wakeUpObject(2);

// у издателя будет заполнен только первичный ключ
$publisher = \Bitrix\Main\Test\Typography\PublisherTable::wakeUpObject(253);

// заполняем поле отношения
$publisher->fillBooks();

// удаление одной конкретной книги
$publisher->removeFromBooks($book);

// или удаление всех книг
$publisher->removeAllBooks();

// во время сохранения поле PUBLISHER_ID в Книгах будет обновлено на пустое значение
// сами книги удалены не будут
$publisher->save();
```

В случае с массивами операции *addTo*, *removeFrom* и *removeAll* невозможны, можно создать связь только со стороны сущности **Книги**.
