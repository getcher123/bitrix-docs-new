# resolveHighloadblock

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblocktable/resolvehighloadblock.php

```
array|null public static
\Bitrix\Highloadblock\HighloadBlockTable::resolveHighloadblock(
	$hlblock
);
```

Метод **resolveHighloadblock** нормализует входные данные и возвращает ассоциативный массив с информацией о highload-блоке по его идентификатору, названию или массиву данных. Статический метод.

С версии 25.0.0 метод выполняет автоматическое кеширование результатов запроса к базе данных на 86400 секунд (24 часа).

Особенности работы метода:

- обращение к базе данных происходит только при передаче в качестве аргумента числа или строки,
- проверка прав доступа к highload-блоку не осуществляется.

#### Параметры

| Параметр | Описание | Версия |
| --- | --- | --- |
| $hlblock | Значение зависит от типа данных:<br><br>        <br>- `int` — идентификатор highload-блока,<br>- `string` — название highload-блока,<br>- `array` — массив с данными highload-блока.<br><br>        Если передано число или строка, начинающаяся с цифры, значение интерпретируется как `ID`. Если передана строка — как `NAME`. <br><br>Например, `123abc` будет воспринято как ID, что может привести к неожиданному поведению. Избегайте имен highload-блоков, которые начинаются с цифр. |  |

#### Возвращаемое значение

Метод возвращает массив с полями highload-блока: `ID`, `NAME` и `TABLE_NAME`. Значение `null` возвращает в случаях:

- передан некорректный параметр,
- highload-блок не найден,
- в переданном массиве отсутствуют обязательные поля,
- имя блока содержит недопустимые символы (допустимы только латинские буквы, цифры и подчеркивание).

#### Примеры

Пример 1. Получить данные highload-блока по ID.

```
$hlblockId = 5;
$highloadInfo = \Bitrix\Highloadblock\HighloadBlockTable::resolveHighloadblock($hlblockId);

if ($highloadInfo !== null)
{
	echo "Название блока: " . $highloadInfo['NAME'] . "\n";
	echo "Таблица: " . $highloadInfo['TABLE_NAME'] . "\n";
}
else
{
	echo "Highload-блок с ID=5 не найден.";
}
```

Пример 2. Получить информацию по имени highload-блока.

```
$hlblockName = 'Products';
$highloadInfo = \Bitrix\Highloadblock\HighloadBlockTable::resolveHighloadblock($hlblockName);

if ($highloadInfo !== null)
{
	$entityId = \Bitrix\Highloadblock\HighloadBlockTable::compileEntityId($highloadInfo['ID']);
	// Теперь можно использовать $entityId, например, при работе с CUserTypeEntity
}
else
{
	echo "Highload-блок с именем 'Products' не найден.";
}
```

Пример 3. Проверить массив с данными.

```
$existingHlblockData = [
	'ID' => 7,
	'NAME' => 'Employees',
	'TABLE_NAME' => 'b_hlblock_employees'
];

$validated = \Bitrix\Highloadblock\HighloadBlockTable::resolveHighloadblock($existingHlblockData);

if ($validated !== null)
{
	// Данные прошли валидацию
	print_r($validated);
}
```
