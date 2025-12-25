# Cookie

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/cookie/index.php

**Cookie** - класс для работы с файлами cookie.

Аналоги в старом ядре:

[CMain::set_cookie](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/set_cookie.php) - для создания,

[CMain::get_cookie](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/get_cookie.php) - для получения.

В ядре D7 cookie задавать нужно через класс *Bitrix\Main\HttpResponse*, получать их нужно через класс [Bitrix\Main\HttpRequest](../../httprequest/index.php.md).

#### Примеры

```
use Bitrix\Main\Application;
use Bitrix\Main\Web\Cookie;
$cookie = new Cookie("TEST", 42);
$cookie->setDomain("example.com");
Application::getInstance()->getContext()->getResponse()->addCookie($cookie);
// Cookie будет доступна только на следующем хите!
echo Application::getInstance()->getContext()->getRequest()->getCookie("TEST");
```
