# PropertyTable

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/propertytable/index.php

**PropertyTable** – класс для работы с таблицей свойств инфоблоков.

#### Цепочка наследования

Является наследником класса [Bitrix\Main\ORM\Data\DataManager](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=05748&LESSON_PATH=3913.5062.5748) (до версии 18.0.2 модуля **Main** – класса [Bitrix\Main\Entity\DataManager](https://dev.1c-bitrix.ru/api_d7/bitrix/main/entity/datamanager/index.php)).

#### Методы класса

| Метод | Описание | С версии |
| --- | --- | --- |
| [getFilePath](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/propertytable/getfilepath.php)Метод возвращает путь к файлу, содержащему определение класса.<br>14.0.0 |  |  |
| [getMap](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/propertytable/getmap.php)Метод возвращает список полей для таблицы свойств инфоблоков.<br>14.0.0 |  |  |
| [getTableName](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/propertytable/gettablename.php)Метод возвращает название таблицы свойств инфоблоков в базе данных.<br>14.0.0 |  |  |
| [validateCode](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/propertytable/validatecode.php)Метод возвращает валидатор для поля `CODE`.<br>14.0.3 |  |  |
| [validateFileType](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/propertytable/validatefiletype.php)Метод возвращает валидатор для поля `FILE_TYPE`.<br>14.0.3 |  |  |
| [validateHint](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/propertytable/validatehint.php)Метод возвращает валидатор для поля `HINT`.<br>14.0.3 |  |  |
| [validateName](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/propertytable/validatename.php)Метод возвращает валидатор для поля `NAME`.<br>14.0.3 |  |  |
| [validateTmpId](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/propertytable/validatetmpid.php)Метод возвращает валидатор для поля `TMP_ID`.<br>14.0.3 |  |  |
| [validateUserType](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/propertytable/validateusertype.php)Метод возвращает валидатор для поля `USER_TYPE`.<br>14.0.3 |  |  |
| [validateXmlId](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/propertytable/validatexmlid.php)Метод возвращает валидатор для поля `XML_ID`.<br>14.0.3 |  |  |

#### Константы пользовательских типов свойств инфоблока

Константы рекомендуется использовать при анализе значения поля **USER_TYPE** свойств инфоблоков.

| Константа | Значение | Описание | С версии |
| --- | --- | --- | --- |
| USER_TYPE_DATE | Date | Идентификатор свойства типа **Дата**. | 23.0.0 |
| USER_TYPE_DATETIME | DateTime | Идентификатор свойства типа **Дата/Время**. | 23.0.0 |
| USER_TYPE_XML_ID | ElementXmlID | Идентификатор свойства типа **Привязка к элементам по XML_ID**. | 23.0.0 |
| USER_TYPE_FILE_MAN | FileMan | Идентификатор свойства типа **Привязка к файлу (на сервере)**. | 23.0.0 |
| USER_TYPE_HTML | HTML | Идентификатор свойства типа **HTML/текст**. | 23.0.0 |
| USER_TYPE_ELEMENT_LIST | EList | Идентификатор свойства типа **Привязка к элементам в виде списка**. | 23.0.0 |
| USER_TYPE_SEQUENCE | Sequence | Идентификатор свойства типа **Счетчик**. | 23.0.0 |
| USER_TYPE_ELEMENT_AUTOCOMPLETE | EAutocomplete | Идентификатор свойства типа **Привязка к элементам с автозаполнением**. | 23.0.0 |
| USER_TYPE_SKU | SKU | Идентификатор свойства типа **Привязка к товарам (SKU)**. | 23.0.0 |
| USER_TYPE_SECTION_AUTOCOMPLETE | SectionAuto | Идентификатор свойства типа **Привязка к разделам с автозаполнением**. | 23.0.0 |
| USER_TYPE_DIRECTORY | directory | Идентификатор свойства типа **Справочник**. | 23.0.0 |
| USER_TYPE_CRM | ECrm | Идентификатор свойства типа **Привязка к элементам CRM**. | 23.300.0 |
| USER_TYPE_MONEY | Money | Идентификатор свойства типа **Деньги**. | 23.300.0 |
| USER_TYPE_DISK | DiskFile | Идентификатор свойства типа **Файл (Диск)**. | 23.300.0 |
| USER_TYPE_GOOGLE_MAP | map_google | Идентификатор свойства типа **Привязка к карте Google Maps**. | 23.300.0 |
| USER_TYPE_YANDEX_MAP | map_yandex | Идентификатор свойства типа **Привязка к Яндекс.Карте**. | 23.300.0 |
| USER_TYPE_FORUM_TOPIC | TopicID | Идентификатор свойства типа **Привязка к теме форума**. | 23.300.0 |
| USER_TYPE_DIRECTORY | directory | Идентификатор свойства типа **Справочник**. | 23.300.0 |
| USER_TYPE_EMPLOYEE | employee | Идентификатор свойства типа **Привязка к сотруднику**. | 23.300.0 |
| USER_TYPE_USER | UserID | Идентификатор свойства типа **Привязка к пользователю**. | 23.300.0 |
