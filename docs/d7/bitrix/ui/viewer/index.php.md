# Просмотрщик

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/viewer/index.php

### Описание и подключение

Javascript-расширение `ui.viewer` позволяет автоматически просматривать разные типы файлов, сохраненные в `b_file`, например, офисные документы, видео- и аудиофайлы, файлы с кодом, автоматически конвертируя их, а также свои кастомные типы. При этом учитывается оригинальная проверка прав в модуле.

### Подключение на PHP-странице

Подключение простое. Во-первых, нужно загрузить расширение:

```
\Bitrix\Main\UI\Extension::load("ui.viewer");
```

Во-вторых, чтобы по клику на ссылку или другую DOM-ноду, запускался просмотрщик, необходимо указать специальные `data-атрибуты`. Для этого лучше воспользоваться классом `\Bitrix\Main\UI\Viewer\ItemAttributes`:

```
//уверен, у вас есть id из b_file.ID
$fileId = 2208;

//и уверен, что у вас есть ссылка на скачивание этого файла.
//Ведь его как-то получают пользователи?
$urlToDownload = '/show_file.php?haha=hihi';

$attributes = \Bitrix\Main\UI\Viewer\ItemAttributes::tryBuildByFileId($fileId, $urlToDownload);
$attributes->setTitle("Назови меня своим именем.mp4");

...
//а дальше в месте вывода html'a вам необходимо просто вывести $attributes
echo "<div {$attributes}>Прикрепленный файл</div>";

//либо как-то так
<div <?= ItemAttributes::tryBuildByFileId($fileId, $urlToDownload)->setTitle('July.jpg')) ?> >Просмотреть файл</div>
```

> **Важно!** Ваша точка отдачи файла должна работать с записью из `b_file`. И вызывать либо `\CFile::viewByUser`, либо `\Bitrix\Main\Engine\Response\BFile`, передавая ID файла, так как именно по ID файла и происходит "магия".

### Поддержка листания нескольких файлов на странице

Если на странице расположены файлы, которые необходимо листать, то при создании `ItemAttributes` для каждого из них нужно установить идентификатор группы, внутри которой будет листание.

```
use \Bitrix\Main\UI\Viewer\ItemAttributes;
$attributes = ItemAttributes::tryBuildByFileId($fileId, $urlToDownload)
	->setTitle("Назови меня своим именем.mp4")
	->setGroupBy("blog-post-4")
;
```

Теперь при запуске просмотра, листание файлов будет между объектами, у которых установлена группа в `blog-post-4`.

### Установка действий

По умолчанию при просмотре файла выводится действие "Скачать". Если необходимо добавить свои действия, то используйте `ItemAttributes::addAction`.

```
use \Bitrix\Main\UI\Viewer\ItemAttributes;
$attributes = ItemAttributes::tryBuildByFileId($fileId, $urlToDownload)
		->setTitle("Назови меня своим именем.mp4")
		->addAction([
			'type' => 'edit',
			'action' => 'BX.SomeModule.Handlers.runEdit',
		])
		->addAction([
			'type' => 'destroy',
			'text' => 'Destroy The Universe',
			'action' => 'BX.SomeModule.Handlers.destroy', //ссылка на фунцкию-обработчик
			'buttonIconClass' => 'ui-btn-icon-remove', //класс иконки кнопки
			'params' => [ //параметры, которые будут переданы внутрь функции-обработчика
				'objectId' => 4546,
			],
			//js-расширение, в котором находятся функции-обработчики.Это расширение будет автоматически загружено при просмотре
			'extension' => 'someModule.viewer.actions',
		]),
		->addAction([
			'type' => 'order',
			'text' => 'Выбрать режим',
			//выпадающее меню. Формат пунктов см. в BX.PopupMenuWindow
			'items' => [
				[
 					'text' => 'Item 1',
					'onclick' => "BX.SomeModule.Handlers.handleClick(1)",
				],
				[
					'text' => 'Item 2',
					'onclick' => "BX.SomeModule.Handlers.handleClick(2)",
			],
		])
;
```

> **Важно!** В `action` передается ссылка на js-функцию, которая будет вызвана при клике на кнопку в просмотрищке. В функцию будет передан текущий просматриваемый элемент и доп.параметры.

```
/**
 * @param {BX.UI.Viewer.Item} item
 * @param {Object} params
 */
BX.SomeModule.Handlers.destroy = function(item, params)
{
	//some work
	console.log(params.objectId); //выведет 4546
}
```

Отметим, что по умолчанию есть тексты, иконки для `type`:

- download
- edit
- share
- print
- info
- delete

### Советы

Просмотрщик спроектирован так, чтобы легко запускаться и внутри слайдера-iframe, поэтому обязательно оформляйте js-обработчики в расширения и указывайте их при добавлении `addAction`.

Не беспокойтесь за проверку прав, ведь просмотрщик всего лишь использует вашу точку отдачи, где вы уже проверили права, и автоматически туда встраивается.

Если у вас уже загружены данные по `b_file.ID`, то воспользуйтесь

```
\Bitrix\Main\UI\Viewer\ItemAttributes::tryBuildByFileData(array $fileData, $sourceUri);
```

Новинки документации в соцсетях:

[https://vk.com/1c_bitrix_doc](https://vk.com/1c_bitrix_doc)

[https://www.youtube.com/channel/UCtugDnALPdpOISTVfA8Hmjw](https://www.youtube.com/channel/UCtugDnALPdpOISTVfA8Hmjw)

[https://rutube.ru/channel/23487950/](https://rutube.ru/channel/23487950/)

[https://t.me/bitrixdoc](https://t.me/bitrixdoc)

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на форумы.
