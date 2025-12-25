# Диск

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/disk/index.php

`\Bitrix\Disk` - пространство имен модуля **Диск**.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('disk');
```

#### Примеры

Получить хранилище

```
<?php
if (\Bitrix\Main\Loader::includeModule('disk'))
{
	$driver = \Bitrix\Disk\Driver::getInstance();
	$storage = $driver->getStorageByUserId(1);//пользователя
	$storage = $driver->getStorageByGroupId(33);//группы
	$storage = $driver->getStorageByCommonId('shared_files_s1');//идентификатор
	$storage = \Bitrix\Disk\Storage::loadById(66);//знаем идентификатор хранилища
	if ($storage)
	{
		//можем работать с хранилищем
	}
}
```

Создать папку в хранилище

```
<?php
if (\Bitrix\Main\Loader::includeModule('disk'))
{
	$storage = \Bitrix\Disk\Driver::getInstance()->getStorageByUserId(1);
	if ($storage)
	{
		$folder = $storage->addFolder(
			array(
				'NAME' => 'New folder',
				'CREATED_BY' => 1
			)
		);
	}
}
```

Поиск папки в хранилище.

```
<?php
if (\Bitrix\Main\Loader::includeModule('disk'))
{
    $storage = \Bitrix\Disk\Driver::getInstance()->getStorageByUserId(1);
    if ($storage)
    {
        // Ищем папку в корне хранилища
        $folder = $storage->getChild([
            '=NAME' => 'New folder',
            'TYPE' => \Bitrix\Disk\Internals\FolderTable::TYPE_FOLDER
        ]);
    }
}
```

Поиск корневой папки и подпапки в ней.

```
<?php
if (\Bitrix\Main\Loader::includeModule('disk'))
{
    $storage = \Bitrix\Disk\Driver::getInstance()->getStorageByUserId(1);
    if ($storage)
    {
        // Получаем корневую папку хранилища
        $parentFolder = $storage->getRootObject();

        if ($parentFolder)
        {
            // Ищем подпапку внутри $parentFolder
            $subFolder = $parentFolder->getChild([
                '=NAME' => 'SubFolder',
                'TYPE' => \Bitrix\Disk\Internals\FolderTable::TYPE_FOLDER
            ]);

            if ($subFolder)
            {
                // Работаем с найденной подпапкой
            }
        }
    }
}
```

Создание подпапки в папке

```
<?php
if (\Bitrix\Main\Loader::includeModule('disk'))  {
	$storage = \Bitrix\Disk\Driver::getInstance()->getStorageByUserId(1);
	if ($storage)  {
		$folder = $storage->getRootObject();
		$folder = $folder->getChild(
			array(
				'=NAME' => 'New folder',
				'TYPE' => \Bitrix\Disk\Internals\FolderTable::TYPE_FOLDER
			)
		);
		if ($folder) {
			$folder->addSubFolder(    array(
				'NAME' => 'New folder 2',
				'CREATED_BY' => 1
			));
		}
	}
}
```

Задание прав на папку

```
<?php
	if ($folder)
	{
		$rightsManager = \Bitrix\Disk\Driver::getInstance()->getRightsManager();
		$accessTaskId = $rightsManager->getTaskIdByName($rightsManager::TASK_READ);//чтение
		//$accessTaskId = $rightsManager->getTaskIdByName($rightsManager::TASK_EDIT);//изменение
		//$accessTaskId = $rightsManager->getTaskIdByName($rightsManager::TASK_ADD);//добавление
		//$accessTaskId = $rightsManager->getTaskIdByName($rightsManager::TASK_FULL);//полные права

		$newFolder = $folder->addSubFolder(
			array( 'NAME' => 'New folder',  'CREATED_BY' => 1),
			array(
				array(
					'ACCESS_CODE' => 'U10', // для пользователя с ID=10 выдадутся выбранные права
					'TASK_ID' => $accessTaskId,
				),
			)
		);
	}
```

Отключение прав на папку. (Доступно с версии 17.0.2 модуля Диск.)

```
<?php
	if ($folder)
	{
		$rightsManager = \Bitrix\Disk\Driver::getInstance()->getRightsManager();
		$accessTaskId = $rightsManager->getTaskIdByName($rightsManager::TASK_READ);//чтение
		//$accessTaskId = $rightsManager->getTaskIdByName($rightsManager::TASK_EDIT);//изменение
		//$accessTaskId = $rightsManager->getTaskIdByName($rightsManager::TASK_ADD);//добавление
		//$accessTaskId = $rightsManager->getTaskIdByName($rightsManager::TASK_FULL);//полные права

		$newFolder = $folder->addSubFolder(
			array( 'NAME' => 'New folder',  'CREATED_BY' => 1),
			array(
				array(
					‘NEGATIVE' => true,
					'ACCESS_CODE' => 'U10',
					'TASK_ID' => $accessTaskId,
				),
			)
		);
	}
