# Совместная работа пары событий

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 1978 — Зацикливание обработчиков событий](lesson_1978.md)
- [Следующий: 4514 — Данные до и после update →](lesson_4514.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=1981

Рассмотрим использование пары обработчиков событий на примере событий метода [CCatalogProduct::GetOptimalPrice](http://dev.1c-bitrix.ru/api_help/catalog/classes/ccatalogproduct/ccatalogproduct__getoptimalprice.7c16046d.php).

Метод имеет два события: [OnGetOptimalPrice](http://dev.1c-bitrix.ru/api_help/catalog/events/ongetoptimalprice.php) и [OnGetOptimalPriceResult](http://dev.1c-bitrix.ru/api_help/catalog/events/ongetoptimalpriceresult.php), различающихся набором передаваемых параметров. Предположим, что для реализации логики обработчика OnGetOptimalPriceResult необходимо знать список групп пользователя, переданный в метод. Но эти данные доступны только в обработчике OnGetOptimalPrice.

Необходимо сохранить параметры вызова метода в одном обработчике (onGetOptimalPrice), а использовать в другом (onGetOptimalPriceResult), после чего очистить кеш параметров внутри обработчика. Реализация работы обработчиков "в паре":

```
class myClass
{
	protected static $handlerDisallow = 0;

	protected static $handlerParams = array();

	public static function disableHandler()
		{
		self::$handlerDisallow--;
		}

	public static function enableHandler()
		{
		self::$handlerDisallow++;
		}

	public static function isEnabledHandler()
 		  {
		return (self::$handlerDisallow >= 0);
		}

	public static function onGetOptimalPrice()
		{
		/* проверяем, что обработчик уже запущен */
		if (!self::isEnabledHandler())
			return;
		/* взводим флаг запуска */
		self::disableHandler();
		self::$handlerParams = func_get_args();
		return true;
	}

	public static function onGetOptimalPriceResult(&$data)
		{
		/*
		далее логика, использующая данные из self::$handlerParams примерно так
		if (self::$handlerParams[0] == 17) //первый параметр из вызова CCatalogProduct::GetOptimalPrice
		$data['RESULT_PRICE']['BASE_PRICE'] = 100;
		*/
		self::$handlerParams = array();  // очищаем параметры - в обязательном порядке
		/* вновь разрешаем запускать обработчик */
		self::enableHandler();
	}
}
```

**Примечание**: в общем случае в обработчик надо передавать все входные данные, но если такой возможности нет, то приходится использовать описанный выше способ.
