# Логирование

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/logging.php

Клиент поддерживает [PSR-3 логгеры](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=15330). Рекомендуется настраивать логирование через **.settings.php** – в этом случае можно создавать разные экземпляры логгера для каждого запроса. Это может быть полезным для логирования пачки асинхронных запросов – например, записывать отладку в разные файлы, а не перемешанные части разных запросов в один файл.

Конструктор логгера получает объект типа `\Bitrix\Main\Web\Http\DebugInterface`, который позволяет установить уровень логирования (см. константы `\Bitrix\Main\Web\HttpDebug`), и объект запроса типа `\Psr\Http\Message\RequestInterface`.

```
return [
	// ...
	'loggers' => [
		'value' => [
			'main.HttpClient' => [
				'constructor' => function (\Bitrix\Main\Web\Http\DebugInterface $debug, \Psr\Http\Message\RequestInterface $request) {
					$debug->setDebugLevel(\Bitrix\Main\Web\HttpDebug::ALL);
					return new \Bitrix\Main\Diag\FileLogger('/home/bitrix/www/httplog'. spl_object_hash($request) . '.txt');
				},
				'level' => \Psr\Log\LogLevel::DEBUG,
			],
		],
	],
	// ...
];
```

Возвращаемому логгеру можно установить свой форматтер. Например, чтобы просто логировать все обращения к внешним ресурсам через http-клиент, можно использовать следующее решение:

```
return [
	// ...
	'loggers' => [
		'value' => [
			'main.HttpClient' => [
				'constructor' => function (\Bitrix\Main\Web\Http\DebugInterface $debug, \Psr\Http\Message\RequestInterface $request) {
					$debug->setDebugLevel(\Bitrix\Main\Web\HttpDebug::REQUEST_HEADERS);

					$logger = new \Bitrix\Main\Diag\FileLogger($_SERVER['DOCUMENT_ROOT'] . '/http.txt');

					$logger->setFormatter(
						new class($request) implements \Bitrix\Main\Diag\LogFormatterInterface
						{
							public function __construct(public \Psr\Http\Message\RequestInterface $request) {}

							public function format($message, array $context = []): string
							{
								// Игнорировать запросы push-сервера
								if ($this->request->getUri()->getPort() === 1337)
								{
									return '';
								}

								return $this->request->getUri() . " \t" . $_SERVER['REQUEST_URI'] . "\n";
							}
						}
					);

					return $logger;
				},
				'level' => \Psr\Log\LogLevel::DEBUG,
			],
		],
		'readonly' => true,
	],
	// ...
];
```
