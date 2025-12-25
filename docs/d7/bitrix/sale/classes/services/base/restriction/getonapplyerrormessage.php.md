# getOnApplyErrorMessage

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/sale/classes/services/base/restriction/getonapplyerrormessage.php

```
public static function \Bitrix\Sale\Services\Base\Restriction::getOnApplyErrorMessage(
);
```

Метод возвращает строку с текстом ошибки. Метод вызывается, если при применении ограничения (вызова метода *save* у класса ограничения) возникла ошибка.

Текст ошибки в зависимости от места может отображаться по-разному. Допустим, если в публичной части сайта при добавлении платёжной системы произошла ошибка применения стандартного ограничения, то на странице высветится красный текст, полученный из этого метода.

#### Параметры

Без параметров.
