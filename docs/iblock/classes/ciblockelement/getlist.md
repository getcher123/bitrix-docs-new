# GetList


### Описание


```
CIBlockResult
CIBlockElement::GetList(
	array arOrder = Array("SORT"=>"ASC"),
	array arFilter = Array(),
	mixed arGroupBy = false,
	mixed arNavStartParams = false,
	array arSelectFields = Array()
);
```

Возвращает список элементов по фильтру *arFilter*. Метод статический.


**Важно!** Начиная с версии **18.6.200** модуля **Информационные блоки**, в методе доступны новые возможности работы с товарами, изменены ключи метода. Читайте подробности в уроке **Товары и CIBlockElement::GetList**. Соответственно, все параметры вида `CATALOG_***` устарели.


**Внимание:** Начиная с версии **20.5.0** модуля **Информационные блоки** в методе более не обрабатываются ключи **CHECK_BP_TASKS_PERMISSIONS** и **TASKSTATUS**.

Поля, перечисленные для сортировки, будут автоматически добавлены в параметр `arSelectFields`или в `arGroupBy`, если указана группировка записей. -<ol> <li>Внутренние ограничения Oracle и MSSQL не позволяют использовать DISTINCT при фильтрации по полям типа blob, поэтому фильтрация по нескольким значениям множественного свойства может дать дублирование. </li> <li> </li> </ol>-


#### Смотрите также

