# Зацикливание обработчиков событий

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2949 — Учет регистрации нового пользователя в статистике](lesson_2949.md)
- [Следующий: 1981 — Совместная работа пары событий →](lesson_1981.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=1978

**Задача**: при изменении элемента инфоблока модифицировать другой элемент. Кейс может быть какой угодно - это и логирование, и деактивация основного товара, когда нет активных предложений, и изменение даты активности связанного элемента. Если создать обработчик, использующий метод [CIBlockElement::Update](http://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/update.php), и повесить его на события [OnBeforeIBlockElementUpdate](http://dev.1c-bitrix.ru/api_help/iblock/events/onbeforeiblockelementupdate.php) / [OnAfterIBlockElementUpdate](http://dev.1c-bitrix.ru/api_help/iblock/events/onafteriblockelementupdate.php), то:

```
вызов обработчика OnBeforeIBlockElementUpdate/OnAfterIBlockElementUpdate
	....
CIBlockElement::Update
вызов обработчика OnBeforeIBlockElementUpdate/OnAfterIBlockElementUpdate
	....
	CIBlockElement::Update

		...
		итог - 500 (Internal Server Error)
```

Причина в том, что происходит рекурсивный вызов обработчика. Ниже приведен код, который избавляет от подобных проблем. В качестве примера взят обработчик **OnAfterIBlockElementUpdate**.

```
class myClass
{
	protected static $handlerDisallow = false;

	public static function iblockElementUpdateHandler(&$fields)
	{
		/* проверяем, что обработчик уже запущен */
		if (self::$handlerDisallow)
			return;
		/* взводим флаг запуска */
		self::$handlerDisallow = true;
		/*  наш код, приводящий к вызову CIBlockElement::Update */
		...
		CIBlockElement :: Update (..., ...);

		/* вновь разрешаем запускать обработчик */
		self::$handlerDisallow = false;
	}
}
```

**Пояснение**. За основу взят класс, так как подобные решения в основном используются в собственных модулях. В классе имеется статическая булевая переменная - **$handlerDisallow**. По умолчанию она имеет значение `false` - нет запрета. В самом начале обработчика необходимо проверять ее значение. Если обработчик уже запущен, она будет равна `true` и выполнение необходимо прервать. Если же выполнять обработчик можно, необходимо присвоить этой переменной `true` на время выполнения всего обработчика. В конце необходимо флаг сбросить (**$handlerDisallow**), иначе до конца хита ваш обработчик не выполнится больше ни разу.

Если используется в качестве обработчика обычная функция, а не класс, то создайте статическую переменную внутри функции.

Можно дополнить класс возможностью блокировать работу обработчика "снаружи". Для этого измените тип переменной и добавьте три метода:

```
class myClass
{
	protected static $handlerDisallow = 0;

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

	public static function iblockElementUpdateHandler(&$fields)
	{
		/* проверяем, что обработчик уже запущен */
		if (!self::isEnabledHandler())
			return;
		/* взводим флаг запуска */
		self::disableHandler();
		/*  наш код, приводящий к вызову CIBlockElement::Update */
	...
	CIBlockElement :: Update (..., ...);

		/* вновь разрешаем запускать обработчик */
		self::enableHandler();
	}
}
```
