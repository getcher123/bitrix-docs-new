# Подключения к Redis, Memcache

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3400 — Обновление, бекап и восстановление](lesson_3400.md)
- [Следующий: 23612 — Локальные настройки SMTP-сервера →](lesson_23612.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=14034

Для создания подключения в файле настроек `bitrix/.settings.php`, необходимо добавить в секцию **connections** именованное подключение.



### Redis

Убедитесь, что у вас установлено расширение Redis для работы через PHP.

**Обычное подключение**:

```
'connections' => [
	'value' => [
		'default' => [
			'className' => \Bitrix\Main\DB\MysqliConnection::class,
			//... настройки существующего подключения в БД
		],
		'custom.redis' => [
			'className' => \Bitrix\Main\Data\RedisConnection::class,
			'port' => 6379,
			'host' => '127.0.0.1',
			'serializer' => \Redis::SERIALIZER_IGBINARY,
		],
		'custom2.redis' => [
			'className' => \Bitrix\Main\Data\RedisConnection::class,
			'port' => 6379,
			'host' => '127.0.0.4',
			'serializer' => \Redis::SERIALIZER_IGBINARY,
		],
	],
	'readonly' => true,
]
```

**Кластер**

Отличие от обычной конфигурации заключается лишь в **servers** дополнительных опциях: serializer, persistent, failover, timeout, read_timeout. Про них можно прочитать в официальной документации.

Redis в режиме cluster может быть настроен двумя способами:

1. Мультимастер кластер: N мастеров (и могут быть слейвы у каждого).
2. Обычный кластер: 1 мастер и N слейвов

Redis cluster в режиме мультимастер, указываются параметры всех мастеров:

```
// bitrix/.settings.php
return [
//...
	'session' => [
		'value' => [
			'mode' => 'default',
			'handlers' => [
				'general' => [
					'type' => 'redis',
					'servers' => [
						[
							'port' => 6379,
							'host' => '127.0.0.1',
						],
						[
							'port' => 6379,
							'host' => '127.0.0.2',
						],
						[
							'port' => 6379,
							'host' => '127.0.0.3',
						],
						'serializer' => \Redis::SERIALIZER_IGBINARY,
						'persistent' => false,
						'failover' => \RedisCluster::FAILOVER_DISTRIBUTE,
						'timeout' => null,
						'read_timeout' => null,
					],
				],
			],
		]
	]
];
```

Redis cluster в режиме 1 мастер + N слейвов. Указываются только параметры мастера блок с опциями опускается:

```
return [
	'session' => [
		'value' => [
			'mode' => 'default',
			'handlers' => [
				'general' => [
					'type' => 'redis',
					'servers' => [
						[
							'port' => '30015',
							'host' => '127.0.0.1'
						],
					],
				],
			],
		],
	],
];
```

**Использование**

Чтобы получить экземпляр соединения, достаточно обратиться по имени соединения, используя метод [\Bitrix\Main\Application::getConnection](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/getconnection.php).

```
/** @var \Redis $redisConnection **/
$redisConnection = \Bitrix\Main\Application::getConnection('custom.redis')->getResource();
$redisConnection->setnx('foo', 'bar');
```

### Memcache

Убедитесь, что у вас установлено расширение Memcache для работы через PHP.

**Обычное подключение**

```
'connections' => [
	'value' => [
		'default' => [
			'className' => \Bitrix\Main\DB\MysqliConnection::class,
			//... настройки существующего подключения в БД
		],
		'custom.memcache' => [
			'className' => \Bitrix\Main\Data\MemcacheConnection::class,
			'port' => 11211,
			'host' => '127.0.0.1',
		],
      'custom42.memcache' => [
        'className' => \Bitrix\Main\Data\MemcacheConnection::class,
        'port' => 6379,
        'host' => '127.0.0.4',
		],
	],
	'readonly' => true,
]
```

**Кластер**

Если необходимо создать кластер из memcache серверов, то достаточно добавить настройку servers.

```
'connections' => [
	'value' => [
		'default' => [
			'className' => \Bitrix\Main\DB\MysqliConnection::class,
			//... настройки существующего подключения в БД
				],
		'custom.memcache' => [
			'className' => \Bitrix\Main\Data\MemcacheConnection::class,
			'servers' => [
				[
				'port' => 11211,
				'host' => '127.0.0.1',
				'weight' => 1, //про настройку weight читайте внимательно в документации по memcahe
				],
				[
				'port' => 11211,
				'host' => '127.0.0.2',
				'weight' => 1, //про настройку weight читайте внимательно в документации по memcahe
				],
			],
		],
	],
	'readonly' => true,
]
```

**Использование**

Чтобы получить экземпляр соединения, достаточно обратиться по имени соединения, используя метод [\Bitrix\Main\Application::getConnection](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/getconnection.php).

```
/** @var \Memcache $memcacheConnection **/
$memcacheConnection = \Bitrix\Main\Application::getConnection('custom.memcache')->getResource();
$memcacheConnection->set('foo', 'bar');
```
