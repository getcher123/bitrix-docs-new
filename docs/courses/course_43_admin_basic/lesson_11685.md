# Bitrix CLI

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 4637 — Composer и Bitrix Framework](lesson_4637.md)
- [Следующий: 3043 — Замечания по $arParams и $arResult →](lesson_3043.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11685

Командный интерфейс реализован на основе библиотеки `symfony/console`. Перед началом использования убедитесь, что [установили зависимости через composer](lesson_4637.md).

Исполняемый файл находится в папке `bitrix`:

```

$ cd bitrix
$ php bitrix.php
```

Для удобства вы можете создать символическую ссылку без постфикса php:

```

$ chmod +x bitrix.php
$ ln -s bitrix.php bitrix
$ ./bitrix
```

Список доступных команд «из коробки»:

- [orm:annotate](lesson_11733.md)
- translate:index
- make:controller — создать класс-контроллер
- make:tablet — создать ORM таблет

С версии **main 24.0.0** появится возможность добавлять свои команды через файлы настроек модуля `{moduleName}/.settings.php`. Команды модуля перечисляются в секции **console**:

```
<?php

return [
	//...
	'console' => [
		'value' => [
			'commands' => [
				\Module\Name\Cli\CustomCommand::class,
				\Module\Name\Feature\Path\Cli\AnotherCommand::class,
			],
		],
		'readonly' => true,
	],
];
```

**Примечание.** Команду рекомендуется называть с префиксом модуля в виде `module:command`.

**Дополнительно**:

- [Инструмент @bitrix/cli](lesson_12435.md).
