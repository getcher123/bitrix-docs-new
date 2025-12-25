# Классы компонентов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2499 — Переменные в компоненте 2.0](lesson_2499.md)
- [Следующий: 2898 — Примеры решения задач →](lesson_2898.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2028

### Поддержка классов

|  | **[Зайцев Артемий](http://dev.1c-bitrix.ru/community/blogs/user/25773.php)**:<br>
<br>Сейчас думаю, что большие компоненты - это зло, даже с классами. Выношу классы в отдельные файлы и автолоадом подключаю.<br>
<br>Но бывает так, что нужна в компоненте пара функций. И тогда такой класс будет очень полезным. А еще статические переменные в классе.
<br>
<br>[**Максим Смирнов**](http://dev.1c-bitrix.ru/community/blogs/oracle/):<br>
<br>
<br>Проектировалось именно с прицелом на это.<br>
<br>Тяжелую бизнес логику лучше держать в такой сущности как "модуль". |
| --- | --- |

Поддержка классов компонентов реализована в виде файла `/component_name/class.php`. Имя **class.php** - зарезервированно. Этот файл автоматически подключается при вызове:

```
$APPLICATION->IncludeComponent()
```

При этом происходит вызов final метода *initComponent* в котором и подключается **class.php** (если он есть) и из него берется самый последний класс наследник от [CBitrixComponent](http://dev.1c-bitrix.ru/api_help/main/reference/cbitrixcomponent/index.php).

Действия вида:

```
class CDemoTest extends CBitrixComponent{}
class CDemoTestDecorator1 extends CDemoTest {}
class CDemoTestDecorator2 extends CDemoTest {}
```

не будут иметь успеха. В итоге будет использоваться *CDemoTestDecorator2*.

Учтите что при изменении базового класса  компонента нужно будет учитывать поведение всех его потомков (других компонентов).

### Пример

Рассмотрим простейший компонент возводящий параметр в квадрат.

Файл `/bitrix/components/demo/sqr/component.php:`



```
<?if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();

$arParams["X"] = intval($arParams["X"]);
if($this->startResultCache()) //startResultCache используется не для кеширования html, а для кеширования arResult
{
	$arResult["Y"] = $arParams["X"] * $arParams["X"];
}
$this->includeComponentTemplate();
?>
```

Файл `/bitrix/components/demo/sqr/templates/.default/template.php`:

```
<?if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();?>
<div class="equation">
<?echo $arParams["X"];?> в квадрате равно <?echo $arResult["Y"];?>
</div>
```

В реальных компонентах вместо операции умножения может быть три десятка строк и таких операций может быть 5-6. В результате файл **component.php** превращается в тяжело понимаемую "вещь в себе".

Выделяем логику компонента в класс.

Файл `/bitrix/components/demo/sqr/class.php`:

```
<?if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();

class CDemoSqr extends CBitrixComponent
{
	// Подготавливаем параметры компонента

	public function onPrepareComponentParams($arParams)
	{
		$result = array(
			"CACHE_TYPE" => $arParams["CACHE_TYPE"],
			"CACHE_TIME" => isset($arParams["CACHE_TIME"]) ?$arParams["CACHE_TIME"]: 36000000,
			"X" => intval($arParams["X"]),
		);
		return $result;
	}

	public function sqr($x)
	{
		return $x * $x;
	}
}?>
```

Файл `/bitrix/components/demo/sqr/component.php`:

```
<?if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();

if($this->startResultCache())//startResultCache используется не для кеширования html, а для кеширования arResult
{
	//$this - экземпляр CDemoSqr
	$arResult["Y"] = $this->sqr($arParams["X"]);
}
$this->includeComponentTemplate();
?>
```

Теперь код в файле **component.php** стал управляемым.

### Наследование

Например:

Файл `/bitrix/components/demo/double_sqr/class.php`:

```
<?if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();

//Необходимо для корректного поиска класса CDemoSqr
CBitrixComponent::includeComponentClass("demo:sqr");
//Наследник расширяющий функциональность:
class CDemoDoubleSqr extends CDemoSqr
{
	public function sqr($x)
	{
		return parent::sqr($x)*2;
	}
}?>
```

Файл `/bitrix/components/demo/double_sqr/component.php` идентичен файлу `/bitrix/components/demo/sqr/component.php`, можно просто скопировать содержание.

Файл `/bitrix/components/demo/double_sqr/templates/.default/template.php`:

```
<?if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();?>
<div class="equation">
<?echo $arParams["X"];?> в квадрате умноженное на два равно <?echo $arResult["Y"];?>
</div>
```

### Компонент без component.php

Создать компонент можно и без файла **component.php**

Для этого достаточно перекрыть метод *executeComponent*. Например:

```
class CDemoSqr extends CBitrixComponent
{
...
	public function executeComponent()
	{
		if($this->startResultCache())
	{
		$this->arResult["Y"] = $this->sqr($this->arParams["X"]);
		$this->includeComponentTemplate();
	}
	return $this->arResult["Y"];
	}
};
```

Теперь из обоих компонентов можно удалить файлы **component.php**.

Обратите внимание, что глобальные переменные недоступны в методе executeComponent() в файле class.php, в отличие от файла component.php. Добавьте строку `global $APPLICATION;`, чтобы использовать глобальные переменные. Например:

```
global $APPLICATION;

// теперь можно вызвать глобальную переменную
$APPLICATION->SetTitle('header');
```
