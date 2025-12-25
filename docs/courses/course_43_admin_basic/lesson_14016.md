# Переменная $_SESSION

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5348 — Примеры оптимизации JS кода](lesson_5348.md)
- [Следующий: 14018 — Сессионный кеш (Local Session) →](lesson_14018.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=14016

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/framework/sessions.html). В ней улучшена структура, описание, примеры.

Работать напрямую с `$_SESSION` - допустимо, но не желательно. Все изменения данных в глобальной переменной будут сохранены, но настоятельно советуем использовать новое API вместо этой переменной.

Вместо прямого использования переменной лучше использовать объект, возвращаемый методом `\Bitrix\Main\Application::getSession()`:

```
$session = \Bitrix\Main\Application::getInstance()->getSession();
if (!$session->has('foo'))
{
	$session->set('foo', 'bar');
}

echo $session['foo']; //bar
```

Данный объект реализует интерфейс `\ArrayAccess`, а также [\Bitrix\Main\Session\SessionInterface](https://dev.1c-bitrix.ru/api_d7/bitrix/main/session/sessionInterface/index.php?clear_cache=Y).
