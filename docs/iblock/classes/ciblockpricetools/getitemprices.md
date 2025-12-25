# GetItemPrices


### Описание и параметры


```
array CIBlockPriceTools::GetItemPrices(
	int IBLOCK_ID,
	array arCatalogPrices,
	array arItem,
	bool bVATInclude = true,
	array arCurrencyParams = array(),
	int USER_ID = 0,
	string LID = SITE_ID
)
```

Метод возвращает рассчитанные с учетом скидок (если это торговый каталог) цены для элемента. Метод статический.


#### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| IBLOCK_ID | Идентификатор инфоблока элемента. В действительности в коде сейчас не используется. |  |
| arCatalogPrices | Массив с данными, зависящий от редакции продукта: - если редакция с модулем **Торговый каталог**, то это массив типов цен, которые вернул метод [CIBlockPriceTools::GetCatalogPrices](getcatalogprices.md). - если редакция без модуля **Торговый каталог**, то это массив свойств, которые вернул метод [CIBlockPriceTools::GetCatalogPrices](getcatalogprices.md). |  |
| arItem | Элемент инфоблока, который был получен с помощью [CIBlockElement::GetList](../ciblockelement/getlist.md): - для редакций с модулем **Торговый каталог** в элементе должны присутствовать данные по ценам. - для редакций без модуля **Торговый каталог** - свойства типа **Число**, упомянутые в [CIBlockPriceTools::GetCatalogPrices](getcatalogprices.md). |  |
| bVATInclude | (*true/false*) Флаг определяет включать ли НДС в цену, если он не был включен. | 7.0.0 |
| arCurrencyParams | Массив параметров, отвечающий за конвертацию цен в одну валюту. | 11.5.1 |
| USER_ID | Идентификатор пользователя (если отсутствует или равен нулю, то группы берутся для текущего пользователя, а если задан, то рассчитываются для этого конкретного пользователя). Параметр влияет на выборку скидок. Необязательный. | 12.0.0 |
| LID | Идентификатор сайта, для которого ведутся расчеты (если не задан, то берется текущий сайт). Параметр влияет на выборку скидок. Необязательный. | 12.0.0 |

---
### Возвращаемое значение

Возвращает массив. В случае ошибки или отсутствия доступных типов цен (ни купить, ни посмотреть либо сами цены не заданы) массив будет пустым. В случае успешного выполнения вернется массив следующей структуры:


1. Для редакций с модулем **Торговый каталог**: Ключ - код типа цены. Значение - массив с полями: - **ID** - идентификатор ценового предложения; - **PRICE_ID** - идентификатор типа цены; - **CAN_ACCESS** - (*true/false*) флаг определяющий возможность просмотра цены этого типа; - **CAN_BUY** - (*true/false*) флаг определяющий возможность покупки по цене этого типа; - **MIN_PRICE** - (*Y/N*) значение *Y* задается для наименьшей из цен, которые можно хотя бы смотреть; - **VALUE_NOVAT** - значение цены без НДС; - **PRINT_VALUE_NOVAT** - отформатированное значение цены без НДС; - **VALUE_VAT** - цена с НДС; - **PRINT_VALUE_VAT** - отформатированная цена с НДС; - **VATRATE_VALUE** - абсолютная величина НДС (не проценты); - **PRINT_VATRATE_VALUE** - отформатированная абс. величина НДС; - **DISCOUNT_VALUE_NOVAT** - цена со скидкой без НДС; - **PRINT_DISCOUNT_VALUE_NOVAT** - отформатированная цена со скидкой без НДС; - **DISCOUNT_VALUE_VAT** - НДС скидки; - **PRINT_DISCOUNT_VALUE_VAT** - отформатированный НДС скидки; - **DISCOUNT_VATRATE_VALUE** - цена со скидкой с НДС; - **PRINT_DISCOUNT_VATRATE_VALUE** - отформатированная цена со скидкой с НДС; - **CURRENCY** - код валюты; - следующие параметры зависят от значения параметра *$bVATInclude*. Если он принимает значение *true*, то в них копируются данные с включенным НДС, если нет - без НДС: - **VALUE** - цена для вывода; - **PRINT_VALUE** - отформатированная цена для вывода; - **DISCOUNT_VALUE** - цена со скидкой; - **PRINT_DISCOUNT_VALUE** - отформатированная цена со скидкой; - **DISCOUNT_DIFF** - величина скидки; - **DISCOUNT_DIFF_PERCENT** - процент скидки с округлением до целого - **PRINT_DISCOUNT_DIFF** - отформатированная величина скидки; - в случае, когда включено приведение к одной валюте и исходная валюта не равна той, в которую надо сконвертировать, появляются ключи с префиксом **ORIG_**. Такие ключи содержат исходные данные.
2. Для редакций без модуля **Торговый каталог** конвертация валют и НДС не используются: Ключ - символьный код свойства. Значение - массив с полями: - **CURRENCY** - берется из **DESCRIPTION** (описания) значения свойства; - **CAN_ACCESS** - всегда *true*; - **CAN_BUY** - всегда *false*; - **PRICE_ID** - идентификатор свойства; - **ID** - идентификатор значения свойства; - **VALUE** - значение свойства; - **PRINT_VALUE** - значение свойства и значение описания (типа валюта); - **DISCOUNT_VALUE** - всегда *VALUE*; - **PRINT_DISCOUNT_VALUE** - всегда *PRINT_VALUE*; - **MIN_PRICE** - Y для минимального из значений свойств; - **DISCOUNT_DIFF_PERCENT** - всегда *0*; - **DISCOUNT_DIFF** - всегда *0*; - **PRINT_DISCOUNT_DIFF** - всегда *0* и описание значения (типа валюта).

---




| ![](../images/61ce4f0c4d.png) 3 **Роман Грачев**18.05.2017 08:10:57 |  |  |
| --- | --- | --- |
| Перед тем как отправлять в параметр arItem полученый нами массив (через гетлист), необходимо добавить фильтр в наш гетлист: \| Код \| \| --- \| \| ``` $arResult["PRICES"] = CIBlockPriceTools::GetCatalogPrices($arParams["IBLOCK_ID"], $arParams["PRICE_CODE"]); foreach($arResult["PRICES"] as &$value) { if (!$value['CAN_VIEW'] && !$value['CAN_BUY']) continue; $arSelect[] = $value["SELECT"]; $arFilter["CATALOG_SHOP_QUANTITY_".$value["ID"]] = $arParams["SHOW_PRICE_COUNT"]; } if (isset($value)) unset($value); ``` \| | Код | ``` $arResult["PRICES"] = CIBlockPriceTools::GetCatalogPrices($arParams["IBLOCK_ID"], $arParams["PRICE_CODE"]); foreach($arResult["PRICES"] as &$value) { if (!$value['CAN_VIEW'] && !$value['CAN_BUY']) continue; $arSelect[] = $value["SELECT"]; $arFilter["CATALOG_SHOP_QUANTITY_".$value["ID"]] = $arParams["SHOW_PRICE_COUNT"]; } if (isset($value)) unset($value); ``` |
| Код |  |  |
| ``` $arResult["PRICES"] = CIBlockPriceTools::GetCatalogPrices($arParams["IBLOCK_ID"], $arParams["PRICE_CODE"]); foreach($arResult["PRICES"] as &$value) { if (!$value['CAN_VIEW'] && !$value['CAN_BUY']) continue; $arSelect[] = $value["SELECT"]; $arFilter["CATALOG_SHOP_QUANTITY_".$value["ID"]] = $arParams["SHOW_PRICE_COUNT"]; } if (isset($value)) unset($value); ``` |  |  |
|  |  |  |
