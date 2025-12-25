# Update


### Описание и параметры


```
bool
CIBlockType::Update(
	string ID,
	array arFields
);
```

Метод изменяет параметры типа информационных блоков с кодом *ID*. Нестатический метод.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ID | Код изменяемой записи. |
| arFields | Массив поле=>значение... Содержит значения [полей типа информационных блоков](../../fields.md#fiblocktype). В элементе массива arFields["LANG"] должен содержаться ассоциативный массив [языковых свойств](../../fields.md#fiblocktypelang) типа. Ключами этого массива служат идентификаторы языков. |


#### Возвращаемое значение

Метод возвращает:


- `true` — если изменение прошло успешно
- `false` — при возникновении ошибки

В случае ошибки в свойстве объекта `LAST_ERROR` будет содержаться текст ошибки. Получить текст ошибки можно методом [getLastError](getlasterror.md).

---
### Смотрите также


- [CIBlockType](index.md)::[Add()](add.md)
- [Поля типа информационных блоков](../../fields.md#fiblocktype)

---
### Примеры использования


```
<?
$arFields = Array(
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
$res = $obBlocktype->Update('catalog', $arFields);
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
