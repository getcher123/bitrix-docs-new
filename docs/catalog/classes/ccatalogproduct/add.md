# Add


### Описание и параметры


```
bool
CCatalogProduct::Add(
	array arFields,
	boolean boolCheck = true
);
```

Метод добавляет (или обновляет) параметры товара к элементу каталога. Нестатический метод.

Метод устарел, вместо него используйте `\Bitrix\Catalog\Model\Product::add`.


#### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| arFields | Ассоциативный массив, ключами которого являются названия параметров товара, а значениями - новые значения параметров. Допустимые ключи: ключи, независящие от вида товаров: - **ID** - код товара (элемента каталога - обязательный); - **AVAILABLE** - доступность товара к покупке (Y/N, поле обновляется автоматически); - **TYPE** - тип товара (значения по умолчанию зависят от вида торгового каталога); ключи для обычных товаров и торговых предложений: - **VAT_ID** - код НДС; - **VAT_INCLUDED** - флаг (Y/N) включен ли НДС в цену; - **QUANTITY** - количество товара на складе; - **QUANTITY_RESERVED** - зарезервированное количество; - **QUANTITY_TRACE** - флаг (Y/N/D)***** "включить количественный учет" (до версии 12.5.0 параметр назывался "уменьшать ли количество при заказе"); - **CAN_BUY_ZERO** - флаг (Y/N/D)***** "разрешить покупку при отсутствии товара"; - **SUBSCRIBE** - флаг (Y/N/D)***** "разрешить подписку при отсутствии товара"; **BUNDLE**- признак наличия набора (Y/N, поле обновляется автоматически); - **PURCHASING_PRICE** - закупочная цена. При указании в массиве этого ключа необходимо обязательно указать и валюту PURCHASING_CURRENCY, иначе метод возвратит *false*. - **PURCHASING_CURRENCY** - валюта закупочной цены; - **WEIGHT** - вес единицы товара; - **WIDTH** - ширина товара (в мм); - **LENGTH** - длина товара (в мм); - **HEIGHT** - высота товара (в мм); - **MEASURE** - ID единицы измерения; - **BARCODE_MULTI** - (Y/N) определяет каждый ли экземпляр товара имеет собственный штрихкод; ключи для продажи контента: - **PRICE_TYPE** - тип цены (S - одноразовый платеж, R - регулярные платежи, T - пробная подписка); - **RECUR_SCHEME_TYPE** - тип периода подписки ("H" - час, "D" - сутки, "W" - неделя, "M" - месяц, "Q" - квартал, "S" - полугодие, "Y" - год); - **RECUR_SCHEME_LENGTH** - длина периода подписки; - **TRIAL_PRICE_ID** - код товара, для которого данный товар является пробным; - **WITHOUT_ORDER** - флаг "Продление подписки без оформления заказа". |  |
| boolCheck | Параметр, указывающий, проверять ли наличие в базе информации о товаре или нет, перед добавлением. По умолчанию - проверять. | 11.0.5 |
| ***D** - значение берется из настроек модуля. |  |  |


#### Возвращаемые значения

Возвращает *true* в случае успешного обновления параметров и *false* в противном случае.


---
### Типы товаров


| Основные | Описание | С версии |
| --- | --- | --- |
| \Bitrix\Catalog\ProductTable::TYPE_PRODUCT | Простой товар | 14.0.0 |
| \Bitrix\Catalog\ProductTable::TYPE_SET | Комплект | 14.0.0 |
| \Bitrix\Catalog\ProductTable::TYPE_SKU | Товар с торговыми предложениями | 16.0.3 |
| \Bitrix\Catalog\ProductTable::TYPE_OFFER | Торговое предложение | 16.0.3 |


| Дополнительные | Описание | С версии |
| --- | --- | --- |
| \Bitrix\Catalog\ProductTable::TYPE_FREE_OFFER | Торговое предложение, у которого нет товара (не указан или удален). | 16.0.3 |
| \Bitrix\Catalog\ProductTable::TYPE_EMPTY_SKU | Специфический тип, означает невалидный товар с торговыми предложениями. | 16.0.3 |


| Добавляемые в корзину | Описание | С версии |
| --- | --- | --- |
| \Bitrix\Catalog\ProductTable::TYPE_PRODUCT | Простой товар | 14.0.0 |
| \Bitrix\Catalog\ProductTable::TYPE_SET | Комплект | 14.0.0 |
| \Bitrix\Catalog\ProductTable::TYPE_OFFER | Торговое предложение | 16.0.3 |


---
### Примеры использования


```
$arFields = array(
	"ID" => $PRODUCT_ID,
	"VAT_ID" => 1, //выставляем тип ндс (задается в админке)
	"VAT_INCLUDED" => "Y" //НДС входит в стоимость
);
if(CCatalogProduct::Add($arFields))
	echo "Добавили параметры товара к элементу каталога ".$PRODUCT_ID.'<br>';
else
	echo 'Ошибка добавления параметров<br>';
```

---



| ![](../images/2068d63a6f.jpg) 3 **Алексей Попович**23.12.2019 13:21:23 |  |  |
| --- | --- | --- |
| Для обновления остатков лучше воспользоваться конструкцией: \| Код \| \| --- \| \| ``` $existProduct = \Bitrix\Catalog\Model\Product::getCacheItem($arFields['ID'],true); if(!empty($existProduct)){ \Bitrix\Catalog\Model\Product::update(intval($arFields['ID']),$arFields); } else { \Bitrix\Catalog\Model\Product::add($arFields); } ``` \| Функция \Bitrix\Catalog\Model\Product::add не проверяет наличие товара, поэтому нужно проверять самостоятельно. | Код | ``` $existProduct = \Bitrix\Catalog\Model\Product::getCacheItem($arFields['ID'],true); if(!empty($existProduct)){ \Bitrix\Catalog\Model\Product::update(intval($arFields['ID']),$arFields); } else { \Bitrix\Catalog\Model\Product::add($arFields); } ``` |
| Код |  |  |
| ``` $existProduct = \Bitrix\Catalog\Model\Product::getCacheItem($arFields['ID'],true); if(!empty($existProduct)){ \Bitrix\Catalog\Model\Product::update(intval($arFields['ID']),$arFields); } else { \Bitrix\Catalog\Model\Product::add($arFields); } ``` |  |  |
|  |  |  |
