# getPublicElementsOrmFilter


```
array
public static function CIBlockElement::getPublicElementsOrmFilter(
	array $filter
);
```

Статический метод для дополнения фильтра orm на основе массива. Служит для получения фильтра, отсекающего неопубликованные записи в режиме документооборота (историю редактирования).

Возвращаемое значение - массив.


#### Параметры функции


| Параметр | Описание |
| --- | --- |
| $filter | Массив фильтра для orm (**\Bitrix\Iblock\ElementTable::getList**) |
