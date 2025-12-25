# GetGroups


```
CDBResult
_CIBElement::GetGroups();
```

Возвращает группы, которым принадлежит текущий элемент и значения свойств типа "привязка к разделам" заданные для данного элемента. Нестатический метод.


#### Возвращаемое значение

Возвращается объект [CDBResult](../../../main/reference/cdbresult/index.md)с полями разделов.
#### Смотрите также


- [CDBResult](../../../main/reference/cdbresult/index.md)
- [CIBlockElement::GetElementGroups](../ciblockelement/getelementgroups.md)


#### Примеры использования


```
<?
$res = CIBlockElement::GetByID($_GET["PID"]);
if($obRes = $res->GetNextElement())
{
	$ar_res = $obRes->GetGroups();
	print_r($ar_res);
}
?>
```
