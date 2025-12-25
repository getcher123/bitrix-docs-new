# delete

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblocktable/delete.php

```
\Bitrix\Main\Entity\DeleteResult public static
\Bitrix\Highloadblock\HighloadBlockTable::delete(
	mixed $primary
);
```

Метод удаляет highload-блок с ключом `$primary`. Метод статический.

#### Параметры

| Параметр | Описание | Версия |
| --- | --- | --- |
| $primary | Идентификатор highload-блока. |  |

#### Примеры

```
//удаление hl-блока с кодом 11
Bitrix\Highloadblock\HighloadBlockTable::delete(11);
```
