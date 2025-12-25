# Приведение типов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11691 — Именованные методы](lesson_11691.md)
- [Следующий: 11695 — Чтение (get, require, remindActual, primary, collectValues, runtime) →](lesson_11695.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11693

В объектах действует строгое приведение значений к типу поля. Это значит, что числа всегда будут числами, а строки - строками:

```

$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
	->fetchObject();

var_dump($book->getId());
// выведет int 1

var_dump($book->getTitle());
// выведет string 'Title 1' (length=7)
```

Особое внимание стоит уделить типу *BooleanField*: в качестве значения ожидается *true* или *false*, несмотря на то, что фактически в базе могут храниться другие значения:

```
//(new BooleanField('IS_ARCHIVED'))
//	->configureValues('N', 'Y'),

$book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
	->fetchObject();

var_dump($book->getIsArchived());
// выведет boolean true

// при установке значений тоже ожидается boolean
$book->setIsArchived(false);
```
