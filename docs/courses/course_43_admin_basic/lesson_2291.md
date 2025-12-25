# Пример. Вывод голосования

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2896 — Модификация шаблона простого компонента в составе комплексного](lesson_2896.md)
- [Следующий: 2895 — Пример. Добавление типа отсутствия →](lesson_2895.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2291

**Задача**:

1. Выдать голосование не в детальном товаре, а на странице со списком товаров.
2. Выдать ее на AJAX стандартными средствами



В каталоге нет голосования. Зато оно есть в комплексном компоненте **Новости**, в детальном просмотре элемента.

**Решение** (для слабоподготовленного разработчика, методом копи-паст).

#### Первая часть задачи

В шаблоне комплексного компонента **Новости** находим такой код:

```
<?$APPLICATION->IncludeComponent(
	"bitrix:iblock.vote",
	"",
	Array(
		"IBLOCK_TYPE" => $arParams["IBLOCK_TYPE"],
		"IBLOCK_ID" => $arParams["IBLOCK_ID"],
		"ELEMENT_ID" => $ElementID,
		"MAX_VOTE" => $arParams["MAX_VOTE"],
		"VOTE_NAMES" => $arParams["VOTE_NAMES"],
		"CACHE_TYPE" => $arParams["CACHE_TYPE"],
		"CACHE_TIME" => $arParams["CACHE_TIME"],
	),
	$component
);?>
```

Вставляем этот код в шаблон компонента **bitrix:catalog.top** куда-нибудь, где он должен выводиться. Например, в таблицу после вывода `<?=$arElement["PREVIEW_TEXT"]?>.`

Теперь нужно сделать, чтобы голосование выводилось для нужного нам элемента. Меняем строку:

`"ELEMENT_ID" => $ElementID,`

на

`"ELEMENT_ID" =>$arElement["ID"],`

#### Вторая часть задачи

В папке с шаблонами компонента **bitrix:iblock.vote** есть два шаблона: .default и ajax. Применяем второй. Вторая проблема тоже решена.
В итоге вызов компонента получился вот таким:

```
<?$APPLICATION->IncludeComponent(
	"bitrix:iblock.vote",
	"ajax",
	Array(
		"IBLOCK_TYPE" => $arParams["IBLOCK_TYPE"],
		"IBLOCK_ID" => $arParams["IBLOCK_ID"],
		"ELEMENT_ID" =>$arElement["ID"],
		"MAX_VOTE" => $arParams["MAX_VOTE"],
		"VOTE_NAMES" => $arParams["VOTE_NAMES"],
		"CACHE_TYPE" => $arParams["CACHE_TYPE"],
		"CACHE_TIME" => $arParams["CACHE_TIME"],
	),
	$component
);?>
```
