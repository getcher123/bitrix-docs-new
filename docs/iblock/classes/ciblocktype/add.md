# Add


### Описание и параметры


```
bool
CIBlockType::Add(
	array arFields
);
```

Метод добавляет новый тип информационных блоков. Нестатический метод.

**Примечание:**вызов метода без ключа **LANG**или с пустым ключом вызывает ошибку.


#### Параметры метода


| Параметр | Описание |
| --- | --- |
| arFields | Массив поле=>значение... Содержит значения [полей типа информационных блоков](../../fields.md#fiblocktype). В элементе массива arFields["LANG"] должен содержаться ассоциативный массив [языковых свойств](../../fields.md#fiblocktypelang) типа.Ключами этого массива служат идентификаторы языков. |


#### Возвращаемое значение

Метод возвращает:


- `true` — если тип успешно добавлен
- `false` — при возникновении ошибки

В случае ошибки в свойстве объекта `LAST_ERROR` будет содержаться текст ошибки. Получить текст ошибки можно методом [getLastError](getlasterror.md).

---
### Смотрите также


- [CIBlockType](index.md)::[Update()](update.md)
- [Поля типа информационных блоков](../../fields.md#fiblocktype)

---
### Примеры использования


```
<?
$arFields = Array(
	'ID'=>'catalog',
	'SECTIONS'=>'Y',
	'IN_RSS'=>'N',
	'SORT'=>100,
	'LANG'=>Array(
		'en'=>Array(
			'NAME'=>'Catalog',
			'SECTION_NAME'=>'Sections',
			'ELEMENT_NAME'=>'Products'
		)
	)
);
$obBlocktype = new CIBlockType;
$DB->StartTransaction();
$res = $obBlocktype->Add($arFields);
if(!$res)
{
	$DB->Rollback();
	echo 'Error: '.$obBlocktype->LAST_ERROR.'<br>';
}
else
	$DB->Commit();
?>
```

---
