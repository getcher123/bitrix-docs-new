# Восстановление (wakeUp)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11701 — Удаление (delete)](lesson_11701.md)
- [Следующий: 11705 — Заполнение (fill) →](lesson_11705.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11703

Если у вас уже есть данные записи, для инициализации объекта необязательно выбирать их повторно из базы данных. Объект можно восстановить, имея как минимум значения первичного ключа:

```
$book = \Bitrix\Main\Test\Typography\Book::wakeUp(1);
```

Указывать можно не только первичный ключ, но и частичный или полный набор данных:

```
$book = \Bitrix\Main\Test\Typography\Book::wakeUp(['ID' => 1, 'TITLE' => 'Title 1', 'PUBLISHER_ID' => 253]);
```

Аналогично созданию объектов, метод актуален и для *EO_* классов, и для вызова непосредственно из *entity*:

```
// свой класс
$book = \Bitrix\Main\Test\Typography\Book::wakeUp(
	['ID' => 1, 'TITLE' => 'Title 1']
);

// системный класс
$book = \Bitrix\Main\Test\Typography\EO_Book::wakeUp(
	['ID' => 1, 'TITLE' => 'Title 1']
);

// через фабрику entity
$book = \Bitrix\Main\Test\Typography\BookTable::wakeUpObject(
	['ID' => 1, 'TITLE' => 'Title 1']
);
```

В *wakeUp* можно передавать не столько скалярные значения, но и значения [Отношений](/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=011735):

```
$book = \Bitrix\Main\Test\Typography\Book::wakeUp([
	'ID' => 2,
	'TITLE' => 'Title 2',
	'PUBLISHER' => ['ID' => 253, 'TITLE' => 'Publisher Title 253'],
	'AUTHORS' => [
		['ID' => 17, 'NAME' => 'Name 17'],
		['ID' => 18, 'NAME' => 'Name 18']
	]
]);
```
