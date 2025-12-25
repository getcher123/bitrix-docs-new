# Отношения (addTo, removeFrom, removeAll)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11705 — Заполнение (fill)](lesson_11705.md)
- [Следующий: 11755 — ArrayAccess →](lesson_11755.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11707

Подробное описание отношений можно найти в соседней главе [Отношения](/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=011735). Здесь же приведена спецификация управляющих отношениями методов.

Для полей отношений работают уже описанные выше методы *get*, *require*, *fill*, *reset*, *unset*.

**Важно!** Несмотря на то, что в качестве значения отношений используется объект Коллекции, изменять связи можно только через методы *addTo*, *removeFrom*, *removeAll* объектов-партнеров. Изменение коллекции напрямую ([add](lesson_11747.md#add), [remove](lesson_11747.md#remove)) не приведет к желаемому результату.

- *addTo*
  Метод *addTo* добавляет новую связь между объектами:
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
  Вызов метода связывает объекты лишь в памяти, после него необходимо зафиксировать изменения методом *save*.
- *removeFrom*
  Удаление связей отношений *removeFrom* работает похожим образом:
  ```
  // инициализация издателя
  $publisher = \Bitrix\Main\Test\Typography\PublisherTable::getByPrimary(253)
  	->fetchObject();
  // инициализация книги
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(2)
  	->fetchObject();
  // удаление одной конкретной книги издателя
  $publisher->removeFromBooks($book);
  // сохранение
  $publisher->save();
  ```
- *removeAll*
  Удаление сразу всех записей можно сделать одним вызовом:
  ```
  // инициализация издателя
  $publisher = \Bitrix\Main\Test\Typography\PublisherTable::getByPrimary(253)
  	->fetchObject();
  // удаление всех книг издателя
  $publisher->removeAllBooks();
  // сохранение
  $publisher->save();
  ```
  Для такой операции необходимо знать исходные значения - какие в данный момент есть **Книги** у **Издателя**. Поэтому, если значение поля *BOOKS* не было выбрано изначально, оно будет выбрано автоматически перед удалением.

В качестве альтернативы можно использовать универсальные неименованные методы:

```
$fieldName = 'BOOKS';

$publisher->addTo($fieldName, $book);
$publisher->removeFrom($fieldName, $book);
$publisher->removeAll($fieldName);
```
