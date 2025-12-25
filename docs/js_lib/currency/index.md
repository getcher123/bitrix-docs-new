# Валюты


### Описание и список функций

**BX.Currency** – библиотека для форматирования цен с учетом текущего языка на js.

Идет в составе модуля валют (**currency**).

Для подключения библиотеки используется следующий код:

``` if (\Bitrix\Main\Loader::includeModule('currency')) { CJSCore::Init(['currency']); } ```

| Функция | Описание | С версии | | --- | --- | --- | | BX.Currency.clean | Стирает форматы всех валют. | | | BX.Currency.clearCurrency | Удаляет формат (если он есть). | | | BX.Currency.currencyFormat | Форматирует цену. | | | BX.Currency.getCurrencyFormat | Возвращает формат валюты. | | | BX.Currency.loadCurrencyFormat | Асинхронная загрузка формата. | 19.0.100 | | BX.Currency.setCurrencies | Задаёт форматы нескольких валют сразу. | | | BX.Currency.setCurrencyFormat | Задаёт формат конкретной валюты. | |

---
### Форматирование цены

``` <script type="text/javascript"> var price = 141.56, currency = 'USD'; item.innerHTML = BX.Currency.currencyFormat(price, currency, true); // вставка отформатированной цены с применением шаблона вывода item2.innerHTML = BX.Currency.currencyFormat(price, currency, false); // вставка отформатированной величины цены без использования шаблона </script> /* Результат item содержит строку $141.56 item2 содержит строку 141.56 (без символа валюты и всего остального, находящегося в шаблоне) */ ```

Перед вызовом форматирования необходимо либо явно задать форматы требуемых валют:

``` <? $currencies = []; // загружаем все валюты, какие есть $currencyIterator = \Bitrix\Currency\CurrencyTable::getList([ 'select' => ['CURRENCY'] ]); while ($currency = $currencyIterator->fetch()) { $currencyFormat = \CCurrencyLang::GetFormatDescription($currency['CURRENCY']); $currencies[] = [ 'CURRENCY' => $currency['CURRENCY'], 'FORMAT' => [ 'FORMAT_STRING' => $currencyFormat['FORMAT_STRING'], 'DEC_POINT' => $currencyFormat['DEC_POINT'], 'THOUSANDS_SEP' => $currencyFormat['THOUSANDS_SEP'], 'DECIMALS' => $currencyFormat['DECIMALS'], 'THOUSANDS_VARIANT' => $currencyFormat['THOUSANDS_VARIANT'], 'HIDE_ZERO' => $currencyFormat['HIDE_ZERO'] ] ]; } ?> <script type="text/javascript"> BX.Currency.setCurrencies(<?=CUtil::PhpToJSObject($currencies, false, true, true);?>); </script> ```

либо асинхронно загрузить их (**currency 19.0.100** и выше ):

``` <script type="text/javascript"> BX.Currency.loadCurrencyFormat('USD').then(function() { item.innerHTML = BX.Currency.currencyFormat(123, 'USD', true); }); </script> ```

При использовании второго способа вы должны сами контролировать процесс загрузки и не использовать метод форматирования до успешной подгрузки данных.

Описание формата (поля объекта) почти полностью соответствует данным, возвращаемым методом CCurrencyLang::GetFormatDescription (нет ключа THOUSANDS_VARIANT).

---
