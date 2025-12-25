# Состояние объекта

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11997 — Проверки (isFilled, isChanged, has)](lesson_11997.md)
- [Следующий: 11699 — Создание и редактирование (save, new) →](lesson_11699.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11999

Объект может принимать 3 состояния:

- новый, данные которого еще ни разу не сохранялись в БД;
- актуальный, данные которого совпадают с хранящимися в БД;
- измененный, данные которого отличаются от хранящихся в БД.

Проверить состояние объекта можно с помощью публичного read-only свойства `state` и констант класса *\Bitrix\Main\ORM\Objectify\State*:

```
use \Bitrix\Main\Test\Typography\Book;
use \Bitrix\Main\ORM\Objectify\State;

$book = new Book;
$book->setTitle('New title');

var_dump($book->state === State::RAW);

$book->save();

var_dump($book->state === State::ACTUAL);

$book->setTitle('Another one title');

var_dump($book->state === State::CHANGED);

$book->delete();

var_dump($book->state === State::RAW);

// true
```
