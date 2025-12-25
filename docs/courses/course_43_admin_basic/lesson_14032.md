# Сервис Локатор

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3570 — Практика. Работа с D7 на примере местоположений](lesson_3570.md)
- [Следующий: 6436 — Контроллер →](lesson_6436.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=14032

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/framework/service-locator.html). В ней улучшена структура, описание, примеры.

### Описание

> **Сервис локатор** (локатор служб) -  это шаблон проектирования для удобной работы с сервисами приложения. Подробнее можно прочитать в [статье](https://ru.wikipedia.org/wiki/%D0%9B%D0%BE%D0%BA%D0%B0%D1%82%D0%BE%D1%80_%D1%81%D0%BB%D1%83%D0%B6%D0%B1).

Идея сервиса в том, что вместо создания конкретных сервисов напрямую (с помощью new), используется специальный объект (сервис локатор), который будет отвечать за создание, нахождение сервисов. Своего рода реестр.

Класс `\Bitrix\Main\DI\ServiceLocator` реализует интерфейс [PSR-11](https://github.com/container-interop/fig-standards/blob/master/proposed/container.md). Доступен с версии main 20.5.400.

**Простой пример использования:**

```
$serviceLocator = \Bitrix\Main\DI\ServiceLocator::getInstance();

if ($serviceLocator->has('someService'))
{
	$someService = $serviceLocator->get('someService');
	//...$someService использование сервиса
}
```

### Регистрация сервиса

**Регистрация через файлы настроек *bitrix/.settings.php***

Прежде чем обращаться к сервису его необходимо зарегистрировать и один из способов это использование файлов настроек **.settings.php**. Все необходимые сервисы перечисляются в секции **services**.

```
<?php
// /bitrix/.settings.php
	return [
		//...
		'services' => [
			'value' => [
				'someServiceName' => [
					'className' => \VendorName\Services\SomeService::class,
				],
				'someGoodServiceName' => [
					'className' => \VendorName\Services\SecondService::class,
					'constructorParams' => ['foo', 'bar'],
				],
		],
	'readonly' => true,
	],
//...
	];
```

В итоге сервисы будут доступны сразу после инициализации ядра. О том, какие есть способы их описания можно прочитать ниже.

```
$serviceLocator = \Bitrix\Main\DI\ServiceLocator::getInstance();
$someGoodServiceName = $serviceLocator->get('someGoodServiceName');
$someServiceName = $serviceLocator->get('someServiceName');
```

**Регистрация через файлы настроек модуля *{moduleName}/.settings.php***

В корне модуля так же может располагаться свой файл **.settings.php**. И в нём можно описать сервисы, которые принадлежат данному модулю и используются в нём. Семантика аналогична описанию в глобальном `bitrix/.settings.php` и правилам описания конфигураций.

```
<?php
// someModule/.settings.php
	return [
	//...
	'services' => [
		'value' => [
			'someModule.someServiceName' => [
			'className' => \VendorName\SomeModule\Services\SomeService::class,
			],
			'someModule.someAnotherServiceName' => [
				'constructor' => static function () {
					return new \VendorName\SomeModule\Services\SecondService('foo', 'bar');
				},
			],
			'someModule.someGoodServiceName' => [
				'className' => \VendorName\SomeModule\Services\SecondService::class,
					'constructorParams' => static function (){
						return ['foo', 'bar'];
				},
			],
		],
		'readonly' => true,
	],
	//...
];
```

**Внимание!** Сервисы будут зарегистрированы только после подключения модуля. Также советуем именовать сервисы модулей, используя префикс имени модуля, чтобы не возникало проблемы уникальности кодов, например:

```
 iblock.imageUploader
	disk.urlManager
	crm.entityManager
	crm.urlManager
	someModule.urlManager.
```

**Регистрация через API**

Сервисы можно зарегистрировать и через API. Для этого воспользуйтесь методами класса [\Bitrix\Main\DI\ServiceLocator](https://dev.1c-bitrix.ru/api_d7/bitrix/main/di/servicelocator/index.php)

### Конфигурация сервиса

Конфигурация описывается в виде массива и подсказывает сервис локатору способ создания объекта. На данный момент есть три способа описания:

1. Указание класса сервиса. Сервис локатор создаст сервис вызвав `new $className`.
  ```
   'someModule.someServiceName' => [
  	'className' => \VendorName\SomeModule\Services\SomeService::class,
  ]
  ```
2. Указание класса сервиса и параметров, которые будут переданы в конструктор. Сервис локатор создаст сервис вызвав `new $className('foo', 'bar')`.
  ```
          'someModule.someServiceName' => [
                  'className' => \VendorName\SomeModule\Services\SomeService::class,
                 'constructorParams' => ['foo', 'bar'],
          ]
          'someModule.someServiceName' => [
                  'className' => \VendorName\SomeModule\Services\SomeService::class,
                  'constructorParams' => static function (){
                  return ['foo', 'bar'];
              },
          ]
  ```
3. Указание замыкания-конструктора, который должен создать и вернуть объект сервиса.
  ```
   'someModule.someAnotherServiceName' => [
              'constructor' => static function () {
                          return new \VendorName\SomeModule\Services\SecondService('foo', 'bar');
                  },
          ]
  ```
