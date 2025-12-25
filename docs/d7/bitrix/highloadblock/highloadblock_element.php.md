# Провайдер highloadblock-element

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblock_element.php

Провайдер предназначен для получения данных для диалога выбора сущности (*EntitySelector*) – для строки быстрого поиска и списка выбора:

![](../../../../images/d7/dev.1c-bitrix.ru/images/admin_expert/entityselector.png)

#### Параметры вызова

| Параметр | Описание | Тип | Обяз. |
| --- | --- | --- | --- |
| highloadblockId | Идентификатор (ID) highload-блока. | Int | Да |
| valueField | Название поля с идентификатором записи в highload-блоке. Значение по умолчанию – `UF_XML_ID` (для свойств инфоблока типа **Справочник**).<br><br>Для пользовательских полей типа **Привязка к элементам highload-блоков** необходимо в этом ключе явно передавать значение `ID`. | String | Нет |
| titleField | Название поля с именем записи в highload-блоке. Значение по умолчанию – `UF_NAME` (для свойств инфоблока типа **Справочник**).<br><br>Для пользовательских полей типа **Привязка к элементам highload-блоков** нужно передавать название поля только в том случае, если оно отличается от `UF_NAME`. | String | Нет |
| orderField | Название поля, по которому идет сортировка элементов. Значение по умолчанию – `UF_SORT`. | String | Нет |
| direction | Направление сортировки – по возрастанию/убыванию. Варианты – `ASC/DESC`. Значение по умолчанию – `ASC`. | String | Нет |

#### Примеры

Пример использования для описания поля фильтра в компоненте [main.ui.filter](../main/systemcomponents/gridandfilter/mainuifilter.php.md) (для свойства инфоблока типа **Справочник**):

```
$field = [
	'type' => 'entity_selector',
	'params' => [
		'multiple' => 'Y',
		'dialogOptions' => [
			'entities' => [
				[
					'id' => 'highloadblock-element', // название провайдера
					'dynamicLoad' => true,
					'dynamicSearch' => true,
					'options' => [
						'highloadblockId' => 13, // заменить на ID своего highload-блока
						'direction' => 'DESC', // сортировка по убыванию
					],
				],
			],
			'searchOptions' => [
				'allowCreateItem' => false,
			],
		],
	],
];
```
