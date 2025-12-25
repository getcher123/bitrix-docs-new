# ArrayAccess

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11707 — Отношения (addTo, removeFrom, removeAll)](lesson_11707.md)
- [Следующий: 11745 — Класс коллекции →](lesson_11745.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11755

Интерфейс доступа к объекту как к массиву может помочь обеспечить обратную совместимость при переходе с массивов на объекты:

```
$author = \Bitrix\Main\Test\Typography\AuthorTable::getByPrimary(17)->fetchObject();

echo $author['NAME'];
// вызов аналогичен методу $author->getName()

$author['NAME'] = 'New name';
// вызов аналогичен методу $author->setName('New name')
```

Что касается *runtime* полей, то в данном случае можно только считывать их значения, но не устанавливать:

```
$author = \Bitrix\Main\Test\Typography\AuthorTable::query()
	->registerRuntimeField(
		new \Bitrix\Main\Entity\ExpressionField('FULL_NAME', 'CONCAT(%s, " ", %s)', ['NAME', 'LAST_NAME'])
	)
	->addSelect('ID')
	->addSelect('FULL_NAME')
	->where('ID', 17)
	->fetchObject();

echo $author['FULL_NAME'];
// вызов аналогичен методу $author->get('FULL_NAME');

$author['FULL_NAME'] = 'New name';
// вызовет исключение
```
