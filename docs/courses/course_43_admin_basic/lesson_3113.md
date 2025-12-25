# События в D7

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2942 — Ещё об агентах](lesson_2942.md)
- [Следующий: 3395 — Как написать обработчик события →](lesson_3395.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3113

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/framework/events.html). В ней улучшена структура, описание, примеры.

По сравнению со старым ядром в **D7** снижены требования к данным, которые должен иметь код, порождающий событие. Пример отправки события:

```
$event = new Bitrix\Main\Event("main", "OnPageStart");
$event->send();
```

При необходимости есть возможность на стороне, отправляющей событие, получить результат его обработки принимающими сторонами.

```
foreach ($event->getResults() as $eventResult)
{
	switch($eventResult->getType())
	{
		case \Bitrix\Main\EventResult::ERROR:
			// обработка ошибки
			break;
		case \Bitrix\Main\EventResult::SUCCESS:
  		          // успешно
			$handlerRes = $eventResult->getParameters(); // получаем то, что вернул нам обработчик события
			break;
		case \Bitrix\Main\EventResult::UNDEFINED:
			/* обработчик вернул неизвестно что вместо объекта класса \Bitrix\Main\EventResult его результат по прежнему доступен через getParameters*/
			break;
	}
}
```

Для уменьшения количества кода могут быть созданы наследники класса *Bitrix\Main\Event* для специфических типов событий. Например, *Bitrix\Main\Entity\Event* делает более комфортной отправку событий, связанных с модификацией сущностей.

Список ссылок по теме:

- [События](lesson_2244.md#events) в ORM.
