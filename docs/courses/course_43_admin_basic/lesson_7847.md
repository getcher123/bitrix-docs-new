# Кастомизация платежных систем

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5329 — Кастомизация служб доставок](lesson_5329.md)
- [Следующий: 8485 — Кастомизация шаблона платежной системы →](lesson_8485.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=7847

Средства системы позволяют кастомизировать и добавлять свои собственные платежные системы, причем в магазине на ядре D7 они представляют из себя классы. Следовательно, можно использовать механизм наследования:

- если необходимо сделать платежную систему, похожую на входящую в состав продукта, то можно унаследоваться от соответствующего класса;
- если требуется написать платежную систему с нуля, то можно унаследоваться от базового класса *Bitrix\Sale\PaySystem\BaseServiceHandler* или *\Bitrix\Sale\PaySystem\ServiceHandler* (первый вариант подходит для платежных систем, которые не являются автоматизированными, например, квитанция Сбербанка).
  Чаще всего при кастомизации используется класс *\Bitrix\Sale\PaySystem\ServiceHandler*, который является наследником класса *Bitrix\Sale\PaySystem\BaseServiceHandler*. Класс *\Bitrix\Sale\PaySystem\ServiceHandler* поддерживает методы, реализовав которые возможна обработка ответа от платежной системы.

Собственный обработчик платёжной системы необходимо добавлять в пространство имён `\Sale\Handlers\PaySystem\`, иначе он не подключится.

Пример наследования для платежных систем:

```

class YandexHandler extends ServiceHandler implements IReturn, IHold
{
	public static function initiatePay(Payment $payment)
	{
		$params = array('URL' = > $this->getUrl($payment, 'pay'));
		$this->setExtraParams($params);

		return $this->showTemplate($payment, "template");
	}

	public static function getIndicativeFields()
	{
		return array('BX_HANDLER' => 'YANDEX');
	}
}
```

Система будет искать обработчик в следующих директориях:

```

protected static $handlerDirectories = array(
	'CUSTOM' =>  путь берется из опции path2user_ps_files (по умолчанию "/php_interface/include/sale_payment/")
	'LOCAL' => '/local/php_interface/include/sale_payment/',
	'SYSTEM' => '/bitrix/modules/sale/handlers/paysystem/'
	'SYSTEM_OLD' => '/bitrix/modules/sale/payment/'
)
```

#### Важно помнить!

Если при копировании не изменить имя (оставить `/bitrix/php_interface/include/sale_payment/yandex`), то в настройках платежных систем можно будет использовать только кастомный обработчик. Системный (тот, который копировался) не будет доступен, то есть кастомный обработчик подменяет системный.

Из этого вытекает следующее: если при копировании системного обработчика в свое пространство имен его имя меняется, то необходимо переименовать класс. Например, если мы скопировали системный yandex в `/bitrix/php_interface/include/sale_payment/yandexnew`, то в файле **handler.php** наследование должно быть так:

```
class YandexNewHandler extends PaySystem\BaseServiceHandler
```

**Обратите внимание!** Имя папки обработчика не может содержать слово handler, т.к. оно присутствует в названии самого класса внутри обработчика. То есть в приведенном примере в имени `/bitrix/php_interface/include/sale_payment/yandexnew` конечная папка yandexnew не должна содержать слово handler. Название папки должно быть в нижнем регистре.

#### Ограничения использования платежной системы

Вы можете ограничить использование платежной системы по каким-либо параметрам. Например, по службе доставки. Для этого применяйте [стандартные ограничения](/learning/course/index.php?COURSE_ID=42&LESSON_ID=12159#restr). Если же необходимо что-то особенное, то создайте [собственные типы ограничений](lesson_7352.md).

#### Требования к файлу .description.php обработчика платежной системы

Структура массива с описанием настроек обработчика платежной системы хранится в переменной **$data** и имеет вид:

```

$data = array(
	'NAME' => 'название_платежной_системы',
	'SORT' => 500,
	'CODES' => array( // массив параметров, необходимых для настройки
		"КОД_ПАРАМЕТРА" => array(
			"NAME" => 'НАЗВАНИЕ_ПАРАМЕТРА',
			"DESCRIPTION" => 'ОПИСАНИЕ_ПАРАМЕТРА',
			'SORT' =>100,
			'GROUP' => 'КОД_ГРУППЫ',
			'DEFAULT' => array( // значение по умолчанию
				'PROVIDER_KEY' => 'КЛЮЧ', // тип значения: (PAYMENT, ORDER, SHIPMENT, USER, COMPANY, VALUE)
				'PROVIDER_VALUE' => 'DATE_BILL' // значение: поля из конкретной сущности, либо произвольное значение
			)
		),
		...
	)
);
```

Для вывода описания при создании обработчика необходимо объявить переменную **$description**:

```

$description = array(
	'MAIN' => 'ОПИСАНИЕ ОБРАБОТЧИКА'
);
```
