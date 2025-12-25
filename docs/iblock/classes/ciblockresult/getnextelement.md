# GetNextElement


### Описание и параметры


```
_CIBElement
CIBlockResult::GetNextElement(
	bool bTextHtmlAuto =  true,
	bool use_tilda =  true
);
```

Метод возвращает из выборки объект [_CIBElement](../cibelement/index.md). Нестатический метод.


#### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| $bTextHtmlAuto | Параметр передается в [CDBResult::GetNext](../../../main/reference/cdbresult/getnext.md). Необязательный, по умолчанию принимает *true*. | 7.1.1 |
| use_tilda |  |  |


#### Возвращаемое значение

Метод возвращает из выборки объект [_CIBElement](../cibelement/index.md), и передвигает курсор на следующую запись.
Если достигнута последняя запись (или в результате нет ни одной записи), метод вернет false. ---
### Смотрите также


- [_CIBElement](../cibelement/index.md) [CIBlockResult](index.md):: [GetNext()](getnext.md)[CIBlockElement](../ciblockelement/index.md):: [GetList()](../ciblockelement/getlist.md)

---
### Примеры использования


```
<?
$res = CIBlockElement::GetByID($_GET["PID"]);
if($obRes = $res->GetNextElement())
{
	$ar_res = $obRes->GetFields();
	echo $ar_res['NAME'];
}
?>
```


```
//выборка всех данных элемента:
$db_elemens = CIblockElement::GetList($arOrder, $arFilter, false, false, $arSelect);

while($obElement = $db_elemens->GetNextElement())
{
	$el = $obElement->GetFields();
	$el["PROPERTIES"] = $obElement->GetProperties();
		$arResult["ITEMS"][] = $el;
}

//Примечание: в данном случае в $arSelect ничего задавать не нужно (можно его вообще не писать). Так как функции GetFields и GetProperties выбирает все свойства, которые есть у элемента.
//Этот способ нужно использовать для выборки элементов, у которых есть множественные свойства, чтобы избежать дублирования элементов, которое наблюдается при стандартном вызове GetNext.
```

---
