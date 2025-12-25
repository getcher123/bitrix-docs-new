# Заполнение (fill)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11703 — Восстановление (wakeUp)](lesson_11703.md)
- [Следующий: 11707 — Отношения (addTo, removeFrom, removeAll) →](lesson_11707.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11705

Когда в объекте заполнены не все поля, и вам нужно дозаполнить их, **не следует** применять следующий подход:

```
// изначально у нас есть только ID и NAME
$author = \Bitrix\Main\Test\Typography\EO_Author::wakeUp(
	['ID' => 17, 'NAME' => 'Name 17']
);

// мы хотим дозаписать LAST_NAME, довыбрав его из базы данных
$row = \Bitrix\Main\Test\Typography\AuthorTable::getByPrimary($author->getId(),
	['select' => ['LAST_NAME']]
)->fetch();

// добавление значения в объект
$author->setLastName($row['LAST_NAME']);
```

В таком случае значение будет считаться вновь установленным, а не актуальным, что теоретически может привести к непредсказуемым коллизиям в дальнейшей работе с объектом.

Правильно будет воспользоваться именованным методом объекта *fill*:

```
// изначально у нас есть только ID и NAME
$author = \Bitrix\Main\Test\Typography\EO_Author::wakeUp(
	['ID' => 17, 'NAME' => 'Name 17']
);

// добавляем LAST_NAME из базы данных
$author->fillLastName();
```

Кроме именованных методов, есть и универсальный. И он предоставляет значительно больше возможностей, чем другие универсальные методы:

```
$author = \Bitrix\Main\Test\Typography\EO_Author::wakeUp(17);

// заполнение нескольких полей
$author->fill(['NAME', 'LAST_NAME']);

// заполнение всех незаполненных на данный момент полей
$author->fill();

// заполнение полей по маске, например все незаполненные скалярные поля
$author->fill(\Bitrix\Main\ORM\Fields\FieldTypeMask::SCALAR);

// незаполненные скалярные и пользовательские поля
$author->fill(
	\Bitrix\Main\ORM\Fields\FieldTypeMask::SCALAR
	| \Bitrix\Main\ORM\Fields\FieldTypeMask::USERTYPE
);

/*
 * Маски бывают следующие:
 *
 * SCALAR - скалярные поля (ORM\ScalarField)
 * EXPRESSION - выражения (ORM\ExpressionField)
 * USERTYPE - пользовательские поля
 * REFERENCE - отношения 1:1 и N:1 (ORM\Fields\Relations\Reference)
 * ONE_TO_MANY - отношения 1:N (ORM\Fields\Relations\OneToMany)
 * MANY_TO_MANY - отношения N:M (ORM\Fields\Relations\ManyToMany)
 *
 * FLAT - скалярные поля и выражения
 * RELATION - все отношения
 *
 * ALL - абсолютно все доступные поля
 */
```

Если вам нужно дозаполнить несколько объектов, то категорически не рекомендуется выполнять эту команду в цикле - это приведет к большому количеству запросов к базе данных. Для работы с несколькими объектами одного типа одновременно следует использовать аналогичный [метод Коллекции](lesson_11749.md).
