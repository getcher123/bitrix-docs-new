# OnIBlockElementSetPropertyValuesEx


### Описание и параметры


```
функция-обработчик(
	int ELEMENT_ID,
	int IBLOCK_ID,
	array PROPERTY_VALUES,
	array propertyList,
	array arDBProps
);
```

Событие вызывается до внесения изменений в базу после валидации входящих данных.


#### Параметры


| Параметр | Описание |
| --- | --- |
| ELEMENT_ID | Идентификатор элемента инфоблока. |
| IBLOCK_ID</td Идентификатор инфоблока. | Идентификатор инфоблока. |
| PROPERTY_VALUES | [Массив значений свойств](../classes/ciblockelement/setpropertyvalues.md) элемента инфоблока. |
| propertyList | Массив, описывающий Список свойств. |
| arDBProps | Текущие значения свойств элемента. |


#### Возвращаемое значение

Нет.

---
### Смотрите также


- [CIBlockElement::SetPropertyValuesEx](../classes/ciblockelement/setpropertyvaluesex.md)

---
