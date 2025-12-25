# Почта

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/mail/index.php

Раздел содержит информацию о классах модуля **Почта**, относящихся к ядру D7 и находящихся соответственно в пространстве имен **\Bitrix\Mail**.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('mail');
```

| Класс, простраство имён | Описание |
| --- | --- |
| [Imap](https://dev.1c-bitrix.ru/api_d7/bitrix/mail/imap/index.php) | Класс для работы с почтой по протоколу Imap. |
| [Smtp](https://dev.1c-bitrix.ru/api_d7/bitrix/mail/smtp/index.php) | Класс для работы с SMTP-клиентом. |
| [Message](https://dev.1c-bitrix.ru/api_d7/bitrix/mail/message/index.php) | Класс для работы с сообщениями. |
| [User](https://dev.1c-bitrix.ru/api_d7/bitrix/mail/user/index.php) | Класс для работы с пользователями. |
