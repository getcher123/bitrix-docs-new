# Механизм реализации

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3753 — Примеры работы](lesson_3753.md)
- [Следующий: 3437 — Работа со стилями в визуальном HTML-редакторе →](lesson_3437.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3517

Таблицы стилей подключаются к шаблону сайта в области пролога с помощью функции [ShowCSS()](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/showcss.php).

```
<?
$APPLICATION->ShowCSS();
?>
```

Функция *ShowCSS()* выполняет подключение файла стилей из текущего шаблона сайта, а также всех дополнительных стилей определенных для данной страницы функцией [SetAdditionalCSS()](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/setadditionalcss.php).

```
<?
$APPLICATION->SetAdditionalCSS("/bitrix/templates/demo/additional.css");
?>
```

Дополнительные стили могут использоваться, например, для оформления форума, веб-форм, таблиц, некоторых типов меню и т.д.

При использовании функции *ShowCSS()* без параметров подключение стилей будет выполнено в виде ссылки на CSS файл:

```
<LINK href="/bitrix/templates/demo/styles.css" type="text/css" rel="STYLESHEET">
```

При этом стили, подключаемые с использованием *SetAdditionalCSS()*, будут включены в код страницы с использованием PHP функции *require()* (т.е. будут полностью включены в итоговый код страницы).

В случае использования функции *ShowCSS()* с параметром `false` файл стилей для текущего дизайна будет также включен в код страницы с использованием *require()*:

```
<?
$APPLICATION->ShowCSS(false);
?>
```
