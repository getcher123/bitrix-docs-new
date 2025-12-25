# GetFields


```
array
_CIBElement::GetFields();
```

Возвращает массив значений полей приведенный в HTML безопасный вид. Также в полях *DETAIL_PAGE_URL* и *LIST_PAGE_URL* заменяются шаблоны вида #IBLOCK_ID# и т.п. на их реальные значения, в результате чего в этих полях будут ссылки на страницу детального просмотра и страницу списка элементов. Нестатический метод.


#### Возвращаемое значение

Метод возвращает массив с [полями элемента информационного блока](../../fields.md#felement)вида Array("поле"=>"преобразованное значение" [, ...]).
#### Смотрите также


- [CIBlockResult](../ciblockresult/index.md)::[GetNext()](../ciblockresult/getnext.md) [Поля элемента информационного блока](../../fields.md#felement)[CIBlockElement](../ciblockelement/index.md):: [GetList()](../ciblockelement/getlist.md)


#### Примеры использования


```
<?
$res = CIBlockElement::GetByID($_GET["PID"]);
if($obRes = $res->GetNextElement())
{
	$ar_res = $obRes->GetFields();
	echo '<a href="'.$ar_res['detail_page_url'].'">'.$ar_res['name'].'</a>';
}
?>
```
