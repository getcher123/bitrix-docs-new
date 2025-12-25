# UpdateEnum


### Описание и параметры


```
CIBlockProperty::UpdateEnum(
	int ID,
	array arVALUES,
	bool bForceDelete = true
);
```

Метод устанавливает значения перечислений свойства типа "список". Нестатический метод.


#### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| ID | Код свойства. |  |
| arVALUES | Массив всех значений в формате Array("код существующего значения"=>"массив полей значения", ..., "массив полей нового значения", ...). Где массив полей имеет вид: Array("VALUE"=>"значение"[, "SORT"=>"порядок сортировки"][, "DEF"=>"является значением по умолчанию (Y\|N)"][, "XML_ID"=>"внешний код"]). |  |
| bForceDelete | Если принимает значение *true*, то удаляются варианты значений, у которых *VALUE* пустой. Значение *false* позволяет сохранить значения, использованные хотя бы у одного элемента. Необязательный параметр. | 11.0.12 |

**Примечание:**массив *arVALUES*должен содержать полный список значений, те значение для которых в этом массиве не будет найден "код существующего значения" будут удалены.

---
### Смотрите также


- [Поля значений свойства типа "список](../../fields.md#fiblockpropertyenum)"
- [CIBlockPropetyEnum](../ciblockpropertyenum/index.md)::[Update()](../ciblockpropertyenum/update.md)
- [CIBlockPropetyEnum](../ciblockpropertyenum/index.md)::[Add()](../ciblockpropertyenum/add.md)

---
### Примеры использования


```
<?
$cnt = 0;
$ar_all_values = Array();
$db_enum_list = CIBlockProperty::GetPropertyEnum($PROP_ID, Array('SORT'=>'ASC'));
while($ar_enum = $db_enum_list->Fetch())
{
	$cnt++;
	$ar_all_values[$ar_enum['ID']] = Array('SORT'=>$cnt, 'VALUE'=>$ar_enum['VALUE']);
}
$CIBlockProp = new CIBlockProperty;
$CIBlockProp->UpdateEnum($PROP_ID, $ar_all_values); ?>
```

---
