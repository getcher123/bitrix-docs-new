# Forum

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/forum/index.php

Раздел содержит информацию о классах модуля **Форум**, относящихся к ядру D7 и находящихся соответственно в пространстве имен **\Bitrix\Forum**.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('forum');
```

| Класс, пространство имён | Описание |
| --- | --- |
| [UserTable](https://dev.1c-bitrix.ru/api_d7/bitrix/forum/usertable/index.php) | Классы для работы с таблицей пользователей форума. Связь с таблицей пользователей - один к одному. |
| [MessageTable](https://dev.1c-bitrix.ru/api_d7/bitrix/forum/messagetable/index.php) | Классы для работы с таблицей сообщений. Связь с таблицей тем форумов - один к одному. |
| [Comments](https://dev.1c-bitrix.ru/api_d7/bitrix/forum/comments/index.php) | Классы для работы с форумными данными, как с комментариями. |
| [ForumTable](https://dev.1c-bitrix.ru/api_d7/bitrix/forum/forumtable/index.php) | Классы для работы с таблицей форумов. Связь с таблицей групп форумов - много к одному. |
| [GroupTable](https://dev.1c-bitrix.ru/api_d7/bitrix/forum/grouptable/index.php) | Классы для работы с таблицей групп форумов. |
| [ForumSiteTable](https://dev.1c-bitrix.ru/api_d7/bitrix/forum/forumsitetable/index.php) | Классы для работы с таблицей, связывающей форум с конкретным сайтом. Привязка форума к сайту по типу многие ко многим. |
| [Replica](https://dev.1c-bitrix.ru/api_d7/bitrix/forum/replica/index.php) | Пространство имён для классов репликации модуля Форум. |