```

Загрузить файл в папку.

```
<?php
if (\Bitrix\Main\Loader::includeModule('disk'))
{
	$storage = \Bitrix\Disk\Driver::getInstance()->getStorageByUserId(1);
	if ($storage)
	{
		$folder = $storage->getChild(
			array(
				'=NAME' => 'New folder',
				'TYPE' => \Bitrix\Disk\Internals\FolderTable::TYPE_FOLDER
			)
		);
	if ($folder)
	{
		$fileArray = \CFile::MakeFileArray($_SERVER['DOCUMENT_ROOT'].'/test.jpg');
		$file = $folder->uploadFile($fileArray, array(
			'CREATED_BY' => 1
		));
	}
	}
}
```

Загрузка файла в корневую папку.

```
if (\Bitrix\Main\Loader::includeModule('disk'))
{
	$storage = \Bitrix\Disk\Driver::getInstance()->getStorageByUserId(1);
	if ($storage)
	{
		$folder = $storage->getRootObject();
		$fileArray = \CFile::MakeFileArray($_SERVER['DOCUMENT_ROOT'].'/test.jpg');
		$file = $folder->uploadFile($fileArray, array(
			'CREATED_BY' => 1
		));
	}
}
```

Высокоуровневая работа с объектом файла.

```
<?php
$newFile->markDeleted($deletedBy);
$newFile->delete($deletedBy);
```

Поиск файла для работы с ним. Работать с файлом можно только перейдя в папку.

```
<?php
if (\Bitrix\Main\Loader::includeModule('disk'))
{
	$storage = \Bitrix\Disk\Driver::getInstance()->getStorageByUserId(1);
	if ($storage)
	{
		$folder = $storage->getRootObject();
		$file = $folder->getChild(
			array(
				'=NAME' => 'test.jpg',
				'TYPE' => \Bitrix\Disk\Internals\FileTable::TYPE_FILE
			)
		);
		if ($file)
		{
			//
		}
	}
}
```

Получение ссылки на файл на портале.

```
<?php
if ($file)
{
		$urlManager = \Bitrix\Disk\Driver::getInstance()->getUrlManager();
		echo $urlManager->getPathFileDetail($file);
}
```

Получение публичной ссылки

```
<?php
if ($file)
{
	$urlManager = \Bitrix\Disk\Driver::getInstance()->getUrlManager();
	$extLink = $file->addExternalLink(
		array(
			'CREATED_BY' => 1,
			'TYPE' => \Bitrix\Disk\Internals\ExternalLinkTable::TYPE_MANUAL,
		)
	);
	$extLinkUrl = $urlManager->getShortUrlExternalLink(
		array(
			'hash' => $extLink->getHash(),
			'action' => 'default',
		),
		true
	);
	echo $extLink->getHash().'<br>';
	echo $extLinkUrl;
}
```

Получение физического файла

```
<?php
if ($file)
{
	//получение айди физического файла
	echo $file->getFileId();
	//работаем с ним
 	   CFile::ViewByUser($file->getFileId(), array('force_download' => true));
}
```

Работа с файлами

```
<?php
//загрузка новой версии файла
if ($file)
{
	$fileArray = \CFile::MakeFileArray($_SERVER['DOCUMENT_ROOT'].'/test.jpg');
	$newVersion = $file->uploadVersion($fileArray, 1);//файл, ID пользователя
// если при загрузке от одного пользователя двух версий файла с одним именем происходит менее 300 секунд - файлы сливаются.
}

//перемещение файла в другую папку
if ($file)
{
	$file->moveTo($folder, $movedBy);//объект папки, пользователь
}
```

Получение физического файла (для загрузки, например)

```
<?php
if ($file)
{
	//получение айди физического файла
	echo $file->getFileId();
	//работаем с ним
	CFile::ViewByUser($file->getFileId(), array('force_download' => true));
}
```

Проверка объекта и вывод ошибок

```
<?php
if ($folder)
{
	$folder->rename('Reports.backup');
}
else
{
	var_dump($folder->getErrors());
}
```

Работа с модулем допустима только высокоуровневыми методами.

```
<?php
//нельзя
FolderTable::update();

//следует
$folder->rename(‘New folder 2’);
```
