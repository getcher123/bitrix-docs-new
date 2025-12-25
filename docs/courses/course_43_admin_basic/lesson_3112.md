# Практика. Некоторые классы

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2534 — Если нет описания API](lesson_2534.md)
- [Следующий: 3570 — Практика. Работа с D7 на примере местоположений →](lesson_3570.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3112

#### Конфигурация

Расположено в пространстве имен [\Bitrix\Main\Config](http://dev.1c-bitrix.ru/api_d7/bitrix/main/config/index.php). Состоит из двух классов: [\Bitrix\Main\Config\Configuration](http://dev.1c-bitrix.ru/api_d7/bitrix/main/config/configuration/index.php) и [\Bitrix\Main\Config\Option](http://dev.1c-bitrix.ru/api_d7/bitrix/main/config/option/index.php).

**Configuration**

```
$realm = \Bitrix\Main\Config\Configuration::getValue("http_auth_realm");
if (is_null($realm))
	$realm = "Bitrix Site Manager"
```

Класс отвечает за глобальные настройки всего приложения. (Это то, что в старом ядре определяется константами.) Класс оперирует единой базой настроек, которые хранятся в файле `/bitrix/.settings.php`. Данные хранятся произвольные. Например, для соединений может храниться целый пул данных для именованных соединений.

**Option**

```
$cookiePrefix = \Bitrix\Main\Config\Option::get('main', 'cookie_name', 'BITRIX_SM');
$cookieLogin = $request->getCookie($cookiePrefix.'_LOGIN');
$cookieMd5Pass = $request->getCookie($cookiePrefix.'_UIDN');
```

Является в некоторой степени аналогом класс [COption](http://dev.1c-bitrix.ru/api_help/main/reference/coption/index.php) старого ядра и работает с параметрами модулей, сайтов, хранимых в базе данных. Это то, что управляется из административной части: настройки каких-то форм, установка и так далее.

#### Файлы

Работа с файлами объектно-ориентированная, вынесена в пространство имён [Bitrix\Main\IO](http://dev.1c-bitrix.ru/api_d7/bitrix/main/io/index.php) и обладает тремя базовыми классами:

- [Path](http://dev.1c-bitrix.ru/api_d7/bitrix/main/io/path/index.php) – работа с путями, статический.
- [Directory](http://dev.1c-bitrix.ru/api_d7/bitrix/main/io/directory/index.php) – работа с папками.
- [File](http://dev.1c-bitrix.ru/api_d7/bitrix/main/io/file/index.php) – работа с файлами.

Кроме них есть и другие классы, в том числе и абстрактные, для организации иерархии.

#### Другие классы

В папке `bitrix/modules/main/lib` расположена библиотека классов для осуществления разных частых действий, которые вынесены в **Main**, а не разнесены по разным модулям. В том числе в соответствующих пространствах  лежат файлы и API для работы:

- [Bitrix\Main\Data](http://dev.1c-bitrix.ru/api_d7/bitrix/main/data/index.php) - с кешем, в том числе управляемый кеш.
- [Bitrix\Main\Text](https://dev.1c-bitrix.ru/api_d7/bitrix/main/text/index.php) - с текстом: классы для конвертации текста и другие
- [Bitrix\Main\Type](http://dev.1c-bitrix.ru/api_d7/bitrix/main/type/index.php) - с типами данных: дата, файл и другие.
- [Bitrix\Main\Web](http://dev.1c-bitrix.ru/api_d7/bitrix/main/web/index.php) - с web: работа с URL, обращения по web'у и другие.

#### Аналог CUtil::jSPostUnescape() в D7

Если необходимо использовать **HttpRequest** при аякс запросах:

```
Application::getInstance()->getContext()->getRequest()->getPost('name')
```

то надо учитывать, что *CUtil::JSPostUnescape* не поможет в случае установки win-1251.

Можно использовать:

```
use Bitrix\Main\Web\PostDecodeFilter;
...
Application::getInstance()->getContext()->getRequest()->addFilter(new PostDecodeFilter)
```

После этого можно получать декодированные данные через *getPost*.
