# Собственный обработчик онлайн-кассы

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8485 — Кастомизация шаблона платежной системы](lesson_8485.md)
- [Следующий: 21928 — Принцип печати чеков через платёжную систему →](lesson_21928.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=5118

Не подходит стандартный обработчик онлайн-кассы? Используйте API продукта и напишите свой обработчик. Для этого вам необходимо:

- Унаследовать класс *\Bitrix\Sale\Cashbox\Cashbox* и реализовать необходимые методы:
  **Примечание:**дополнительно вы можете использовать следующие интерфейсы:
  - *\Bitrix\Sale\Cashbox\IPrintImmediately* - необходим для отправки чека на печать сразу же после его создания;
  - *\Bitrix\Sale\Cashbox\ICheckable* - необходим, если требуется запрашивать информацию о результатах печати чека.
  ```
  use \Bitrix\Sale\Cashbox\Cashbox,
  	\Bitrix\Sale\Cashbox\Check,
  	\Bitrix\Sale\Cashbox\IPrintImmediately,
  	\Bitrix\Sale\Cashbox\ICheckable;
  class CashboxCustom extends Cashbox implements IPrintImmediately, ICheckable
  {
  	/**
  	 * @param Check $check
  	 * @return array
  	 */
  	public function buildCheckQuery(Check $check)
  	{
  		// построение запроса с информацией по чеку
  	}
  	/**
  	 * @param $id
  	 * @return array
  	 */
  	public function buildZReportQuery($id)
  	{
  		// построение запроса на печать z-отчета
  		// если печать z-отчета не требуется, возвращается пустой массив
  	}
  	public function printImmediately(Check $check)
  	{
  		// алгоритм отправки чека на печать
  	}
  	public function check(Check $check)
  	{
  		// алгоритм запроса состояния чека
  	}
  	/**
  	 * @return string
  	 */
  	public static function getName()
  	{
  		// название обработчика
  		return Localization\Loc::getMessage('SALE_CASHBOX_CUSTOM_TITLE');
  	}
  	/**
  	 * @param array $data
  	 * @throws Main\NotImplementedException
  	 * @return array
  	 */
  	protected static function extractCheckData(array $data)
  	{
  		// извлечение данных по чеку дальнейшего сохранения
  	}
  	public static function getVersion() ?: float
  	{
  		// версия ФФД, с которой работает обработчик
  		return null;
  	}
  }
  ```
- Подключить обработчик кассы к системе с помощью события *OnGetCustomCashboxHandlers*. Обработчик события должен возвращать массив вида: *array(полное_имя_класса =&gt; путь_к_файлу)*:
  ```
  AddEventHandler("sale", "OnGetCustomCashboxHandlers", 'myCashboxFunction');
  function myCashboxFunction()
  {
  	return new \Bitrix\Main\EventResult(
  		\Bitrix\Main\EventResult::SUCCESS,
  		array(
  		'\CashboxCustom' => '/bitrix/php_interface/include/cashboxcustom.php',
  		)
  	);
  }
  ```

В результате в административном разделе сайта в настройках кассы появится ваш обработчик.

Список ссылок по теме:

- [Подготовка платёжной системы](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/cashbox/preparation.php)
- [Методы реализации кассы](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/cashbox/cashbox_implementation.php)
