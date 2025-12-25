# GroupTaskTable

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/grouptasktable/index.php

**GroupTaskTable** - класс описывает ORM-сущность GroupTaskTable.

#### Цепочка наследования

Является наследником класса [Bitrix\Main\ORM\Data\DataManager](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=05748&LESSON_PATH=3913.5062.5748) (до версии 18.0.2 модуля **Main** - класса [Bitrix\Main\Entity\DataManager](https://dev.1c-bitrix.ru/api_d7/bitrix/main/entity/datamanager/index.php)).

#### Методы класса

| Метод | Описание | С версии |
| --- | --- | --- |
| [getTableName](https://dev.1c-bitrix.ru/api_d7/bitrix/main/grouptasktable/gettablename.php) | Метод возвращает название таблицы БД для сущности. |  |
| [getMap](https://dev.1c-bitrix.ru/api_d7/bitrix/main/grouptasktable/getmap.php) | Метод возвращает список полей для таблицы. |  |
| [validateExternalId](https://dev.1c-bitrix.ru/api_d7/bitrix/main/grouptasktable/validateexternalid.php) | Метод возвращает валидаторы для поля EXTERNAL_ID. |  |

**Поля таблицы сущности**

| Поле | Описание | Тип | Обяз. |
| --- | --- | --- | --- |
| GROUP_ID | Идентификатор группы. | Int | Да |
| TASK_ID | Код уровня доступа | Int | Да |
| EXTERNAL_ID | Не используется | String | Нет |
