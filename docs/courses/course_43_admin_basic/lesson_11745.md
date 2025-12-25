# Класс коллекции

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11755 — ArrayAccess](lesson_11755.md)
- [Следующий: 11747 — Доступ к элементам коллекции →](lesson_11747.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11745

Действует абсолютно [та же логика](lesson_11689.md) с префиксом *EO_*, что и у [Объектов](/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=011687). У каждой сущности свой класс Коллекции, унаследованный от *Bitrix\Main\ORM\Objectify\Collection*. Для сущности *Book* по умолчанию он будет иметь вид *EO_Book_Collection*. Чтобы задать свой класс, нужно создать наследника этого класса и обозначить его в классе *Table* сущности:

```
//Файл bitrix/modules/main/lib/test/typography/books.php

namespace Bitrix\Main\Test\Typography;

class Books extends EO_Book_Collection
{
}
```

```

//Файл bitrix/modules/main/lib/test/typography/booktable.php

namespace Bitrix\Main\Test\Typography;

class BookTable extends Bitrix\Main\ORM\Data\DataManager
{
	public static function getCollectionClass()
	{
		return Books::class;
	}
	//...
}
```

Теперь метод *fetchCollection* будет возвращать коллекцию *Bitrix\Main\Test\Typography\Books* объектов класса *Bitrix\Main\Test\Typography\Book*. [Аннотации](lesson_11733.md) позволят IDE давать подсказки, облегчая работу разработчика.
