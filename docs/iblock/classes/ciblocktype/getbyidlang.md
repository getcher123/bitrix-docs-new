# GetByIDLang


### Описание и параметры


```
mixed
CIBlockType::GetByIDLang(
	string ID,
	string LANGUAGE_ID,
	bool bFindAny = true
);
```

Метод возвращает языковые настройки типа информационных блоков по его коду *ID*, для языка *LANGUAGE_ID*. Если для языка *LANGUAGE_ID* нет настроек и параметр *bFindAny* установлен в true, метод вернет настройки типа для языка по умолчанию. Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ID | Код типа. |
| LANGUAGE_ID | Код языка. |
| bFindAny | Возвращать настройки для языка по умолчинию или нет. Необязательный. По умолчанию - возвращать. |


#### Возвращаемое значение

Если языковые настройки найдены, то метод возвратит массив [полей](../../fields.md#fiblocktype)типа информационных блоков объединенный с массивом языкозависимых [параметров](../../fields.md#fiblocktypelang)типа, в противном случае метод вернет false. ---
### Смотрите также


- [Поля CIBlockType](../../fields.md#fiblocktype)
- [Языкозависимые поля CIBlockType](../../fields.md#fiblocktypelang)

---
### Примеры использования


```
<?
$db_iblock_type = CIBlockType::GetList();
while($ar_iblock_type = $db_iblock_type->Fetch())
{
	if($arIBType = CIBlockType::GetByIDLang($ar_iblock_type["ID"], LANG))
	{
		echo htmlspecialcharsex($arIBType["NAME"])."<br>";
	}
}
?>
```

---
