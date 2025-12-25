# compileEntityId

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblocktable/compileentityid.php

```
string public static
\Bitrix\Highloadblock\HighloadBlockTable::compileEntityId(
	$id
);
```

Метод возвращает ID сущности-владельца полей highload-блока (**string**). Статический метод.

#### Параметры

| Параметр | Описание | Версия |
| --- | --- | --- |
| $id | Идентификатор highload-блока (Тип: **int** или **string**). |  |

#### Примеры

```
//добавление поля в highload-блок
$id = 10; //ID highload-блока
$fields = array(
	'ENTITY_ID' => \Bitrix\Highloadblock\HighloadBlockTable::compileEntityId($id),
	... // все остальные поля
);
```
