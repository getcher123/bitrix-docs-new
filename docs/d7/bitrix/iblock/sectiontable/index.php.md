# SectionTable

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/sectiontable/index.php

**SectionTable** – класс для работы с таблицей разделов инфоблоков.

#### Цепочка наследования

Является наследником класса [Bitrix\Main\ORM\Data\DataManager](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=05748&LESSON_PATH=3913.5062.5748) (до версии 18.0.2 модуля **Main** – класса [Bitrix\Main\Entity\DataManager](https://dev.1c-bitrix.ru/api_d7/bitrix/main/entity/datamanager/index.php)).

#### Методы класса

| Метод | Описание | С версии |
| --- | --- | --- |
| [getFilePath](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/sectiontable/getfilepath.php)Метод возвращает путь к файлу, содержащему определение класса.<br>12.0.4 |  |  |
| [getMap](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/sectiontable/getmap.php)Метод возвращает список полей для таблицы разделов инфоблоков.<br>12.0.4 |  |  |
| [getTableName](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/sectiontable/gettablename.php)Метод возвращает название таблицы разделов инфоблоков в базе данных.<br>12.0.4 |  |  |
| [validateCode](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/sectiontable/validatecode.php)Метод возвращает валидатор для поля `CODE`.<br>14.0.3 |  |  |
| [validateName](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/sectiontable/validatename.php)Метод возвращает валидатор для поля `NAME`.<br>14.0.3 |  |  |
| [validateTmpId](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/sectiontable/validatetmpid.php)Метод возвращает валидатор для поля `TMP_ID`.<br>14.0.3 |  |  |
| [validateXmlId](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/sectiontable/validatexmlid.php)Метод возвращает валидатор для поля `XML_ID`.<br>14.0.3 |  |  |

> **Примечание:** Методы *add*, *delete* и *update* (наследуемые от класса DataManager) в классе SectionTable **заблокированы** (см. [ограничения](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=012864) нового объектного ORM).
