# deleteMessages

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/imconnector/customconnectors/deletemessages.php

```
public static function
\Bitrix\ImConnector\CustomConnectors::deleteMessages(
   $connector,
   $line,
   $data
)
```

Метод для  удаления сообщений в ОЛ.

| Метод | Описание | С версии |
| --- | --- | --- |
| connector | ID коннектора, который был указан при регистрации обработчика. |  |
| line | ID открытой линии |  |
| data | массив массивов сообщений, где каждое сообщение описывается следующим форматом:<br><br>```<br>array(<br>  //Массив описания пользователя<br>  'user' => array(<br>     'id',//ID пользователя во внешней системе *<br>     'last_name',//Фамилия<br>     'name',//Имя<br>     'picture' =><br>     array(<br>        'url'//Ссылка на аватарку пользователя, доступную для портала<br>     ),<br>     'url',//Ссылка на профиль пользователя<br>     'sex',//Пол. Допустимо male и female<br>  ),<br>  //Массив описания сообщения<br>  'message' => array(<br>     'id', //ID сообщения во внешней системе.*<br>     )<br>  ),<br>  //Массив описания чата<br>  'chat' => array(<br>     'id',//ID чата во внешней системе *<br>     'name', //Имя чата во внешней системе<br>     'url', //Ссылка на чат во внешней системе<br>  ),<br>);<br>``` |  |
