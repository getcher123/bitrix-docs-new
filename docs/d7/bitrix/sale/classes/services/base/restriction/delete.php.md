# delete

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/sale/classes/services/base/restriction/delete.php

```
public static function \Bitrix\Sale\Services\Base\Restriction::delete(
	$restrictionId,
	$entityId = 0
);
```

Метод удаляет ограничения для сервиса. Метод статический.

#### Параметры

| Параметр | Описание | Версия |
| --- | --- | --- |
| $restrictionId | Идентификатор ограничения. |  |
| $entityId | Идентификатор сущности. |  |

#### Примеры

```
public static function delete($restrictionId, $entityId = 0)
{
	return ServiceRestrictionTable::delete($restrictionId);
}
```
