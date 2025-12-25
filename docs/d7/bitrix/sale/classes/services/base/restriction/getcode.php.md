# getCode

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/sale/classes/services/base/restriction/getcode.php

```
public static function \Bitrix\Sale\Services\Base\Restriction::getCode(
);
```

Метод возвращает тип ограничения. Метод статический.

Для ограничения из неймспейса **Bitrix\*** в качестве типа вернётся название класса без неймспейсов. Для [пользовательского](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=7352) ограничения в качестве типа вернётся полное название класса с неймспейсом. Примеры:

- для класса ограничения валюты `Bitrix\Currency` будет возвращено `currency`;
- для класса пользовательского ограничения валюты `Vendor\Currency` будет возвращено `Vendor\Currency`.

#### Параметры

Без параметров.

#### Примеры

```
public static function getCode(): string
{
	$class = new \ReflectionClass(static::class);
	if (self::isBitrixNamespace($class->getNamespaceName()))
	{
		return $class->getShortName();
	}
	return $class->getName();
}
```
