# Highload-блоки

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/highloadblock/index.php

`\Bitrix\Highloadblock` - пространство имен модуля **Highload-блоки**.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('highloadblock');
```

| Класс | Описание |
| --- | --- |
| [DataManager](datamanager/index.php.md) | Класс для работы с данными highload-блоков. |
| [HighloadBlockLangTable](highloadblocklangtable/index.php.md) | Класс для работы с таблицей языкозависимых параметров highload-блоков. |
| [HighloadBlockRightsTable](highloadblockrightstable/index.php.md) | Класс для работы с таблицей прав к highload-блокам. |
| [HighloadBlockTable](highloadblocktable/index.php.md) | Класс для работы с таблицей highload-блоков. |

> **Важно!** Нельзя вызывать highloadblock до обработчика пользовательских свойств.
