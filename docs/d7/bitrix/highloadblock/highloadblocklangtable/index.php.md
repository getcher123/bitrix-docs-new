# HighloadBlockLangTable

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblocklangtable/index.php

**HighloadBlockLangTable** - класс для работы с таблицей языкозависимых параметров highload-блоков.

> **Внимание!** С версии **22.300.0** первичный ключ класса **HighloadBlockLangTable** включает поля `ID` и `LID`.

#### Цепочка наследования

Является наследником класса [Bitrix\Main\ORM\Data\DataManager](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=05748&LESSON_PATH=3913.5062.5748) (до версии 18.0.2 модуля **Main** - класса [Bitrix\Main\Entity\DataManager](https://dev.1c-bitrix.ru/api_d7/bitrix/main/entity/datamanager/index.php)).

#### Методы класса

| Метод | Описание | С версии |
| --- | --- | --- |
| [getMap](https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblocklangtable/getmap.php)Метод возвращает список полей для таблицы языкозависимых параметров highload-блока. |  |  |
| [getTableName](https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblocklangtable/gettablename.php)Метод возвращает название таблицы языкозависимых параметров highload-блоков. |  |  |
| [validateLid](https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblocklangtable/validatelid.php)Метод возвращает валидатор для поля `LID`. |  |  |
| [validateName](https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/highloadblocklangtable/validatename.php)Метод возвращает валидатор для поля `NAME`. |  |  |

Помимо работы с классом по правилам D7, получить языкозависимые параметры highload-блока можно следующим образом при выборке:

```
$res = \Bitrix\Highloadblock\HighloadBlockTable::getList(array(
	'select' => array('*', 'NAME_LANG' => 'LANG.NAME'),
	'order' => array('NAME_LANG' => 'ASC', 'NAME' => 'ASC')
));
while ($row = $res->fetch())
{
	if ($row['NAME_LANG'] != '')
	{
		echo $row['NAME_LANG'];//языкозависимое название есть
	}
	else
	{
		echo $row['NAME'];//языкозависимого названия нет
	}
}
```
