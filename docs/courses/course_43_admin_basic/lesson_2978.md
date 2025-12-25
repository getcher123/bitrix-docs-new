# Сache Dependencies (тегированный кеш)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2995 — Пример. Исключение шаблона компонента из кэша](lesson_2995.md)
- [Следующий: 5284 — Пример. Добавление своего тега →](lesson_5284.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2978

### Теги кеша

Главный модуль поддерживает

			теги кеша

                    Тегируется не выборка, а файл кеша.

		. Кеш можно помечать тегами и сбрасывать по ним. Сброс кеша компонентов инфоблоков происходит при изменении в них информации.

**Внимание!** Для часто обновляемого большого массива данных использовать тегированный кеш не оправданно.

Базовый код тегирования кеша:

```
01: $cache_id = md5(serialize($arParams));
02: $cache_dir = "/tagged_getlist";
03:
04: $obCache = new CPHPCache;
05: if($obCache->InitCache(36000, $cache_id, $cache_dir))
06: {
07: 	$arElements = $obCache->GetVars();
08: }
09: elseif(CModule::IncludeModule("iblock") && $obCache->StartDataCache())
10: {
11: 	$arElements = array();
12: 	$rsElements = CIBlockElement::GetList($arParams["order"], $arParams["filter"]);
13:
14: 	global $CACHE_MANAGER;
15: 	$CACHE_MANAGER->StartTagCache($cache_dir);
16: 	while($arElement = $rsElements->Fetch())
17: 	{
18: 		$CACHE_MANAGER->RegisterTag("iblock_id_".$arElement["IBLOCK_ID"]);
19: 		$arElements[] = $arElement;
20: 	}
21: 		$CACHE_MANAGER->RegisterTag("iblock_id_new");
22: 		$CACHE_MANAGER->EndTagCache();
23:
24: 		$obCache->EndDataCache($arElements);
25: }
26: else
27: {
28: 	$arElements = array();
29: }
```

В строке 01 инициализируется уникальный идентификатор файла кеша. Далее определяется каталог относительно `/bitrix/cache`, в котором будут сохранятся файлы кеша с разными значениями `$arParams`. Важно, что этот путь начинается со слеша и им не заканчивается. При использовании в качестве кеша **memcached** или **APC** это будет критичным при сбросе кеша.

В строках 04-05 инициализируется объект кеша. Если время кеширования не истекло, то будет выполнена строка 07 и мы получим данные из файла кеша.

Условие в строке 09 фактически всегда будет `true`. Это подключение модуля и начало кеширования.

В строке 12 происходит обращение к базе данных. Важно, чтобы все параметры от которых зависит результат выборки "поучаствовали" в идентификаторе кеша (`$cache_id`).

В 14-й строчке объявляется доступ к переменной `$CACHE_MANAGER`. Этот объект будет управлять тегами.

Строка 15 — все последующие назначаемые теги будут привязаны к каталогу `$cache_dir`. При сбросе кеша по одному из них содержимое этого каталога будет удалено. То есть если в один каталог пишется кеш с разными тегами, при сбросе кеша только по одному тегу все равно будет удален весь кеш.

`StartTagCache` — может использоваться вложено. Например:

```
$CACHE_MANAGER->StartTagCache($cache_dir1);
	$CACHE_MANAGER->StartTagCache($cache_dir2);
		$CACHE_MANAGER->StartTagCache($cache_dir3);
		$CACHE_MANAGER->EndTagCache();
	$CACHE_MANAGER->EndTagCache();
$CACHE_MANAGER->EndTagCache();
```

Важно чтобы вызовы *StartTagCache* и *EndTagCache* были сбалансированы. Объект `$CACHE_MANAGER` создает и отслеживает стек каталогов кеша. При этом теги назначенные на каталог `$cache_dir3` будут также связаны и с `$cache_dir2` и `$cache_dir1`. Теги назначенные на `cache_dir2` будут связаны и с `$cache_dir1`.

В строке 18 происходит отметка кеша тегом с помощью метода *RegisterTag*. Длина тела может быть до 100 символов. В методе *RegisterTag* автоматически удаляются дубликаты тегов.

Строка 21 — необходима для сброса кеша при добавлении нового инфоблока, ведь у него на момент создания кеша тег не записывается (инфоблока ещё нет).

Строка 22 — запись тегов каталога в таблицу базы данных. Можно считать по одному insert'у на тег.

Сброс кеша:

```
$CACHE_MANAGER->ClearByTag("iblock_id_7");
```

или (с 15.0.7):

```
CIBlock::clearIblockTagCache( 7 );
```

Для отключения тегирования конкретных инфоблоков используйте:

```
CIBlock::DisableTagCache($iblock_id)
```

### Компоненты инфоблоков

Для запуска механизма необходимо определить константу в файле **dbconn.php**. (Это можно сделать простым включением Управляемого кеша на закладке **Управляемый кеш** на странице Настройки &gt; Настройки продукта &gt; Автокеширование.)

```
define("BX_COMP_MANAGED_CACHE", true);
```

При этом в методе [StartResultCache](http://dev.1c-bitrix.ru/api_help/main/reference/cbitrixcomponent/startresultcache.php) компонента будет вызываться *StartTagCache* с путем к кешу компонента (с учетом страницы). А в методе *EndResultCache* (который в свою очередь вызывается из *IncludeComponentTemplate*) — *EndTagCache*.

В модуле инфоблоков [CIBlockElement::GetList](http://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/getlist.php) и [CIBlockSection::GetList](http://dev.1c-bitrix.ru/api_help/iblock/classes/ciblocksection/getlist.php) возвращают объект класса [CIBlockResult](http://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockresult/index.php).

В методе *Fetch/GetNext* этого объекта будут вызываться `$CACHE_MANAGER->RegisterTag("iblock_id_".$res["IBLOCK_ID"]);`.

Если выборка не содержит элементов, то значение идентификатора инфоблока будет взято из фильтра.

Если выборка НЕ пустая, в arSelect не запрашивается IBLOCK_ID, но есть фильтрация по IBLOCK_ID, то сброс кеша произойдёт.

Сброс кеша вызывается из методов *Add/Update/Delete* для элементов, разделов и инфоблоков.

Не стоит использовать этот механизм при частом обновлении элементов или разделов. С другой стороны это должно быть удобным для редакторов сайтов: изменения моментально отображаются на сайте. Еще один плюс — можно задавать практически бесконечное время кеширования.
