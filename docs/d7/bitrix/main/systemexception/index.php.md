# SystemException

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/systemexception/index.php

### Описание и пример

**SystemException** - базовый класс для всех исключений в системе.

В D7 обработка ошибок производится при помощи механизма исключений в полной аналогии с механизмом [исключений в php](http://php.net/manual/en/language.exceptions.php). Если происходит ошибка - выводится исключение. Если необходимо обработать ошибку - нужно поймать исключение.

Аналоги в старом ядре:

- [CMain::ThrowException](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/throwexception.php),
- [CMain::ResetException](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/resetexception.php),
- [CMain::GetException](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/getexception.php).

| Метод | Описание | С версии |
| --- | --- | --- |
| [construct](https://dev.1c-bitrix.ru/api_d7/bitrix/main/systemexception/__construct.php) | метод создаёт новый объект исключений. |  |

- [Исключения](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2803) в курсе Разработчик Bitrix Framework

**Примеры**

```
// D7
use Bitrix\Main\SystemException;

try
{
	// ...
	throw new SystemException("Error");
}
catch (SystemException $exception)
{
	echo $exception->getMessage();
}
```

### Иерархия исключений в D7

- `Bitrix\Main\SystemException` - базовый класс всех системных исключений

  - [Bitrix\Main\IO\IoException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/ioexception/index.php) - базовый класс всех исключений файлового ввода-вывода

    - [Bitrix\Main\IO\FileDeleteException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/filedeleteexception/index.php) - исключение при удалении файла
    - [Bitrix\Main\IO\FileNotFoundException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/filenotfoundexception/index.php) - отсутствие требуемого файла
    - [Bitrix\Main\IO\FileOpenException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/fileopenexception/index.php) - исключение при открытии файла
    - [Bitrix\Main\IO\InvalidPathException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/invalidpathexception/index.php) - не корректный путь
    - [Bitrix\Main\IO\FileNotOpenedException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/io/filenotopenedexception/index.php) - файл не открыт
  - [Bitrix\Main\Config\ConfigurationException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/config/configurationexception/index.php)   - ошибка в конфигурации
  - `Bitrix\Main\Security\SecurityException` - ошибка безопасности

    - [\Bitrix\Main\Security\Sign\BadSignatureException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/security/sign/badsignatureexception/index.php) - исключения ошибок подписи.
  - [Bitrix\Main\ArgumentException](../argumentexception/index.php.md)      - базовый класс исключений, связанных с входящими параметрами методов

    - [Bitrix\Main\ArgumentNullException](../argumentnullexception/index.php.md)   - параметр должен быть не пустым
    - [Bitrix\Main\ArgumentOutOfRangeException](../argumentoutofrangeexception/index.php.md)   - параметр вне допустимого диапазона
    - [Bitrix\Main\ArgumentTypeException](../argumenttypeexception/index.php.md)   - параметр не допустимого типа
  - [Bitrix\Main\DB\Exception](https://dev.1c-bitrix.ru/api_d7/bitrix/main/db/exception/index.php) - базовый класс для исключений БД

    - `Bitrix\Main\DB\ConnectionException`   - исключение при соединении
    - [Bitrix\Main\DB\SqlException](https://dev.1c-bitrix.ru/api_d7/bitrix/main/db/sqlexpression/index.php)      - исключение при выполнении запроса
  - [Bitrix\Main\NotSupportedException](../notsupportedexception/index.php.md)   - вызывается, если функционал не поддерживается
  - [Bitrix\Main\NotImplementedException](../notimplementedexception/index.php.md)   - вызывается, если функционал должен поддерживаться, но пока не реализован
  - [Bitrix\Main\AccessDeniedException](../accessdeniedexception/index.php.md) - вызывается когда доступ запрещён
- [\Bitrix\Main\ObjectPropertyException](../objectpropertyexception/index.php.md) - исключение выводится когда свойства объекта не валидны.
- [\Bitrix\Main\ObjectNotFoundException](../objectnotfoundexception/index.php.md)  - выводит исключение когда объект не существует.
- [\Bitrix\Main\ObjectException](../objectexception/index.php.md) - исключение выводится, если объект не может быть создан.
- `Bitrix\Main\LoaderException` - исключение в загрузчике
