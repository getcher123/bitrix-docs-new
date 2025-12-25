# Сессионный кеш (Local Session)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 14016 — Переменная $_SESSION](lesson_14016.md)
- [Следующий: 14024 — Сессия разделенный режим (hot&cold) →](lesson_14024.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=14018

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/framework/sessions.html). В ней улучшена структура, описание, примеры.

Иногда возникает задача кешировать данные, которые связаны с текущим пользователем. Конечно, один из вариантов, это использовать сессию, но это не всегда подходит, так как:

1. сессия не создана для кеширования,
2. большое количество данных сказывается на скорость работы с сессией,
3. возникают блокировки хитов.

Один из альтернативных вариантов, это создать кеш, который привязан к session_id(). По сути, это простая имитация сессии. С версии main 20.5.400 есть новая возможность.

**Пример:**

```
$localStorage = \Bitrix\Main\Application::getInstance()->getLocalSession('someCategory');
if (!isset($localStorage['productIds']))
{
	$localStorage->set('productIds', [1, 2, 100]);
	$localStorage->set('price', 42);
}

var_dump($localStorage->get('productIds'));
```

#### Принцип работы

Принцип работы достаточно прост: при вызове `\Bitrix\Main\Application::getLocalSession($name)` всегда возвращается экземпляр `\Bitrix\Main\Data\LocalStorage\SessionLocalStorage`. Это элемент кеша, который автоматически опирается на **session_id()**.

При этом, если это первое обращение и данных нет, то будет создан пустой контейнер, если же в кеше были данные по **$name**, то контейнер будет наполнен данными.

Все SessionLocalStorage сохраняются в конце хита ядром автоматически.

**Внимание!** SessionLocalStorage работает на [кеше](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=02795#cache), который описан в настройках [.settings.php](lesson_14026.md).

**Примечание**: Если кеш файловый, то SessionLocalStorage будет использовать для хранения $_SESSION, так как иначе возникает проблема контроля и удаления устаревших файлов, что может повлиять на работу файловой системы.

|  | #### Документация по теме: |
| --- | --- |

- Документация D7: [SessionLocalStorage](https://dev.1c-bitrix.ru/api_d7/bitrix/main/data/localstorage/sessionlocalstorage.php)
