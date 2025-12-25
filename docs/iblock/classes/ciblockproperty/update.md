# Update


### Описание и параметры


```
bool CIBlockProperty::Update(
	int ID,
	array arFields
);
```

Метод изменяет параметры свойства с кодом *ID*. Перед изменением параметров вызываются обработчики события [OnBeforeIBlockPropertyUpdate](../../events/onbeforeiblockpropertyupdate.md) из которых можно отменить изменения или переопределить поля. А после изменения параметром вызывается событие [OnAfterIBlockPropertyUpdate](../../events/onafteriblockpropertyupdate.md). Нестатический метод.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ID | ID изменяемой записи. |
| arFields | Массив Array("поле"=>"значение", ...). Содержит значения [всех полей](../../fields.md#fproperty) изменяемого свойства. Кроме того, с помощью поля "VALUES", значением которого должен быть массив вида Array(Array("VALUE"=>"значение", "DEF"=>"по умолчанию (Y/N)", "SORT"=>"индекс сортировки"),...), можно установить варианты выбора для свойств типа "список" (подробнее смотрите метод [CIBlockProperty](index.md)::[UpdateEnum()](updateenum.md)). |

**Примечание:**без необходимости не передавайте в *arFields*параметр *IBLOCK_ID*. Если в *arFields*передается *IBLOCK_ID*и в инфоблоке включена поддержка свойств для разделов (и умный фильтр), то свойство отвяжется от верхнего раздела и снова привяжется к верхнему разделу. ``` $arFields = Array( "IBLOCK_ID"=>"1", "SORT" => 2, ); $ibp = new CIBlockProperty; if(!$ibp->Update($prop['ID'], $arFields)) echo $ibp->LAST_ERROR; ``` Код не только изменит индекс сортировки, но еще добавит привязку к верхнему разделу инфоблока.



#### Возвращаемое значение

Метод возвращает true если изменение прошло успешно, при возникновении ошибки метод вернет false, а в свойстве LAST_ERROR объекта будет содержаться текст ошибки. **Примечание:** если используются **Инфоблоки 2.0** и изменяется базовый тип свойства, то все текущие значения свойств у существующих элементов очищаются.

---
### Смотрите также


- [CIBlockProperty::Add](add.md)
- [Поля свойства](../../fields.md#fproperty)
- [OnBeforeIBlockPropertyUpdate](../../events/onbeforeiblockpropertyupdate.md)
- [OnAfterIBlockPropertyUpdate](../../events/onafteriblockpropertyupdate.md)



---
### Примеры использования

Пример 1:


```
<?
$arFields = Array(
	"NAME" => "Цвет",
	"ACTIVE" => "Y",
	"SORT" => "100",
	"CODE" => "color",
	"PROPERTY_TYPE" => "L",
	"IBLOCK_ID" => 11
);

$arFields["VALUES"][0] = Array
	"VALUE" => "Красный",
	"DEF" => "N",
	"SORT" => "100"
);

$arFields["VALUES"][1] = Array(
	"VALUE" => "Желтый",
	"DEF" => "N",
	"SORT" => "200"
);

$arFields["VALUES"][2] = Array(
	"VALUE" => "Зеленый",
	"DEF" => "Y",
	"SORT" => "300"
);

$ibp = new CIBlockProperty;
if(!$ibp->Update($ID, $arFields))
	echo $ibp->LAST_ERROR;
?>
```

Пример 2:

В случае обновления информации в пользовательском типе свойства для сохранения ключа USER_TYPE_SETTINGS необходимо указать еще ключ USER_TYPE с реальным значением. В противном случае ключ USER_TYPE_SETTINGS не обновится. Неверными будут следующие варианты:


```
$arFields = array(
	'PROPERTY_TYPE' => 'E',
	'USER_TYPE_SETTINGS' => array(
		'WIDTH' => '10',
		'HEIGHT' => '10',
	),
);
$ibp = new CIBlockProperty();
$ibp->Update($ID, $arFields));
```

и
```
$arFields = array(
	'PROPERTY_TYPE' => 'E',
	'USER_TYPE_SETTINGS' => array(
		'WIDTH' => '10',
		'HEIGHT' => '10',
	),
	'USER_TYPE' => '',
);
$ibp = new CIBlockProperty();
$ibp->Update($ID, $arFields));
```

Рабочий вариант:
```
$arFields = array(
	'PROPERTY_TYPE' => 'E',
	'USER_TYPE_SETTINGS' => array(
		'WIDTH' => '10',
		'HEIGHT' => '10',
	),
	'USER_TYPE' => 'xxx'
);
$ibp = new CIBlockProperty();
$ibp->Update($ID, $arFields));
```

Пример 3:


```
//включить индексацию свойства для поиска
$arFields = Array(
	'SEARCHABLE'=>'Y'
);
$ibp = new CIBlockProperty;
if(!$ibp->Update($prop['ID'], $arFields))
	echo $ibp->LAST_ERROR;
```

Пример 4:


```
// добавление свойства в умный фильтр:
$arFields = Array('SMART_FILTER' => 'Y', 'IBLOCK_ID' => 123);
$ibp = new CIBlockProperty();
if(!$ibp->Update($prop['ID'], $arFields))
echo $ibp->LAST_ERROR;

//IBLOCK_ID в arFields указывать обязательно, иначе свойство не будет включено в умный фильтр, и при этом не выдаст ошибки.
//Чтобы исключить свойство из умного фильтра в arFileds заменить:  'SMART_FILTER'=>'N'
```

---




| ![](../images/6aaadcf196.jpg) 0 **Яковенко Виталий**12.05.2014 17:52:24 |  |  |
| --- | --- | --- |
| Чтоб корректно добавить свойство в умный фильтр, необходимо перед апдейтом добавить проверку: \| Код \| \| --- \| \| ``` if(CIBlock::GetArrayByID($IBLOCK_ID, "SECTION_PROPERTY") !== "Y") { $ib = new CIBlock; $ib->Update($IBLOCK_ID, array("SECTION_PROPERTY" => "Y")); } ``` \| подробнее **тут** | Код | ``` if(CIBlock::GetArrayByID($IBLOCK_ID, "SECTION_PROPERTY") !== "Y") { $ib = new CIBlock; $ib->Update($IBLOCK_ID, array("SECTION_PROPERTY" => "Y")); } ``` |
| Код |  |  |
| ``` if(CIBlock::GetArrayByID($IBLOCK_ID, "SECTION_PROPERTY") !== "Y") { $ib = new CIBlock; $ib->Update($IBLOCK_ID, array("SECTION_PROPERTY" => "Y")); } ``` |  |  |
|  |  |  |
