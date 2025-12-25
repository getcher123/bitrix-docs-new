# Delete


```
bool
CIBlockPropertyEnum::Delete(
	int ID
);
```

Метод удаляет вариант значения свойства типа "список". Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ID | Код варианта значения свойства. |


#### Возвращаемое значение

В случае успешного удаления возвращается true, иначе - false.






| ![image](../images/7dd82aba60.gif) 0 **Атем Прозоров**16.10.2019 16:04:40 |  |  |
| --- | --- | --- |
| Пример: \| Код \| \| --- \| \| ``` if (! \Bitrix\Main\Loader::includeModule('iblock')) { throw new \Bitrix\Main\LoaderException('Unable to load IBLOCK module'); } $property = \CIBlockProperty::GetList([], ['IBLOCK_ID' => $iblockId, 'CODE' => $propertyCode])->Fetch(); if (! $property) { throw new \Exception('No such property'); } $query = \CIBlockPropertyEnum::GetList( [], ["IBLOCK_ID" => $iblockId, "XML_ID" => 6, "PROPERTY_ID" => $property['ID']] ); $value = $query->GetNext(); if (! $value) { throw new \Exception('No such value'); } $delete = \CIBlockPropertyEnum::delete($value['ID']); if (! $delete) { throw new \Exception('Error while deleting the property value'); } ``` \| | Код | ``` if (! \Bitrix\Main\Loader::includeModule('iblock')) { throw new \Bitrix\Main\LoaderException('Unable to load IBLOCK module'); } $property = \CIBlockProperty::GetList([], ['IBLOCK_ID' => $iblockId, 'CODE' => $propertyCode])->Fetch(); if (! $property) { throw new \Exception('No such property'); } $query = \CIBlockPropertyEnum::GetList( [], ["IBLOCK_ID" => $iblockId, "XML_ID" => 6, "PROPERTY_ID" => $property['ID']] ); $value = $query->GetNext(); if (! $value) { throw new \Exception('No such value'); } $delete = \CIBlockPropertyEnum::delete($value['ID']); if (! $delete) { throw new \Exception('Error while deleting the property value'); } ``` |
| Код |  |  |
| ``` if (! \Bitrix\Main\Loader::includeModule('iblock')) { throw new \Bitrix\Main\LoaderException('Unable to load IBLOCK module'); } $property = \CIBlockProperty::GetList([], ['IBLOCK_ID' => $iblockId, 'CODE' => $propertyCode])->Fetch(); if (! $property) { throw new \Exception('No such property'); } $query = \CIBlockPropertyEnum::GetList( [], ["IBLOCK_ID" => $iblockId, "XML_ID" => 6, "PROPERTY_ID" => $property['ID']] ); $value = $query->GetNext(); if (! $value) { throw new \Exception('No such value'); } $delete = \CIBlockPropertyEnum::delete($value['ID']); if (! $delete) { throw new \Exception('Error while deleting the property value'); } ``` |  |  |
|  |  |  |
