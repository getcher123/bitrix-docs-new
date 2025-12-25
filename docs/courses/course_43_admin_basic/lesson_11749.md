# Групповые действия

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11747 — Доступ к элементам коллекции](lesson_11747.md)
- [Следующий: 11751 — Восстановление коллекции →](lesson_11751.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11749

Коллекции позволяют совершать групповые операции над содержащимися в ней элементами.

- *save (добавление)*
  Метод *save()* в случае с новыми объектами выполняет их первичное сохранение, формируя один групповой запрос:
  ```
  use \Bitrix\Main\Test\Typography\Books;
  use \Bitrix\Main\Test\Typography\Book;
  $books = new Books;
  $books[] = (new Book)->setTitle('Title 112');
  $books[] = (new Book)->setTitle('Title 113');
  $books[] = (new Book)->setTitle('Title 114');
  $books->save(true);
  // INSERT INTO ...  (`TITLE`, `ISBN`) VALUES
  	('Title 112', DEFAULT),
  	('Title 113', DEFAULT),
  	('Title 114', '114-000')
  ```
  При этом в метод передан параметр `$ignoreEvents = true`, отменяющий выполнение событий ORM во время добавления записей. Дело в том, что именно при мульти-вставке с автоинкрементным полем (`ID`) невозможно получить множественные значения этого поля, как это возможно при вставке одной записи с помощью функций вроде `mysqli_insert_id()`.
  В остальных случаях, когда в сущности нет автоинкрементных полей, выполнение событий остается на усмотрение разработчика. По умолчанию события будут выполняться.
- *save (редактирование)*
  Метод *save()* в случае с уже существующими, но измененными объектами, выполняет их сохранение одним запросом *UPDATE*:
  ```
  use \Bitrix\Main\Test\Typography\PublisherTable;
  use \Bitrix\Main\Test\Typography\BookTable;
  $books = BookTable::getList()->fetchCollection();
  $publisher = PublisherTable::wakeUpObject(254);
  foreach ($books as $book)
  {
  	$book->setPublisher($publisher);
  }
  $books->save();
  // UPDATE ... SET `PUBLISHER_ID` = '254'
  	WHERE `ID` IN ('1', '2')
  ```
  Групповое обновление сработает только в случае, если набор изменных данных единый для всех объектов. Если же хотя бы в одном объекте измененные данные отличаются, то все записи будут сохранены по отдельности.
  Как и в случае с добавлением, при обновлении можно отключать выполнение событий параметром `$ignoreEvents` в методе *save()*. По умолчанию они выполняются для каждого элемента коллекции.
- *fill*
  Коллекционная операция *fill* является прекрасной альтернативой [аналогичной операции в Объекте](lesson_11705.md), выполненной в цикле. В случае с циклом количество запросов к базе данных будет равно количеству объектов:
  ```
  /** @var \Bitrix\Main\Test\Typography\Book[] $books */
  $books = [
  	\Bitrix\Main\Test\Typography\Book::wakeUp(1),
  	\Bitrix\Main\Test\Typography\Book::wakeUp(2)
  ];
  foreach ($books as $book)
  {
  	$book->fill();
  	// SELECT ... WHERE ID = ...
  	// так делать не надо!
  }
  ```
  В случае же с коллекцией запрос будет только один:
  ```
  $books = new \Bitrix\Main\Test\Typography\Books;
  // или $books = \Bitrix\Main\Test\Typography\BookTable::createCollection();
  $books[] = \Bitrix\Main\Test\Typography\Book::wakeUp(1);
  $books[] = \Bitrix\Main\Test\Typography\Book::wakeUp(2);
  $books->fill();
  // SELECT ... WHERE ID IN(1,2)
  ```
  Как и в случае с объектами, в качестве параметров в *fill* можно передавать массив имен полей для заполнения или маску типа:
  ```
  $books->fill(['TITLE', 'PUBLISHER_ID']);
  $books->fill(\Bitrix\Main\ORM\Fields\FieldTypeMask::FLAT);
  ```
  Более подробно возможные значения параметра описаны в [fill Объектов](lesson_11705.md).
- *get*List*
  Не самый редкий сценарий - получить из результата запроса список значений отдельного поля. В обычном случае это может выглядеть так:
  ```
  $books = \Bitrix\Main\Test\Typography\BookTable::getList()
  	->fetchCollection();
  $titles = [];
  foreach ($books as $book)
  {
  	$titles[] = $book->getTitle();
  }
  ```
  Именованный групповой "геттер" позволяет сократить такой цикл до одной строчки кода:
  ```
  $books = \Bitrix\Main\Test\Typography\BookTable::getList()
  	->fetchCollection();
  $titles = $books->getTitleList();
  ```
  Такие "геттеры" доступны для всех полей сущности и описываются в [аннотациях для IDE](lesson_11733.md).
