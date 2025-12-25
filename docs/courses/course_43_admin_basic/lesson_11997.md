# Проверки (isFilled, isChanged, has)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11697 — Запись (set, reset, unset)](lesson_11697.md)
- [Следующий: 11999 — Состояние объекта →](lesson_11999.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11997

- *isFilled*
  Чтобы проверить, содержит ли объект актуальное значение из базы данных, используется метод *isFilled*:
  ```
  use \Bitrix\Main\Test\Typography\Book;
  // актуальными считаются значения из методов fetch* и wakeUp
  // в примере при инициализации объекта передается только первичный ключ
  $book = Book::wakeUp(1);
  var_dump($book->isTitleFilled());
  // false
  $book->fillTitle();
  var_dump($book->isTitleFilled());
  // true
  ```
- *isChanged*
  Метод *isChanged* отвечает на вопрос, было ли установлено новое значение в течение сеанса:
  ```
  use \Bitrix\Main\Test\Typography\Book;
  // объект может иметь исходное значение, а может и не иметь
  // это не повлияет на дальнешее поведение
  $book = Book::wakeUp(['ID' => 1, 'TITLE' => 'Title 1']);
  var_dump($book->isTitleChanged());
  // false
  $book->setTitle('New title 1');
  var_dump($book->isTitleChanged());
  // true
  ```
  Такое поведение справедливо и для новых объектов, пока их значения не сохранены в базу данных.
- *has*
  Метод *has* проверяет, есть ли в объекте хоть какое-то значение поля - актуальное из БД или установленное в течение сеанса. По сути, это сокращение от `isFilled() || isChanged()`:
  ```
  use \Bitrix\Main\Test\Typography\Book;
  $book = Book::wakeUp(['ID' => 1, 'TITLE' => 'Title 1']);
  $book->setIsArchived(true);
  var_dump($book->hasTitle());
  // true
  var_dump($book->hasIsArchived());
  // true
  var_dump($book->hasIsbn());
  // false
  ```
