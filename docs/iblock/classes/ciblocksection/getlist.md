# GetList


### Описание


```
CIBlockResult
CIBlockSection::GetList(
	array arOrder = Array("SORT"=>"ASC"),
	array arFilter = Array(),
	bool bIncCnt = false,
	array Select = Array(),
	array NavStartParams = false
);
```

Возвращает список разделов, отсортированных в порядке*arOrder* по фильтру *arFilter*. Нестатический метод.


#### Смотрите также


- [CIBlockResult](../ciblockresult/index.md)
- [Поля раздела информационного блока](../../fields.md#fsection)

---
### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| arOrder | Массив для сортировки, имеющий вид *by1*=>*order1*[, *by2*=>*order2* [, ..]], где *by1, ...* - поле сортировки, может принимать значения: - **id** - код раздела; - **section** - код родительской раздела; - **name** - название раздела; - **code** - символьный код раздела; - **active** - активности раздела; - **left_margin** - левая граница; - **depth_level** - глубина вложенности (начинается с 1); - **sort** - индекс сортировки; - **created** - по времени создания раздела; - **created_by** - по идентификатору создателя раздела; - **modified_by** - по идентификатору пользователя изменившего раздел; - **element_cnt** - количество элементов в разделе, работает только если **bIncCnt** = true; - **timestamp_x** - по времени последнего изменения. *order1, ...* - порядок сортировки, может принимать значения: - **asc** - по возрастанию; - **desc** - по убыванию. Кроме того, сортировка возможна и по пользовательским свойствам UF_XXX. Значение по умолчанию Array("SORT"=>"ASC") означает, что результат выборки будет отсортирован по возрастанию. Если задать пустой массив Array(), то результат отсортирован не будет. |  |
| arFilter | Массив вида array("фильтруемое поле"=>"значение" [, ...]). *Фильтруемое поле* может принимать значения: - **ACTIVE** - фильтр по активности (Y\|N); - **GLOBAL_ACTIVE** - фильтр по активности, учитывая активность вышележащих разделов (Y\|N); - **NAME** - по названию (можно искать по шаблону [%_]); - **CODE** - по символьному коду (по шаблону [%_]); - **XML_ID** или **EXTERNAL_ID** - по внешнему коду (по шаблону [%_]); - **SECTION_ID** - по коду раздела-родителя (если указать false, то будут возвращены корневые разделы); - **DEPTH_LEVEL** - по уровню вложенности (начинается с 1); - **LEFT_BORDER**, **RIGHT_BORDER** - по левой и правой границе (используется, когда необходимо выбрать некий диапазон разделов, см. [пример №4](#ex4)); - **LEFT_MARGIN**, **RIGHT_MARGIN** - по положению в дереве (используется, когда необходима выборка дерева подразделов, см. [пример №4](#ex4)); - **ID** - по коду раздела; - **IBLOCK_ID** - по коду родительского информационного блока. Обязателен, если нужно получить пользовательское свойство; - **IBLOCK_ACTIVE** - по активности родительского информационного блока; - **IBLOCK_NAME** - по названию информационного блока (по шаблону [%_]); - **IBLOCK_TYPE** - по типу информационного блока (по шаблону [%_]); - **IBLOCK_CODE***-*по символьному коду информационного блока (по шаблону [%_]); - **IBLOCK_XML_ID** или **IBLOCK_EXTERNAL_ID** - по внешнему коду информационного блока (по шаблону [%_]); - TIMESTAMP_X - по времени последнего изменения; - DATE_CREATE - по времени создания; - MODIFIED_BY - по коду пользователя изменившему раздел; - CREATED_BY - по содателю; - SOCNET_GROUP_ID - по привязке к группе Социальной сети; - **MIN_PERMISSION** - фильтр по правам доступа, по умолчанию принимает *R* (уровень доступа *Чтение*); - **CHECK_PERMISSIONS** - если установлено значение "N", то проверки прав не происходит; - **PERMISSIONS_BY** - фильтрация по правам произвольного пользователя. Значение - ID пользователя или 0 (неавторизованный). - **PROPERTY***-*по значениям свойств внутрилежащих элементов, PROPERTY - массив вида Array("код свойства"=>"значение", ...). - **HAS_ELEMENT** - по наличию элемента. Используется в компоненте **catalog.detail**. Все фильтруемые поля могут содержать перед названием **тип проверки фильтра**. **Значения фильтра** одиночное значение или массив. **Важно!**Чтобы фильтрация выполнялась по пользовательским свойствам, необходимо обязательно передавать в фильтр *IBLOCK_ID*. Само свойство надо указывать в виде UF_... Необязательное. По умолчанию записи не фильтруются. |  |
| bIncCnt | Возвращать ли поле *ELEMENT_CNT* - количество элементов в разделе. При этом arFilter дополнительно обрабатывает следующие фильтруемые поля: - **ELEMENT_SUBSECTIONS** - подсчитывать элементы вложенных подразделов или нет (Y\|N). По умолчанию Y; - **CNT_ALL** - подсчитывать еще неопубликованные элементы (Y\|N). По умолчанию N. Актуально при установленном модуле документооборота; - **CNT_ACTIVE** - при подсчете учитывать активность элементов (Y\|N). По умолчанию N. Учитывается флаг активности элемента ACTIVE и даты начала и окончания активности. Необязательный параметр, по умолчанию равен false. **Примечание:** в случае если в фильтре есть ключ PROPERTY то в количестве элементов вернется то значение, которое попадает под этот фильтр по значению свойств. |  |
| arSelect | Массив для выборки. - **ID** - ID группы информационного блока. - **CODE** - Символьный идентификатор. - **EXTERNAL_ID или XML_ID** - Внешний код. - **IBLOCK_ID** - ID информационного блока. - **IBLOCK_SECTION_ID** - ID группы родителя, если не задан то группа корневая. - **TIMESTAMP_X** - Дата последнего изменения параметров группы. - **SORT** - Порядок сортировки (среди групп внутри одной группы-родителя). - **NAME** - Наименование группы. - **ACTIVE** - Флаг активности (Y\|N) - **GLOBAL_ACTIVE** - Флаг активности, учитывая активность вышележащих (родительских) групп (Y\|N). Вычисляется автоматически (не может быть изменен вручную). - **PICTURE** - Код картинки в таблице файлов. - **DESCRIPTION** - Описание группы. - **DESCRIPTION_TYPE** - Тип описания группы (text/html). - **LEFT_MARGIN** - Левая граница группы. Вычисляется автоматически (не устанавливается вручную). - **RIGHT_MARGIN** - Правая граница группы. Вычисляется автоматически (не устанавливается вручную). - **DEPTH_LEVEL** - Уровень вложенности группы. Начинается с 1. Вычисляется автоматически (не устанавливается вручную). - **SEARCHABLE_CONTENT** Содержимое для поиска при фильтрации групп. Вычисляется автоматически. Складывается из полей **NAME** и **DESCRIPTION** (без html тэгов, если **DESCRIPTION_TYPE** установлен в html). - **SECTION_PAGE_URL** - Шаблон URL-а к странице для детального просмотра раздела. Определяется из параметров информационного блока. Изменяется автоматически. - **MODIFIED_BY** - Код пользователя, в последний раз изменившего элемент. - **DATE_CREATE** - Дата создания элемента. - **CREATED_BY** - Код пользователя, создавшего элемент. - **DETAIL_PICTURE** - Код картинки в таблице файлов для детального просмотра. Кроме того, можно вывести пользовательские свойства, если задать их код (см. примечание ниже). | 6.0.3 |
| arNavStartParams | Массив для постраничной навигации. Может содержать следующие ключи: - **bShowAll** - разрешить вывести все элементы при постраничной навигации; - **iNumPage** - номер страницы при постраничной навигации; - **nPageSize** - количество элементов на странице при постраничной навигации; - **nTopCount** - ограничить количество возвращаемых методом записей сверху значением этого ключа (ключ доступен с версии **15.5.5**). Если в параметр передать пустой массив, то результат выборки будет ограничен десятью записями. А если передать значение *false* - то выборка будет полной. | 11.0.0 |


#### Возвращаемое значение

Возвращается объект [CIBlockResult](../ciblockresult/index.md)**Примечание №1:**для вывода пользовательских свойств обязательно должен быть передан *IBLOCK_ID*и в arSelect код необходимых свойств *UF_XXX*. Если необходимо вывести все пользовательские свойства, то в arSelect необходимо передать *UF_**.

**Примечание №2:**поле для сортировки *left_margin*, так называемая "сквозная" сортировка, высчитывается на основании поля *sort*, уровня вложенности и сортировкой верхнего уровня. Отличие полей *sort*и *left_margin*в том, что *sort*указывается пользователем, для сортировки разделов между собой в пределах одного раздела-родителя, а вычисляемое *left_margin*предназначено для сортировки во всем информационном блоке.

**Примечание №3:**нет возможности фильтровать разделы в выборке по количеству элементов.


#### Дополнительно

Выбор пользовательских свойств разделов возможен только при передаче в ключ фильтра IBLOCK_ID одиночного значения.

---
### Примеры использования

Пример 1:


```
<?
$arIBTYPE = CIBlockType::GetByIDLang($type, LANGUAGE_ID);
if($arIBTYPE!==false)
{
	// выборка только активных разделов из инфоблока $IBLOCK_ID, в которых есть элементы
	// со значением свойства SRC, начинающееся с https://
	$arFilter = Array('IBLOCK_ID'=>$IBLOCK_ID, 'GLOBAL_ACTIVE'=>'Y', 'PROPERTY'=>Array('SRC'=>'https://%'));
	$db_list = CIBlockSection::GetList(Array($by=>$order), $arFilter, true);
	$db_list->NavStart(20);
	echo $db_list->NavPrint($arIBTYPE["SECTION_NAME"]);
	while($ar_result = $db_list->GetNext())
	{
		echo $ar_result['ID'].' '.$ar_result['NAME'].': '.$ar_result['ELEMENT_CNT'].'<br>';
	}
	echo $db_list->NavPrint($arIBTYPE["SECTION_NAME"]);
}
?>
```

Пример 2:


```
//пример выборки дерева подразделов для раздела
$rsParentSection = CIBlockSection::GetByID(ID_необходимой_секции);
if ($arParentSection = $rsParentSection->GetNext())
{
	$arFilter = array('IBLOCK_ID' => $arParentSection['IBLOCK_ID'],'>LEFT_MARGIN' => $arParentSection['LEFT_MARGIN'],'<RIGHT_MARGIN' => $arParentSection['RIGHT_MARGIN'],'>DEPTH_LEVEL' => $arParentSection['DEPTH_LEVEL']); // выберет потомков без учета активности
	$rsSect = CIBlockSection::GetList(array('left_margin' => 'asc'),$arFilter);
	while ($arSect = $rsSect->GetNext())
	{
		// получаем подразделы
	}
}
```

Пример 3:


```
//в шаблоне меню, построенного по структуре инфоблока, менять ссылку на элемент, если заполнено пользовательское поле

<?
//внутри цикла построения меню
$uf_iblock_id = 1; //ID инфоблока
$uf_name = Array("UF_PAGE_LINK"); //пользовательское поле UF_PAGE_LINK

preg_match('/\?ID=([0-9]+)\&?/i', $arItem["LINK"], $matches); //SEF отключен, поэтому спокойно берем SECTION_ID из ссылки по шаблону ID=#SECTION_ID#
$uf_section_id = $matches[1];
if(CModule::IncludeModule("iblock")): //подключаем модуль инфоблок для работы с классом CIBlockSection
	$uf_arresult = CIBlockSection::GetList(Array("SORT"=>"­­ASC"), Array("IBLOCK_ID" => $uf_iblock_id, "ID" => $uf_section_id), false, $uf_name);
	if($uf_value = $uf_arresult->GetNext()):
		if(strlen($uf_value["UF_PAGE_LINK"]) > 0): //проверяем что поле заполнено
			$arItem["LINK"] = $uf_value["UF_PAGE_LINK"]; //подменяем ссылку и используем её в дальнейшем
		endif;
	endif;
endif;
?>
```

Пример 4:


```
//рассмотрим разницу использования фильтра по LEFT_MARGIN, RIGHT_MARGIN и LEFT_BORDER, RIGHT_BORDER
//допустим, что у некоторого раздела LEFT_MARGIN (значение в базе) = 10, RIGHT_MARGIN (значение в базе) = 40

//в первом примере кода будет выбран как сам раздел, так и все его подразделы,
//поскольку всегда LEFT_MARGIN раздела-потомка > LEFT_MARGIN раздела-родителя
//и RIGHT_MARGIN раздела-потомка < RIGHT_MARGIN раздела-родителя

$arFilter = array('IBLOCK_ID' => 10, 'LEFT_MARGIN' => 10, 'RIGHT_MARGIN' => 40);
$rsSections = CIBlockSection::GetList(array('LEFT_MARGIN' => 'ASC'), $arFilter);
while ($arSection = $rsSections->Fetch())
{
	echo htmlspecialcharsbx($arSection['NAME']).' LEFT_MARGIN: '.$arSection['LEFT_MARGIN'].' RIGHT_MARGIN: '.$arSection['RIGHT_MARGIN'].'&ltbr>';
}

//во втором примере кода будет возвращена только одна запись - сам раздел

$arFilter = array('IBLOCK_ID' => 10, 'LEFT_BORDER' => 10, 'RIGHT_BORDER' => 40);
$rsSections = CIBlockSection::GetList(array('LEFT_MARGIN' => 'ASC'), $arFilter);
while ($arSction = $rsSections->Fetch())
{
	echo htmlspecialcharsbx($arSection['NAME']).' LEFT_MARGIN: '.$arSection['LEFT_MARGIN'].' RIGHT_MARGIN: '.$arSection['RIGHT_MARGIN'].'<br>';
}
```

<p>Пример 5:</p>
<pre class="syntax">
//ограничения на количество элементов для вывода:
$res = CIBlockElement::GetList(
     $arOrder = Array("SORT"=>"DESC") , //Сортировка в обратном порядке
     $arFilter = array('IBLOCK_ID'=>1),
     $arGroupBy = false,
     $arNavStartParams = Array("nTopCount"=>4) //Выведет 4 элемента
);
</pre>
--!>

</div>
<!-----



Страницы: 1 2След.
| ![](../images/3ade78de6e.jpg) 3 **Олег Постоев**18.10.2023 17:25:24 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Поиск по UF_* с отрицанием не работает, как это устроено при работе с элементами. То есть, вместо: \| Код \| \| --- \| \| ``` '!UF_MY_BOOL' => true ``` \| нужно использовать: \| Код \| \| --- \| \| ``` 'UF_MY_BOOL' => false ``` \| | Код | ``` '!UF_MY_BOOL' => true ``` | Код | ``` 'UF_MY_BOOL' => false ``` |
| Код |  |  |  |  |
| ``` '!UF_MY_BOOL' => true ``` |  |  |  |  |
| Код |  |  |  |  |
| ``` 'UF_MY_BOOL' => false ``` |  |  |  |  |
|  |  |  |  |  |


| ![](../images/73f104d41a.jpg) 3 **Виталий Савицкий**22.03.2023 17:42:13 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Самая короткая запись, чтобы найти id раздела (секции) по символьному коду родительского информационного блока и символьному коду самого искомого раздела: \| Код \| \| --- \| \| ``` $sectionId = CIBlockSection::GetList([], ['IBLOCK_CODE' => 'iblocCode', 'CODE' => 'sectionCode'])->Fetch()['ID']; ``` \| И то же самое, только по id родительского информационного блока: \| Код \| \| --- \| \| ``` $sectionId = CIBlockSection::GetList([], ['IBLOCK_ID' => 1, 'CODE' => 'sectionCode'])->Fetch()['ID']; ``` \| | Код | ``` $sectionId = CIBlockSection::GetList([], ['IBLOCK_CODE' => 'iblocCode', 'CODE' => 'sectionCode'])->Fetch()['ID']; ``` | Код | ``` $sectionId = CIBlockSection::GetList([], ['IBLOCK_ID' => 1, 'CODE' => 'sectionCode'])->Fetch()['ID']; ``` |
| Код |  |  |  |  |
| ``` $sectionId = CIBlockSection::GetList([], ['IBLOCK_CODE' => 'iblocCode', 'CODE' => 'sectionCode'])->Fetch()['ID']; ``` |  |  |  |  |
| Код |  |  |  |  |
| ``` $sectionId = CIBlockSection::GetList([], ['IBLOCK_ID' => 1, 'CODE' => 'sectionCode'])->Fetch()['ID']; ``` |  |  |  |  |
|  |  |  |  |  |


| ![](../images/03ba6d72d6.jpg) 0 **Александр Николаев**29.11.2022 15:35:30 |  |  |
| --- | --- | --- |
| Вывел картинку раздела по пользовательское полю раздела UF_FILE в catalog.section.list \| Код \| \| --- \| \| ``` foreach($arResult["SECTIONS"] as $k=>$s){ $db_list = CIBlockSection::GetList(Array($by => $order), $arFilter = Array("IBLOCK_ID" => $arParams["IBLOCK_ID"], "ID" => $s["ID"]), true, $arSelect = Array("UF_FILE")); while ($ar_result = $db_list->GetNext()) { $arResult["SECTIONS"][$k]["PIC"] = CFile::GetPath($ar_result["UF_FILE"]); } } ``` \| | Код | ``` foreach($arResult["SECTIONS"] as $k=>$s){ $db_list = CIBlockSection::GetList(Array($by => $order), $arFilter = Array("IBLOCK_ID" => $arParams["IBLOCK_ID"], "ID" => $s["ID"]), true, $arSelect = Array("UF_FILE")); while ($ar_result = $db_list->GetNext()) { $arResult["SECTIONS"][$k]["PIC"] = CFile::GetPath($ar_result["UF_FILE"]); } } ``` |
| Код |  |  |
| ``` foreach($arResult["SECTIONS"] as $k=>$s){ $db_list = CIBlockSection::GetList(Array($by => $order), $arFilter = Array("IBLOCK_ID" => $arParams["IBLOCK_ID"], "ID" => $s["ID"]), true, $arSelect = Array("UF_FILE")); while ($ar_result = $db_list->GetNext()) { $arResult["SECTIONS"][$k]["PIC"] = CFile::GetPath($ar_result["UF_FILE"]); } } ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 1 **ocpbbtx**14.07.2020 10:10:47 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Сортировка разделов по пользовательскому свойству: \| Код \| \| --- \| \| ``` $arSort = array( "UF_RATING"=>"asc", ); ``` \| Это все можно передать в подключение компонента "bitrix:catalog.section.list" Там есть параметр: CUSTOM_SECTION_SORT \| Код \| \| --- \| \| ``` <?$APPLICATION->IncludeComponent( "bitrix:catalog.section.list", ".default", Array( "IBLOCK_TYPE" => $arParams["IBLOCK_TYPE"], "IBLOCK_ID" => $arParams["IBLOCK_ID"], "CUSTOM_SECTION_SORT"=>$arSort, .... ``` \| И вуаля, все отфильтруется! | Код | ``` $arSort = array( "UF_RATING"=>"asc", ); ``` | Код | ``` <?$APPLICATION->IncludeComponent( "bitrix:catalog.section.list", ".default", Array( "IBLOCK_TYPE" => $arParams["IBLOCK_TYPE"], "IBLOCK_ID" => $arParams["IBLOCK_ID"], "CUSTOM_SECTION_SORT"=>$arSort, .... ``` |
| Код |  |  |  |  |
| ``` $arSort = array( "UF_RATING"=>"asc", ); ``` |  |  |  |  |
| Код |  |  |  |  |
| ``` <?$APPLICATION->IncludeComponent( "bitrix:catalog.section.list", ".default", Array( "IBLOCK_TYPE" => $arParams["IBLOCK_TYPE"], "IBLOCK_ID" => $arParams["IBLOCK_ID"], "CUSTOM_SECTION_SORT"=>$arSort, .... ``` |  |  |  |  |
|  |  |  |  |  |


| ![](../images/00a36d1d02.JPG) 5 **Эдуард Пащенко**15.06.2020 11:00:34 |
| --- |
| Если вы хотите выбрать подразделы раздела, то необходимо id основного раздела передавать с ключом SECTION_ID, а не IBLOCK_SECTION_ID (как указано в доке) |
|  |


| ![](../images/505bdd5535.png) 3 **Антон Царук**18.12.2016 00:05:26 |
| --- |
| Фильтрация разделов по пользовательскому свойству типа "Дата" производится "в формате сайта", а не в формате БД. То есть, в фильтре надо писать даты в формате d.m.Y, а не Y-m-d, как следует из логики... |
|  |


| ![image](../images/7dd82aba60.gif) 0 **Пётр Громов**15.12.2016 12:06:59 |
| --- |
| Если в arFilter нет фильтрации по IBLOCK_ID, а например, только айдишник секции, все выборки UF_( |
|  |


| ![image](../images/7dd82aba60.gif) 10 **Алексей Сучков**15.06.2016 15:33:54 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Если вам нужно вывести постраничную навигацию разделов (для старта отлично подойдёт компонет news.list): \| Код \| \| --- \| \| ``` $rsSections = CIBlockSection::GetList($arSort, array_merge($arFilter, $arrFilter),false, array("ID","IBLOCK_ID","IBLOCK_SECTION_ID","NAME","DESCRIPTION","UF_*"),$arNavParams); while ($arSection = $rsSections->Fetch()) { $arResult["ITEMS"][]=$arSection; } $arResult["NAV_STRING"] = $rsSections->GetPageNavStringEx( $navComponentObject, $arParams["PAGER_TITLE"], $arParams["PAGER_TEMPLATE"], $arParams["PAGER_SHOW_ALWAYS"], $this, $navComponentParameters ); $arResult["NAV_CACHED_DATA"] = null; $arResult["NAV_RESULT"] = $rsSections; $arResult["NAV_PARAM"] = $navComponentParameters; ``` \| Если у вас не трансформируется "SECTION_PAGE_URL" и выводится вида #SITE_DIR#/какой-то путь/#SECTION_CODE_PATH#/ и вы в селекте указали все необходимые поля ("ID","IBLOCK_ID","IBLOCK_TYPE_ID","IBLOCK_SECTION_ID","CODE" ![;)](../images/d4c2237403.png) скорее всего вы делаете выборку через Fetch, попробуйте заменить его на GetNext: \| Код \| \| --- \| \| ``` $SectList = CIBlockSection::GetList($arSort, array("IBLOCK_ID"=>$arParams["IBLOCK_ID"],"ACTIVE"=>"Y") ,false, array("ID","IBLOCK_ID","IBLOCK_TYPE_ID","IBLOCK_SECTION_ID","CODE","SECTION_ID","NAME","SECTION_PAGE_URL")); while ($SectListGet = $SectList->GetNext()) { $arResult["LIST"][]=$SectListGet; } ``` \| | Код | ``` $rsSections = CIBlockSection::GetList($arSort, array_merge($arFilter, $arrFilter),false, array("ID","IBLOCK_ID","IBLOCK_SECTION_ID","NAME","DESCRIPTION","UF_*"),$arNavParams); while ($arSection = $rsSections->Fetch()) { $arResult["ITEMS"][]=$arSection; } $arResult["NAV_STRING"] = $rsSections->GetPageNavStringEx( $navComponentObject, $arParams["PAGER_TITLE"], $arParams["PAGER_TEMPLATE"], $arParams["PAGER_SHOW_ALWAYS"], $this, $navComponentParameters ); $arResult["NAV_CACHED_DATA"] = null; $arResult["NAV_RESULT"] = $rsSections; $arResult["NAV_PARAM"] = $navComponentParameters; ``` | Код | ``` $SectList = CIBlockSection::GetList($arSort, array("IBLOCK_ID"=>$arParams["IBLOCK_ID"],"ACTIVE"=>"Y") ,false, array("ID","IBLOCK_ID","IBLOCK_TYPE_ID","IBLOCK_SECTION_ID","CODE","SECTION_ID","NAME","SECTION_PAGE_URL")); while ($SectListGet = $SectList->GetNext()) { $arResult["LIST"][]=$SectListGet; } ``` |
| Код |  |  |  |  |
| ``` $rsSections = CIBlockSection::GetList($arSort, array_merge($arFilter, $arrFilter),false, array("ID","IBLOCK_ID","IBLOCK_SECTION_ID","NAME","DESCRIPTION","UF_*"),$arNavParams); while ($arSection = $rsSections->Fetch()) { $arResult["ITEMS"][]=$arSection; } $arResult["NAV_STRING"] = $rsSections->GetPageNavStringEx( $navComponentObject, $arParams["PAGER_TITLE"], $arParams["PAGER_TEMPLATE"], $arParams["PAGER_SHOW_ALWAYS"], $this, $navComponentParameters ); $arResult["NAV_CACHED_DATA"] = null; $arResult["NAV_RESULT"] = $rsSections; $arResult["NAV_PARAM"] = $navComponentParameters; ``` |  |  |  |  |
| Код |  |  |  |  |
| ``` $SectList = CIBlockSection::GetList($arSort, array("IBLOCK_ID"=>$arParams["IBLOCK_ID"],"ACTIVE"=>"Y") ,false, array("ID","IBLOCK_ID","IBLOCK_TYPE_ID","IBLOCK_SECTION_ID","CODE","SECTION_ID","NAME","SECTION_PAGE_URL")); while ($SectListGet = $SectList->GetNext()) { $arResult["LIST"][]=$SectListGet; } ``` |  |  |  |  |
|  |  |  |  |  |


| ![](../images/72312d3fd6.jpg) 8 **Дмитрий Гуров**21.09.2015 15:18:57 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Получаем разделы и вложенные подразделы в иерархическом виде: \| Код \| \| --- \| \| ``` <?php function getSectionList($filter, $select) { $dbSection = CIBlockSection::GetList( Array( 'LEFT_MARGIN' => 'ASC', ), array_merge( Array( 'ACTIVE' => 'Y', 'GLOBAL_ACTIVE' => 'Y' ), is_array($filter) ? $filter : Array() ), false, array_merge( Array( 'ID', 'IBLOCK_SECTION_ID' ), is_array($select) ? $select : Array() ) ); while( $arSection = $dbSection-> GetNext(true, false) ){ $SID = $arSection['ID']; $PSID = (int) $arSection['IBLOCK_SECTION_ID']; $arLincs[$PSID]['CHILDS'][$SID] = $arSection; $arLincs[$SID] = &$arLincs[$PSID]['CHILDS'][$SID]; } return array_shift($arLincs); } ?> ``` \| Пример использования: \| Код \| \| --- \| \| ``` <?php $arSections = getSectionList( Array( 'IBLOCK_ID' => 25 ), Array( 'NAME', 'SECTION_PAGE_URL' ) ); echo "<pre>"; var_dump($arSections); echo "</pre>"; ?> ``` \| | Код | ``` <?php function getSectionList($filter, $select) { $dbSection = CIBlockSection::GetList( Array( 'LEFT_MARGIN' => 'ASC', ), array_merge( Array( 'ACTIVE' => 'Y', 'GLOBAL_ACTIVE' => 'Y' ), is_array($filter) ? $filter : Array() ), false, array_merge( Array( 'ID', 'IBLOCK_SECTION_ID' ), is_array($select) ? $select : Array() ) ); while( $arSection = $dbSection-> GetNext(true, false) ){ $SID = $arSection['ID']; $PSID = (int) $arSection['IBLOCK_SECTION_ID']; $arLincs[$PSID]['CHILDS'][$SID] = $arSection; $arLincs[$SID] = &$arLincs[$PSID]['CHILDS'][$SID]; } return array_shift($arLincs); } ?> ``` | Код | ``` <?php $arSections = getSectionList( Array( 'IBLOCK_ID' => 25 ), Array( 'NAME', 'SECTION_PAGE_URL' ) ); echo "<pre>"; var_dump($arSections); echo "</pre>"; ?> ``` |
| Код |  |  |  |  |
| ``` <?php function getSectionList($filter, $select) { $dbSection = CIBlockSection::GetList( Array( 'LEFT_MARGIN' => 'ASC', ), array_merge( Array( 'ACTIVE' => 'Y', 'GLOBAL_ACTIVE' => 'Y' ), is_array($filter) ? $filter : Array() ), false, array_merge( Array( 'ID', 'IBLOCK_SECTION_ID' ), is_array($select) ? $select : Array() ) ); while( $arSection = $dbSection-> GetNext(true, false) ){ $SID = $arSection['ID']; $PSID = (int) $arSection['IBLOCK_SECTION_ID']; $arLincs[$PSID]['CHILDS'][$SID] = $arSection; $arLincs[$SID] = &$arLincs[$PSID]['CHILDS'][$SID]; } return array_shift($arLincs); } ?> ``` |  |  |  |  |
| Код |  |  |  |  |
| ``` <?php $arSections = getSectionList( Array( 'IBLOCK_ID' => 25 ), Array( 'NAME', 'SECTION_PAGE_URL' ) ); echo "<pre>"; var_dump($arSections); echo "</pre>"; ?> ``` |  |  |  |  |
|  |  |  |  |  |


| ![](../images/d5be55ed54.jpg) 0 **Денис Клоков**07.11.2014 15:35:57 |  |  |
| --- | --- | --- |
| Как происходит фильтрация по пользовательским полям секций: \| Код \| \| --- \| \| ``` $arFilter = array( "IBLOCK_ID" => 5, "UF_PROP1" => "1" // Пользовательское свойство - число ); $res = CIBlockSection::GetList($arSort, $arFilter, false, $arSelect); ``` \| | Код | ``` $arFilter = array( "IBLOCK_ID" => 5, "UF_PROP1" => "1" // Пользовательское свойство - число ); $res = CIBlockSection::GetList($arSort, $arFilter, false, $arSelect); ``` |
| Код |  |  |
| ``` $arFilter = array( "IBLOCK_ID" => 5, "UF_PROP1" => "1" // Пользовательское свойство - число ); $res = CIBlockSection::GetList($arSort, $arFilter, false, $arSelect); ``` |  |  |
|  |  |  |

Страницы: 1 2След.