[CDBResult](../../../main/reference/cdbresult/index.md)[Поля элементов](../../fields.md#felement)---
### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| arOrder | Массив вида Array(*by1*=>*order1*[, *by2*=>*order2* [, ..]]), где *by* - поле для сортировки, может принимать значения: - **id** - ID элемента. Может принимать значения: - **asc** - по возрастанию; - **desc** - по убыванию; - **массив ID** - в этом случае элементы будут выводиться в том порядке, в котором они перечислены в массиве. (С версии 18.6.700) **Важно!**Этот же массив должен быть передан в фильтр (параметр **arFilter**). - **sort** - индекс сортировки; - **timestamp_x** - дата изменения; - **name** - название; - date_active_from - начало периода действия элемента; - date_active_to - окончание периода действия элемента; - **status** - код статуса элемента в документообороте; - **code** - символьный код элемента; - **iblock_id** - числовой код информационного блока; - **modified_by** - код последнего изменившего пользователя; - **active** - признак активности элемента; - *show_counter*- количество показов элемента (учитывается методом [CIBlockElement](index.md)::[CounterInc](counterinc.md)); - **show_counter_start** - время первого показа элемента (учитывается методом [CIBlockElement](index.md)::[CounterInc](counterinc.md)); - **shows** - усредненное количество показов (количество показов / продолжительность показа); - **rand** - случайный порядок; - xml_id или external_id - внешний код; - tags - теги; - created - время создания; - created_date - дата создания без учета времени; - cnt - количество элементов (только при заданной группировке); - **property_<PROPERTY_CODE>** - по значению свойства с числовым или символьным кодом *PROPERTY_CODE* (например, PROPERTY_123 или PROPERTY_NEWS_SOURCE); - **propertysort_<PROPERTY_CODE>** - по индексу сортировки варианта значения свойства. Только для свойств типа "Список" ; - **catalog_<CATALOG_FIELD>_<PRICE_TYPE>** - по полю CATALOG_FIELD (может быть PRICE - цена, CURRENCY - валюта или PRICE_SCALE - цена с учетом валюты) из цены с типом *PRICE_TYPE* (например, catalog_PRICE_1 или CATALOG_CURRENCY_3). С версии 16.0.3 модуля **Торговый каталог** сортировка по цене также идет с учетом валюты. - **IBLOCK_SECTION_ID** - ID раздела; - ***CATALOG_QUANTITY** - общее количество товара; - ***CATALOG_WEIGHT** - вес товара; - ***CATALOG_AVAILABLE** - признак доступности товара (Y\|N). Товар считается недоступным, если его количество меньше либо равно нулю, включен количественный учет и запрещена покупка при нулевом количестве. - ***CATALOG_STORE_AMOUNT_<идентификатор_склада>** - сортировка по количеству товара на конкретном складе (доступно с версии 15.5.5 модуля **Торговый каталог**). - ***CATALOG_BUNDLE** - сортировка по наличию набора у товара (доступно с версии 16.0.3 модуля **Торговый каталог**). - PROPERTY_<PROPERTY_CODE>.<FIELD> - по значению поля элемента указанного в качестве привязки. **PROPERTY_CODE** - символьный код свойства типа привязка к элементам. FIELD может принимать значения: - ID - TIMESTAMP_X - MODIFIED_BY - CREATED - CREATED_DATE - CREATED_BY - IBLOCK_ID - ACTIVE - SORT - NAME - SHOW_COUNTER - SHOW_COUNTER_START - CODE - TAGS - XML_ID - STATUS - PROPERTY_<PROPERTY_CODE>.PROPERTY_< PROPERTY_CODE2 > - по значению свойства элемента указанного в качестве привязки. PROPERTY_CODE - символьный код свойства типа привязки к элементам. PROPERTY_CODE2- код свойства связанных элементов. - **HAS_PREVIEW_PICTURE** и **HAS_DETAIL_PICTURE** - сортировка по наличию и отсутствию картинок. - **order** - порядок сортировки, пишется без пробелов, может принимать значения: - **asc** - по возрастанию; - nulls,asc - по возрастанию с пустыми значениями в начале выборки; - asc,nulls - по возрастанию с пустыми значениями в конце выборки; - **desc** - по убыванию; - nulls,desc - по убыванию с пустыми значениями в начале выборки; - desc,nulls - по убыванию с пустыми значениями в конце выборки; Необязательный. По умолчанию равен *Array("sort"=>"asc")* <li>*<b>CATALOG_PRICE_<i>&lt;ID типа цен&gt;</i></b> - по ценам торговых предложений.</li> **Примечание 1:**если задать разным свойствам одинаковый символьный код, но в разном регистре, то при работе сортировки по одному из свойств (например, PROPERTY_rating) будет возникать ошибочная ситуация (элементы в списке задублируются, сортировки не будет). **Примечание 2:**указанные поля сортировки автоматически добавляются в arGroupBy (если он задан) и arSelectFields. |  |
| arFilter | Массив вида array("фильтруемое поле"=>"значения фильтра" [, ...]). "фильтруемое поле" может принимать значения: - **ID** - по числовому коду (фильтр [Число](../../filters/number.md)); - **ACTIVE** - фильтр по активности (Y\|N); передача пустого значения (*"ACTIVE"=>""*) выводит все элементы без учета их состояния (фильтр [Строка](../../filters/string_equal.md)); - **NAME** - по названию (фильтр [Маска](../../filters/string.md)); - **CODE** - по символьному идентификатору (фильтр [Маска](../../filters/string.md)); - **IBLOCK_SECTION_ID** - используйте этот ключ только в режиме выбора **основного раздела для элемента** либо когда все товары привязаны только к одному разделу. Во всех остальных случаях используйте фильтр по SECTION_ID. - **TAGS** - по тегам (фильтр [Маска](../../filters/string.md)); - **XML_ID** или**EXTERNAL_ID** - по внешнему коду (фильтр [Маска](../../filters/string.md)); - **PREVIEW_TEXT** - по анонсу (фильтр [Маска](../../filters/string.md)); - **PREVIEW_TEXT_TYPE** - по типу анонса (html\|text, фильтр [Строка](../../filters/string_equal.md)); - **PREVIEW_PICTURE** - коду картинки для анонса (фильтр [Число](../../filters/number.md)); - **DETAIL_TEXT** - по детальному описанию (фильтр [Маска](../../filters/string.md)); - **DETAIL_TEXT_TYPE** - по типу детальному описания (html\|text, фильтр [Строка](../../filters/string_equal.md)); - **DETAIL_PICTURE** - по коду детальной картинки (фильтр [Число](../../filters/number.md)); - **CHECK_PERMISSIONS** - если установлен в "Y", то в выборке будет осуществляться проверка прав доступа к информационным блокам. По умолчанию права доступа не проверяются. - **PERMISSIONS_BY** - фильтрация по правам произвольного пользователя. Значение - ID пользователя или 0 (неавторизованный). - ***CATALOG_TYPE** - фильтрация по типу товара; - **MIN_PERMISSION** - минимальный уровень доступа, будет обработан только если **CHECK_PERMISSIONS** установлен в "Y". По умолчанию "R". Список прав доступа см. в [CIBlock](../ciblock/index.md)::[SetPermission](../ciblock/setpermission.md)(). - **SEARCHABLE_CONTENT** - по содержимому для поиска. Включает в себя название, описание для анонса и детальное описание (фильтр [Маска](../../filters/string.md)); - **SORT** - по сортировке (фильтр [Число](../../filters/number.md)); - **TIMESTAMP_X** - по времени изменения (фильтр [Дата](../../filters/date.md)); - **DATE_MODIFY_FROM** - по времени изменения. Будут выбраны элементы измененные после времени указанного в фильтре. Время указывается в формате сайта. Возможно использовать операцию отрицания "!DATE_MODIFY_FROM"; - **DATE_MODIFY_TO** - по времени изменения. Будут выбраны элементы измененные ранее времени указанного в фильтре. Время указывается в формате сайта. Возможно использовать операцию отрицания "!DATE_MODIFY_TO"; - **MODIFIED_USER_ID**или**MODIFIED_BY** - по коду пользователя, изменившего элемент (фильтр [Число](../../filters/number.md)); - **DATE_CREATE** - по времени создания (фильтр [Дата](../../filters/date.md)); - **CREATED_USER_ID**или**CREATED_BY** - по коду пользователя, добавившего элемент (фильтр [Число](../../filters/number.md)); - **DATE_ACTIVE_FROM** - по дате начала активности (фильтр [Дата](../../filters/date.md)) Формат даты должен соответствовать **формату даты**, установленному на сайте. Чтобы выбрать элементы с пустым полем начала активности, следует передать значение *false*; - **DATE_ACTIVE_TO** - по дате окончания активности (фильтр [Дата](../../filters/date.md))Формат даты должен соответствовать **формату даты**, установленному на сайте. Чтобы выбрать элементы с пустым полем окончания активности, следует передать значение *false*; - **ACTIVE_DATE** - непустое значение задействует фильтр по датам активности. Будут выбраны активные по датам элементы.Если значение не установлено (*""*), фильтрация по датам активности не производится; Чтобы выбрать все не активные по датам элементы, используется такой синтаксис: ``` $el_Filter[ "!ACTIVE_DATE" ]= "Y"; ``` - **IBLOCK_ID** - по коду информационного блока (фильтр [Число](../../filters/number.md)); При использовании инфоблоков 1.0 можно в IBLOCK_ID передать массив идентификаторов, чтобы сделать выборку из элементов нескольких инфоблоков: ``` $arFilter = array("IBLOCK_ID" => array(1, 2, 3), ...); ``` Для инфоблоков 2.0 такая выборка будет работать только в том случае, если в ней не запрашиваются свойства элементов. В некоторых случаях точное указание IBLOCK_ID в фильтре может ускорить выборку элементов. Так как зависимости сложные, каждый конкретный случай надо рассматривать отдельно. - **IBLOCK_CODE** - по символьному коду информационного блока (фильтр [Маска](../../filters/string.md)); - **IBLOCK_SITE_ID** или IBLOCK_LID или SITE_ID или LID - по сайту (фильтр [Строка](../../filters/string_equal.md)); - **IBLOCK_TYPE** - по типу информационного блока (фильтр [Маска](../../filters/string.md)); - **IBLOCK_ACTIVE** - по активности информационного блока (Y\|N, фильтр [Строка](../../filters/string_equal.md)); - **SECTION_ID** - по родительской группе. Если значение фильтра false, "" или 0, то будут выбраны элементы не привязанные ни к каким разделам. Иначе будут выбраны элементы привязанные к заданному разделу. Значением фильтра может быть и массив. В этом случае будут выбраны элементы привязанные хотя бы к одному из разделов указанных в фильтре. Возможно указание отрицания "!". В этом случае условие будет инвертировано; - **SECTION_CODE** - по символьному коду родительской группы. Аналогично SECTION_ID; - **INCLUDE_SUBSECTIONS** - если задан фильтр по родительским группам **SECTION_ID**, то будут также выбраны элементы находящиеся в подгруппах этих групп (имеет смысле только в том случае, если **SECTION_ID > 0**); - SUBSECTION - по принадлежности к подразделам раздела. Значением фильтра может быть массив из двух элементов задающих левую и правую границу дерева разделов. Операция отрицания поддерживается. - SECTION_ACTIVE - если ключ есть в фильтре, то проверяется активность групп к которым привязан элемент. - SECTION_GLOBAL_ACTIVE - аналогично предыдущему, но учитывается также активность родительских групп. - SECTION_SCOPE - задает уточнение для фильтров SECTION_ACTIVE и SECTION_GLOBAL_ACTIVE. Если значение "IBLOCK", то учитываются только привязки к разделам инфоблока. Если значение "PROPERTY", то учитываются только привязки к разделам свойств. "PROPERTY_" - привязки к разделам конкретного свойства. - ***CATALOG_AVAILABLE** - признак доступности товара (Y\|N). Товар считается недоступным, если его количество меньше либо равно нулю, включен количественный учет и запрещена покупка при нулевом количестве; - ***CATALOG_CATALOG_GROUP_ID_N** - по типу цен; - ***CATALOG_SHOP_QUANTITY_N** - фильтрация по диапазону количества в цене; - ***CATALOG_QUANTITY** - по общему количеству товара; - ***CATALOG_WEIGHT** - по весу товара; - ***CATALOG_STORE_AMOUNT_<идентификатор_склада>** - фильтрация по наличию товара на конкретном складе (доступно с версии 15.0.2 модуля **Торговый каталог**). В качестве значения фильтр принимает количество товара на складе либо *false*. - ***CATALOG_PRICE_SCALE_<тип_цены>** - фильтрация по цене с учетом валюты (доступно с версии 16.0.3 модуля **Торговый каталог**). - ***CATALOG_BUNDLE** - фильтрация по наличию набора у товара (доступно с версии 16.0.3 модуля **Торговый каталог**). - **SUBQUERY** - массив ``` $filter = array("SUBQUERY" => array( "FIELD" => "имя поля", "FILTER" => array(фильтр для отбора предложений) )) ``` из двух параметров: - FIELD - [строка](../../filters/string_equal.md), имя поля - FILTER - массив, фильтр для отбора предложений. Внутри GetList преобразовывается в: ``` ID => CIBlockElement::SubQuery($filter['SUBQUERY']['FIELD'], $filter['SUBQUERY']['FILTER']) ``` Доступен с версии 21.300.0 модуля iblock. - **SHOW_COUNTER** - по количеству показов (фильтр [Число](../../filters/number.md)); - **SHOW_COUNTER_START** - по времени первого показа (фильтр [Дата](../../filters/date.md)); - **WF_COMMENTS** - по комментарию документооборота (фильтр [Маска](../../filters/string.md)); - **WF_STATUS_ID** или WF_STATUS - по коду статуса документооборота (фильтр [Число](../../filters/number.md)); - **SHOW_HISTORY** - если установлен в значение "Y", то вместе с элементами будут выводится и их архив (история), по умолчанию выводятся только опубликованные элементы. Для фильтрации по WF_STATUS_ID **SHOW_HISTORY** должен стоять в "Y". - **SHOW_NEW** - если **SHOW_HISTORY** не установлен или не равен Y и **SHOW_NEW**=Y, то будут показываться ещё неопубликованные элементы вместе с опубликованными; - **WF_PARENT_ELEMENT_ID** - по коду элемента-родителя в документообороте для выборки истории изменений (фильтр [Число](../../filters/number.md)); - **WF_NEW** - флаг что элемент ещё ни разу не был опубликован (Y\|N); - **WF_LOCK_STATUS** - статус заблокированности элемента в документооборте (red\|green\|yellow); - **PROPERTY_<PROPERTY_CODE****>** - фильтр по значениям свойств, где PROPERTY_CODE - код свойства или символьный код. Для свойств типа "Список", "Число", "Привязка к элементам" и "Привязка к разделам" - фильтр [Число](../../filters/number.md). Для прочих - фильтр [Маска](../../filters/string.md); - **PROPERTY_<****PROPERTY_CODE>_VALUE** - фильтр по значениям списка для свойств типа "список" (фильтр [Маска](../../filters/string.md)), поиск будет осуществляться по строковому значению списка, а не по идентификатору; - ***CATALOG_<CATALOG_FIELD>_<PRICE_TYPE>** - по полю *CATALOG_FIELD* из цены типа *PRICE_TYPE* (ID типа цены), где *CATALOG_FIELD* может быть: PRICE - цена, CURRENCY - валюта. - PROPERTY_<PROPERTY_CODE>.<FIELD> - фильтр по значениям полей связанных элементов. , где PROPERTY_CODE - ID или символьный код свойства привязки, а FIELD - поле указанного в привязке элемента. FIELD может принимать следующие значения: ACTIVE, DETAIL_TEXT_TYPE, PREVIEW_TEXT_TYPE, EXTERNAL_ID, NAME, XML_ID, TMP_ID, DETAIL_TEXT, SEARCHABLE_CONTENT, PREVIEW_TEXT, CODE, TAGS, WF_COMMENTS, ID, SHOW_COUNTER, WF_PARENT_ELEMENT_ID, WF_STATUS_ID, SORT, CREATED_BY, PREVIEW_PICTURE, DETAIL_PICTURE, IBLOCK_ID, TIMESTAMP_X, DATE_CREATE, SHOW_COUNTER_START, DATE_ACTIVE_FROM, DATE_ACTIVE_TO, ACTIVE_DATE, DATE_MODIFY_FROM, DATE_MODIFY_TO, MODIFIED_USER_ID, MODIFIED_BY, CREATED_USER_ID, CREATED_BY. Правила фильтров идентичны тем, которые описаны выше. - **PRODUCT_BARCODE** - по штрихкоду. - **PRODUCT_BARCODE_STORE** - по привязке к складу штрихкода. - **PRODUCT_BARCODE_ORDER** - по привязке к заказу штрихкода. Перед названием фильтруемого поля можно указать тип проверки фильтра: - "!" - не равно - "<" - меньше - "<=" - меньше либо равно - ">" - больше - ">=" - больше либо равно - "><" - между - и т.д. *Значения фильтра* - одиночное значение или массив значений. Для исключения пустых значений необходимо использовать *false*. Необязательное. По умолчанию записи не фильтруются. **Примечание 1:**(по настройке фильтра для свойства типа "Дата/Время"): свойство типа Дата/Время хранится как строковое с датой в формате YYYY-MM-DD HH:MI:SS. Соответственно сортировка по значению такого свойства будет работать корректно, а вот значение для фильтрации формируется примерно так: $cat_filter[">"."PROPERTY_available"] = date("Y-m-d"); **Примечание 2:**при использовании типа проверки фильтра "><" для целых чисел, заканчивающихся нулем, необходимо использовать тип поля *число*или разделительный знак "," для десятичных значений (например, 20000,00). Иначе работает не корректно. |  |
| ****** arGroupBy | Массив полей для группировки элемента. Если поля указаны, то выборка по ним группируется (при этом параметр arSelectFields будет проигнорирован), а в результат добавляется поле CNT - количество сгруппированных элементов. Если указать в качестве arGroupBy пустой массив, то метод вернет количество элементов CNT по фильтру. Группировать можно по полям элемента, а также по значениям его свойств. Для этого в качестве одного из полей группировки необходимо указать *PROPERTY_<PROPERTY_CODE>*, где PROPERTY_CODE - ID или символьный код свойства. Необязательное. По умолчанию false - записи не группируются. | 3.2.1 |
| ****** arNavStartParams | Параметры для постраничной навигации и ограничения количества выводимых элементов. Массив вида "Название параметра"=>"Значение", где название параметра: - **nTopCount** - ограничить количество сверху. Если задать nTopCount и хранить свойства в общей таблице, то этот параметр ограничивает именно количество запросов. Если есть множественные свойства, то это будет отдельный запрос. То есть чтобы сделать запрос к 2 элементам со множественным свойством из 2 и 3 значений, то nTopCount должен быть равен 5. Решение проблемы: переместить свойства в отдельную таблицу. ; - **nOffset** - смещение. Ключ работает только при передаче непустого значения в ключе nTopCount. Доступен с версии iblock 21.700.100; - **bShowAll**; - разрешить вывести все элементы при постраничной навигации; - **iNumPage**; - номер страницы при постраничной навигации; - **nPageSize**; - количество элементов на странице при постраничной навигации; - **nElementID**; - ID элемента, который будет выбран вместе со своими соседями. Количество соседей определяется параметром nPageSize. Например: если nPageSize равно 2-м, то будут выбраны максимум 5-ть элементов. Соседи определяются порядком сортировки, заданным в параметре arOrder (см. выше). При этом действуют следующие ограничения: - Если элемент с таким ID отсутствует в выборке, то результат будет не определен. - nElementID не работает, если задана группировка (см. параметр arGroupBy выше). - в параметре arSelect обязательно должно присутствовать поле "ID". - обязательно должна быть задана сортировка arOrder. - поля в сортировке catalog_* не учитываются, и результат выборки становится не определенным. - в выборку добавляется поле RANK - порядковый номер элемента в "полной" выборке. Необязательное. По умолчанию *false* - не ограничивать выводимые элементы. Если передать в параметр *arNavStartParams* пустой массив, то ставится ограничение на 10 выводимых элементов. | 3.2.1 |
| arSelectFields | Массив возвращаемых [полей элемента](../../fields.md#felement). **Обратите внимание!**В параметре используются поля, но **не массивы**. Таким образом, попытка выборки по IBLOCK_SECTION (Массив идентификаторов групп, к которым относится элемент) приведет к нарушению работы метода. В списке полей элемента можно сразу выводить значения его свойств. Обязательно должно быть использованы поля IBLOCK_ID и ID, иначе не будет работать корректно. Кроме того, также в качестве одного из полей необходимо указать *PROPERTY_<PROPERTY_CODE>*, где PROPERTY_CODE - ID или символьный код (задается в верхнем регистре, даже если в определении свойств инфоблока он указан в нижнем регистре). В результате будет выведены значения свойств элемента в виде полей *PROPERTY_<PROPERTY_CODE>_VALUE* - значение; *PROPERTY_<PROPERTY_CODE>_ID* - код значения у элемента; *PROPERTY_<PROPERTY_CODE>_ENUM_ID* - код значения (для свойств типа список). При установленном модуле торгового каталога можно выводить и цены элемента. Для этого в качестве одного из полей необходимо указать **CATALOG_GROUP_<PRICE_CODE>*, где PRICE_CODE - ID типа цены. Также есть возможность выбрать поля элементов по значениям свойства типа "Привязка к элементам". Для этого необходимо указать *PROPERTY_<PROPERTY_CODE>.<FIELD>*, где PROPERTY_CODE - ID или символьный код свойства привязки, а FIELD - поле указанного в привязке элемента. См. ниже "Поля связанных элементов для сортировки". Можно выбрать и значения свойств элементов по значениям свойства типа "Привязка к элементам". Для этого необходимо указать *PROPERTY_<PROPERTY_CODE>.**PROPERTY_<PROPERTY_CODE2>*, где PROPERTY_CODE - ID или символьный код свойства привязки, а PROPERTY_CODE2 - свойство указанного в привязке элемента. По умолчанию выводить все поля. Значения параметра игнорируются, если используется параметр группировки *arGroupBy*. **Примечание 1**: если в массиве используются свойство, являющееся множественным, то для элементов, где используются несколько значений этого свойства, будет возвращено несколько записей вместо одной. Для решения этой проблемы инфоблоки нужно перевести в **Режим хранения свойств в отдельных таблицах**, в этом случае для свойства будет отдаваться массив значений. Либо можно не указывать свойства в параметрах выборки, а получать их значения на каждом шаге перебора выборки с помощью _CIBElement::GetProperties(). | 3.2.1 |
| * - Параметры вида `CATALOG_***` устарели в версии **18.6.200** модуля **Информационные блоки**. Подробнее: **Товары и CIBlockElement::GetList** | ** - В случае, если параметром **arGroupBy** передается пустой массив - данные параметра **arNavStartParams** - игнорируются. |  |
| ** - В случае, если параметром **arGroupBy** передается пустой массив - данные параметра **arNavStartParams** - игнорируются. |  |  |
| ** - В случае, если параметром **arGroupBy** передается пустой массив - данные параметра **arNavStartParams** - игнорируются. |  |  |

---
### Частные случаи

Рассмотрим несколько частных случаев фильтрации:


- $arFilter = array("PROPERTY_CML2_SCAN_CODE") =>false - используется, чтобы выбрать все элементы с незаполненными свойствами;
- $arFilter = array("PROPERTY_CML2_SCAN_CODE") =>"" - используется, чтобы выбрать все элементы;
- $arFilter = array("PROPERTY_CML2_SCAN_CODE") =>qwe - при фильтрации элементов проверяется точное совпадение с заданными свойствами;
- $arFilter = array("?PROPERTY_CML2_SCAN_CODE") =>we" - при фильтрации элементов проверяется наличие заданной подстроки свойствах.


- $arFilter = array("!PROPERTY_CML2_SCAN_CODE") =>false - используется, чтобы выбрать только элементы с заполненными свойствами;
- $arFilter = array("!PROPERTY_CML2_SCAN_CODE") =>qwe - при фильтрации элементов проверяется точное совпадение с заданными свойствами;
- $arFilter = array("!%PROPERTY_CML2_SCAN_CODE") =>we - при фильтрации элементов проверяется отсутствие заданной подстроки свойствах.

---
### Фильтр со сложной логикой

Параметр arFilter может содержать вложенные фильтры. Ключом массива вложенного фильтра должно быть число. Например:

- $arFilter = array("NAME" => "A%", array(..<здесь пары "поле" => "фильтр">...), "IBLOCK_ID" => $IBLOCK_ID);

Вложенность фильтров теоретически не ограничена.
Так же условия фильтра могут объединяться не только по условию "И", но и "ИЛИ". Для этого в качестве фильтруемого поля надо указать "LOGIC". Может принимать два значения: "AND" и "OR". По умолчанию - "AND". Например выберем маленькие зрелые и большие не зрелые апельсины:


```
$arFilter = array(
	"IBLOCK_ID" => $IBLOCK_ID,
	"SECTION_CODE" => "orange",
	"INCLUDE_SUBSECTIONS" => "Y",
	array(
		"LOGIC" => "OR",
		array(" 50, "=PROPERTY_CONDITION" => "Y"),
		array(">=PROPERTY_RADIUS" => 50, "!=PROPERTY_CONDITION" => "Y"),
	),
);
```

В этом примере фильтр по свойствам апельсинов является подфильтром инфоблока фруктов.

---
### Поля связанных элементов


- ID - числовой идентификатор элемента;
- TIMESTAMP_X - время последней модификации в полном формате сайта;
- MODIFIED_BY - идентификатор пользователя вносившего последние правки;
- DATE_CREATE - время создания элемента в полном формате сайта
- CREATED_BY - идентификатор пользователя создавшего элемент;
- IBLOCK_ID - числовой идентификатор инфоблока элемента;
- ACTIVE - активность (Y|N);
- SORT - значение сортировки;
- NAME - имя элемента;
- PREVIEW_PICTURE - идентификатор изображения;
- PREVIEW_TEXT - текст анонса;
- PREVIEW_TEXT_TYPE - тип текста анонса (html|text);
- DETAIL_PICTURE - идентификатор изображения;
- DETAIL_TEXT - детальное описание;
- DETAIL_TEXT_TYPE - тип детального описания (html|text);
- SHOW_COUNTER - счетчик показов;
- SHOW_COUNTER_START - время первого показа элемента в полном формате сайта;
- CODE - символьный код элемента;
- TAGS - теги;
- XML_ID - внешний идентификатор;
- IBLOCK_SECTION_ID - минимальный идентификатор раздела элемента (если задан);

Дополнительно присоединяется таблица инфоблоков:
- IBLOCK_TYPE_ID - идентификатор типа инфоблока;
- IBLOCK_CODE - символьный код инфоблока;
- IBLOCK_NAME - название инфоблока;
- IBLOCK_EXTERNAL_ID - внешний код инфоблока;
- DETAIL_PAGE_URL - путь к элементу;
- LIST_PAGE_URL - путь к списку элементов;


---
### Возвращаемое значение

Возвращается объект [CIBlockResult](../ciblockresult/index.md).

---
### Примеры использования

Пример 1:


```
<?
$arSelect = Array("ID", "NAME", "DATE_ACTIVE_FROM");
$arFilter = Array("IBLOCK_ID"=>IntVal($yvalue), "ACTIVE_DATE"=>"Y", "ACTIVE"=>"Y");
$res = CIBlockElement::GetList(Array(), $arFilter, false, Array("nPageSize"=>50), $arSelect);
while($ob = $res->GetNextElement())
{
	$arFields = $ob->GetFields();
	print_r($arFields);
}
?>
```

Пример 2:


```
<?
// выборка активных элементов из информационного блока $yvalue,
// у которых установлено значение свойства с символьным кодом SRC
// и дата начала автивности старше 1 января 2003 года
// выбранные элементы будут сгруппированы по дате активности
$arFilter = Array(
	"IBLOCK_ID"=>IntVal($yvalue),
	">DATE_ACTIVE_FROM"=>date($DB->DateFormatToPHP(CLang::GetDateFormat("SHORT")), mktime(0,0,0,1,1,2003)),
	"ACTIVE"=>"Y",
	"!PROPERTY_SRC"=>false
);
$res = CIBlockElement::GetList(Array("SORT"=>"ASC", "PROPERTY_PRIORITY"=>"ASC"), $arFilter, Array("DATE_ACTIVE_FROM"));
while($ar_fields = $res->GetNext())
{
	echo $ar_fields["DATE_ACTIVE_FROM"].": ".$ar_fields["CNT"]."<br>";
}
?>
```

Пример 3:


```
//вывод архива из просроченных элементов (news.list)
$arFilter = array(
	"IBLOCK_ID" => $arResult["ID"],
	"IBLOCK_LID" => SITE_ID,
	"ACTIVE" => "Y",
	"CHECK_PERMISSIONS" => "Y", //сильно грузит систему, но проверяет права
	" DateFormatToPHP(CLang::GetDateFormat("SHORT")),
);
```

Пример 4:


```
//выборка элементов инфоблока, чтобы в возвращаемом результате находилось 5 случайных элементов
$rs = CIBlockElement::GetList (
	Array("RAND" => "ASC"),
	Array("IBLOCK_ID" => $IBLOCK_ID),
	false,
	Array ("nTopCount" => 5)
);
```

Пример 5:


```
//для фильтрации по нескольким значениям множественного свойства, нужно использовать подзапросы.
CModule::IncludeModule('iblock');

$rs = CIBlockElement::GetList(
	array(),
	array(
		"IBLOCK_ID" => 21,
		array("ID" => CIBlockElement::SubQuery("ID", array("IBLOCK_ID" => 21, "PROPERTY_PKE" => 7405))),
		array("ID" => CIBlockElement::SubQuery("ID", array("IBLOCK_ID" => 21, "PROPERTY_PKE" => 7410))),
		array("ID" => CIBlockElement::SubQuery("ID", array("IBLOCK_ID" => 21, "PROPERTY_PKE" => 7417)))
	),
	false,
	false,
	array("ID")
);

while($ar = $rs->GetNext()) {
	echo '<pre>';
	print_r($ar);
	echo '</pre>';
}
```

Пример 6:


```
//следующий и предыдущий товар с учетом сортировки в подробном просмотре
 $arrSortAlown = array('price'=> 'catalog_PRICE_1' , 'name'=> 'NAME', 'rating' => 'PROPERTY_RATING' , 'artnumber'=> 'PROPERTY_ARTNUMBER');

	$_sort = isset($arrSortAlown[$_GET['sort']]) ? $arrSortAlown[$_GET['sort']] : 'NAME';
	$_order = isset($_GET['order']) && $_GET['order']=='desc' ? 'DESC' : 'ASC';

	$sort_url = 'sort=' .( isset($_GET['sort'])? $_GET['sort'] : 'name')
                        .'&order='. (isset($_GET['order'])? $_GET['order'] : 'asc');


	$res = CIBlockElement::GetList(
		array("$_sort" => $_order),
		Array(
			"IBLOCK_ID"=>$arResult["IBLOCK_ID"],
			"ACTIVE_DATE"=>"Y", "ACTIVE"=>"Y" ,
			"IBLOCK_SECTION_ID" =>
			$arResult["IBLOCK_SECTION_ID"]
		),
		false,
		array("nPageSize" => "1","nElementID" => $arResult["ID"]),
		array_merge(Array("ID", "NAME","DETAIL_PAGE_URL"), array_values($arrSortAlown))
	);
	$navElement = array();
	while($ob = $res->GetNext()){
		$navElement[] = $ob;
	}

//вывод:
<noindex>
<div class="navElement" style="float:right; clear:both;">
	<span class="l">
		<small><a href="<?=$navElement[0]['DETAIL_PAGE_URL']?>?<?=$sort_url?>">Предыдущий товар</a></small>
	</span>
	<span class="r">
		<small><a href="<?=$navElement[2]['DETAIL_PAGE_URL']?>?<?=$sort_url?>">Следующий товар</a></small>
	</span>
</div>
</noindex>
```

Пример 7:


```
//вывод ненаступивших и, следовательно, неактивных анонсов событий без правки компонента
// в компоненте указываем имя фильтра, а сам фильтр добавляем перед компонентом:
<?
	$arrFilter=Array(array(
		"LOGIC" => "OR",
		array("DATE_ACTIVE_TO"=>false),
		array(">DATE_ACTIVE_TO"=>ConvertTimeStamp(time(),"FULL"))

	));
?>
```

Пример 8:


```
//В iblock v18.6.700 появилась возможность сортировать выборку в порядке ID, указанных в массиве

// сортировать в таком порядке ID
$ids = [115, 120, 117, 109, 128];
$rs = CIBlockElement::GetList(
	['ID' => $ids],
	['IBLOCK_ID' => '5', 'ID' => $ids],
	false, false,
	['ID', 'IBLOCK_ID', 'NAME']
);
while ($ar = $rs->Fetch()) {
	echo $ar['ID'] . ' ';
}

// имеем вывод:
// 115 120 117 109 128
```

Пример 9:


```
//В iblock v21.700.100 в arNavStartParams добавлен ключ nOffset (смещение)

\Bitrix\Main\Loader::includeModule('iblock');

$res = CIBlockElement::GetList(
	['ID' => 'ASC'],
	['IBLOCK_ID' => 2],
	false,
	['nTopCount' => 5, 'nOffset' => 1000],
	['ID', 'IBLOCK_ID', 'NAME']
);

while ($row = $res->Fetch())
{
	echo '<pre>', mydump($row), '</pre>';
}

// nTopCount - сколько
// nOffset - с каким смещением
```

Пример 10. Вывести элементы с непустым значением множественного свойства типа список


```
${$FILTER_NAME}[]=array(
	 "ID" => CIBlockElement::SubQuery("ID", array(
		"IBLOCK_ID" => $arParams['IBLOCK_ID'],
		"!=PROPERTY_".$arProp["CODE"] => false
	))
);
```

Пример 11. Организация поиска по каталогу с помощью поля SEARCHEBLE_CONTENT.


```
<?
CModule::IncludeModule('iblock');
$IBLOCK_ID = intval($_REQUEST['IBLOCK_ID']);
$QUERY = trim($_REQUEST['q']);
if($QUERY) {
	$arSelect = Array("ID", "NAME", "DATE_ACTIVE_FROM", "DETAIL_PAGE_URL", "PREVIEW_PICTURE";
	$arFilter = Array("IBLOCK_ID"=>$IBLOCK_ID, "ACTIVE_DATE"=>"Y", "ACTIVE"=>"Y", "SEARCHABLE_CONTENT"=>'%'.$_REQUEST['q'].'%');
	$res = CIBlockElement::GetList(Array(), $arFilter, false, Array("nPageSize"=>50), $arSelect);
	while($ob = $res->GetNextElement())
	{
		$arFields = $ob->GetFields();
		print_r($arFields);
	}
}
?>
```

Пример 12. Для фильтрации по Дате например с 12.09.2014 по 18.09.2014 включительно фильтр будет выглядеть следующим образом:


```
$date_from = '12.09.2014';
$date_to = '18.09.2014';

$db_el = CIBlockElement::GetList(
	array('ID' => 'DESC'),
	array(
		'>=DATE_CREATE' => $date_from,
		'<=DATE_CREATE' => $date_to . ' 23:59:59'
	)
);
```

Пример 13. Выборка полей элемента и всех свойств:


```
<?php
$arSelect = ["ID", "NAME", "IBLOCK_ID"];
$arFilter = ["IBLOCK_ID"=>(int)$iblockId, "ID"=> (int)$elementId];
$res = CIBlockElement::GetList([], $arFilter, false, false, $arSelect);
$ob = $res->GetNextElement());
if ($ob)
{
	$fields = $ob->GetFields(); // указанные в $arSelect поля
	print_r($fields);
	$properties = $ob->GetProperties();
	print_r($properties);
}
```

---



Страницы: 1 23След.
| ![image](../images/7dd82aba60.gif) 0 **Александр Семашко**22.10.2022 11:38:57 |  |  |
| --- | --- | --- |
| В arrFilter поле MODIFIED_BY может принимать массив с пользователями \| Код \| \| --- \| \| ``` $arFilter = array("MODIFIED_BY" => array(1, 107120)); ``` \| | Код | ``` $arFilter = array("MODIFIED_BY" => array(1, 107120)); ``` |
| Код |  |  |
| ``` $arFilter = array("MODIFIED_BY" => array(1, 107120)); ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 2 **Антон Короленко**10.02.2022 09:18:10 |  |  |
| --- | --- | --- |
| \| Цитата \| \| --- \| \| пишет: Если нужно посчитать количество записей if(\Bitrix\Main\Loader::includeModule('iblock')){ $arFilter = [ "IBLOCK_ID"=>1, "ACTIVE"=>"Y", "=PROPERTY_18"=>["vase"] ]; $db = \CIBlockElement::GetList([], $arFilter, false, [], ['ID']); echo \CIBlockElement::GetList([], $arFilter, false, [], ['ID'])->AffectedRowsCount(); } \| что бы посчитать записи можно в arGroupBy передать пустой массив CIBlockElement::GetList([], $arFilter, []); сразу вернется число записей [SIZE=13px][COLOR=#000000][/COLOR] [COLOR=#737373][/COLOR][/SIZE] | Цитата | пишет: Если нужно посчитать количество записей if(\Bitrix\Main\Loader::includeModule('iblock')){ $arFilter = [ "IBLOCK_ID"=>1, "ACTIVE"=>"Y", "=PROPERTY_18"=>["vase"] ]; $db = \CIBlockElement::GetList([], $arFilter, false, [], ['ID']); echo \CIBlockElement::GetList([], $arFilter, false, [], ['ID'])->AffectedRowsCount(); } |
| Цитата |  |  |
| пишет: Если нужно посчитать количество записей if(\Bitrix\Main\Loader::includeModule('iblock')){ $arFilter = [ "IBLOCK_ID"=>1, "ACTIVE"=>"Y", "=PROPERTY_18"=>["vase"] ]; $db = \CIBlockElement::GetList([], $arFilter, false, [], ['ID']); echo \CIBlockElement::GetList([], $arFilter, false, [], ['ID'])->AffectedRowsCount(); } |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 2 **Михаил Микулин**21.08.2021 18:17:18 |  |  |
| --- | --- | --- |
| Найти по значению свойства, которое содержит нужный вам текст : \| Код \| \| --- \| \| ``` $arFilter = Array("IBLOCK_ID"=>$_POST["IBLOCK"], 'PROPERTY_CML2_ARTICKLE'=>$ar, 'PROPERTY_ADRES_TOVARA_NA_SKLADE_VALUE'=>'%'.'P1-B4'.'%' ); ``` \| | Код | ``` $arFilter = Array("IBLOCK_ID"=>$_POST["IBLOCK"], 'PROPERTY_CML2_ARTICKLE'=>$ar, 'PROPERTY_ADRES_TOVARA_NA_SKLADE_VALUE'=>'%'.'P1-B4'.'%' ); ``` |
| Код |  |  |
| ``` $arFilter = Array("IBLOCK_ID"=>$_POST["IBLOCK"], 'PROPERTY_CML2_ARTICKLE'=>$ar, 'PROPERTY_ADRES_TOVARA_NA_SKLADE_VALUE'=>'%'.'P1-B4'.'%' ); ``` |  |  |
|  |  |  |


| ![](../images/0402b21914.jpg) 4 **Кирилл Черныш**07.04.2021 14:37:21 |
| --- |
| *CATALOG_TYPE - фильтрация по типу товара; Может принимать значения простой: 1 товар с предложениями: 3 невалидный товар с предложениями: 6 комплект: 2 |
|  |


| ![](../images/506c3eb240.jpg) 0 **Евгений Милютин**03.03.2021 16:16:06 |  |  |
| --- | --- | --- |
| Получить cвойство тип (HTML/TEXT). Символьный код свойства HTML_CONTENT \| Код \| \| --- \| \| ``` $arSelect = Array("ID", "IBLOCK_ID", "CODE", "NAME", "PROPERTY_HTML_CONTENT"); $arFilter = Array("IBLOCK_ID"=>$infoblocks, "ACTIVE_DATE"=>"Y", "ACTIVE"=>"Y"); $res = CIblockElement::GetList(Array("DATE_CREATE" => "DESC"), $arFilter, false, $arPages, $arSelect); while($ob = $res->GetNextElement()){ $arFields = $ob->GetFields(); $content = $arFields['PROPERTY_HTML_CONTENT_VALUE']['HTML'] ? htmlspecialcharsBack($arFields['PROPERTY_HTML_CONTENT_VALUE']['HTML']) : htmlspecialcharsBack($arFields['PROPERTY_HTML_CONTENT_VALUE']['TEXT']); } ``` \| | Код | ``` $arSelect = Array("ID", "IBLOCK_ID", "CODE", "NAME", "PROPERTY_HTML_CONTENT"); $arFilter = Array("IBLOCK_ID"=>$infoblocks, "ACTIVE_DATE"=>"Y", "ACTIVE"=>"Y"); $res = CIblockElement::GetList(Array("DATE_CREATE" => "DESC"), $arFilter, false, $arPages, $arSelect); while($ob = $res->GetNextElement()){ $arFields = $ob->GetFields(); $content = $arFields['PROPERTY_HTML_CONTENT_VALUE']['HTML'] ? htmlspecialcharsBack($arFields['PROPERTY_HTML_CONTENT_VALUE']['HTML']) : htmlspecialcharsBack($arFields['PROPERTY_HTML_CONTENT_VALUE']['TEXT']); } ``` |
| Код |  |  |
| ``` $arSelect = Array("ID", "IBLOCK_ID", "CODE", "NAME", "PROPERTY_HTML_CONTENT"); $arFilter = Array("IBLOCK_ID"=>$infoblocks, "ACTIVE_DATE"=>"Y", "ACTIVE"=>"Y"); $res = CIblockElement::GetList(Array("DATE_CREATE" => "DESC"), $arFilter, false, $arPages, $arSelect); while($ob = $res->GetNextElement()){ $arFields = $ob->GetFields(); $content = $arFields['PROPERTY_HTML_CONTENT_VALUE']['HTML'] ? htmlspecialcharsBack($arFields['PROPERTY_HTML_CONTENT_VALUE']['HTML']) : htmlspecialcharsBack($arFields['PROPERTY_HTML_CONTENT_VALUE']['TEXT']); } ``` |  |  |
|  |  |  |


| ![](../images/2068d63a6f.jpg) 3 **Алексей Попович**03.12.2019 16:14:37 |  |  |
| --- | --- | --- |
| Пример фильтрации товаров по наличию на определенных складах: \| Код \| \| --- \| \| ``` if(!empty($arParams['STORES'])){ $storesFilter = [ 'LOGIC'=>'OR' ]; foreach ($arParams['STORES'] as $store_id){ $storesFilter[] = ['STORE_NUMBER' => intval($store_id),'>STORE_AMOUNT'=>0]; } $GLOBALS[$arParams['FILTER_NAME']][] = $storesFilter; } ``` \| | Код | ``` if(!empty($arParams['STORES'])){ $storesFilter = [ 'LOGIC'=>'OR' ]; foreach ($arParams['STORES'] as $store_id){ $storesFilter[] = ['STORE_NUMBER' => intval($store_id),'>STORE_AMOUNT'=>0]; } $GLOBALS[$arParams['FILTER_NAME']][] = $storesFilter; } ``` |
| Код |  |  |
| ``` if(!empty($arParams['STORES'])){ $storesFilter = [ 'LOGIC'=>'OR' ]; foreach ($arParams['STORES'] as $store_id){ $storesFilter[] = ['STORE_NUMBER' => intval($store_id),'>STORE_AMOUNT'=>0]; } $GLOBALS[$arParams['FILTER_NAME']][] = $storesFilter; } ``` |  |  |
|  |  |  |


| ![](../images/c7099e7e38.png) 1 **Василий Андреев**18.06.2019 14:22:39 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Для получения цены из каталога указывая в \| Код \| \| --- \| \| ``` $arSelect=array("ID", "IBLOCK_ID", "CATALOG_GROUP_<ID типа цены>"); ``` \| в массиве полученном методом GetNext() необходимо использовать ключ \| Код \| \| --- \| \| ``` CATALOG_PRICE_<ID типа цены> ``` \| | Код | ``` $arSelect=array("ID", "IBLOCK_ID", "CATALOG_GROUP_<ID типа цены>"); ``` | Код | ``` CATALOG_PRICE_<ID типа цены> ``` |
| Код |  |  |  |  |
| ``` $arSelect=array("ID", "IBLOCK_ID", "CATALOG_GROUP_<ID типа цены>"); ``` |  |  |  |  |
| Код |  |  |  |  |
| ``` CATALOG_PRICE_<ID типа цены> ``` |  |  |  |  |
|  |  |  |  |  |


| ![](../images/6dd74262d2.jpg) 0 **Леонид Тропин**06.10.2017 16:58:20 |  |  |  |  |
| --- | --- | --- | --- | --- |
| \| Цитата \| \| --- \| \| [Антон Долганин](https://dev.1c-bitrix.ru/community/webdev/user/11948/) пишет: Не знаю было ли, частый кейс с nElementID - предыдущая и следующая новость в текущей новости \| Не знаю, насколько часто это случается, но один раз метод показанный Антоном не сработал. Может из-за специфической сортировки при выборке, может ещё из-за чего. Есть ещё один способ: \| Код \| \| --- \| \| ``` $arResult['PREV'] = $arResult['CURRENT'] = $arResult['NEXT'] = array(); //предыдущая и следующая if (\Bitrix\Main\Loader::includeModule('iblock')) { $i = 0; $arSort = array('SORT' => 'ASC', 'ID' => 'DESC'); $arFilter = array('ACTIVE' => 'Y', 'IBLOCK_ID' => $arParams['IBLOCK_ID']); $arSelect = array('ID', 'NAME', 'DETAIL_PAGE_URL'); $res = CIBlockElement::getList($arSort, $arFilter, false, array('nElementID' => $element['ID'], 'nPageSize' => 1), $arSelect); while ($row = $res->fetch()) { if ($element['ID'] == $row['ID']) { $arResult['CURRENT'] = $row; } $arRows[$row['RANK']] = $row; } if(isset($arRows[$arResult['CURRENT']['RANK']-1])) { $arResult['PREV'] = $arRows[$arResult['CURRENT']['RANK']-1]; } if(isset($arRows[$arResult['CURRENT']['RANK']+1])) { $arResult['NEXT'] = $arRows[$arResult['CURRENT']['RANK']+1]; } unset($arRows); } ``` \| | Цитата | [Антон Долганин](https://dev.1c-bitrix.ru/community/webdev/user/11948/) пишет: Не знаю было ли, частый кейс с nElementID - предыдущая и следующая новость в текущей новости | Код | ``` $arResult['PREV'] = $arResult['CURRENT'] = $arResult['NEXT'] = array(); //предыдущая и следующая if (\Bitrix\Main\Loader::includeModule('iblock')) { $i = 0; $arSort = array('SORT' => 'ASC', 'ID' => 'DESC'); $arFilter = array('ACTIVE' => 'Y', 'IBLOCK_ID' => $arParams['IBLOCK_ID']); $arSelect = array('ID', 'NAME', 'DETAIL_PAGE_URL'); $res = CIBlockElement::getList($arSort, $arFilter, false, array('nElementID' => $element['ID'], 'nPageSize' => 1), $arSelect); while ($row = $res->fetch()) { if ($element['ID'] == $row['ID']) { $arResult['CURRENT'] = $row; } $arRows[$row['RANK']] = $row; } if(isset($arRows[$arResult['CURRENT']['RANK']-1])) { $arResult['PREV'] = $arRows[$arResult['CURRENT']['RANK']-1]; } if(isset($arRows[$arResult['CURRENT']['RANK']+1])) { $arResult['NEXT'] = $arRows[$arResult['CURRENT']['RANK']+1]; } unset($arRows); } ``` |
| Цитата |  |  |  |  |
| [Антон Долганин](https://dev.1c-bitrix.ru/community/webdev/user/11948/) пишет: Не знаю было ли, частый кейс с nElementID - предыдущая и следующая новость в текущей новости |  |  |  |  |
| Код |  |  |  |  |
| ``` $arResult['PREV'] = $arResult['CURRENT'] = $arResult['NEXT'] = array(); //предыдущая и следующая if (\Bitrix\Main\Loader::includeModule('iblock')) { $i = 0; $arSort = array('SORT' => 'ASC', 'ID' => 'DESC'); $arFilter = array('ACTIVE' => 'Y', 'IBLOCK_ID' => $arParams['IBLOCK_ID']); $arSelect = array('ID', 'NAME', 'DETAIL_PAGE_URL'); $res = CIBlockElement::getList($arSort, $arFilter, false, array('nElementID' => $element['ID'], 'nPageSize' => 1), $arSelect); while ($row = $res->fetch()) { if ($element['ID'] == $row['ID']) { $arResult['CURRENT'] = $row; } $arRows[$row['RANK']] = $row; } if(isset($arRows[$arResult['CURRENT']['RANK']-1])) { $arResult['PREV'] = $arRows[$arResult['CURRENT']['RANK']-1]; } if(isset($arRows[$arResult['CURRENT']['RANK']+1])) { $arResult['NEXT'] = $arRows[$arResult['CURRENT']['RANK']+1]; } unset($arRows); } ``` |  |  |  |  |
|  |  |  |  |  |


| ![](../images/ee42e7da8d.jpg) 4 **Сергей Талызенков**03.08.2017 12:57:31 |  |  |
| --- | --- | --- |
| Свойство типа "справочник" нужно фильтровать по значению UF_XML_ID элемента справочника \| Код \| \| --- \| \| ``` $arFilter['PROPERTY_LOCATION'] = 't9DgyAPm'; //t9DgyAPm это значение поля UF_XML_ID элемента справочника ``` \| | Код | ``` $arFilter['PROPERTY_LOCATION'] = 't9DgyAPm'; //t9DgyAPm это значение поля UF_XML_ID элемента справочника ``` |
| Код |  |  |
| ``` $arFilter['PROPERTY_LOCATION'] = 't9DgyAPm'; //t9DgyAPm это значение поля UF_XML_ID элемента справочника ``` |  |  |
|  |  |  |


| ![](../images/867d055ea3.png) 4 **Антон Козлов**16.03.2017 10:56:35 |
| --- |
| Если необходимо отфильтровать элементы по "Основному разделу", то можно воспользоваться "IBLOCK_SECTION_ID", т.к. "SECTION_ID" фильтрует по всем разделам, к которым привязан элемент. |
|  |

Страницы: 1 23След.
