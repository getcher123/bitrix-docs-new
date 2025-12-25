# Библиотека iblock.field-selector

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/iblock_field_selector.php

### Описание и пример

Библиотека **iblock.field-selector** предназначена для использования в [пользовательских типах свойств](../../../iblock/classes/user_properties/index.md) инфоблока и UF-полях привязки к сущностям модуля **Информационные блоки**.

Библиотека позволяет использовать **TagSelector** в полях ввода формы или грида. В качестве значений могут быть целые числа либо строки.

Использование:

```
	\Bitrix\Main\Loader::includeModule('iblock');

	\Bitrix\Main\UI\Extension::load('iblock.field-selector');

	$containerId = 'my_element'; // ID dom-контейнера для TagSelector'а

	$values = 100; // текущее значение

	$config = \Bitrix\Main\Web\Json::encode([
		'containerId' => $containerId,
		'fieldName' => 'myfield',
		'multiple' => false,
		'collectionType' => 'int',
		'selectedItems' => $values,
		'iblockId' => 41,
		'userType' => \Bitrix\Iblock\PropertyTable::USER_TYPE_ELEMENT_AUTOCOMPLETE,
		'entityId' => \Bitrix\Iblock\Integration\UI\EntitySelector\IblockPropertyElementProvider::ENTITY_ID,
	]);

	return <<<HTML
		<div id="$containerId"></div>
		<script>
			(function() {
				const selector = new BX.Iblock.FieldSelector($config);
				selector.render();
			})();
		</script>
HTML;
```

В примере выше реализован выбор элементов, принадлежащих инфоблоку c ID = 41 для одиночного (**multiple**) свойства типа "Привязка к элементам с автозаполнением" (**userType**). Текущее значение (**selectedItems**) – 100. Тип значения передается в ключе **collectionType** и может принимать значения `int` или `string`.

Идентификатор провайдера данных указан в ключе **entityId**.

> **Внимание**! Одновременно можно работать только с одним провайдером. Это обусловлено спецификой использования библиотеки.

DOM-элемент контейнера для селектора необходимо отрисовывать самостоятельно.

### Входные параметры

| Параметр | Тип | Описание |
| --- | --- | --- |
| containerId * | string | Идентификатор DOM-элемента страницы, в котором будет размещён селектор. |
| fieldName * | string | Имя поля формы, в которое будет записан результат. Для селектора с множественным выбором к имени поля необходимо добавлять `[]`. |
| multiple | bool | Одиночное или множественное свойство/поле. По умолчанию `false`. |
| collectionType | string | Тип значений свойства/поля. Возможные значения – `int` или `string`. Значение по умолчанию `int`. <br><br>> **Внимание**! Текущие значения для селектора должны быть приведены к указанному типу. |
| selectedItems * | - для одиночных значений: `string`, `int` или массив с одним значением;<br>- для множественных – всегда массив значений | Текущие значения свойства/поля. |
| iblockId * | int | ID инфоблока, из которого производится выборка. Если свойство/поле не привязано к конкретному инфоблоку, необходимо передавать 0. |
| userType | string | Идентификатор пользовательского типа свойства/поля. |
| entityId * | string | Идентификатор провайдера данных. Доступные штатные провайдеры:<br><br>- `\Bitrix\Iblock\Integration\UI\EntitySelector\IblockPropertyE­lementProvider::ENTITY_ID` – для выбора элементов инфоблоков;<br>- `\Bitrix\Iblock\Integration\UI\EntitySelector\IblockPropertyS­ectionProvider::ENTITY_ID` – для выбора разделов инфоблоков;<br>- `\Bitrix\Highloadblock\Integration\UI\EntitySelector\ElementP­rovider::ENTITY_ID` – для выбора элементов highload-блоков. |
| searchMessages | object | Сообщения окна поиска в случае пустого результата. Объект содержит поля:<br><br>- **title** – заголовок окна, строка;<br>- **subtitle** – поясняющий текст, строка. |
| changeEvents | arrays | Список js-событий, которые будут вызваны после изменений значения в селекторе. |

***** – обязательные параметры.
