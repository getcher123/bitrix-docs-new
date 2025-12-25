# Создание и редактирование (save, new)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11999 — Состояние объекта](lesson_11999.md)
- [Следующий: 11701 — Удаление (delete) →](lesson_11701.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11699

Для фиксации изменений объекта в базе данных используется метод *save*:

```

$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
	->fetchObject();

$book->setTitle("New title");

$book->save();
```

**Примечание:** если вы скопируете этот пример и попробуете выполнить его с тестовой сущностью из пространства имен *Bitrix\Main\Test\Typography*, то в силу специфики тестовых данных получите SQL- ошибку. Но при этом вы увидите, что часть запроса с данными построена корректно.

С момента сохранения все текущие значения объекта преобразуются в актуальные:

```

$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
	->fetchObject();

echo $book->remindActualTitle();
// выведет "Title 1"

$book->setTitle("New title");

echo $book->remindActualTitle();
// выведет "Title 1"

$book->save();

echo $book->remindActualTitle();
// выведет "New title"
```

Что касается новых объектов, есть два пути их создания. Наиболее читаемый способ — через прямое инстанциирование:

```

$newBook = new \Bitrix\Main\Test\Typography\Book;
$newBook->setTitle('New title');
$newBook->save();

$newAuthor = new \Bitrix\Main\Test\Typography\EO_Author;
$newAuthor->setName('Some name');
$newAuthor->save();
```

Способ работает как со стандартными *EO_* классами, так и с переопределенными. И даже если вы сначала использовали *EO_* класс, а потом решили создать свой, то не придется переписывать существующий код - обратная совместимость сохранится автоматически. Системный класс с префиксом *EO_* станет "алиасом" вашему классу.

Более универсальный и обезличенный метод создавать новые объекты — через фабрику сущности:

```

$newBook = \Bitrix\Main\Test\Typography\BookTable::createObject();
$newBook->setTitle('New title');
$newBook->save();
```

По умолчанию, в новом объекте устанавливаются все значения по умолчанию, описанные в "маппинге" *getMap*. Абсолютно чистый объект можно получить, передав соответствующий аргумент в конструктор:

```
$newBook = new \Bitrix\Main\Test\Typography\Book(false);
$newBook = \Bitrix\Main\Test\Typography\BookTable::createObject(false);
```

Состояние значений меняется аналогично, как при редактировании. До сохранения объекта значения считаются текущими, после сохранения в базе данных переходят в статус *actual*.
