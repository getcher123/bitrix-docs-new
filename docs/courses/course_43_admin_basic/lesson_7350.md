# Пользовательские типы свойств заказа

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 12183 — Товары и CIBlockElement::GetList](lesson_12183.md)
- [Следующий: 7352 — Пользовательские ограничения →](lesson_7352.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=7350

### Свои типы свойств

В системе имеются следующие стандартные типы свойств: *Строка*, *Число*, *Да/Нет*, *Перечисление*, *Файл*, *Дата* и *Местоположение*. Но вы можете добавлять свои типы свойств и самостоятельно определять их внешний вид. Таким образом, у покупателя при оформлении заказа будет спрашиваться какое-то значение, которое вы сами запрограммируете. Для этого вам необходимо выполнить следующие действия:

- Унаследовать класс пользовательского типа:
  ```
  class MyType extends \Bitrix\Sale\Internals\Input\Base
  {
  	protected static function getEditHtmlSingle($name, array $input, $value){...}
  	protected static function getErrorSingle(array $input, $value){...}
  	static function getSettings(array $input, $reload){...}
  }
  ```
- Подключить тип свойства к системе - тип подключается на событии *registerInputTypes*:
  ```
  \Bitrix\Main\EventManager::getInstance()->addEventHandler(
  	'sale',
  	'registerInputTypes',
  	'myFunction'
  );
  ```
- В обработчике события зарегистрировать свой тип свойства с помощью метода *Manager::register*, где указывается ваш класс-обработчик и имя вашего типа:
  ```
  public function myFunction(\Bitrix\Main\Event $event)
  {
  	\Bitrix\Sale\Internals\Input\Manager::register(
  		"myType",
  		array(
  			'CLASS' => '\MyNamespace\MyType',
  			'NAME' => 'Мой тип',
  		)
  	);
  }
  ```
- Описать JS-класс
                      Иногда при разработке компонента его шаблон необходимо наделить js-функциональностью, событиями и прочим.
  [Подробнее ...](lesson_7971.md)
  		 для работы со свойством и
  			подключить
                      Перед написанием JS-кода встает резонный вопрос - где его хранить?
  [Подробнее ...](lesson_8765.md)
  		 его:
  ```
  BX.Sale.Input.Manager.MyType = MyType;
  BX.Sale.Input.Utils.extend(MyType, BX.Sale.Input.BaseInput);
  BX.Sale.Input.Manager.register('myType', MyType);
  function MyType(name, settings, value, publicO)
  {
  	MyType.__super__.constructor.call(this, name, settings, value, publicO);
  }
  MyType.prototype.createEditorSingle = function (name, value)
  {
  	...
  };
  MyType.prototype.afterEditorSingleInsert = function (item)
  {
  	...
  };
  MyType.prototype.setValueSingle = function (item, value)
  {
  	...
  };
  MyType.prototype.getValueSingle = function (item)
  {
  	...
  };
  MyType.prototype.setDisabledSingle = function (item, disabled)
  {
  	...
  };
  MyType.prototype.addEventSingle = function (item, name, action)
  {
  	...
  };
  ```

**Важно!** Название типа *myType* должно быть **уникальным** в рамках всей системы.

В результате в дальнейшем, когда менеджер магазина будет создавать новое свойство заказа, ему среди стандартных типов будет доступен для выбора и ваш созданный тип свойства.

**Обратите внимание!** Поддержку созданного пользовательского свойства в компоненте оформления заказа

			sale.order.ajax

                    Компонент служит для оформления заказа на одной странице с использованием технологии AJAX. Компонент является стандартным и входит в дистрибутив модуля.



						[Описание компонента «Оформление заказа» в пользовательской документации.](http://dev.1c-bitrix.ru/user_help/detail.php?ID=146775)

		 необходимо делать самостоятельно.

### Пример создания типа свойств String

Наследуем класс, подключаем тип свойства к системе и регистрируем его:

```
class StringInput extends \Bitrix\Sale\Internals\Input\Base
{
	public static function getEditHtmlSingle($name, array $input, $value)
	{
		if ($input['MULTILINE'] == 'Y')
		{
			$attributes = static::extractAttributes($input,
				array('DISABLED'=>'', 'READONLY'=>'', 'AUTOFOCUS'=>'', 'REQUIRED'=>''),
				array('FORM'=>1, 'MAXLENGTH'=>1, 'PLACEHOLDER'=>1, 'DIRNAME'=>1, 'ROWS'=>1, 'COLS'=>1, 'WRAP'=>1));

			return '<textarea name="'.$name.'"'.$attributes.'>'.htmlspecialcharsbx($value).'</textarea>';
		}
		else
		{
			$attributes = static::extractAttributes($input,
				array('DISABLED'=>'', 'READONLY'=>'', 'AUTOFOCUS'=>'', 'REQUIRED'=>'', 'AUTOCOMPLETE'=>'on'),
				array('FORM'=>1, 'MAXLENGTH'=>1, 'PLACEHOLDER'=>1, 'DIRNAME'=>1, 'SIZE'=>1, 'LIST'=>1, 'PATTERN'=>1));

			return '<input type="text" name="'.$name.'" value="'.htmlspecialcharsbx($value).'"'.$attributes.'>';
		}
	}

	/**
	 * @param $name
	 * @param array $input
	 * @param $value
	 * @return string
	 */
	public static function getFilterEditHtml($name, array $input, $value)
	{
		return static::getEditHtmlSingle($name, $input, $value);
	}

	public static function getErrorSingle(array $input, $value)
	{
		$errors = array();

		$value = trim($value);

		if ($input['MINLENGTH'] && strlen($value) < $input['MINLENGTH'])
			$errors['MINLENGTH'] = Loc::getMessage('INPUT_STRING_MINLENGTH_ERROR', array("#NUM#" => $input['MINLENGTH']));

		if ($input['MAXLENGTH'] && strlen($value) > $input['MAXLENGTH'])
			$errors['MAXLENGTH'] = Loc::getMessage('INPUT_STRING_MAXLENGTH_ERROR', array("#NUM#" => $input['MAXLENGTH']));

		if ($input['PATTERN'] && !preg_match($input['PATTERN'], $value))
			$errors['PATTERN'] = Loc::getMessage('INPUT_STRING_PATTERN_ERROR');

		return $errors;
	}

	static function getSettings(array $input, $reload)
	{
		$settings = array(
			'MINLENGTH' => array('TYPE' => 'NUMBER', 'LABEL' => Loc::getMessage('INPUT_STRING_MINLENGTH'), 'MIN' => 0, 'STEP' => 1),
			'MAXLENGTH' => array('TYPE' => 'NUMBER', 'LABEL' => Loc::getMessage('INPUT_STRING_MAXLENGTH'), 'MIN' => 0, 'STEP' => 1),
			'PATTERN'   => array('TYPE' => 'STRING', 'LABEL' => Loc::getMessage('INPUT_STRING_PATTERN'  )),
			'MULTILINE' => array('TYPE' => 'Y/N'   , 'LABEL' => Loc::getMessage('INPUT_STRING_MULTILINE'), 'ONCLICK' => $reload),
		);

		if ($input['MULTILINE'] == 'Y')
		{
			$settings['COLS'] = array('TYPE' => 'NUMBER', 'LABEL' => Loc::getMessage('INPUT_STRING_SIZE'), 'MIN' => 0, 'STEP' => 1);
			$settings['ROWS'] = array('TYPE' => 'NUMBER', 'LABEL' => Loc::getMessage('INPUT_STRING_ROWS'), 'MIN' => 0, 'STEP' => 1);
		}
		else
		{
			$settings['SIZE'] = array('TYPE' => 'NUMBER', 'LABEL' => Loc::getMessage('INPUT_STRING_SIZE'), 'MIN' => 0, 'STEP' => 1);
		}

		return $settings;
	}
}

\Bitrix\Sale\Internals\Input\Manager::register('STRING', array(
	'CLASS' => '\StringInput',
	'NAME' => \Bitrix\Main\Localization\Loc::getMessage('INPUT_STRING'),
));
```

Описываем и подключаем JS-класс:

```

BX.Sale.Input.Manager.StringInput = StringInput;
BX.Sale.Input.Utils.extend(StringInput, BX.Sale.Input.BaseInput);
BX.Sale.Input.Manager.register('STRING', StringInput);

function StringInput(name, settings, value, publicO)
{
	StringInput.__super__.constructor.call(this, name, settings, value, publicO);
}

StringInput.prototype.createEditorSingle = function (name, value)
{
	var s, size = 5, settings = this.settings;

	if ((s = settings.MIN) && s.toString().length > size)
		size = s;

	if ((s = settings.MAX) && s.toString().length > size)
		size = s;

	if ((s = settings.STEP) && s.toString().length > size)
		size = s;

	var element = document.createElement('input');
	element.type  = 'text';
	element.name  = name;
	element.value = value;
	element.size  = size;

	BX.Sale.Input.Utils.applyBooleanAttributesTo(element, settings, BX.Sale.Input.Utils.globalBooleanAttributes, {DISABLED:'', READONLY:'', AUTOFOCUS:'', REQUIRED:'', AUTOCOMPLETE:'on'});
	BX.Sale.Input.Utils.applyValueAttributesTo(element, settings, BX.Sale.Input.Utils.globalValueAttributes, {FORM:1, LIST:1, PLACEHOLDER:1});
	this.applyEventAttributesTo(element, settings, BX.Sale.Input.Utils.globalEventAttributes);

	return [element];
};

StringInput.prototype.afterEditorSingleInsert = function (item)
{
	item[0].focus();
};

StringInput.prototype.setValueSingle = function (item, value)
{
	item[0].value = value;
};

StringInput.prototype.getValueSingle = function (item)
{
	var element = item[0];
	return element.disabled ? null : element.value;
};

StringInput.prototype.setDisabledSingle = function (item, disabled)
{
	item[0].disabled = disabled;
};

StringInput.prototype.addEventSingle = function (item, name, action)
{
	BX.Sale.Input.Utils.addEventTo(item[0], name, action);
};
```
