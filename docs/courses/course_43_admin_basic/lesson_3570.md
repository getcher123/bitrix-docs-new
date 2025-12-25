# Практика. Работа с D7 на примере местоположений

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3112 — Практика. Некоторые классы](lesson_3112.md)
- [Следующий: 14032 — Сервис Локатор →](lesson_14032.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3570

Не забудьте подключить модуль sale.



### Типы местоположений

Добавление типа местоположения:

```
$res = \Bitrix\Sale\Location\TypeTable::add(array(
	'CODE' => 'CITY',
	'SORT' => '100', // уровень вложенности
	'DISPLAY_SORT' => '200', // приоритет показа при поиске
	'NAME' => array( // языковые названия
		'ru' => array(
			'NAME' => 'Город'
		),
		'en' => array(
			'NAME' => 'City'
		),
	)
));
if($res->isSuccess())
{
	print('Type added with ID = '.$res->getId());
}
```

Обновление типа местоположения

```
$res = \Bitrix\Sale\Location\TypeTable::update(21, array(
	'SORT' => '300',
	'NAME' => array(
		'ru' => array(
			'NAME' => 'Новый Город'
		),
	)
));
if($res->isSuccess())
{
	print('Updated!');
}
```

Удаление типа местоположения

```
$res = \Bitrix\Sale\Location\TypeTable::delete(21);
if($res->isSuccess())
{
	print('Deleted!');
}
```

Получение типа местоположения по ID

```
$item = \Bitrix\Sale\Location\TypeTable::getById(14)->fetch();
print_r($item);
```

Получение списка типов с названиями на текущем языке

```
$res = \Bitrix\Sale\Location\TypeTable::getList(array(
	'select' => array('*', 'NAME_RU' => 'NAME.NAME'),
	'filter' => array('=NAME.LANGUAGE_ID' => LANGUAGE_ID)
));
while($item = $res->fetch())
{
	print_r($item);
}
```

Получаем группы с учётом иерархии, в которых есть данное местоположение

```
<?
\Bitrix\Main\Loader::includeModule('sale');

function getGroupsByLocation($locationId)
{
    $res = \Bitrix\Sale\Location\LocationTable::getList([
        'filter' => ['=ID' => $locationId],
        'select' => [
            'ID', 'LEFT_MARGIN', 'RIGHT_MARGIN'
        ]
    ]);

    if(!$loc = $res->fetch())
    {
        return [];
    }

    $locations = [$locationId];

    $res = \Bitrix\Sale\Location\LocationTable::getList([
        'filter' => [
            '<LEFT_MARGIN' => $loc['LEFT_MARGIN'],
            '>RIGHT_MARGIN' => $loc['RIGHT_MARGIN'],
            'NAME.LANGUAGE_ID' => LANGUAGE_ID,
        ],
        'select' => [
            'ID',
            'LOCATION_NAME' => 'NAME.NAME'
        ]
    ]);

    while($locParent = $res->fetch())
    {
        $locations[] = $locParent['ID'];
    }

    $res = \Bitrix\Sale\Location\GroupLocationTable::getList([
        'filter' => ['=LOCATION_ID' => $locations]
    ]);

    $groups = [];

    while($groupLocation = $res->fetch())
    {
        $groups[] = $groupLocation['LOCATION_GROUP_ID'];
    }

    return $groups;
}
```

### Местоположения

Добавление

```
$res = \Bitrix\Sale\Location\LocationTable::add(array(
	'CODE' => 'newly-created-location-code',
	'SORT' => '100', // приоритет показа при поиске
	'PARENT_ID' => 1, // ID родительского местоположения
	'TYPE_ID' => 14, // ID типа
	'NAME' => array( // языковые названия
		'ru' => array(
			'NAME' => 'Архангельск'
		),
		'en' => array(
			'NAME' => 'Arkhangelsk'
		),
	),
	'EXTERNAL' => array( // значения внешних сервисов
		array(
			'SERVICE_ID' => 1, // ID сервиса
			'XML_ID' => '163000' // значение
		),
		array(
			'SERVICE_ID' => 1,
			'XML_ID' => '163061'
		),
	)
));
if($res->isSuccess())
{
	print('Location added with ID = '.$res->getId());
}
else
{
	print_r($res->getErrorMessages());
}
```

Обновление

```
$res = \Bitrix\Sale\Location\LocationTable::update(3156, array(
	'PARENT_ID' => 33,
	'NAME' => array(
		'de' => array(
			'NAME' => 'Arkhangelsk'
		),
	)
));
if($res->isSuccess())
{
	print('Updated!');
}
```

Удаление

```
$res = \Bitrix\Sale\Location\LocationTable::delete(3156);
if($res->isSuccess())
{
	print('Deleted!');
}
```

Получение местоположения по ID

```
$item = \Bitrix\Sale\Location\LocationTable::getById(3159)->fetch();
print_r($item);
```

Получение местоположения по `CODE`, с опциональной фильтрацией\выборкой полей. Фактически это обертка над *\Bitrix\Sale\Location\LocationTable::getList()*.

```
$item = \Bitrix\Sale\Location\LocationTable::getByCode('newly-created-location-code', array(
	'filter' => array('=NAME.LANGUAGE_ID' => LANGUAGE_ID),
	'select' => array('*', 'NAME_RU' => 'NAME.NAME')
))->fetch();
print_r($item);
```

Получение списка местоположений с названиями на текущем языке и кодами типов

```
$res = \Bitrix\Sale\Location\LocationTable::getList(array(
	'filter' => array('=NAME.LANGUAGE_ID' => LANGUAGE_ID),
	'select' => array('*', 'NAME_RU' => 'NAME.NAME', 'TYPE_CODE' => 'TYPE.CODE')
));
while($item = $res->fetch())
{
	print_r($item);
}
```

Получение прямых потомков узла с ID=1 с названиями на текущем языке, кодами и названиями типов местоположений

```
$res = \Bitrix\Sale\Location\LocationTable::getList(array(
	'filter' => array(
		'=ID' => 1,
		'=CHILDREN.NAME.LANGUAGE_ID' => LANGUAGE_ID,
		'=CHILDREN.TYPE.NAME.LANGUAGE_ID' => LANGUAGE_ID,
	),
	'select' => array(
		'CHILDREN.*',
		'NAME_RU' => 'CHILDREN.NAME.NAME',
		'TYPE_CODE' => 'CHILDREN.TYPE.CODE',
		'TYPE_NAME_RU' => 'CHILDREN.TYPE.NAME.NAME'
	)
));
while($item = $res->fetch())
{
	print_r($item);
}
```

Получение родительских узлов для трех узлов

```
$res = \Bitrix\Sale\Location\LocationTable::getList(array(
	'filter' => array(
		'=ID' => array(3159, 85, 17),
		'=PARENT.NAME.LANGUAGE_ID' => LANGUAGE_ID,
		'=PARENT.TYPE.NAME.LANGUAGE_ID' => LANGUAGE_ID,
	),
	'select' => array(
		'PARENT.*',
		'NAME_RU' => 'PARENT.NAME.NAME',
		'TYPE_CODE' => 'PARENT.TYPE.CODE',
		'TYPE_NAME_RU' => 'PARENT.TYPE.NAME.NAME'
	)
));
while($item = $res->fetch())
{
	print_r($item);
}
```

Получение пути от корня дерева до текущего элемента

```
$res = \Bitrix\Sale\Location\LocationTable::getList(array(
	'filter' => array(
		'=ID' => 224,
		'=PARENTS.NAME.LANGUAGE_ID' => LANGUAGE_ID,
		'=PARENTS.TYPE.NAME.LANGUAGE_ID' => LANGUAGE_ID,
	),
	'select' => array(
		'I_ID' => 'PARENTS.ID',
		'I_NAME_RU' => 'PARENTS.NAME.NAME',
		'I_TYPE_CODE' => 'PARENTS.TYPE.CODE',
		'I_TYPE_NAME_RU' => 'PARENTS.TYPE.NAME.NAME'
	),
	'order' => array(
		'PARENTS.DEPTH_LEVEL' => 'asc'
	)
));
while($item = $res->fetch())
{
	print_r($item);
}
```

Получение списка корневых узлов с указанием количества потомков

```
$res = \Bitrix\Sale\Location\LocationTable::getList(array(
	'filter' => array(
		'=PARENT_ID' => 0,
		'=NAME.LANGUAGE_ID' => LANGUAGE_ID,
		'=TYPE.NAME.LANGUAGE_ID' => LANGUAGE_ID,
	),
	'select' => array(
		'ID',
		'NAME_RU' => 'NAME.NAME',
		'TYPE_CODE' => 'TYPE.CODE',
		'TYPE_NAME_RU' => 'TYPE.NAME.NAME',
		'CHILD_CNT'
	)
));
while($item = $res->fetch())
{
	print_r($item);
}
```

Получение внешних данных для местоположений с указанием кода сервиса

```
$res = \Bitrix\Sale\Location\LocationTable::getList(array(
	'filter' => array(
		'CODE' => array('newly-created-location-code', '0000028090'),
	),
	'select' => array(
		'EXTERNAL.*',
		'EXTERNAL.SERVICE.CODE'
	)
));
while($item = $res->fetch())
{
	print_r($item);
}
```

Получение поддерева узла с названиями на текущем языке

```
$res = \Bitrix\Sale\Location\LocationTable::getList(array(
	'runtime' => array(
		'SUB' => array(
			'data_type' => '\Bitrix\Sale\Location\Location',
			'reference' => array(
				'>=ref.LEFT_MARGIN' => 'this.LEFT_MARGIN',
				'<=ref.RIGHT_MARGIN' => 'this.RIGHT_MARGIN'
			),
			'join_type' => "inner"
		)
	),
	'filter' => array(
		'=CODE' => '0000028042',
		'=SUB.NAME.LANGUAGE_ID' => LANGUAGE_ID
	),
	'select' => array(
		'S_CODE' => 'SUB.CODE',
		'S_NAME_RU' => 'SUB.NAME.NAME',
		'S_TYPE_CODE' => 'SUB.TYPE.CODE'
	)
));
while($item = $res->fetch())
{
	print_r($item);
}
```

Получаем местоположения входящие в группу без учёта иерархии.

```
\Bitrix\Main\Loader::includeModule('sale');

/* Идентификатор группы */
$groupId = 1

/* Получаем местоположения входящие в группу */
$res = \Bitrix\Sale\Location\GroupLocationTable::getConnectedLocations(1);

while($item = $res->fetch())
{
    var_dump($item);
}
```
