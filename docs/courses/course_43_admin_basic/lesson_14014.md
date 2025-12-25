# Контроллеры и компонент

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 6436 — Контроллер](lesson_6436.md)
- [Следующий: 21160 — Практика. Советы →](lesson_21160.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=14014

Для обработки аяксовых запросов в компоненте можно использовать два подхода:



### class.php

Обработчик запросов в классе компонента (файл **class.php**) позволяет:

- Инкапсулировать весь код в одном классе
- Повторно использовать методы, данные и параметры компонента
- Использовать языковые фразы, шаблоны компонента
- Переопределять в компонентах-потомках стандартное поведение

Чтобы класс компонента мог обрабатывать запросы необходимо:

- Реализовать интерфейс *\Bitrix\Main\Engine\Contract\Controllerable*
- Определить метод-действия с суффиксом Action
- Реализовать метод *configureActions* (обычно возвращает пустой массив === конфигурацию по умолчанию)
- Если нужно добавлять, обрабатывать ошибки, то стоит реализовать *\Bitrix\Main\Errorable*

**Примечание**: При выполнении компонента в аяксовом режиме выполняются последовательно CBitrixComponent::onIncludeComponentLang, CBitrixComponent::onPrepareComponentParams и запуск действия с фильтрами..

**Внимание!** При выполнении компонента в аяксовом режиме метод CBitrixComponent::executeComponent() не запускается.

#### Пример

```
<?php
#components/bitrix/example/class.php
use Bitrix\Main\Error;
use Bitrix\Main\ErrorCollection;
if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();
class ExampleComponent extends \CBitrixComponent implements \Bitrix\Main\Engine\Contract\Controllerable, \Bitrix\Main\Errorable
{
	/** @var ErrorCollection */
	protected $errorCollection;
	public function configureActions()
	{
		//если действия не нужно конфигурировать, то пишем просто так. И будет конфиг по умолчанию
		return [];
	}
	public function onPrepareComponentParams($arParams)
	{
		$this->errorCollection = new ErrorCollection();

		//подготовка параметров
		//Этот код **будет** выполняться при запуске аяксовых-действий
	}

	public function executeComponent()
	{
		//Внимание! Этот код **не будет** выполняться при запуске аяксовых-действий
	}

	//в параметр $person будут автоматически подставлены данные из REQUEST
	public function greetAction($person = 'guest')
	{
		return "Hi {$person}!";
	}
	//пример обработки ошибок
	public function showMeYourErrorAction():? string
	{
		if (rand(3, 43) === 42)
		{
			$this->errorCollection[] = new Error('You are so beautiful or so handsome');
			//теперь в ответе будут ошибки и будет автоматически выставлен статус ответа 'error'.

			return  null;
		}
		return "Ok";
	}

	/**
	* Getting array of errors.
	* @return Error[]
	*/
	public function getErrors()
	{
		return $this->errorCollection->toArray();
	}
	/**
	* Getting once error with the necessary code.
	* @param string $code Code of error.
	* @return Error
	*/
	public function getErrorByCode($code)
	{
		return $this->errorCollection->getErrorByCode($code);
	}
}
```

### ajax.php

Обработчик контроллера запросов в файле ajax.php позволяет создать легковесный обработчик аякс-запросов, явно выделяя логику из компонента.

Чтобы его реализовать:

- Создать в корне компонента файл ajax.php
- Определить метод-действия с суффиксом Action



Сама логика работы контроллера полностью аналогична описанию [контроллера модуля](lesson_6436.md#modul).

```
<?php
#components/bitrix/example/ajax.php
if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();
class ExampleAjaxController extends \Bitrix\Main\Engine\Controller
{
	#в параметр $person будут автоматически подставлены данные из REQUEST
	public function sayByeAction($person = 'guest')
	{
		return "Goodbye {$person}";
	}
	public function listUsersAction(array $filter)
	{
		$users = [];
		//выборка пользователей по фильтру
		//наполнения массива данными для ответа

		return $users;
	}
}
```
