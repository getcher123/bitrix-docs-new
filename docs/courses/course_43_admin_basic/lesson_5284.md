# Пример. Добавление своего тега

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2978 — Сache Dependencies (тегированный кеш)](lesson_2978.md)
- [Следующий: 3796 — Пример. Сортировка в компонентах →](lesson_3796.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=5284

При выполнении инструкций по добавлению своего тега к кешам компонентов подразумевается, что у вас включено [тегированное кеширование](lesson_2978.md).

### Способ 1

В тело компонента добавьте следующий код:

```

if ($this->StartResultCache(......))
{
	if (defined('BX_COMP_MANAGED_CACHE') && is_object($GLOBALS['CACHE_MANAGER']))
	{
		$GLOBALS['CACHE_MANAGER']->RegisterTag('my_custom_tag');
	}

	// do something

	$this->IncludeComponentTemplate();
}
else
{
	$this->AbortResultCache();
}
```

### Способ 2

В шаблон компонента (в **result_modifier.php**) добавьте следующий код:

```

<?
if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();

if (defined('BX_COMP_MANAGED_CACHE') && is_object($GLOBALS['CACHE_MANAGER']))
{
	$cp =& $this->__component;
	if (strlen($cp->getCachePath()))
	{
		$GLOBALS['CACHE_MANAGER']->RegisterTag('my_custom_tag');
	}
}
?>
```

Чтобы сбросить все кеши, помеченные вашим тегом, выполните следующий код:

```
if (defined('BX_COMP_MANAGED_CACHE') && is_object($GLOBALS['CACHE_MANAGER']))
	$GLOBALS['CACHE_MANAGER']->ClearByTag('my_custom_tag');
```

**Примечание:**один и тот же кеш может быть помечен несколькими тегами. Например, если вы пометите своим тегом кеш компонента **bitrix:news.list**, то у кеша будет два тега: штатный "iblock_id_XX" и ваш "my_custom_tag". Соответственно, кеш будет сбрасываться и при добавлении/изменении элемента в инфоблоке XX (штатный функционал), и при сбросе кеша вручную через `ClearByTag('my_custom_tag')`.
