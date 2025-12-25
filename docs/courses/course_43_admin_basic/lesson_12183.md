# Товары и CIBlockElement::GetList

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11985 — Использование ES6](lesson_11985.md)
- [Следующий: 7350 — Пользовательские типы свойств заказа →](lesson_7350.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=12183

### CIBlockElement::GetList

Как вы знаете, метод [CIBlockElement::GetList](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/getlist.php) модуля **Информационные блоки** может работать с данными товара (при наличии модуля **Торговый каталог**). Это подробно описано в [документации](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/getlist.php) и активно используется как в публичных компонентах, так и на административных страницах и скриптах. Однако архитектурные особенности реализации, равно как и неправильное использование этих возможностей, приводят к резкому падению производительности.

Давайте сделаем разные вызовы *CIBlockElement::GetList* и посмотрим, какие запросы будут выполнены в итоге.

1. Сначала сделаем простую выборку товаров из инфоблока с ID = 2:
  ```
  $iterator = \CIBlockElement::GetList(
  	array(),
  	array('IBLOCK_ID' => 2),
  	false,
  	false,
  	array('ID', 'NAME', 'IBLOCK_ID')
  );
  ```
  Запрос, который пойдет в базу:
  ```
  SELECT  BE.ID as ID,BE.NAME as NAME,BE.IBLOCK_ID as IBLOCK_ID
  FROM b_iblock B
  INNER JOIN b_lang L ON B.LID=L.LID
  INNER JOIN b_iblock_element BE ON BE.IBLOCK_ID = B.ID
  WHERE 1=1
  	AND (
  		((((BE.IBLOCK_ID = '2'))))
  	)
  	AND (((BE.WF_STATUS_ID=1 AND BE.WF_PARENT_ELEMENT_ID IS NULL)))
  ```
2. Теперь в выборку добавим фильтрацию по доступности товара:
  ```
  $iterator = \CIBlockElement::GetList(
  	array(),
  	array('IBLOCK_ID' => 2, 'CATALOG_AVAILABLE' => 'Y'),
  	false,
  	false,
  	array('ID', 'NAME', 'IBLOCK_ID')
  );
  ```
  Это приводит к запросу:
  ```
  SELECT  BE.ID as ID,BE.NAME as NAME,BE.IBLOCK_ID as IBLOCK_ID ,CAT_PR.QUANTITY as CATALOG_QUANTITY,
  IF (CAT_PR.QUANTITY_TRACE = 'D', 'Y', CAT_PR.QUANTITY_TRACE) as CATALOG_QUANTITY_TRACE,
  CAT_PR.QUANTITY_TRACE as CATALOG_QUANTITY_TRACE_ORIG, CAT_PR.WEIGHT as CATALOG_WEIGHT,
  CAT_PR.VAT_ID as CATALOG_VAT_ID, CAT_PR.VAT_INCLUDED as CATALOG_VAT_INCLUDED,
  IF (CAT_PR.CAN_BUY_ZERO = 'D', 'N', CAT_PR.CAN_BUY_ZERO) as CATALOG_CAN_BUY_ZERO,
  CAT_PR.CAN_BUY_ZERO as CATALOG_CAN_BUY_ZERO_ORIG,
  CAT_PR.PURCHASING_PRICE as CATALOG_PURCHASING_PRICE, CAT_PR.PURCHASING_CURRENCY as CATALOG_PURCHASING_CURRENCY,
  CAT_PR.QUANTITY_RESERVED as CATALOG_QUANTITY_RESERVED,
  IF (CAT_PR.SUBSCRIBE = 'D', 'Y', CAT_PR.SUBSCRIBE) as CATALOG_SUBSCRIBE, CAT_PR.SUBSCRIBE as CATALOG_SUBSCRIBE_ORIG,
  CAT_PR.WIDTH as CATALOG_WIDTH, CAT_PR.LENGTH as CATALOG_LENGTH, CAT_PR.HEIGHT as CATALOG_HEIGHT,
  CAT_PR.MEASURE as CATALOG_MEASURE, CAT_PR.TYPE as CATALOG_TYPE, CAT_PR.AVAILABLE as CATALOG_AVAILABLE,
  CAT_PR.BUNDLE as CATALOG_BUNDLE, CAT_PR.PRICE_TYPE as CATALOG_PRICE_TYPE,
  CAT_PR.RECUR_SCHEME_LENGTH as CATALOG_RECUR_SCHEME_LENGTH, CAT_PR.RECUR_SCHEME_TYPE as CATALOG_RECUR_SCHEME_TYPE,
  CAT_PR.TRIAL_PRICE_ID as CATALOG_TRIAL_PRICE_ID, CAT_PR.WITHOUT_ORDER as CATALOG_WITHOUT_ORDER,
  CAT_PR.SELECT_BEST_PRICE as CATALOG_SELECT_BEST_PRICE,
  IF (CAT_PR.NEGATIVE_AMOUNT_TRACE = 'D', 'N', CAT_PR.NEGATIVE_AMOUNT_TRACE) as CATALOG_NEGATIVE_AMOUNT_TRACE,
  CAT_PR.NEGATIVE_AMOUNT_TRACE as CATALOG_NEGATIVE_AMOUNT_TRACE_ORIG, CAT_VAT.RATE as CATALOG_VAT
  	FROM b_iblock B
  	INNER JOIN b_lang L ON B.LID=L.LID
  	INNER JOIN b_iblock_element BE ON BE.IBLOCK_ID = B.ID
  	left join b_catalog_product as CAT_PR on (CAT_PR.ID = BE.ID)
  	left join b_catalog_iblock as CAT_IB on ((CAT_PR.VAT_ID IS NULL or CAT_PR.VAT_ID = 0) and CAT_IB.IBLOCK_ID = BE.IBLOCK_ID)
  	left join b_catalog_vat as CAT_VAT on
  		(CAT_VAT.ID = IF((CAT_PR.VAT_ID IS NULL OR CAT_PR.VAT_ID = 0), CAT_IB.VAT_ID, CAT_PR.VAT_ID))
  	WHERE 1=1
  	AND (
  		((((BE.IBLOCK_ID = '2'))))
  		AND ((((CAT_PR.AVAILABLE='Y'))))
  	)
  	AND (((BE.WF_STATUS_ID=1 AND BE.WF_PARENT_ELEMENT_ID IS NULL)))
  ```
  Таким образом, любое обращение к данным товара (фильтрация, сортировка, выборка одного из полей) приводит к join трех таблиц и выборке всех полей товара.
3. Уберем фильтрацию, но будем выбирать цену одного из типов (ID типа цены - 1):
  ```
  $iterator = \CIBlockElement::GetList(
  	array(),
  	array('IBLOCK_ID' => 2),
  	false,
  	false,
  	array('ID', 'NAME', 'IBLOCK_ID', 'CATALOG_CATALOG_GROUP_ID_1')
  );
  ```
  Видим, что стало еще хуже:
  ```
  SELECT BE.ID as ID,BE.NAME as NAME,BE.IBLOCK_ID as IBLOCK_ID,
  CAT_P1.CATALOG_GROUP_ID as CATALOG_GROUP_ID_1, CAT_P1.ID as CATALOG_PRICE_ID_1,
  CAT_P1.PRICE as CATALOG_PRICE_1, CAT_P1.CURRENCY as CATALOG_CURRENCY_1,
  CAT_P1.QUANTITY_FROM as CATALOG_QUANTITY_FROM_1, CAT_P1.QUANTITY_TO as CATALOG_QUANTITY_TO_1,
  CAT_P1.EXTRA_ID as CATALOG_EXTRA_ID_1,
  'Базовая цена' as CATALOG_GROUP_NAME_1, 'Y' as CATALOG_CAN_ACCESS_1, 'Y' as CATALOG_CAN_BUY_1,
  CAT_PR.QUANTITY as CATALOG_QUANTITY, IF (CAT_PR.QUANTITY_TRACE = 'D', 'Y', CAT_PR.QUANTITY_TRACE) as CATALOG_QUANTITY_TRACE,
  CAT_PR.QUANTITY_TRACE as CATALOG_QUANTITY_TRACE_ORIG, CAT_PR.WEIGHT as CATALOG_WEIGHT,
  CAT_PR.VAT_ID as CATALOG_VAT_ID, CAT_PR.VAT_INCLUDED as CATALOG_VAT_INCLUDED,
  IF (CAT_PR.CAN_BUY_ZERO = 'D', 'N', CAT_PR.CAN_BUY_ZERO) as CATALOG_CAN_BUY_ZERO,
  CAT_PR.CAN_BUY_ZERO as CATALOG_CAN_BUY_ZERO_ORIG, CAT_PR.PURCHASING_PRICE as CATALOG_PURCHASING_PRICE,
  CAT_PR.PURCHASING_CURRENCY as CATALOG_PURCHASING_CURRENCY, CAT_PR.QUANTITY_RESERVED as CATALOG_QUANTITY_RESERVED,
  IF (CAT_PR.SUBSCRIBE = 'D', 'Y', CAT_PR.SUBSCRIBE) as CATALOG_SUBSCRIBE, CAT_PR.SUBSCRIBE as CATALOG_SUBSCRIBE_ORIG,
  CAT_PR.WIDTH as CATALOG_WIDTH, CAT_PR.LENGTH as CATALOG_LENGTH, CAT_PR.HEIGHT as CATALOG_HEIGHT,
  CAT_PR.MEASURE as CATALOG_MEASURE, CAT_PR.TYPE as CATALOG_TYPE, CAT_PR.AVAILABLE as CATALOG_AVAILABLE,
  CAT_PR.BUNDLE as CATALOG_BUNDLE, CAT_PR.PRICE_TYPE as CATALOG_PRICE_TYPE,
  CAT_PR.RECUR_SCHEME_LENGTH as CATALOG_RECUR_SCHEME_LENGTH, CAT_PR.RECUR_SCHEME_TYPE as CATALOG_RECUR_SCHEME_TYPE,
  CAT_PR.TRIAL_PRICE_ID as CATALOG_TRIAL_PRICE_ID, CAT_PR.WITHOUT_ORDER as CATALOG_WITHOUT_ORDER,
  CAT_PR.SELECT_BEST_PRICE as CATALOG_SELECT_BEST_PRICE,
  IF (CAT_PR.NEGATIVE_AMOUNT_TRACE = 'D', 'N', CAT_PR.NEGATIVE_AMOUNT_TRACE) as CATALOG_NEGATIVE_AMOUNT_TRACE,
  CAT_PR.NEGATIVE_AMOUNT_TRACE as CATALOG_NEGATIVE_AMOUNT_TRACE_ORIG, CAT_VAT.RATE as CATALOG_VAT
  FR OM b_iblock B
  INNER JOIN b_lang L ON B.LID=L.LID
  INNER JOIN b_iblock_element BE ON BE.IBLOCK_ID = B.ID
  left join b_catalog_price as CAT_P1 on (CAT_P1.PRODUCT_ID = BE.ID and CAT_P1.CATALOG_GROUP_ID = 1)
  left join b_catalog_product as CAT_PR on (CAT_PR.ID = BE.ID)
  left join b_catalog_iblock as CAT_IB on ((CAT_PR.VAT_ID IS NULL or CAT_PR.VAT_ID = 0) and CAT_IB.IBLOCK_ID = BE.IBLOCK_ID)
  left join b_catalog_vat as CAT_VAT on (CAT_VAT.ID = IF((CAT_PR.VAT_ID IS NULL OR CAT_PR.VAT_ID = 0), CAT_IB.VAT_ID, CAT_PR.VAT_ID))
  WH ERE 1=1
  	AND (
  		((((BE.IBLOCK_ID = '2'))))
  	)
  	AND (((BE.WF_STATUS_ID=1 AND BE.WF_PARENT_ELEMENT_ID IS NULL)))
  ```
  Если мы попробуем выбрать еще и данные по складам, то ситуация будет аналогичной.

Подведем промежуточные итоги:



- Выборки цен, количества на складах в *CIBlockElement::GetList* необходимо избегать категорически (особенно при наличии сортировки и неважно по каким полям). Эти данные нужно получать отдельными вызовами АПИ. К слову сказать, в штатных компонентах это было сделано еще в версии 17.0.
- Остается фильтрация и сортировка по полям товара, ценам, складам. Обращение к полям товара по ключам **CATALOG_** дает дополнительный join трех таблиц. Обращение к N типам цен или складов - join N+3 таблиц. Мало того, что время запроса увеличивается, так еще можно получить ошибку MySql *"Too many tables; MySQL can only use 61 tables in a join"*.

До выпуска связки обновлений catalog 18.6.100 + iblock 18.6.200 все вышеописанное относится, в том числе, к штатным компонентам и административным спискам модуля **Информационные блоки** (особенно в режиме совместного просмотра элементов и разделов, смотрите примечание ниже). После выхода данных обновлений в *CIBlockElement::GetList* доступны новые возможности работы с товарами.

**Примечание:** ранее для всех больших инфоблоков мы рекомендовали не использовать режим совместного просмотра по причине большого расхода памяти. С выходом версии 18.5.5 модуля **Информационные блоки** эта проблема решена - инфоблок со 100 тысячами элементов спокойно выводится в административном разделе в этом режиме (расход памяти снижен примерно в 20 раз).

### С версий catalog 18.6.100 + iblock 18.6.200

С версии iblock 18.6.200 изменяются ключи метода. По всем ключам возможна фильтрация, сортировка, выборка.

## Поля товара

| \| **Ключ** \| **Описание** \|<br>\| --- \| --- \|<br>\| TYPE \| Тип товара. Значения:
<br>
<br>- 1 - Простой товар<br>- 2 - Комплект<br>- 3 - Товар с предложением<br>- 4 - Предложение \|<br>\| AVAILABLE \| Доступность. \|<br>\| BUNDLE \| Наличие набора. \|<br>\| QUANTITY \| Доступное количество. \|<br>\| QUANTITY_RESERVED \| Зарезервированное количество. \|<br>\| QUANTITY_TRACE \| Включен количественный учет (с учетом значения "по умолчанию" в настройках модуля) - Y/N. \|<br>\| QUANTITY_TRACE_RAW \| Включен количественный учет (необработанное значение) - Y/N/D. \|<br>\| CAN_BUY_ZERO \| Разрешена покупка «в минус» (с учетом значения "по умолчанию" в настройках модуля) - Y/N. \|<br>\| CAN_BUY_ZERO_RAW \| Разрешена покупка «в минус» (необработанное значение) - Y/N/D. \|<br>\| SUBSCRIBE \| Разрешена подписка на уведомления о поступлении товара (с учетом значения "по умолчанию" в настройках модуля) - Y/N. \|<br>\| SUBSCRIBE_RAW \| Разрешена подписка на уведомления о поступлении товара (необработанное значение) - Y/N/D. \|<br>\| VAT_ID \| Идентификатор НДС товара. \|<br>\| VAT_INCLUDED \| Признак «НДС включен в цену». \|<br>\| PURCHASING_PRICE \| Закупочная цена. \|<br>\| PURCHASING_CURRENCY \| Валюта закупочной цены. \|<br>\| BARCODE_MULTI \| Множественность штрихкодов. \|<br>\| WEIGHT \| Вес. \|<br>\| WIDTH \| Ширина. \|<br>\| LENGTH \| Длина. \|<br>\| HEIGHT \| Высота. \|<br>\| MEASURE \| Идентификатор единицы измерения. \|<br>\| PAYMENT_TYPE \| Для продажи подписки. \|<br>\| RECUR_SCHEME_LENGTH \| Для продажи подписки. \|<br>\| RECUR_SCHEME_TYPE \| Для продажи подписки. \|<br>\| TRIAL_PRICE_ID \| Для продажи подписки. \|<br>\| WITHOUT_ORDER \| Для продажи подписки. \| |
| --- |

## С версии catalog 20.0.200 добавились поля товара

| \| **Ключ** \| **Описание** \|<br>\| --- \| --- \|<br>\| PRODUCT_BARCODE \| Штрихкод. \|<br>\| PRODUCT_BARCODE_STORE \| Привязка штрихкода к складу. \|<br>\| PRODUCT_BARCODE_ORDER \| Привязка штрихкода к заказу. \| |
| --- |

Теперь вызов метода с фильтрацией по доступности выглядит так:

```

$iterator = \CIBlockElement::GetList(
	array(),
	array('IBLOCK_ID' => 2, '=AVAILABLE' => 'Y'),
	false,
	false,
	array('ID', 'NAME', 'IBLOCK_ID')
);
```

а в запросе только то, что просили, и join только один:

```

SELECT  BE.ID as ID,BE.NAME as NAME,BE.IBLOCK_ID as IBLOCK_ID

FROM b_iblock B
INNER JOIN b_lang L ON B.LID=L.LID
INNER JOIN b_iblock_element BE ON BE.IBLOCK_ID = B.ID
left join b_catalog_product as PRD on (PRD.ID = BE.ID)

	WHERE 1=1
AND (
	((((BE.IBLOCK_ID = '2'))))
	AND ((((PRD.AVAILABLE='Y'))))
)
AND (((BE.WF_STATUS_ID=1 AND BE.WF_PARENT_ELEMENT_ID IS NULL)))
```

Сделаем выборку размеров и веса доступных простых товаров:

```

$iterator = \CIBlockElement::GetList(
	array(),
	array('IBLOCK_ID' => 2, '=AVAILABLE' => 'Y', '=TYPE' => 1),
	false,
	false,
	array('ID', 'NAME', 'IBLOCK_ID', 'WEIGHT', 'WIDTH', 'HEIGHT', 'LENGTH')
);
```

Запрос получается следующим:

```

SELECT  BE.ID as ID,BE.NAME as NAME,BE.IBLOCK_ID as IBLOCK_ID ,
PRD.WEIGHT as WEIGHT, PRD.WIDTH as WIDTH, PRD.HEIGHT as HEIGHT, PRD.LENGTH as LENGTH

FROM b_iblock B
INNER JOIN b_lang L ON B.LID=L.LID
INNER JOIN b_iblock_element BE ON BE.IBLOCK_ID = B.ID
left join b_catalog_product as PRD on (PRD.ID = BE.ID)

WHERE 1=1
AND (
	((((BE.IBLOCK_ID = '2'))))
	AND ((((PRD.AVAILABLE='Y'))))
	AND ((((PRD.TYPE = '1'))))
)
AND (((BE.WF_STATUS_ID=1 AND BE.WF_PARENT_ELEMENT_ID IS NULL)))
```

## Поля цен (без привязки к конкретному типу цены)

| \| **Ключ** \| **Описание** \| **Для чего доступен** \|<br>\| --- \| --- \| --- \|<br>\| PRICE_TYPE \| Идентификатор типа цены. \| Фильтр. \|<br>\| PRICE \| Цена. \| Фильтр. \|<br>\| CURRENCY \| Валюта. \| Фильтр. \|<br>\| QUANTITY_TO \| Минимальное количество товара. \| Фильтр. \|<br>\| QUANTITY_FROM \| Максимальное количество товара. \| Фильтр. \|<br>\| EXTRA_ID \| Идентификатор наценки. \| Фильтр. \|<br>\| SCALED_PRICE \| Цена в базовой валюте. \| Фильтр. \|<br>\| QUANTITY_RANGE_FILTER \| Количество товара, для которого искать цены. \| Только фильтр, вспомогательное. \|<br>\| CURRENCY_FOR_SCALE \| Фильтрация по цене с указанием валюты (т.е. когда необходимо отфильтровать цены в любых валютах с учетом курса). \| Только фильтр, вспомогательное. \| |
| --- |

## Поля цен (с указанием типа цены)

| \| **Ключ** \| **Описание** \| **Для чего доступен** \|<br>\| --- \| --- \| --- \|<br>\| PRICE_ИДцены \| Цена. \| Фильтр, сортировка, выборка. \|<br>\| CURRENCY_ИДцены \| Валюта. \| Фильтр, сортировка, выборка. \|<br>\| QUANTITY_TO_ИДцены \| Минимальное количество товара. \| Фильтр, сортировка, выборка. \|<br>\| QUANTITY_FROM_ИДцены \| Максимальное количество товара. \| Фильтр, сортировка, выборка. \|<br>\| EXTRA_ID_ИДцены \| Идентификатор наценки. \| Фильтр, сортировка, выборка. \|<br>\| SCALED_PRICE_ИДцены \| Цена в базовой валюте. \| Фильтр, сортировка, выборка. \|<br>\| QUANTITY_RANGE_FILTER_ИДцены \| Количество товара, для которого искать цены. \| Только фильтр, вспомогательное. \|<br>\| CURRENCY_FOR_SCALE_ИДцены \| Фильтрация по цене с указанием валюты (т.е. когда необходимо отфильтровать цены в любых валютах с учетом курса). \| Только фильтр, вспомогательное. \| |
| --- |

## Поля складов

| \| **Ключ** \| **Описание** \|<br>\| --- \| --- \|<br>\| STORE_NUMBER \| Идентификатор склада. \|<br>\| STORE_AMOUNT \| Количество на складе. \|<br>\| STORE_AMOUNT_ИДсклада \| Количество на конкретном складе. \| |
| --- |

### Примеры выборок

Фильтрация по цене любого типа:

```

$iterator = \CIBlockElement::GetList(
	array(),
	array('IBLOCK_ID' => 2, '=AVAILABLE' => 'Y', '=TYPE' => 1, '>PRICE' => 500),
	false,
	false,
	array('ID', 'NAME', 'IBLOCK_ID', 'WEIGHT', 'WIDTH', 'HEIGHT', 'LENGTH')
);
```

Фильтрация для типа цены с кодом 1 (обычно это базовая цена):

```

$iterator = \CIBlockElement::GetList(
	array(),
	array('IBLOCK_ID' => 2, '=AVAILABLE' => 'Y', '=TYPE' => 1, '>PRICE' => 500, '=PRICE_TYPE' => 1),
	false,
	false,
	array('ID', 'NAME', 'IBLOCK_ID', 'WEIGHT', 'WIDTH', 'HEIGHT', 'LENGTH')
);
```

Или в таком варианте:

```

$iterator = \CIBlockElement::GetList(
	array(),
	array('IBLOCK_ID' => 2, '=AVAILABLE' => 'Y', '=TYPE' => 1, '>PRICE_1' => 500),
	false,
	false,
	array('ID', 'NAME', 'IBLOCK_ID', 'WEIGHT', 'WIDTH', 'HEIGHT', 'LENGTH')
);
```

Теперь можно делать фильтры, ранее недоступные. Выбрать все товары, имеющие цены любого типа от 500 до 1000:

```

$iterator = \CIBlockElement::GetList(
	array(),
	array('IBLOCK_ID' => 2, '=AVAILABLE' => 'Y', '=TYPE' => 1, '>=PRICE' => 500, '<=PRICE' => 1000),
	false,
	false,
	array('ID', 'NAME', 'IBLOCK_ID')
);
```

Или только цены типов с кодом 1,4,5:

```

$iterator = \CIBlockElement::GetList(
	array(),
	array('IBLOCK_ID' => 2, '=AVAILABLE' => 'Y', '=TYPE' => 1, '>=PRICE' => 500, '<=PRICE' => 1000, '@PRICE_TYPE' => [1,4,5]),
	false,
	false,
	array('ID', 'NAME', 'IBLOCK_ID')
);
```

Выбрать все товары с ценами в любой валюте, эквивалентными диапазону от 100 до 200 USD:

```

$iterator = \CIBlockElement::GetList(
	array(),
	array('IBLOCK_ID' => 2, '=AVAILABLE' => 'Y', '=TYPE' => 1, '>=PRICE' => 100, '<=PRICE' => 200, 'CURRENCY_FOR_SCALE' => 'USD'),
	false,
	false,
	array('ID', 'NAME', 'IBLOCK_ID')
);
```

Выбрать товары, которых на любом складе не больше 3:

```

$iterator = \CIBlockElement::GetList(
	array(),
	array('IBLOCK_ID' => 2, '<=STORE_AMOUNT' => 3),
	false,
	false,
	array('ID', 'NAME', 'IBLOCK_ID')
);
```

Выбрать товары, которых на 17-м складе от 5 до 7:

```

$iterator = \CIBlockElement::GetList(
	array(),
	array('IBLOCK_ID' => 2, '<=STORE_AMOUNT' => 7, '>=STORE_AMOUNT' => 5, 'STORE_NUMBER' => 17),
	false,
	false,
	array('ID', 'NAME', 'IBLOCK_ID')
);
```

Либо в таком виде:

```

$iterator = \CIBlockElement::GetList(
	array(),
	array('IBLOCK_ID' => 2, '<=STORE_AMOUNT_17' => 7, '>=STORE_AMOUNT_17' => 5),
	false,
	false,
	array('ID', 'NAME', 'IBLOCK_ID')
);
```

Фильтрация товаров по наличию на определенных складах:

```
if(!empty($arParams['STORES'])){
	$GLOBALS[$arParams['FILTER_NAME']]['@STORE_NUMBER'] => $arParams['STORES'];
	$GLOBALS[$arParams['FILTER_NAME']]['>STORE_AMOUNT'] = 0;
}
```

Другой пример фильтрации товаров по наличию на определенных складах:

```
if(!empty($arParams['STORES'])){

	$storesFilter = [
		'LOGIC'=>'OR'
	];
		foreach ($arParams['STORES'] as $store_id){
			$storesFilter[] = ['STORE_NUMBER' => intval($store_id),'>STORE_AMOUNT'=>0];
		}

	$GLOBALS[$arParams['FILTER_NAME']][] = $storesFilter;
}
```

|  | #### Заключение |
| --- | --- |

После установки обновлений catalog 18.6.100 + iblock 18.6.200 настоятельно рекомендуется перевести свои компоненты и скрипты на новые ключи. Увеличение производительности прямо пропорционально числу товаров в каталоге. Так, при тестах на разделе из 1,5 тысяч товаров прирост скорости выполнения составил порядка 30%. Штатные компоненты (

			catalog.section

                     Компонент выводит список элементов раздела с указанным набором свойств.



						[Описание компонента «Элементы раздела» в пользовательской документации.](http://dev.1c-bitrix.ru/user_help/detail.php?ID=62980)

		,

			catalog.element

                    Компонент выводит детальную информацию по элементу каталога.

						[Описание компонента «Элемент каталога детально» в пользовательской документации.](http://dev.1c-bitrix.ru/user_help/detail.php?ID=62981)

		,

			catalog.top

                    Компонент выводит в таблице top элементов из всех разделов в соответствии с заданной сортировкой (используется как правило на главной странице сайта).

						[Описание компонента «top элементов каталога» в пользовательской документации.](http://dev.1c-bitrix.ru/user_help/detail.php?ID=62986)

		), а также все компоненты наследники [\Bitrix\Iblock\Component\Base](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/component/base/index.php) переведены на новые фильтры.
