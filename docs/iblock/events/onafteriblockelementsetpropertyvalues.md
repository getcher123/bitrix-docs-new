# OnAfterIBlockElementSetPropertyValues


### Описание и параметры


```
функция-обработчик(
	int ELEMENT_ID,
	int IBLOCK_ID,
	array PROPERTY_VALUES,
	string PROPERTY_CODE
);
```

Событие "OnAfterIBlockElementSetPropertyValues" вызывается после попытки сохранения значений всех свойств элемента инфоблока методом [CIBlockElement::SetPropertyValues](../classes/ciblockelement/setpropertyvalues.md).


#### Параметры


| Параметр | Описание | ELEMENT_ID | Код элемента, значения свойств которого необходимо установить. | IBLOCK_ID | Код информационного блока. | PROPERTY_VALUES | Массив значений свойств, в котором коду свойства ставится в соответствие значение свойства. | PROPERTY_CODE | Код изменяемого свойства. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ELEMENT_ID | Код элемента, значения свойств которого необходимо установить. |  |  |  |  |  |  |  |  |
| IBLOCK_ID | Код информационного блока. |  |  |  |  |  |  |  |  |
| PROPERTY_VALUES | Массив значений свойств, в котором коду свойства ставится в соответствие значение свойства. |  |  |  |  |  |  |  |  |
| PROPERTY_CODE | Код изменяемого свойства. |  |  |  |  |  |  |  |  |


#### Возвращаемое значение

Нет.

---
### Смотрите также


- [CIBlockElement::SetPropertyValues](../classes/ciblockelement/setpropertyvalues.md)

---
