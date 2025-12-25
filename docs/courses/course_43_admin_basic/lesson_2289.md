# Дополнительные методы

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3574 — Внешняя авторизация](lesson_3574.md)
- [Следующий: 3008 — Переопределение входящих переменных →](lesson_3008.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2289

#### Дополнительные методы, доступные в компонентах и шаблонах

В компонентах и шаблонах можно использовать дополнительные методы из класса [CComponentEngine](http://dev.1c-bitrix.ru/api_help/main/reference/ccomponentengine/index.php).

`string CComponentEngine::MakePathFromTemplate($pageTemplate, $arParams);`

где:

`$pageTemplate` - шаблон вида `/catalog/#IBLOCK_ID#/section/#SECTION_ID#.php` или `catalog.php?BID=#IBLOCK_ID#&SID=#SECTION_ID#`,

`$arParams` - ассоциативный массив замен параметров, в котором ключ - это название параметра, а значение - это значение параметра. Возвращает путь на основании шаблона пути `$pageTemplate` и массива замен.

Пример:

```
$url = CComponentEngine::MakePathFromTemplate
("/catalog/#IBLOCK_ID#/section/#SECTION_ID#.php",
	array(
		"IBLOCK_ID" => 21,
		"SECTION_ID" => 452
		)
);
```

#### Организация явной связи между компонентами на одной странице комплексного компонента

Явную связь можно организовывать через возвращаемые значения и входящие параметры этих компонентов.

Если из компонента **comp1** нужно передать данные в компонент **comp2**, то в конце кода компонента **comp1** нужно написать: `return данные;`

Подключить **comp1** нужно следующим образом:

`$result = $APPLICATION->IncludeComponent(comp1, ...);`

Теперь данные находятся в переменной `$result` и их можно передать входящими параметрами в **comp2**.
