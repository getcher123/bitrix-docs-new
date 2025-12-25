# HighloadBlockRightsTable

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblockrightstable/index.php

**HighloadBlockRightsTable** - класс для работы с таблицей прав к highload-блокам.

В связи с архитектурой модуля проверка прав доступа в модуле не реализована на уровне запросов. Но вы можете самостоятельно проверить права на тот или иной highload-блок перед действиями с ним с помощью метода [\Bitrix\HighloadBlock\HighloadBlockRightsTable::getOperationsName](https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblockrightstable/getoperationsname.php).

#### Цепочка наследования

Является наследником класса [Bitrix\Main\ORM\Data\DataManager](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=05748&LESSON_PATH=3913.5062.5748) (до версии 18.0.2 модуля **Main** - класса [Bitrix\Main\Entity\DataManager](https://dev.1c-bitrix.ru/api_d7/bitrix/main/entity/datamanager/index.php)).

#### Методы класса

| Метод | Описание | С версии |
| --- | --- | --- |
| [getMap](https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblockrightstable/getmap.php) | Метод возвращает список полей для таблицы прав к highload-блокам. |  |
| [getOperationsName](https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblockrightstable/getoperationsname.php) | Метод выполняет проверку прав доступа к highload-блоку для текущего пользователя. |  |
| [getTableName](https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblockrightstable/gettablename.php) | Метод возвращает название таблицы прав к highload-блокам. |  |
| [validateAccessCode](https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblockrightstable/validateaccesscode.php) | Метод возвращает валидатор для поля `ACCESS_CODE`. |  |
