# sendMessages

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/imconnector/customconnectors/sendmessages.php

```
public static function
\Bitrix\ImConnector\CustomConnectors::sendMessages(
	$connector,
	$line,
	$data
)
```

Метод для отправки сообщений в Открытую Линию.

#### Параметры

| Метод | Описание | С версии |
| --- | --- | --- |
| connector | ID коннектора, который был указан при регистрации обработчика. |  |
| line | ID открытой линии |  |
| data | массив массивов сообщений, где каждое сообщение описывается следующим форматом:<br><br>```<br>array(<br>	//Массив описания пользователя<br>	'user' => array(<br>		'id',//ID пользователя во внешней системе *<br>		'last_name',//Фамилия<br>		'name',//Имя<br>		'picture' =><br>		array(<br>			'url'//Ссылка на аватарку пользователя, доступную для портала<br>		),<br>		'url',//Ссылка на профиль пользователя<br>		'sex',//Пол. Допустимо male и female<br>		'email', //email<br>		'phone', //телефон<br>	),<br>	//Массив описания сообщения<br>	'message' => array(<br>		'id', //ID сообщения во внешней системе.*<br>		'date', //Время сообщения в формате timestamp *<br>		'disable_crm' => 'Y' ,//отключить чат трекер (CRM трекер)<br>		'text', //Текст сообщения. Должен быть указан либо элемент text или files. Допустимое форматирование (BB коды) описаны здесь: https://dev.1c-bitrix.ru/learning/course/?COURSE_ID=93&LESSON_ID=7679&LESSON_PATH=7657.7677.7679<br>		'files' => array(//Массив массивов, с описанием файлов, со ссылкой, которая доступна порталу<br>			array('url')<br>		)<br>	),<br>	//Массив описания чата<br>	'chat' => array(<br>		'id',//ID чата во внешней системе *<br>		'name', //Имя чата во внешней системе<br>		'url', //Ссылка на чат во внешней системе<br>	),<br>);<br>``` |  |
