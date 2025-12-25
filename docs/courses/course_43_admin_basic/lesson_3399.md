# Работа с пользовательскими свойствами инфоблоков

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5746 — Архитектура модуля](lesson_5746.md)
- [Следующий: 5534 — Примеры работы с множественными свойствами →](lesson_5534.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3399

Примеры решения задач, возникающих при работе с элементами, разделами и свойствами инфоблоков.

  [Получить значения всех свойств элемента, зная его ID](#task_1)
  [Получить свойства элементов, используя метод CIBlockElement::GetList](#task_2)
  [Добавить свойство типа TEXT/html для элемента](#task_3)
  [Заполнить множественное свойство типа Файл](#task_4)
  [Заполнить множественное свойство типа Список](#task_5)
  [Получить пользовательское свойство раздела](#task_6)
  [Пример создания своего типа данных для пользовательского свойства](#task_7)
  [Как удалить файл в свойстве элемента инфоблока](#task_9)

**Задача 1**:

Получить значения всех свойств элемента, зная его ID.

```
1 <? $db_props = CIBlockElement::GetProperty(IBLOCK_ID, ELEMENT_ID, "sort", "asc", array());
2 $PROPS = array();
3 while($ar_props = $db_props->GetNext())
4 $PROPS[$ar_props['CODE']] = $ar_props['VALUE'];?>
```

Теперь символьный код свойства является ключом ассоциативного массива `$PROPS`, то есть, если вам нужно значение свойства с кодом **price**, то оно будет храниться в `$PROPS['price']`.

**Задача 2**:

Получить свойства элементов, используя метод [CIBlockElement::GetList](http://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/getlist.php)

```
1	<? $arSelect = array("ID", "NAME", "PROPERTY_prop_code_1", "PROPERTY_prop_code_2");
2 $res = CIBlockElement::GetList(array(), array(), false, array(), $arSelect);?>
```

Дальше использовать цикл и получить свойства с символьными кодами **prop_code_1** и **prop_code_2**.

|  | **Советы веб-разработчиков.**<br>
<br>[**Антон Долганин**](https://dev.1c-bitrix.ru/community/webdev/user/11948/): Если для какого-либо изменения в БД предусмотрен специальный метод, следует использовать именно его, а не более общий метод изменения БД.
<br>
<br>Хороший пример: модуль интернет-магазина и работа с заказом. Можно изменить флаг оплаты заказа путем [CSaleOrder::Update](http://dev.1c-bitrix.ru/api_help/sale/classes/csaleorder/csaleorder__update.a8be5ffa.php), а можно путем [CSaleOrder::PayOrder](http://dev.1c-bitrix.ru/api_help/sale/classes/csaleorder/csaleorder__payorder.88101c0f.php). Так вот, следует применять именно *PayOrder*, потому что в нем произойдет вызов соответствующих обработчиков. |
| --- | --- |

**Задача 3**:

 Добавить свойство типа **TEXT/html** для элемента.

Если свойство не множественное:

```
01 <? $element = new CIBlockElement;
02 $PROP = array();
03 $PROP['символьный код свойства']['VALUE']['TYPE'] = 'text'; // или html
04 $PROP['символьный код свойства']['VALUE']['TEXT'] = 'значение, которое нужно забить';
05 $arLoadArray = array(
06 	"IBLOCK_ID"      => IBLOCK_ID,
07 	"PROPERTY_VALUES"=> $PROP,
08 	"NAME"           => "Название элемента"
09 	);
10 	$element->Add($arLoadArray);?>
```

Если свойство множественное:

```
01	<? // В $ITEMS хранятся значения множественного свойства, которое нужно забить
02 foreach($ITEMS as $item)
03 {
04 	$VALUES[]['VALUE'] = array(
05 	'TYPE' => 'text', // или html
06 	'TEXT' => $item,
07 	);
08	}
09	$element = new CIBlockElement;
10	$PROPS = array();
11	$PROPS['символьный код свойства'] = $VALUES;
12	$arLoadArray = array(
13	  "IBLOCK_ID"      => IBLOCK_ID,
14	  "PROPERTY_VALUES"=> $PROPS,
15	  "NAME"           => "Название элемента"
16	  );
17 $element->Add($arLoadArray);?>
```

**Задача 4**:

Заполнить множественное свойство типа **Файл**. Довольно часто при добавлении элемента в инфоблок может понадобиться привязать к нему несколько файлов. Для этого удобно создать у инфоблока множественное свойство типа **Файл** и хранить файлы в нём. Пример заполнения свойства:

```
01 <?
02 $arFiles = array();
03 for($i = 1; $i < 10; $i++)
04 {
05 	if(file_exists($_SERVER['DOCUMENT_ROOT'].'/images/image_'.$i.'.jpg'))
06 	{
07 		$arFiles[] = array('VALUE' => CFile::MakeFileArray($_SERVER["DOCUMENT_ROOT"].'/images/image_'.$i.'.jpg'), 'DESCRIPTION' => '');
08 	}
09 }
10 ?>
```

После этого массив `$arFiles` передается как значение свойства при добавлении элемента.

**Задача 5**:

Заполнить множественное свойство типа **Список** с отображением в виде флажков. В данном случае у каждого элемента списка значений есть свой **ID**. Посмотреть их можно, зайдя в детальное редактирование свойства. Заполняется свойство следующим образом:

```
1 <?
2 if($first_condition == true) $values[] = array('VALUE' => 1);
3 if($second_condition == true) $values[] = array('VALUE' => 2);
4 CIBlockElement::SetPropertyValuesEx($ELEMENT_ID, $IBLOCK_ID, array('property_code' => $values));
5 ?>
```

В данном случае при выполнении первого и второго условий мы отмечаем флажками элементы списка с **ID =1** и **ID=2** соответственно. Заменить следует `$ELEMENT_ID`, `$IBLOCK_ID` и `property_code` на нужные значения.

**Задача 6**:

Получить пользовательское свойство раздела

```
1 <? $section_props = CIBlockSection::GetList(array(), array('IBLOCK_ID' => IBLOCK_ID, 'ID' => SECTION_ID), true, array("UF_ADDITIONAL_PRICE"));
2 $props_array = $section_props->GetNext(); ?>
```

Теперь в `$props_array['UF_ADDITIONAL_PRICE']` лежит значение свойства **UF_ADDITIONAL_PRICE** раздела инфоблока.

|  | **Совет от веб-разработчиков.**<br>
<br>[**Алексей Коваленко**](http://dev.1c-bitrix.ru/community/webdev/user/10337/): При работе с инфоблоками удобнее все коды свойств именовать заглавными буквами. В таком случае вы сможете избежать небольших несостыковок в своей работе.
<br>
<br>Например, значение свойства с кодом **foto** при работе с компонентами часто доступно через `[PROPERTIES][foto][VALUE]?`, а при использовании метода *GetList* вы можете получить `PROPERTY_FOTO_VALUE`. |
| --- | --- |

#### Пример создания своего типа данных для пользовательского свойства

В качестве значения свойства попробуем завести картинку с превью. Это могут быть например фотографии гостиницы на туристическом сайте или что-то подобное. В варианте такого применения и рассмотрим решение задачи.

Один из вариантов реализации: хранить изображения в отдельном инфоблоке и показывать как привязку к элементу. Пример кода:

```
AddEventHandler("iblock", "OnIBlockPropertyBuildList", array("CIBlockPropertyPicture", "GetUserTypeDescription"));
AddEventHandler("iblock", "OnBeforeIBlockElementDelete", array("CIBlockPropertyPicture", "OnBeforeIBlockElementDelete"));
class CIBlockPropertyPicture
{
	function GetUserTypeDescription()
	{
		return array(
			"PROPERTY_TYPE"      =>"E",
			"USER_TYPE"      =>"Picture",
			"DESCRIPTION"      =>"Картинка",
			"GetPropertyFieldHtml" =>array("CIBlockPropertyPicture", "GetPropertyFieldHtml"),
			"GetPublicViewHTML" =>array("CIBlockPropertyPicture", "GetPublicViewHTML"),
			"ConvertToDB" =>array("CIBlockPropertyPicture", "ConvertToDB"),
			//"GetPublicEditHTML" =>array("CIBlockPropertyPicture","GetPublicEditHTML"),
			//"GetAdminListViewHTML" =>array("CIBlockPropertyPicture","GetAdminListViewHTML"),
			//"CheckFields" =>array("CIBlockPropertyPicture","CheckFields"),
			//"ConvertFromDB" =>array("CIBlockPropertyPicture","ConvertFromDB"),
			//"GetLength" =>array("CIBlockPropertyPicture","GetLength"),
			);
	}
	function GetPropertyFieldHtml($arProperty, $value, $strHTMLControlName)
	{
		$LINK_IBLOCK_ID = intval($arProperty["LINK_IBLOCK_ID"]);
		if($LINK_IBLOCK_ID)
		{
			$ELEMENT_ID = intval($value["VALUE"]);
			if($ELEMENT_ID)
			{
				$rsElement = CIBlockElement::GetList(array(), array("IBLOCK_ID" => $arProperty["LINK_IBLOCK_ID"], "ID" => $value["VALUE"]), false, false, array("ID", "PREVIEW_PICTURE", "DETAIL_PICTURE"));
			$arElement = $rsElement->Fetch();
			if(is_array($arElement))
				$file_id = $arElement["DETAIL_PICTURE"];
			else
				$file_id = 0;
			}
			else
			{
				$file_id = 0;
			}
			if($file_id)
			{
				$db_img = CFile::GetByID($file_id);
				$db_img_arr = $db_img->Fetch();
			if($db_img_arr)
			{
				$strImageStorePath = COption::GetOptionString("main", "upload_dir", "upload");
				$sImagePath = "/".$strImageStorePath."/".$db_img_arr["SUBDIR"]."/".$db_img_arr["FILE_NAME"];
				return '<label><input name="'.$strHTMLControlName["VALUE"].'[del]" value="Y" type="checkbox">Удалить файл '.$sImagePath.'</label>.'<input name="'.$strHTMLControlName["VALUE"].'[old]" value="'.$ELEMENT_ID.'" type="hidden">';
			}
			}
			return '<input type="file" size="'.$arProperty["COL_COUNT"].'" name="'.$strHTMLControlName["VALUE"].'"/>';
		}
		else
		{
         return "Ошибка настройки свойства. Укажите инфоблок в котором будут храниться картинки.";
		}
	}
	function GetPublicViewHTML($arProperty, $value, $strHTMLControlName)
	{
		$LINK_IBLOCK_ID = intval($arProperty["LINK_IBLOCK_ID"]);
		if($LINK_IBLOCK_ID)
		{
			$ELEMENT_ID = intval($value["VALUE"]);
			if($ELEMENT_ID)
			{
				$rsElement = CIBlockElement::GetList(array(), array("IBLOCK_ID" => $arProperty["LINK_IBLOCK_ID"], "ID" => $value["VALUE"]), false, false, array("ID", "PREVIEW_PICTURE", "DETAIL_PICTURE"));
				$arElement = $rsElement->Fetch();
				if(is_array($arElement))
					return CFile::Show2Images($arElement["PREVIEW_PICTURE"], $arElement["DETAIL_PICTURE"]);
			}
		}
		return "";
	}
	function ConvertToDB($arProperty, $value)
	{
		$arResult = array("VALUE" => "", "DESCRIPTION" => "");
		$LINK_IBLOCK_ID = intval($arProperty["LINK_IBLOCK_ID"]);
		if($LINK_IBLOCK_ID)
		{
			if(
				is_array($value["VALUE"])
				&& is_array($value["VALUE"]["error"])
				&& $value["VALUE"]["error"]["VALUE"] == 0
				&& $value["VALUE"]["size"]["VALUE"] > 0
			)
			{
				$arDetailPicture =  array(
					"name" => $value["VALUE"]["name"]["VALUE"],
					"type" => $value["VALUE"]["type"]["VALUE"],
					"tmp_name" => $value["VALUE"]["tmp_name"]["VALUE"],
					"error" => $value["VALUE"]["error"]["VALUE"],
					"size" => $value["VALUE"]["size"]["VALUE"],
				);
				$obElement = new CIBlockElement;
				$arResult["VALUE"] = $obElement->Add(array(
					"IBLOCK_ID" => $LINK_IBLOCK_ID,
					"NAME" => $arDetailPicture["name"],
					"DETAIL_PICTURE" => $arDetailPicture,
				), false, false, true);
			}
			elseif(
				is_array($value["VALUE"])
				&& isset($value["VALUE"]["size"])
				&& !is_array($value["VALUE"]["size"])
				&& $value["VALUE"]["size"] > 0
			)
			{
				$arDetailPicture =  array(
					"name" => $value["VALUE"]["name"],
					"type" => $value["VALUE"]["type"],
					"tmp_name" => $value["VALUE"]["tmp_name"],
					"error" => intval($value["VALUE"]["error"]),
					"size" => $value["VALUE"]["size"],
					);
					$obElement = new CIBlockElement;
					$arResult["VALUE"] = $obElement->Add(array(
					"IBLOCK_ID" => $LINK_IBLOCK_ID,
					"NAME" => $arDetailPicture["name"],
					"DETAIL_PICTURE" => $arDetailPicture,
				), false, false, true);
			}
			elseif($value["VALUE"]["del"])
			{
				$obElement = new CIBlockElement;
				$obElement->Delete($value["VALUE"]["old"]);
			}
			elseif($value["VALUE"]["old"])
			{
				$arResult["VALUE"] = $value["VALUE"]["old"];
			}
				elseif(!is_array($value["VALUE"]) && intval($value["VALUE"]))
			{
				$arResult["VALUE"] = $value["VALUE"];
			}
		}
		return $arResult;
	}
	function OnBeforeIBlockElementDelete($ELEMENT_ID)
	{
		$arProperties = array();
		$rsElement = CIBlockElement::GetList(array(), array("ID" => $ELEMENT_ID), false, false, array("ID", "IBLOCK_ID"));
		$arElement = $rsElement->Fetch();
		if($arElement)
		{
			$rsProperties = CIBlockProperty::GetList(array(), array("IBLOCK_ID" => $arElement["IBLOCK_ID"], "USER_TYPE" => "Picture"));
			while($arProperty = $rsProperties->Fetch())
            $arProperties[] = $arProperty;
		}
		$arElements = array();
		foreach($arProperties as $arProperty)
		{
         $rsPropValues = CIBlockElement::GetProperty($arElement["IBLOCK_ID"], $arElement["ID"], array(), array(
            "EMPTY" => "N",
            "ID" => $arProperty["ID"],
				));
				while($arPropValue = $rsPropValues->Fetch())
			{
					$ID = intval($arPropValue["VALUE"]);
					if($ID > 0)
						$arElements[$ID] = $ID;
			}
		}
		foreach($arElements as $to_delete)
		{
         CIBlockElement::Delete($to_delete);
		}
	}
}
```

Что мы в итоге имеем:

- Интерфейс редактирования элемента с возможностью добавления и удаления изображений.
- При удалении элемента связанная с ним информация удаляется.
- Поддержка компонента в публичной части.


**Инструкция по применению:**

- Этот код разместите в файле `/bitrix/php_interface/init.php`.
- Создайте инфоблок для хранения изображений и в его настройках укажите параметры генерации картинки предварительного просмотра из детальной (на вкладке **Поля**).
- В инфоблоке **Гостиницы** добавьте свойство типа **Картинка** и в дополнительных настройках этого свойства укажите созданный на первом шаге инфоблок. Не забудьте указать символьный код свойства.
- Создайте элемент и "поиграйтесь" со значениями этого свойства.
- В публичной части, например в компоненте news, в параметрах настройки списка элементов выбрать это свойство.

#### Как удалить файл в свойстве элемента инфоблока

Обновить любое свойство можно с помощью методов:

- [Update](http://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/update.php)
- [SetPropertyValues](http://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/setpropertyvalues.php)
- [SetPropertyValuesEx](http://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/setpropertyvaluesex.php)

При использовании любого метода на ключ массива обновления идет код свойства, а значение - новое значение. Для удаления файла нам надо передать вот такой простой массив:

```
array('MY_FILE' => array('XXX' => array('del' => 'Y')));
```

Способ универсален и подходит что для инфоблоков, что для инфоблоков 2.0, что для документооборота. `MY_FILE` - это код вашего свойства типа **Файл**. А что такое ХХХ? В нём содержится ID значения_ свойства. То есть не ID свойства, а именно ID значения.

```
CModule::IncludeModule('iblock');
$IB = 24;
$ID = 220304;
$CODE = 'ONE_FL';
if ($arProp = CIBlockElement::GetProperty($IB, $ID, 'ID', 'DESC', array('CODE' => $CODE))->fetch()) {
	$XXX = $arProp['PROPERTY_VALUE_ID'];
	CIBlockElement::SetPropertyValueCode($ID, $CODE, array($XXX => array('del' => 'Y')));
}
```

Вот таким образом получается этот универсальный XXX, именно так его и надо передавать для каждого файла, который мы хотим удалить.

Что делать в случае множественного файла? Как удалить конкретный файл в списке? Все просто - используем в примере выше не **if**, а **while**, ну и дополнительно фильтруем, какой файл надо удалить.
