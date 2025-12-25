# post

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/post.php

```
string|boolean public
\Bitrix\Main\Web\HttpClient::post(
	string $url,
	array|string|resource $postData = null,
	$multipart = false
);
```

Нестатический метод выполняет POST запрос.

> **Примечания**:
>
> 1. Заголовки устанавливает метод [setHeader](setheader.php.md).
>
> 2. XML можно передать тремя способами:
>
>    - как поле формы,
>
>    - как файл формы,
>
>    - просто в теле запроса.

#### Параметры

| Параметр | Описание | Версия |
| --- | --- | --- |
| $url | Абсолютный URI в виде: `"http://user:pass@host:port/path/?query"`. |  |
| $postData | Сущность POST/PUT <br>		<br>			запроса<br>			<br>				<br>                    <br>                    Вид запроса зависит от того, как именно сервер принимает. Будьте внимательны.<br>                <br>			<br>		<br>		. Если это - обработчик ресурсов, то чтение данных осуществляется непосредственно из потока. |  |
| $multipart | По умолчанию *false*. Использовать или нет multipart/form-data. Если *true*, то метод принимает файл как источник или как массив с ключами **resource** (или **content**) и опциональными ключами **filename** и **contentType**. | 17.5.5 |

#### Примеры
