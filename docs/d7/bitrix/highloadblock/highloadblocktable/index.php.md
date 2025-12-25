# HighloadBlockTable

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblocktable/index.php

**HighloadBlockTable** - класс для работы с таблицей highload-блоков.

#### Цепочка наследования

Является наследником класса [Bitrix\Main\ORM\Data\DataManager](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=05748&LESSON_PATH=3913.5062.5748) (до версии 18.0.2 модуля **Main** - класса [Bitrix\Main\Entity\DataManager](https://dev.1c-bitrix.ru/api_d7/bitrix/main/entity/datamanager/index.php)).

#### Методы класса

| Метод | Описание | С версии |
| --- | --- | --- |
| [add](add.php.md)Метод добавляет новый highload-блок.<br>12.0.0 |  |  |
| [delete](delete.php.md)Метод удаляет highload-блок с ключом `$primary`.<br>12.0.0 |  |  |
| [compileEntityId](compileentityid.php.md)Метод возвращает ID сущности-владельца полей highload-блока.<br>20.0.0 |  |  |
| [getTableName](gettablename.php.md)Метод возвращает название таблицы highload-блоков в базе данных.<br>12.0.0 |  |  |
| [resolveHighloadblock](resolvehighloadblock.php.md)Метод возвращает массив с информацией о highload-блоке. |  |  |
| [update](update.php.md)Метод изменяет параметры highload-блока с ключом `$primary`.<br>12.0.0 |  |  |

#### Поля Highload-блоков

| Поле | Описание | Тип | Обяз. |
| --- | --- | --- | --- |
| ID | Идентификатор highload-блока. | Int | Да |
| NAME | Название highload-блока. | String | Да |
| TABLE_NAME | Название таблицы с элементами highload-блока. | String | Да |
