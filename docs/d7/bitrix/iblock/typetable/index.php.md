# TypeTable

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/typetable/index.php

**TypeTable** – класс для работы с таблицей типов информационных блоков.

#### Цепочка наследования

Является наследником класса [Bitrix\Main\ORM\Data\DataManager](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=05748&LESSON_PATH=3913.5062.5748) (до версии 18.0.2 модуля **Main** – класса [Bitrix\Main\Entity\DataManager](https://dev.1c-bitrix.ru/api_d7/bitrix/main/entity/datamanager/index.php)).

#### Методы класса

| Метод | Описание | С версии |
| --- | --- | --- |
| [getFilePath](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/typetable/getfilepath.php)Метод возвращает путь к файлу, содержащему определение класса.<br>14.0.1 |  |  |
| [getMap](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/typetable/getmap.php)Метод возвращает список полей для таблицы типов инфоблоков.<br>14.0.1 |  |  |
| [getTableName](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/typetable/gettablename.php)Метод возвращает название таблицы типов инфоблоков в базе данных.<br>14.0.1 |  |  |
| [onDelete](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/typetable/ondelete.php)Обработчик удаляет информационные блоки заданного типа и языковые сообщения из базы данных.<br>15.0.1 |  |  |
| [validateEditFileAfter](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/typetable/validateeditfileafter.php)Метод возвращает валидатор для поля `EDIT_FILE_AFTER` (полный путь к файлу-обработчику вывода интерфейса редактирования элемента).<br>14.0.3 |  |  |
| [validateEditFileBefore](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/typetable/validateeditfilebefore.php)Метод возвращает валидатор для поля `EDIT_FILE_BEFORE` (полный путь к файлу-обработчику массива полей элемента перед сохранением на странице редактирования элемента).<br>14.0.3 |  |  |
| [validateId](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/typetable/validateid.php)Метод возвращает валидатор для поля `ID` (идентификатор типа инфоблоков).<br>14.0.3 |  |  |
