# Доступ к элементам коллекции

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11745 — Класс коллекции](lesson_11745.md)
- [Следующий: 11749 — Групповые действия →](lesson_11749.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11747

- *foreach*
  Базовый класс коллекции реализует интерфейс *\Iterator*, что позволяет перебирать элементы в цикле:
  ```
  $books = \Bitrix\Main\Test\Typography\BookTable::getList()
  	->fetchCollection();
  foreach ($books as $book)
  {
  	// ...
  }
  ```
- *getAll*, *getByPrimary*
  Объекты коллекции можно получить не только в цикле, но и напрямую. Метод *getAll* вернет все содержащиеся объекты в виде массива:
  ```
  $books = \Bitrix\Main\Test\Typography\BookTable::getList()
  	->fetchCollection();
  $bookObjects = $books->getAll();
  echo $bookObjects[0]->getId();
  // выведет значение ID первого объекта
  ```
  Для получения конкретных объектов, содержащихся в коллекции, предусмотрен метод *getByPrimary*:
  ```
  // 1. пример с простым первичным ключном
  $books = \Bitrix\Main\Test\Typography\BookTable::getList()
  		->fetchCollection();
  $book = $books->getByPrimary(1);
  // книга с ID=1
  // 2. пример с составным первичным ключом
  $booksToAuthor = \Bitrix\Main\Test\Typography\BookAuthorTable::getList()
  	->fetchCollection();
  $bookToAuthor = $booksToAuthor->getByPrimary(
  	['BOOK_ID' => 2, 'AUTHOR_ID' => 18]
  );
  // будет присвоен объект отношения книги ID=2 с автором ID=18
  ```
- *has, hasByPrimary*
  Проверить наличие конкретного объекта в коллекции можно методом *has*:
  ```
  $book1 = \Bitrix\Main\Test\Typography\Book::wakeUp(1);
  $book2 = \Bitrix\Main\Test\Typography\Book::wakeUp(2);
  $books = \Bitrix\Main\Test\Typography\BookTable::query()
  	->addSelect('*')
  	->whereIn('ID', [2, 3, 4])
  	->fetchCollection();
  var_dump($books->has($book1));
  // выведет false
  var_dump($books->has($book2));
  // выведет true
  ```
  Аналогично работает метод *hasByPrimary*, когда удобнее сделать проверку по первичному ключу:
  ```
  $books = \Bitrix\Main\Test\Typography\BookTable::query()
  	->addSelect('*')
  	->whereIn('ID', [2, 3, 4])
  	->fetchCollection();
  var_dump($books->hasByPrimary(1));
  // выведет false
  var_dump($books->hasByPrimary(2));
  // выведет true
  ```
- *add, []*
  Добавление объектов реализовано методом *add* и интерфейсом *ArrayAccess*, позволяющим использовать конструкцию *[]*:
  ```
  $book1 = \Bitrix\Main\Test\Typography\Book::wakeUp(1);
  $books = \Bitrix\Main\Test\Typography\BookTable::query()
  	->addSelect('*')
  	->whereIn('ID', [2, 3, 4])
  	->fetchCollection();
  $books->add($book1);
  // или
  $books[] = $book1;
  ```
- *remove*, *removeByPrimary*
  Удалить объект из коллекции можно, задав его явно или указав первичный ключ:
  ```
  $book1 = \Bitrix\Main\Test\Typography\Book::wakeUp(1);
  $books = \Bitrix\Main\Test\Typography\BookTable::getList()
  	->fetchCollection();
  $books->remove($book1);
  // из коллекции удалится книга с ID=1
  $books->removeByPrimary(2);
  // из коллекции удалится книга с ID=2
  ```
