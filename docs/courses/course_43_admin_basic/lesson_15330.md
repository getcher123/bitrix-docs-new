# Логгеры

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 13770 — Генерация ссылок](lesson_13770.md)
- [Следующий: 14380 — Вложенные транзакции →](lesson_14380.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=15330

### Введение

В ядро добавлены логгеры, реализующие интерфейс [PSR-3](https://www.php-fig.org/psr/psr-3/):

- базовый абстрактный класс *\Bitrix\Main\Diag\Logge*r, реализующий интерфейс PSR-3;
- файловый логгер *\Bitrix\Main\Diag\FileLogger*;
- syslog логгер *\Bitrix\Main\Diag\SysLogge*r.

Логгеры пользуются форматтером логов *\Bitrix\Main\Diag\LogFormatter*, который делает замены плейсхолдеров в соответствии с PSR-3.

**Примечание**: Библиотека доступна с версии main 21.900.0.

### Logger Interface

Интерфейс *\Psr\Log\LoggerInterface* довольно прост, это - набор функций логирования, поддерживающих уровни логирования. Уровни задаются константами `\Psr\Log\LogLevel::*`.

```
interface LoggerInterface
{
	public function emergency($message, array $context = array());
	public function alert($message, array $context = array());
	public function critical($message, array $context = array());
	public function error($message, array $context = array());
	public function warning($message, array $context = array());
	public function notice($message, array $context = array());
	public function info($message, array $context = array());
	public function debug($message, array $context = array());
	public function log($level, $message, array $context = array());
}
```

В сообщении могут быть `{плейсхолдеры}`, которые заменяются данными из ассоциативного массива **$context**.

Также полезным может быть интерфейс *\Psr\Log\LoggerAwareInterface*, если вы хотите сообщить, что ваш объект готов принять логгер PSR-3:

```
interface LoggerAwareInterface
{
	public function setLogger(LoggerInterface $logger);
}
```

### Логгеры в продукте

Логгеры в продукте расширены по сравнению с PSR-3. Можно:

- установить минимальный уровень логирования, ниже которого логгер ничего не выведет,
- установить форматтер.

Файловый логгер *\Bitrix\Main\Diag\FileLogger* умеет записывать сообщения в файл, указанный в конструкторе. Если размер лога превышает указанный максимальный, производится однократная ротация файла. Ноль означает не делать ротацию. По умолчанию размер 1 Мб.

```
$logger = new Diag\FileLogger($logFile, $maxLogSize);
$logger->setLevel(\Psr\Log\LogLevel::ERROR);
// выведет в лог
$logger->error($message, $context);
// НЕ выведет в лог
$logger->debug($message, $context);
```

Syslog логгер *\Bitrix\Main\Diag\SysLogger* является надстройкой над функцией php [syslog](https://www.php.net/manual/ru/function.syslog.php). Конструктор принимает параметры, использующиеся функцией [openlog](https://www.php.net/manual/ru/function.openlog.php).

```
$logger = new Diag\SysLogger('Bitrix WAF', LOG_ODELAY, $facility);
$logger->warning($message);
```

На файловый логгер переведена функция [AddMessage2Log](https://dev.1c-bitrix.ru/api_help/main/functions/debug/addmessage2log.php) и класс *\Bitrix\Main\Diag\FileExceptionHandlerLog*, а также логирование в модуле [Проактивная защита](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&CHAPTER_ID=04547) (**security**).

В настройках [.settings.php](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=02795) можно:

- указать логгер для AddMessage2Log с версии 23.500.0;
- переопределить логгер по умолчанию для модуля Конвертер файлов (**transformer**). Идентификатор id логгера – transformer.Default. С версии модуля transformer 23.0.0.

### Форматирование сообщения

В логгер можно установить форматтер сообщения. По умолчанию используется форматтер *\Bitrix\Main\Diag\LogFormatter*, реализующий интерфейс *\Bitrix\Main\Diag\LogFormatterInterface*:

```
interface LogFormatterInterface
{
	public function format($message, array $context = []): string;
}
```

Конструктор форматтера принимает параметры `$showArguments = false, $argMaxChars = 30` (показывать значение аргументов в трейсе, максимальная длина аргумента).

```
$logger = new Main\Diag\FileLogger(LOG_FILENAME, 0);
$formatter = new Main\Diag\LogFormatter($showArgs);
$logger->setFormatter($formatter);
```

Основная задача форматтера - подставлять значения в плейсхолдеры сообщения из массива контекста. Форматтер умеет обрабатывать определенные плейсхолдеры:

- `{date}` - текущее время * ;
- `{host}` - HTTP host * ;
- `{exception}` - объект исключения (\Throwable);
- `{trace}` - массив бектрейса;
- `{delimiter}` - разделитель сообщений * .

* - не обязательно передавать в массиве контекста, подставляется автоматически.

```
$logger->debug(
	"{date} - {host}\n{trace}{delimiter}\n",
	[
		'trace' => Diag\Helper::getBackTrace(6, DEBUG_BACKTRACE_IGNORE_ARGS, 3)
	]
);
```

Значения из массива контекста форматтер старается привести к удобному виду в зависимости от типа значения. Принимаются строки, массивы, объекты.

**Форматтер JsonLinesFormatter**

С версии 25.300.0 Главного модуля доступен форматтер `Bitrix\Main\Diag\JsonLinesFormatter`. Он игнорирует параметр сообщения `$message` и выводит данные из контекста `$context` в формате [JSON Lines](https://jsonlines.org) (каждая запись лога — отдельная строка в формате JSON).

### Использование

В простом виде объект может принять логгер снаружи, поддерживая интерфейс *\Psr\Log\LoggerAwareInterface*. Можно использовать соответствующий трейт:

```
use Bitrix\Main\Diag;
use Psr\Log;

class MyClass implements Log\LoggerAwareInterface
{
	use Log\LoggerAwareTrait;

	public function doSomething()
	{
		if ($this->logger)
		{
			$this->logger->error('Error!');
		}
	}
}

$object = new MyClass();
$logger = new Diag\FileLogger("/var/log/php/error.log");
$object->setLogger($logger);
$object->doSomething();
```

Однако, не удобно менять код на работающем проекте, чтобы передать логгер в нужный объект. Для этого в классе логгера предусмотрена своя фабрика. На вход фабрике передается строка-идентификатор логгера:

```
use Bitrix\Main\Diag;
use Psr\Log;

class MyClass implements Log\LoggerAwareInterface
{
	use Log\LoggerAwareTrait;

	public function doSomething()
	{
		if ($logger = $this->getLogger())
		{
		$logger->error('Error!');
		}
	}

	protected function getLogger()
	{
		if ($this->logger === null)
		{
			$logger = Diag\Logger::create('myClassLogger', [$this]);
			$this->setLogger($logger);
		}

		return $this->logger;
	}
}
```

#### Настройка

В корневой секции файла **.settings.php** логгеры указываются в ключе **loggers**. Синтаксис описания совпадает с настройками [ServiceLocator](lesson_14032.md#registration). Отличие состоит в том, что сервис-локатор является реестром, а здесь настраивается фабрика.

В замыкание-конструктор *constructor* можно передать дополнительные параметры через второй параметр фабрики `Diag\Logger::create('logger.id', [$this])`. Параметры позволяют гибко включать логирование в зависимости от переданных параметров, в том числе вызывать методы самого объекта.

Дополнительно можно указать минимальный уровень журналирования (level) и собственный форматтер (formatter). Форматтер ищется в сервис локаторе по его идентификатору.

```
// /bitrix/.settings.php
return [
	//...
	'services' => [
		'value' => [
			//...
			'formatter.Arguments' => [
				'className' => '\Bitrix\Main\Diag\LogFormatter',
				'constructorParams' => [true],
			],
		],
		'readonly' => true,
	],
	'loggers' => [
		'value' => [
			//...
			'main.HttpClient' => [
//				'className' => '\\Bitrix\\Main\\Diag\\FileLogger',
//				'constructorParams' => ['/home/bitrix/www/log.txt'],
//				'constructorParams' => function () { return ['/home/bitrix/www/log.txt']; },
				'constructor' => function (\Bitrix\Main\Web\HttpClient $http, $method, $url) {
					$http->setDebugLevel(\Bitrix\Main\Web\HttpDebug::ALL);
					return new \Bitrix\Main\Diag\FileLogger('/home/bitrix/www/log.txt');
				},
				'level' => \Psr\Log\LogLevel::DEBUG,
				'formatter' => 'formatter.Arguments',
			],
		],
		'readonly' => true,
	],
	//...
];
```



При указании замыкания-конструктора constructor желательно использовать файл **.settings_extra.php**, чтобы не потерять код при сохранении настроек из API.

Существует *\Psr\Log\NullLogger*, его можно установить, если не хочется писать `if($logger)` перед каждым вызовом логгера. Однако, следует учитывать, стоит ли делать дополнительную работу по формированию сообщения и контекста.

### Классы

Список классов, поддерживающих фабрику логгеров:

| \| Класс \| Id логгера \| Передаваемые параметры \|<br>\| --- \| --- \| --- \|<br>\| [\Bitrix\Main\Web\HttpClient](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/index.php) \| main.HttpClient \| `[$this, $this->queryMethod, $this->effectiveUrl]` \| |
| --- |
