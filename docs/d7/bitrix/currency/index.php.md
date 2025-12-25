# Валюты

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/currency/index.php

Раздел содержит информацию о классах модуля **Валюты**, относящихся к ядру D7 и находящихся соответственно в пространстве имен `\Bitrix\Currency`.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('currency');
```

| Класс | Описание |
| --- | --- |
| [CurrencyClassifier](https://dev.1c-bitrix.ru/api_d7/bitrix/currency/currencyclassifier/index.php)Класс для работы с классификатором валют. |  |
| [CurrencyLangTable](https://dev.1c-bitrix.ru/api_d7/bitrix/currency/currencylangtable/index.php)Класс для работы с таблицей языкозависимых параметров валют. |  |
| [CurrencyManager](https://dev.1c-bitrix.ru/api_d7/bitrix/currency/currencymanager/index.php)Класс для управления валютами. |  |
| [CurrencyRateTable](https://dev.1c-bitrix.ru/api_d7/bitrix/currency/currencyratetable/index.php)Класс для работы с таблицей курсов валют. |  |
| [CurrencyTable](https://dev.1c-bitrix.ru/api_d7/bitrix/currency/currencytable/index.php)Класс для работы с таблицей валют. |  |
| [Helpers](https://dev.1c-bitrix.ru/api_d7/bitrix/currency/helpers/index.php)Пространство имен `\Bitrix\Currency\Helpers` содержит вспомогательные классы. |  |
