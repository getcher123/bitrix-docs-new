# GetNext


### Описание и параметры


```
mixed
CDBResult::GetNext(
	bool TextHtmlAuto=true,
	bool use_tilda=true
)
```

Возвращает массив значений полей приведенный в HTML-безопасный вид. Если достигнут конец результата выборки метод вернет *false*. Нестатический метод.


#### Параметры


| Параметр | Описание | С версии |
| --- | --- | --- |
| *TextHtmlAuto* | Если значение данного параметра - "true", то метод будет автоматически обрабатывать поля с выбором формата text/html. Необязательный. По умолчанию - "true". |  |
| *use_tilda* | Если значение данного параметра - "true", то помимо преобразованных в HTML-безопасный вид полей, в результирующий массив будут включены также оригинальные (исходные) значения этих полей (ключи массива с оригинальными значениями этих полей будут иметь суффикс "~"). Необязательный. По умолчанию - "true". | 3.0.11 |

---
### Смотрите также


- CDBResult::Fetch CDBResult::ExtractFieldsCDBResult::NavNext

---
### Примеры использования


```
<select>
<?
$rs = CGroup::GetList($order="ID", $by="ASC");
while ($arGroup=$rs->GetNext()) :
	?><option value="<?=$arGroup["ID"]?>"
	<?if (IntVal($arGroup["ID"])==IntVal($show_perms_for)) echo " selected";?>
	><?=$arGroup["NAME"]?></option><?
endwhile;
?>
</select>
```

---
