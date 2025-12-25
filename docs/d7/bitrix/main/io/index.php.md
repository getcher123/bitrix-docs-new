# IO

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/index.php

**IO** - объектно-ориентированная работа с файлами, обладает тремя базовыми классами: `\Path`, `\Directory`, `\File`. Кроме них есть и другие классы, в том числе и абстрактные, для организации иерархии.

| Класс | Описание | С версии |
| --- | --- | --- |
| [File](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/file/index.php) | Класс для работы с файлами. |  |
| [Directory](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/directory/index.php) | Класс для работы с директориями. |  |
| [Path](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/path/index.php) | Класс для работы с путями. |  |
| [FileDeleteException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/filedeleteexception/index.php) | Исключение при удалении файла |  |
| [FileNotFoundException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/filenotfoundexception/index.php) | Исключение при отсутствии требуемого файла |  |
| [FileOpenException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/fileopenexception/index.php) | Исключение при открытии файла |  |
| [InvalidPathException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/invalidpathexception/index.php) | Исключение не корректного пути к файлу. |  |
| [IoException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/ioexception/index.php) | Базовый класс всех исключений файлового ввода-вывода. |  |

<!-- Про старое ядро перенести в delete после создания страниццы. При добавлении новых классов и страниц использовать: http://mrcappuccino.ru/blog/post/work-with-file-system-bitrix-d7 -->

В старом ядре [DeleteDirFilesEx](http://dev.1c-bitrix.ru/api_help/main/functions/file/deletedirfilesex.php) принимал путь от корня сайта, а его аналог принимает абсолютный путь к файлу от корня сервера.

> Обратите внимание : вместо $_SERVER["DOCUMENT_ROOT"] сейчас можно использовать [\Bitrix\Main\Application::getDocumentRoot](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/getdocumentroot.php).

**Примеры**

```
// D7
use Bitrix\Main\Application;
use Bitrix\Main\IO\Directory;
use Bitrix\Main\IO\File;

Directory::createDirectory(
	Application::getDocumentRoot() . "/foo/bar/baz/"
);
File::putFileContents(
Application::getDocumentRoot() . "/foo/bar/baz/1.txt",
	"hello from D7"
);
Directory::deleteDirectory(
	Application::getDocumentRoot() . "/foo/bar/baz/"
);
```
