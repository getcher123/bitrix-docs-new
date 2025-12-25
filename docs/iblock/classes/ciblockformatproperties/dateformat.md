# DateFormat


```
string CIBlockFormatProperties::DateFormat(
	string format,
	string timestamp
)
```

Конвертирует дату в нужный формат. Доступные форматы можно посмотреть, вызвав **CIBlockParameters::GetDateFormat**. Метод статический.

**Примечание:**является функцией-оберткой для [FormatDate](../../../main/functions/date/formatdate.md).


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| format | Формат даты/времени. Может дополнительно принимать 2 значения: *SHORT* и *FULL* (для них берется формат даты или времени для сайта). |
| timestamp | Метка времени в Unix формате. |


#### Возвращаемое значение

Отформатированная строка.
