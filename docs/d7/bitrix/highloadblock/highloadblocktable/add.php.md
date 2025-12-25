# add

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblocktable/add.php

```
\Bitrix\Main\Entity\AddResult public static
\Bitrix\Highloadblock\HighloadBlockTable::add(
	array $data
);
```

Метод добавляет новый highload-блок. Метод статический.

#### Параметры

| Параметр | Описание | Версия |
| --- | --- | --- |
| $data | Массив, содержащий значения полей highload-блока. |  |

#### Примеры

```
//создание hl-блока
$result = Bitrix\Highloadblock\HighloadBlockTable::add(array(
	'NAME' => 'MyTbl',//должно начинаться с заглавной буквы и состоять только из латинских букв и цифр
	'TABLE_NAME' => 'myname',//должно состоять только из строчных латинских букв, цифр и знака подчеркивания
));
if (!$result->isSuccess()) {
	$errors = $result->getErrorMessages();
} else {
	$id = $result->getId();
}
...
```
