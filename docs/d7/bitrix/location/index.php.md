# Адреса и местоположения

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/location/index.php

`\Bitrix\Location` - пространство имен модуля **Адреса и местоположения**.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('location');
```

| Класс, пространство имен | Описание |
| --- | --- |
| [Entity](https://dev.1c-bitrix.ru/api_d7/bitrix/location/entity/index.php) | Подпространство имён, содержит сущности Адрес, Формат, Местоположение. |
| [Address](https://dev.1c-bitrix.ru/api_d7/bitrix/location/entity/address/index.php) | Класс для работы с адресами. |
| [Format](https://dev.1c-bitrix.ru/api_d7/bitrix/location/entity/format/index.php) | Класс для работы с форматами местоположений. |
| [Location](https://dev.1c-bitrix.ru/api_d7/bitrix/location/entity/location/index.php) | Класс для работы с местоположениями. |
| [Service](https://dev.1c-bitrix.ru/api_d7/bitrix/location/service/index.php) | Сервисы (фасады), предоставляемые модулем для работы с сущностями из Bitrix\Location\Entity. |
