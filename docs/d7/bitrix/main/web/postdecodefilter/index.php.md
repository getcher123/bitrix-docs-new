# PostDecodeFilter

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/postdecodefilter/index.php

Класс декодирует данные в коллекции. Актуально при работе с коллекциями _POST.

| Метод | Описание | С версии |
| --- | --- | --- |
| [filter](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/postdecodefilter/filter.php) | Метод возвращает массив декодированных данных через getPost(). |  |

#### Примеры

```
Application::getInstance()->getContext()->getRequest()->addFilter(new PostDecodeFilter)
```
