# Настройка хранения данных сессии

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 14024 — Сессия разделенный режим (hot&cold)](lesson_14024.md)
- [Следующий: 2465 — Работа с сессиями →](lesson_2465.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=14026

Ядро поддерживает четыре варианта для хранения (файлы, redis, database, memcache) данных сессии. Способ хранения описывается в bitrix/.settings.php в секции 'session':



По умолчанию cекция `'session'` может отсутствовать в файле .settings.php. Добавьте ее вручную при необходимости.

### Файлы

```
// bitrix/.settings.php
return [
//...
	'session' => [
		'value' => [
			'mode' => 'default',
			'handlers' => [
			'general' => [
				'type' => 'file',
				]
			],

		]
	]
];
```

**Настройка для разделённой сессии**:

```
// bitrix/.settings.php
return [
//...
	'session' => [
		'value' => [
			'lifetime' => 14400, // +
			'mode' => 'separated',  // +
			'handlers' => [
				'kernel' => 'encrypted_cookies',  // +
				'general' => [
					'type' => 'file',
				],
			],
		]
	]
];
```

### Redis

```
// bitrix/.settings.php
return [
'session' => [
	'value' => [
		'mode' => 'default',
		'handlers' => [
			'general' => [
				'type' => 'redis',
				'port' => '6379',
				'host' => '127.0.0.1',
			],
		],
	],
]
```

**Кластерное хранения данных сессии**

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

**Настройка для разделённой сессии**:

```
// bitrix/.settings.php
return [
//...
	'session' => [
		'value' => [
			'lifetime' => 14400, // +
			'mode' => 'separated', // +
			'handlers' => [
				'kernel' => 'encrypted_cookies',  // +
				'general' => [
					'type' => 'redis',
					'port' => '6379',
					'host' => '127.0.0.1',
					],
				],
			]
		]
];
```

### Memcache

```
// bitrix/.settings.php
return [
//...
	'session' => [
		'value' => [
			'mode' => 'default',
			'handlers' => [
				'general' => [
					'type' => 'memcache',
					'port' => '11211',
					'host' => '127.0.0.1',
					],
				],
			]
	]
];
```

**Кластерное хранения данных сессии**

Если необходимо создать кластер из memcache серверов, то достаточно добавить настройку **servers**.

```
// bitrix/.settings.php
return [
//...
	'session' => [
		'value' => [
			'mode' => 'default',
			'handlers' => [
				'general' => [
					'type' => 'memcache',
					'servers' => [
						[
							'port' => 11211,
							'host' => '127.0.0.1',
							'weight' => 1, //про настройку weight читайте внимательно в документации по memcahe
						],
						[
							'port' => 11211,
							'host' => '127.0.0.2',
						],
					],
				],
			],
		]
	]
];
```

**Настройка для разделённой сессии**:

```
// bitrix/.settings.php
return [
//...
	'session' => [
		'value' => [
			'lifetime' => 14400, // +
			'mode' => 'separated', // +
			'handlers' => [
				'kernel' => 'encrypted_cookies',  // +
				'general' => [
					'type' => 'memcache',
					'port' => '11211',
					'host' => '127.0.0.1',
						],
					],
				]
		]
];
```

### Mysql

Данные хранятся в таблице **b_user_session**

```
// bitrix/.settings.php
return [
//...
	'session' => [
		'value' => [
			'mode' => 'default',
			'handlers' => [
				'general' => [
					'type' => 'database',
					]
				],
			]
		]
];
```

**Настройка для разделённой сессии**:

```
// bitrix/.settings.php
return [
//...
	'session' => [
		'value' => [
			'lifetime' => 14400, // +
			'mode' => 'separated', // +
			'handlers' => [
				'kernel' => 'encrypted_cookies',  // +
				'general' => [
					'type' => 'database',
					]
				],
			]
		]
];
```
