# Примеры работы с множественными свойствами

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3399 — Работа с пользовательскими свойствами инфоблоков](lesson_3399.md)
- [Следующий: 5744 — Копирование значений полей элементов в свойства →](lesson_5744.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=5534

**Задача 1:** удаление одного из значений множественного свойства элемента инфоблока.

**Решение**:

```

$el = new CIBlockElement;
$PROP = array();
$PROP[property_id][id] = "4";
$PROP[property_id][id] = "5";
$PROP[property_id][id] = "6";

$arLoadProductArray = Array(
	"IBLOCK_ID" => $B_ID,
	"PROPERTY_VALUES" => $PROP,
	"NAME" => "Element",
	);

$PRODUCT_ID = $E_ID;
$res = $el->Update($PRODUCT_ID, $arLoadProductArray);
```

При этом для удаления достаточно исключить из массива `$PROP` пару: ключ и значение удаляемого свойства.
Данное решение является оптимальным в ситуации, когда необходимо сохранить *id* значения свойства прежним:

```
$PROP[property_id ][id ]
```

Также вариантом решения задачи может стать использование метода [SetPropertyValues](http://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/setpropertyvalues.php):

```
CIBlockElement::SetPropertyValues($ELEMENT_ID, $IBLOCK_ID, $PROPERTY_VALUE, $PROPERTY_CODE);
```

в четвёртый параметр функции следует передавать *false*, а в третий - массив *"код свойства"=&gt;"значение"*.

При этом все значения будут удалены кроме тех, которые указаны в массиве, переданном в третий параметр.

**Задача 2:** добавление определенного значения для множественного свойства типа **файл**:

**Решение**:

```

//FILES - символьный код множественного свойства типа файл;

$ELEMENT_ID = 392;
$arFile = CFile::MakeFileArray($_SERVER["DOCUMENT_ROOT"]."/images/help.gif");
$arFile["MODULE_ID"] = "iblock";

CIBlockElement::SetPropertyValueCode($ELEMENT_ID, "FILES", Array("VALUE"=>$arFile)  );
```

**Задача 3:** добавление нескольких значений для множественного свойства типа **файл**:

**Решение**:

```

$arFile = array(
0 => array("VALUE" => CFile::MakeFileArray($_SERVER["DOCUMENT_ROOT"]."/images/01.gif"),"DESCRIPTION"=>""),
1 => array("VALUE" => CFile::MakeFileArray($_SERVER["DOCUMENT_ROOT"]."/images/help.gif"),"DESCRIPTION"=>"")
);
CIBlockElement::SetPropertyValueCode($ELEMENT_ID, $PROPERTY_CODE, $arFile);
```

**Задача 4:** удаление определенного значения множественного свойства типа **файл**:

**Решение**:

```

//FILES - символьный код множественного свойства типа файл;
//2033 - id значения свойства;

$ELEMENT_ID = 392;
$arFile["MODULE_ID"] = "iblock";
$arFile["del"] = "Y";

CIBlockElement::SetPropertyValueCode($ELEMENT_ID, "FILES", Array ("2033" => Array("VALUE"=>$arFile) ) );
```

**Задача 5:** обновление определенного значения множественного свойства типа **файл**:

**Решение**:

```

//FILES - символьный код множественного свойства типа файл;
//2033 - id значения свойства;

$ELEMENT_ID = 392;
$arFile = CFile::MakeFileArray($_SERVER["DOCUMENT_ROOT"]."/images/help.gif");
$arFile["MODULE_ID"] = "iblock";

CIBlockElement::SetPropertyValueCode($ELEMENT_ID, "FILES", Array ("2033" => Array("VALUE"=>$arFile) ) );
```

**Задача 6:** установка множественного свойства типа **строка** с полем для описания значения:

**Решение с помощью [SetPropertyValueCode](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/setpropertyvaluecode.php)**:

```

$arValues = array(
	0 => array("VALUE"=>"значение","DESCRIPTION"=>"описание значения"),
	1 => array("VALUE"=>"значение2","DESCRIPTION"=>"описание значения2")
);
CIBlockElement::SetPropertyValueCode($ELEMENT_ID, $PROP_CODE, $arValues);
```

**Решение с помощью [SetPropertyValuesEx](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/setpropertyvaluesex.php)**:

```

$PROPERTY_VALUE = array(
	0 => array("VALUE"=>"значение","DESCRIPTION"=>"описание значения"),
	1 => array("VALUE"=>"значение2","DESCRIPTION"=>"описание значения2")
);
CIBlockElement::SetPropertyValuesEx($ELEMENT_ID, $IBLOCK_ID, array($PROPERTY_CODE => $PROPERTY_VALUE));
```

**Задача 7:** обновление множественного свойства типа **Текст** и сохранение при этом **DESCRIPTION**:

**Решение**:

```

CIBlockElement::SetPropertyValues($nProductID, $nIblockID, array(
	array(
		"VALUE" => array(
			"TEXT"=>time(),
			"TYPE"=>"HTML"
		),
  		"DESCRIPTION"=>"111"),
	array(
		"VALUE" => array(
		"TEXT"=>time(),
		"TYPE"=>"HTML"
		),
		"DESCRIPTION"=>"222"),
	), $prop['ID']);
```
