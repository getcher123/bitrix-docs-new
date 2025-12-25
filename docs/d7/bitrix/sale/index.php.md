# Интернет-магазин

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/sale/index.php

`\Bitrix\Sale` – пространство имен модуля **Интернет-магазин**.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule(
	'sale'
);
```

| Класс, пространство имен | Описание |
| --- | --- |
| [Archive](classes/archive/index.php.md)Класс для работы с архивацией заказов. |  |
| [Basket](classes/basket/index.php.md) | Класс для работы с корзиной. Наследник класса `\Bitrix\Sale\BasketItemCollection`. |
| [BasketBase](classes/basketbase/index.php.md) | Класс для работы с корзиной. |
| [BasketItemCollection](classes/basketitemcollection/index.php.md) | Класс коллекции товарных позиций. |
| [BusinessValue](classes/businessvalue/index.php.md) | Класс для работы с бизнес-смыслами. |
| [Configuration](classes/configuration/index.php.md) | Класс для работы с настройками резервирования товаров, складского учета и настройками смены статусов интернет-магазина. |
| [Delivery](classes/delivery/index.php.md) | Пространство имен, содержащее классы для работы со службами доставок. |
| [Discount](classes/discount/index.php.md) | Пространство имен, содержащее подпространства, классы и методы для расчета всех скидок (каталога и магазина) и округления цен для корзины или заказа. |
| [DiscountCouponsManager](classes/discountcouponsmanager/index.php.md) | Класс для работы с купонами при расчетах. |
| [Fuser](classes/fuser/index.php.md) | Класс для получения идентификатора покупателя. |
| [Internals](classes/internals/index.php.md) | Подпространство, содержащее классы для работы с таблицами модуля **Интернет-магазин**. |
| [Location](classes/location/index.php.md) | Подпространство имен, содержащее классы для работы с местоположениями. |
| [Notify](classes/notify/index.php.md) | Класс для работы с уведомлениями. |
| [Order](classes/order/index.php.md) | Класс для работы с заказами. |
| [OrderBase](classes/orderbase/index.php.md) | Базовый класс для работы с заказами. |
| [OrderDiscountManager](classes/orderdiscountmanager/index.php.md) | Класс для работы с правилами корзины при расчетах. |
| [Payment](classes/payment/index.php.md) | Класс оплаты. |
| [PaymentCollection](classes/paymentcollection/index.php.md) | Класс коллекции оплат. |
| [PropertyValueCollectionBase](classes/propertyvaluecollectionbase/index.php.md) | Базовый класс коллекции свойств заказа. |
| [ProviderBase](classes/providerbase/index.php.md) | Базовый класс для работы с провайдерами магазина. |
| [Result](classes/result/index.php.md) | Класс для работы с результатами. |
| [SalesZone](classes/saleszone/index.php.md) | Класс для задания зоны обслуживания магазином. |
| [Services](classes/services/index.php.md) | Базовая общая часть служб доставок и платежных систем. |
| [Shipment](classes/shipment/index.php.md) | Класс отгрузок. |
| [ShipmentCollection](classes/shipmentcollection/index.php.md) | Класс коллекции отгрузок. |
| [ShipmentItem](classes/shipmentitem/index.php.md) | Класс элемента отгрузки. |
| [ShipmentItemStore](classes/shipmentitemstore/index.php.md) | Класс штрих-кодов элементов отгрузки. |
| [StatusBase](classes/statusbase/index.php.md) | Базовый класс статусов. |
| [Tax](classes/tax/index.php.md) | Класс налогов. |
| [TradingPlatform](classes/tradingplatform/index.php.md) | Класс для работы с торговыми платформами. |
