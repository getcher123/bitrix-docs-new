# Компонент фильтра


#### JS-библиотека landing.uifilterconverter

Служит для преобразования условий отбора элементов источника в фильтр блока.

Должна быть подключена в шаблоне компонента формы:


```
\Bitrix\Main\UI\Extension::load('landing.uifilterconverter');
```

Содержит класс **UiFilterConverter**. Методы:

**Конструктор класса**


```
UiFilterConverter(
	{filterId: 'ИД_фильтра'}
)
```


| Параметры | Тип | Описание | С версии |
| --- | --- | --- | --- |
| filterId | объект | Содержит ИД_фильтра (тот, что инициализировал main.uni.filter) |  |


**UiFilterConverter.getFilter**

Возвращает фильтр из main.ui.filter, преобразованный в формат блока.
