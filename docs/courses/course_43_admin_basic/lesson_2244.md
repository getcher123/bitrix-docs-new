# Операции с сущностями

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 4803 — Концепция, описание сущности](lesson_4803.md)
- [Следующий: 11689 — Класс объекта →](lesson_11689.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2244

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/orm/entity-operations.html). В ней улучшена структура, описание, примеры.

Для операций записи используются три метода уже описанного нами класса: *BookTable::add*, *BookTable::update*, *BookTable::delete*.

  [BookTable::add](#add)
  [BookTable::update](#update)
  [BookTable::delete](#delete)
  [Валидаторы](#validator)
  [События](#events)
  [Форматирование значений](#formatting)
  [Вычисляемые значения](#ExpressionField)
  [Предупреждения об ошибках](#warning)

#### BookTable::add

Метод  для добавления записи принимает на вход массив со значениями, где ключи - имена полей сущности:

```
namespace SomePartner\MyBooksCatalog;

use Bitrix\Main\Type;

$result = BookTable::add(array(
	'ISBN' => '978-0321127426',
	'TITLE' => 'Patterns of Enterprise Application Architecture',
	'PUBLISH_DATE' => new Type\Date('2002-11-16', 'Y-m-d')
));

if ($result->isSuccess())
{
	$id = $result->getId();
}
```

Метод возвращает объект результата *Entity\AddResult*, и в примере выше показано, как проверить успешность добавления и получить ID добавленной записи.

**Примечание**. Для значений полей типов **DateField** и **DateTimeField**, а также для пользовательских полей **Дата** и **Дата со временем**, необходимо использовать объекты классов *Bitrix\Main\Type\Date* и *Bitrix\Main\Type\DateTime*. По умолчанию в конструктор передается строковая дата в формате сайта, но можно и явно указать формат передаваемой даты.

**Внимание!** Поле **fields** необходимо использовать в верхнем регистре: **FIELDS**. В нижнем регистре это поле зарезервировано для нужд системы. Аналогично зарезервировано и поле **auth_context**.

#### BookTable::update

Обновление записи происходит похожим образом, только к массиву значений в параметрах добавляется значение первичного ключа:

```
$result = BookTable::update($id, array(
	'PUBLISH_DATE' => new Type\Date('2002-11-15', 'Y-m-d')
));
```

В примере исправлена неправильно указанная при добавлении дата. В качестве результата возвращается объект *Entity\UpdateResult*, у которого так же есть проверочный метод *isSuccess()* (не было ли ошибок в запросе), и, дополнительно, можно узнать была ли запись фактически обновлена: *getAffectedRowsCount()*.

#### BookTable::delete

Для удаления записи нужен только первичный ключ:

```
$result = BookTable::delete($id);
```

**Примечание**. Для удаления или обновления составного ключа следует передавать оба значения:

```
BookTable::delete(['key1' => value1, 'key2' => value2]);
```

#### Результаты операции

Если во время операции произошла одна или несколько ошибок, их текст можно получить из результата:

```
$result = BookTable::update(...);

if (!$result->isSuccess())
{
	$errors = $result->getErrorMessages();
}
```

#### Значения по умолчанию

Бывает, что у большинства новых записей значение какого-то поля всегда одно и то же, или вычисляется автоматически. Пусть у каталога книг дата издания/публикации по умолчанию будет сегодняшним днем (логично добавлять книгу в каталог сразу в день ее выхода). Вернемся к описанию поля в сущности и используем параметр `\`default_value\``:

```
new Entity\DateField('PUBLISH_DATE', array(
	'default_value' => new Type\Date
))
```

Теперь при добавлении записи без явного указания даты издания ее значением будет текущий день:

```
$result = BookTable::add(array(
	'ISBN' => '978-0321127426',
	'TITLE' => 'Some new book'
));
```

Усложнение задачи: если нет возможности оперативно добавлять книги в день их выхода, но известно, что, как правило, новые книги выходят по пятницам. Соответственно, они добавлены будут только на следующей неделе:

```
new Entity\DateField('PUBLISH_DATE', array(
	'default_value' => function () {
		// figure out last friday date
		$lastFriday = date('Y-m-d', strtotime('last friday'));
		return new Type\Date($lastFriday, 'Y-m-d');
	}
))
```

Значением параметра `\`default_value\`` может быть любой `\`callable\``: имя функции, массив из класса/объекта и названия метода, или анонимная функция.

#### Валидаторы

Перед записью новых данных в БД нужно обязательно проверять их на корректность. Для этого предусмотрены валидаторы:

```
new Entity\StringField('ISBN', array(
	'required' => true,
	'column_name' => 'ISBNCODE',
	'validation' => function() {
		return array(
			new Entity\Validator\RegExp('/[\d-]{13,}/')
		);
	}
))
```

Теперь при добавлении и изменении записей ISBN будет проверен по шаблону `[\d-]{13,}` - код должен содержать только цифры и дефис, минимум 13 цифр.

Валидация задается параметром `'validation'` в конструкторе поля и представляет собой callback, который возвращает массив валидаторов.

**Примечание**: Почему validation - callback, а не сразу массив валидаторов? Это своего рода отложенная загрузка: валидаторы будут инициализированы только тогда, когда действительно нужна будет валидация данных. В большинстве же случаев - при выборке данных из БД - валидация не нужна.

В качестве валидатора принимается наследник *Entity\Validator\Base* или любой `callable`, который должен вернуть `true`, или текст ошибки, или объект *Entity\FieldError* (в случае, если вы хотите использовать собственный код ошибки).

Точно известно, что в ISBN коде должно быть 13 цифр, эти цифры могут разделять несколько дефисов:

978-0321127426

978-1-449-31428-6

9780201485677

Чтобы удостовериться, что цифр там именно 13, напишем свой собственный валидатор:

```
new Entity\StringField('ISBN', array(
	'required' => true,
	'column_name' => 'ISBNCODE',
	'validation' => function() {
		return array(
			function ($value) {
				$clean = str_replace('-', '', $value);

				if (preg_match('/^\d{13}$/', $clean))
				{
					return true;
				}
				else
				{
					return 'Код ISBN должен содержать 13 цифр.';
				}
			}
		);
	}
))
```

Первым параметром в валидатор передается значение данного поля, но опционально доступно больше информации:

```
new Entity\StringField('ISBN', array(
	'required' => true,
	'column_name' => 'ISBNCODE',
	'validation' => function() {
		return array(
			function ($value, $primary, $row, $field) {
				// value - значение поля
				// primary - массив с первичным ключом, в данном случае [ID => 1]
				// row - весь массив данных, переданный в ::add или ::update
				// field - объект валидируемого поля - Entity\StringField('ISBN', ...)
			}
		);
	}
))
```

С таким набором данных можно произвести гораздо больший спектр сложных проверок.

Если к полю приписано несколько валидаторов, и есть необходимость программно узнать, какой конкретно из них сработал, можно воспользоваться кодом ошибки. Например, у кода ISBN последняя цифра - контрольная, служит для проверки правильности числовой части ISBN. Надо добавить валидатор для ее проверки и обработаем его результат особым образом:

```
// описываем валидатор в поле сущности
new Entity\StringField('ISBN', array(
	'required' => true,
	'column_name' => 'ISBNCODE',
	'validation' => function() {
		return array(
			function ($value) {
				$clean = str_replace('-', '', $value);

				if (preg_match('/^\d{13}$/', $clean))
				{
					return true;
				}
				else
				{
					return 'Код ISBN должен содержать 13 цифр.';
				}
			},
			function ($value, $primary, $row, $field) {
				// проверяем последнюю цифру
				// ...
				// если цифра неправильная - возвращаем особую ошибку
				return new Entity\FieldError(
					$field, 'Контрольная цифра ISBN не сошлась', 'MY_ISBN_CHECKSUM'
				);
			}
		);
	}
))
```

```
// выполняем операцию
$result = BookTable::update(...);

if (!$result->isSuccess())
{
	// смотрим, какие ошибки были выявлены
	$errors = $result->getErrors();

	foreach ($errors as $error)
	{
		if ($error->getCode() == 'MY_ISBN_CHECKSUM')
		{
			// сработал наш валидатор
		}
	}
}
```

По умолчанию есть 2 стандартных кода ошибки: `BX_INVALID_VALUE`, если сработал валидатор, и `BX_EMPTY_REQUIRED`, если при добавлении записи не указано обязательное required поле.

Валидаторы срабатывают как при добавлении новых записей, так и при обновлении существующих. Такое поведение исходит из общего назначения валидаторов - гарантировать корректные и целостные данные в БД. Для проверки данных только при добавлении или только при обновлении, а также для других манипуляций существует механизм событий.

В типовых случаях рекомендуем вам использовать штатные валидаторы:

- *Entity\Validator\RegExp* - проверка по регулярному выражению,
- [Entity\Validator\Length](https://dev.1c-bitrix.ru/api_d7/bitrix/main/entity/validator/length/index.php) - проверка на минимальную/максимальную длину строки,
- *Entity\Validator\Range* - проверка на минимальное/максимальное значение числа,
- *Entity\Validator\Unique* - проверка на уникальность значения

Описанные валидаторы не применимы к Пользовательским полям — проверка их значений конфигурируется в настройках поля через административный интерфейс.

#### События

В примере с валидаторами одной из проверок поля ISBN была проверка на наличие 13 цифр. Помимо цифр, в ISBN коде могут встречаться дефисы, но с технической точки зрения они не несут никакой ценности. Чтобы хранить в БД "чистые" данные - только 13 цифр, без дефисов - можно воспользоваться внутренним обработчиком события:

```
class BookTable extends Entity\DataManager
{
	...

	public static function onBeforeAdd(Entity\Event $event)
	{
		$result = new Entity\EventResult;
		$data = $event->getParameter("fields");

		if (isset($data['ISBN']))
		{
			$cleanIsbn = str_replace('-', '', $data['ISBN']);
			$result->modifyFields(array('ISBN' => $cleanIsbn));
		}

		return $result;
	}
}
```

Метод *onBeforeAdd*, определенный в сущности, автоматически распознается системой как обработчик события "перед добавлением", и в нем можно изменить данные или провести дополнительные проверки. В приведенном примере мы изменили поле ISBN посредством метода *`modifyFields`*.

```
// до преобразования
978-0321127426
978-1-449-31428-6
9780201485677

// после преобразования
9780321127426
9781449314286
9780201485677
```

После такого преобразования можно вновь вернуться к лаконичному валидатору RegExp вместо анонимной функции (ведь мы уже знаем, что допустимых дефисов в значении не будет, должны остаться только цифры):

```
'validation' => function() {
	return array(
		//function ($value) {
		//	$clean = str_replace('-', '', $value);
		//
		//	if (preg_match('/^\d{13}$/', $clean))
		//	{
		//		return true;
		//	}
		//	else
		//	{
		//		return 'Код ISBN должен содержать 13 цифр.';
		//	}
		//},
		new Entity\Validator\RegExp('/\d{13}/'),
		...
	);
}
```

Помимо изменения данных, в обработчике события можно удалить данные или вовсе прервать выполнение операции. Например, необходимо запретить обновление ISBN кода для уже существующих в каталоге книг. Сделать это можно в событии *onBeforeUpdate* двумя способами:

```
public static function onBeforeUpdate(Entity\Event $event)
{
	$result = new Entity\EventResult;
	$data = $event->getParameter("fields");

	if (isset($data['ISBN']))
	{
		$result->unsetFields(array('ISBN'));
	}

	return $result;
}
```

В таком варианте ISBN будет "тихо" удален из набора данных, будто его и не передавали. Второй способ запретить его обновлять - сгенерировать ошибку:

```
public static function onBeforeUpdate(Entity\Event $event)
{
	$result = new Entity\EventResult;
	$data = $event->getParameter("fields");

	if (isset($data['ISBN']))
	{
		$result->addError(new Entity\FieldError(
			$event->getEntity()->getField('ISBN'),
			'Запрещено менять ISBN код у существующих книг'
		));
	}

	return $result;
}
```

В случае возврата ошибки мы сформировали объект *Entity\FieldError* для того, чтобы впоследствии при обработке ошибок знать, на каком именно поле сработала проверка. Если ошибка относится к нескольким полям или целиком ко всей записи, то более уместно будет воспользоваться объектом *Entity\EntityError*:

```
public static function onBeforeUpdate(Entity\Event $event)
{
	$result = new Entity\EventResult;
	$data = $event->getParameter("fields");

	if (...) // комплексная проверка данных
	{
		$result->addError(new Entity\EntityError(
			'Невозможно обновить запись'
		));
	}

	return $result;
}
```

В примерах использовались два события: onBeforeAdd и onBeforeUpdate, всего же таких событий девять:

- *OnBeforeAdd* (параметры: fields)
- *OnAdd* (параметры: fields)
- *OnAfterAdd* (параметры: fields, primary)
- *OnBeforeUpdate* (параметры: primary, fields)
- *OnUpdate* (параметры: primary, fields)
- *OnAfterUpdate* (параметры: primary, fields)
- *OnBeforeDelete* (параметры: primary)
- *OnDelete* (параметры: primary)
- *OnAfterDelete* (параметры: primary)

Порядок вызова событий и допустимые действия в обработчиках каждого из них:

![](/images/dev_full/d_7/ORM/event order.jpeg)

Конечно же, обрабатывать эти события можно не только в самой сущности в одноименных методах. Чтобы подписаться на событие в произвольном месте выполнения скрипта, нужно вызвать менеджер событий:

```
$em = \Bitrix\Main\ORM\EventManager::getInstance();

$em->addEventHandler(
	BookTable::class, // класс сущности
    	DataManager::EVENT_ON_BEFORE_ADD, // код события
		function () { // ваш callback
			var_dump('handle entity event');
		}
);
```

#### Форматирование значений

Иногда может возникнуть необходимость хранить данные в одном формате, а работать с ними в программе уже в другом. Самый распространенный пример: работа с массивом и его сериализация перед сохранением в БД. На этот случай предусмотрены параметры поля `'save_data_modification'` и `'fetch_data_modification'`. Определяются они аналогично валидаторам, через callback.

На примере каталога книг опишем текстовое поле EDITIONS_ISBN: оно будет хранить коды ISBN других изданий книги, если таковые имеются:

```
new Entity\TextField('EDITIONS_ISBN', array(
	'save_data_modification' => function () {
		return array(
			function ($value) {
				return serialize($value);
			}
		);
	},
	'fetch_data_modification' => function () {
		return array(
			function ($value) {
				return unserialize($value);
			}
		);
	}
))
```

В параметре `save_data_modification` мы указали сериализацию значения перед сохранением в БД, а в параметре `fetch_data_modification` рассериализацию при выборке из БД. Теперь при написании бизнес-логики вы можете просто работать с массивом, не отвлекаясь на вопросы конвертации.

**Внимание!** Прежде чем создать у себя сериализованное поле, подумайте не помешает ли сериализация при фильтрации или связывании таблиц. Искать по одиночному значению в WHERE среди сериализованных строк крайне неэффективно. Возможно, вам больше подойдет [нормализованная схема](lesson_3269.md) хранения данных.

Поскольку сериализация - это наиболее типичный пример для конвертации значений, она вынесена в отдельный параметр `serialized`:

```
new Entity\TextField('EDITIONS_ISBN', array(
	'serialized' => true
))
```

Но вы по-прежнему можете описать свои callable для других вариантов модификации данных.

#### Вычисляемые значения

Очень часто разработчики сталкиваются с реализацией счетчиков, где для целостности данных предпочтительно рассчитывать новое значение на стороне БД, вместо выборки старого значения и пересчете его на стороне приложения. Другими словами, нужно выполнять запросы вида:

```
UPDATE my_book SET READERS_COUNT = READERS_COUNT + 1 WHERE ID = 1
```

Если описать числовое поле READERS_COUNT в сущности, то инкремент счетчика можно будет запустить следующим образом:

```
BookTable::update($id, array(
	'READERS_COUNT' => new DB\SqlExpression('?# + 1', 'READERS_COUNT')
));
```

Плейсхолдер `?#` означает, что следующим аргументом в конструкторе идет идентификатор БД - имя базы данных, таблицы или колонки, и это значение будет экранировано соответствующим образом. Для всех изменяемых параметров рекомендуется обязательно использовать плейсхолдеры - такой подход поможет избежать проблем с SQL инъекциями.

Например, если инкрементируемое число читателей переменно, то лучше описать выражение так:

```
// правильно
BookTable::update($id, array(
	'READERS_COUNT' => new DB\SqlExpression('?# + ?i', 'READERS_COUNT', $readersCount)
));

// неправильно
BookTable::update($id, array(
	'READERS_COUNT' => new DB\SqlExpression('?# + '.$readersCount, 'READERS_COUNT')
));
```

Список доступных на данный момент плейсхолдеров:

- `?` или `?s` - значение экранируется и заключается в кавычки '
- `?#` - значение экранируется как идентификатор
- `?i` - значение приводится к integer
- `?f` - значение приводится к float

#### Предупреждения об ошибках

В предыдущих примерах есть нюанс: запрос на обновление данных вызывается без проверки результата:

```
// вызов без проверки успешности выполнения запроса
BookTable::update(...);

// с проверкой
$result = BookTable::update(...);
if (!$result->isSuccess())
{
	// обработка ошибки
}
```

Несомненно, второй вариант более предпочтителен с точки зрения контроля происходящего. Но если код выполняется только в режиме агента, нам некому и незачем показывать список возникших в процессе валидации ошибок. В таком случае, если запрос не прошел из-за "проваленной" валидации, и не была вызвана проверка isSuccess(), система сгенерирует `E_USER_WARNING` со списком ошибок, который можно будет увидеть в логе сайта (если соответствующим образом настроить [.settings.php](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=02795)).

По результатам данной главы произошли некоторые изменения в описании сущности, теперь оно выглядит так:

```
namespace SomePartner\MyBooksCatalog;

use Bitrix\Main\Entity;
use Bitrix\Main\Type;

class BookTable extends Entity\DataManager
{
	public static function getTableName()
	{
		return 'my_book';
	}

	public static function getUfId()
	{
		return 'MY_BOOK';
	}

	public static function getMap()
	{
		return array(
			new Entity\IntegerField('ID', array(
				'primary' => true,
				'autocomplete' => true
			)),
			new Entity\StringField('ISBN', array(
				'required' => true,
				'column_name' => 'ISBNCODE',
				'validation' => function() {
					return array(
						new Entity\Validator\RegExp('/\d{13}/'),
						function ($value, $primary, $row, $field) {
							// проверяем последнюю цифру
							// ...
							// если цифра неправильная - возвращаем особую ошибку
							return new Entity\FieldError(
								$field, 'Контрольная цифра ISBN не сошлась', 'MY_ISBN_CHECKSUM'
							);
						}
					);
				}
			)),
			new Entity\StringField('TITLE'),
			new Entity\DateField('PUBLISH_DATE', array(
				'default_value' => function () {
					// figure out last friday date
					$lastFriday = date('Y-m-d', strtotime('last friday'));
					return new Type\Date($lastFriday, 'Y-m-d');
				}
			)),
			new Entity\TextField('EDITIONS_ISBN', array(
				'serialized' => true
			)),
			new Entity\IntegerField('READERS_COUNT')
		);
	}

	public static function onBeforeAdd(Entity\Event $event)
	{
		$result = new Entity\EventResult;
		$data = $event->getParameter("fields");

		if (isset($data['ISBN']))
		{
			$cleanIsbn = str_replace('-', '', $data['ISBN']);
			$result->modifyFields(array('ISBN' => $cleanIsbn));
		}

		return $result;
	}
}
```

Скопировав этот код, вы можете поэкспериментировать со всеми описанными выше возможностями.
