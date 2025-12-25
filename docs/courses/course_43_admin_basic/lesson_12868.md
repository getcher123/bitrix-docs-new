# Чтение и запись

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 12866 — Концепция и архитектура](lesson_12866.md)
- [Следующий: 12870 — События и кастомные типы свойств →](lesson_12870.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=12868

Для **получения значений свойств** достаточно указать их имена в запросе:

```
$elements = $iblock->getEntityDataClass()::getList([
	'select' => ['ID', 'SOME_FIELD', 'ANOTHER_FIELD.ELEMENT']
])->fetchCollection();

foreach ($elements as $element)
{
	echo $element->getSomeField()->getValue();
	echo $element->getAnotherField()->getElement()->getTitle();
}
```

Поддерживаются стандартные механики отношений ORM.

При фильтрации следует помнить о структуре свойств. Поле свойства является ссылкой (**Reference** или **OneToMany**) на целую сущность, поэтому указание в фильтре имени свойства ни к чему не приведет:

```
// неправильный пример
$element = $iblock->getEntityDataClass()::query()
	->where('SOME_FIELD', 'some value')
	->fetchObject();
```

Значение свойства хранится в поле сущности, и это поле всегда называется **VALUE**. Поэтому корректно указывать именно его в фильтре:

```
// правильный пример
$element = $iblock->getEntityDataClass()::query()
	->where('SOME_FIELD.VALUE', 'some value')
	->fetchObject();
```

## Перебор по классике в while

Пример выше создаёт соблазн использовать то же самое для перебора по классике в while таким образом:

```
$query = $iblock->getEntityDataClass()::query()
	->where('SOME_FIELD.VALUE', 'some value');

while ($element = $query->fetchObject()) {
	// $element
}
```

Но сработает это не так как ожидалось, будет бесконечный цикл с получением первого элемента. Потому что *fetchObject* для получения элементов в цикле нужно вызывать для `\Bitrix\Main\ORM\Query\Result`, а у нас `\Bitrix\Main\ORM\Query\Query`, в котором это сокращенная запись для `$this->exec()->fetchObject()`, т.е. будет выполняться запрос -&gt; извлечен первый элемент, потом снова выполнится запрос и снова извлекается первый элемент.

Чтобы сработало как нужно, стоит делать так:

```
$result = $iblock->getEntityDataClass()::query()
	->where('SOME_FIELD.VALUE', 'some value')
	->exec();

while ($element = $result->fetchObject()) {
	// $element
}
```

Тогда будет получены все элементы поочередно.

То есть наличие метода fetchObject и в Query и в Result может запутать, будьте внимательны.

Для **создания нового объекта** можно использовать как **конструктор** соответствующего класса,

```
$newElement = new \Bitrix\Iblock\Elements\EO_ElementLink;
```

так и **фабрику сущности**.

```
$newElement = $iblock->getEntityDataClass()::createObject();
```

**Изменение** значений и описаний свойств происходит непосредственно через объект свойства:

```
// установка строкового значения
$element->getSomeString()->setValue('new value');

// установка описания
$element->getSomeString()->setDescription('new descr');

// установка привязки к элементу
$element->getSomeElement()->setElement($anotherElement);
```

Кроме этого, можно поставить значение напрямую в поле свойства:

```
$element->setSomeString('new value');
```

А также можно воспользоваться псевдо объектом значения свойства `Bitrix\Iblock\ORM\PropertyValue`:

```
use Bitrix\Iblock\ORM\PropertyValue;

// только значение
$value = new PropertyValue('new value');

// значение и описание
$value = new PropertyValue('new value', 'new descr');

// установка значения/описания
$element->setSomeString($value);
```

Установка значений для множественных свойств работает аналогично с той лишь разницей, что речь идет не о *Reference*, а об отношении *OneToMany*:

```
use Bitrix\Iblock\ORM\PropertyValue;

foreach ($element->getOtherField() as $value)
{
	$value->setValue('new value');
	$value->setDescription('new descr');
}

$element->addToOtherField(new PropertyValue('new value'));
$element->addToOtherField(new PropertyValue('new value', 'new descr'));
```

Объект элемента **сохраняется** так же, как и любой другой объект ORM:

```
$element->save();
```

Несмотря на то, что значения свойств фактически хранятся в разных таблицах в виде отношений с объектом, при сохранении внутри объекта все будет разложено по своим местам.

**Удалить** элемент можно через метод объекта delete:

```
$element->delete();
```

При удалении так же, как и при сохранении, значения свойств обрабатываются автоматически. Удалятся и привязки к секциям.
