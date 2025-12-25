# Update


### Описание и параметры


```
bool CIBlockPropertyEnum::Update(
	int ID,
	array arFields
);
```

Метод изменяет параметры варианта свойства с кодом *ID*. Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ID | ID изменяемой записи. |
| arFields | Массив Array("поле"=>"значение", ...). Содержит значения [всех полей](../../fields.md#fpropertyenum) варианта значения свойства. |


#### Возвращаемое значение

Метод возвращает true если изменение прошло успешно, при возникновении ошибки метод вернет false.

---
### Смотрите также


- [CIBlockPropertyEnum::Add](add.md) [Поля свойства](../../fields.md#fpropertyenum)

---
### Примеры использования


#### Примеры использования


```
<?
$ibpenum = new CIBlockPropertyEnum;
$ibpenum->Update($PROPERTY_ENUM_ID, Array('VALUE'=>'Enum 1'));
?>
```

---
