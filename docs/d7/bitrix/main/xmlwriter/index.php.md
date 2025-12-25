# XmlWriter

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/xmlwriter/index.php

### Описание и методы

**XmlWriter** - класс для экспорта в XML

| Метод | Описание | С версии |
| --- | --- | --- |
| [construct](https://dev.1c-bitrix.ru/api_d7/bitrix/main/xmlwriter/__construct.php) | Метод - конструктор |  |
| [writeItem](https://dev.1c-bitrix.ru/api_d7/bitrix/main/xmlwriter/writeitem.php) | Метод записывает один блок в xml файл. |  |
| [writeFullTag](https://dev.1c-bitrix.ru/api_d7/bitrix/main/xmlwriter/writefulltag.php) | Метод записывает полный тег в файл. |  |
| [writeEndTag](https://dev.1c-bitrix.ru/api_d7/bitrix/main/xmlwriter/writeendtag.php) | Метод записывает конец тега в файл. |  |
| [writeBeginTag](https://dev.1c-bitrix.ru/api_d7/bitrix/main/xmlwriter/writebegintag.php) | Метод начинает запись тега в файл. |  |
| [openFile](https://dev.1c-bitrix.ru/api_d7/bitrix/main/xmlwriter/openfile.php) | Метод открывает файл для записи и начинает XML запись. |  |
| [getErrors](https://dev.1c-bitrix.ru/api_d7/bitrix/main/xmlwriter/geterrors.php) | Метод возвращает ошибку. |  |
| [closeFile](https://dev.1c-bitrix.ru/api_d7/bitrix/main/xmlwriter/closefile.php) | Метод закрывает открытый файл. |  |

### Примеры

```
$export = new \Bitrix\Main\XmlWriter(array(
	'file' => '<относительный путь, куда пишем>',
	'create_file' => true,
	'charset' => SITE_CHARSET,
	'lowercase' => true //приводить ли все теги к нижнему регистру (для педантов)
));

//открываем файл
$export->openFile();

//обрамляем массив тегом
$export->writeBeginTag('items');

//получаем в выборке элемент - заметьте, вложенность поддерживается
$test = array(
	'name' => 'Tra & tata',
	'Timе' => time(),
	'array' => array(
		'one' => 1,
		'two' => 2,
		'subarray' => array(
			't1' => 1,
			't2' => 2
			)
		)
);

//пишем тег (элемент выше)
$export->writeItem($test, 'item');

//вторым параметром мы передаем обрамляющий тег для этого массива, это то же самое, что и
$export->writeItem(array('item' =>  $test));

//словили ли ошибки
//$export->getErrors()

//закрываем массив тегом
$export->writeEndTag('items');

//закрываем файл
$export->closeFile();
```

Удобство класса в возможности пошаговой записи в файл. Например, у вас идет экспорт и вы пишите большой массив данных из базы в файл. Вот переписанный пример выше для реализации пошагового алгоритма (отличия помечены (***)).

```
$export =  new \Bitrix\Main\XmlWriter(array(
	'file' => '<относительный путь, куда пишем>',
	'create_file' => $step == 0,//создаем файл только на первом шаге (***)
	'charset' => SITE_CHARSET,
	'lowercase' => true //приводить ли все теги к нижнему регистру
));

//открываем файл
$export->openFile();

//обрамляем массив тегом (***)
if ($step == 0)
{
	$export->writeBeginTag('items');
}

//пишем тег (элемент выше) (***) - вот сюда мы возвращаем раз за разом на каждом хите мастера
$export->writeItem($test, 'item');

//закрываем массив тегом (***)
if ($step == 0)
{
	$export->writeEndTag('items');
}

//закрываем файл
$export->closeFile();
```
