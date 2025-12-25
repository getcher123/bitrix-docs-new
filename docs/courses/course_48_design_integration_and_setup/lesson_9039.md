# Создание собственных счетчиков и атрибутов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 9035 — Настройка модуля](lesson_9035.md)
- [Следующий: 20240 — Проверьте себя →](lesson_20240.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=9039

**Внимание!**

                    Этот урок предполагает наличие у администратора навыков по работе с кодом и минимальных знаний PHP. Если у вас возникают трудности по реализации описанного в уроке алгоритма, обратитесь к разработчикам вашего сайта.




Для правильной работы примеров необходима версия модуля **Конверсия** не ниже 15.5.6.






### Счетчики




Для подсчета числа посетителей в день модуль **Конверсия** поступает следующим образом:




```

$context = Bitrix\Conversion\DayContext::getInstance(); // контекст текущего дня и текущего пользователя
$context->addDayCounter('conversion_visit_day', 1);     // прибавить 1 к счетчику 'conversion_visit_day' в этом контексте
```




Для примера рассмотрим задачу подсчета количества посещений корневой `'/'` страницы сайта.
Код необходимо поместить в `bitrix/php_interface/init.php`.




**Внимание**! Ошибка в файле

			init.php

                    **init.php** - необязательный файл в рамках структуры файлов Bitrix Framework. Он автоматически подключается в прологе.
[Подробнее...](/learning/course/?COURSE_ID=43&LESSON_ID=2916)

		 приводит к полной потере работоспособности сайта, поэтому внесение изменений в него стоит предоставить разработчику.




```

class MyConversionHandlers
{
	// накрутка наших счетчиков
	static function addCounters()
	{
		if ($_SERVER['REQUEST_URI'] == '/' && Bitrix\Main\Loader::includeModule('conversion'))
		{
			$context = Bitrix\Conversion\DayContext::getInstance();
			$context->addDayCounter('my_page_day', 1); // прибавить 1 к счетчику my_page_day один раз в день
			$context->addCounter   ('my_page_all', 1); // прибавить 1 к счетчику my_page_all
		}
	}

	// информация о наших счетчиках для модуля Конверсия
	static function getCounterTypes()
	{
		return array(
			'my_page_day' => array('MODULE' => 'my', 'NAME' => 'Количество посещений в день', 'GROUP' => 'day'), // дневная группа информирует о счетчике действий
			'my_page_all' => array('MODULE' => 'my', 'NAME' => 'Общее количество посещений'),
		);
	}
}

// регистрируем обработчики в системе
$eventManager = \Bitrix\Main\EventManager::getInstance();
$eventManager->addEventHandler('main'      , 'OnProlog'         , array('MyConversionHandlers', 'addCounters'    ));
$eventManager->addEventHandler('conversion', 'OnGetCounterTypes', array('MyConversionHandlers', 'getCounterTypes'));
```





Метод [addDayCounter](https://dev.1c-bitrix.ru/api_d7/bitrix/conversion/daycontext/adddaycounter.php) добавляет один счетчик для пользователя один раз в день, вне зависимости от того сколько раз он будет вызван. Он и используется для вычисления конверсии.




Метод [addCounter](https://dev.1c-bitrix.ru/api_d7/bitrix/conversion/daycontext/addcounter.php) увеличивает счетчики столько раз, сколько он будет вызван. Его целесообразно использовать для накопления информационных данных.




Теперь нужно перейти в настройки модуля Конверсия и убедиться, что для модуля

			'my'

                    Вместо 'my' укажите нужный вам модуль, работу с которым поддерживает модуль Конверсия. См. урок [Настройки модуля](lesson_9035.md)

		 стоит галочка учета конверсии. Это все что нужно, для того чтобы начать подсчет посещений корневой страницы нашего сайта. Чтобы посчитать и вывести конверсию по этим счетчикам, нужно добавить еще один метод в наш класс:




```

 // информация для вычисления конверсии
	static function getRateTypes()
	{
		return array(
			'my_page' => array(
				'NAME'      => 'Посещения главной',
				'MODULE'    => 'my',
				'SORT'      => 100, // порядок отображения конверсии
				'SCALE'     => array(0.5, 1, 1.5, 2, 5), // шкала: Плохо 0% - Отлично 5%

				// счетчики которые будут переданы в функцию вычисления конверсии
				'COUNTERS'  => array('conversion_visit_day', 'my_page_day', 'my_page_all'),

				// функция вычисления конверсии
				'CALCULATE' => function (array $counters)
				{
					$denominator = $counters['conversion_visit_day'] ?: 0; // знаменатель
					$numerator   = $counters['my_page_day'         ] ?: 0; // числитель
					$quantity    = $counters['my_page_all'         ] ?: 0;

					return array(
						'DENOMINATOR' => $denominator,
						'NUMERATOR'   => $numerator,
						'QUANTITY'    => $quantity,
						'RATE'        => $denominator ? $numerator / $denominator : 0, // формула конверсии
					);
				},
			),
		);
	}
```




Зарегистрируем новый обработчик:




```

$eventManager->addEventHandler('conversion', 'OnGetRateTypes'   , array('MyConversionHandlers', 'getRateTypes'   ));
```




Теперь конверсия по счетчикам будет посчитана и отображена на странице [Пульс конверсии](/learning/course/index.php?COURSE_ID=139&LESSON_ID=12177).





### Контекст





> **Контекст** - это уникальный набор атрибутов.




Эти атрибуты, которые фиксируются счетчиками, задаются для каждого пользователя и действуют в течение дня. Например модуль Конверсия устанавливает атрибуты контекста таким образом:




```

$context = Bitrix\Conversion\DayContext::getInstance();
$сontext->setAttribute('conversion_site', $siteId); // задает атрибуту 'conversion_site' значение переменной $siteId
```




Благодаря атрибуту `'conversion_site'` можно будет отфильтровать все счетчики только по определенному сайту.




Допустим, стоит задача определить настроение и пол человека зашедшего на сайт. Для примера сгенерируем эти данные случайным образом. Добавим два новых метода в класс *MyConversionHandlers*:




```

// установка наших атрибутов контекста
	static function setDayContextAttributes(Bitrix\Conversion\DayContext $context)
	{
		// установить атрибут 'my_mood' со значением от 1 до 3
		$context->setAttribute('my_mood', rand(1, 3));

		// установить атрибут 'my_male_gender' или 'my_female_gender' без значений
		$context->setAttribute('my_'.(rand(0, 1) ? '' : 'fe').'male_gender');
	}

	// информация о наших атрибутах для модуля Конверсия
	static function getAttributeTypes()
	{
		return array(
		'my_mood' => array(
			'NAME'   => 'Настроение',
			'MODULE' => 'my',
			'SORT'   => 100, // порядок установки атрибутов
			'GET_VALUES' => function (array $ids) // информация по значениям атрибута
			{
				$values = array();

				$moods = array(
					1 => array('NAME' => 'Плохое'    ),
					2 => array('NAME' => 'Нормальное'),
					3 => array('NAME' => 'Хорошее'   ),
				);

			foreach ($ids as $id)
				if (isset($moods[$id]))
					$values[$id] = $moods[$id];

			return $values;
			},
		),
		'my_male_gender' => array(
			'NAME'     => 'Мужчины',
			'MODULE'   => 'my',
			'SORT'     => 200,
			'GROUP'    => 'gender',  // группировка атрибутов
			'BG_COLOR' => '#be6ac4', // цвет шапки атрибута на странице Пульса конверсии
			'SPLIT_BY' => 'my_mood', // вывод в разрезе настроения на детальной странице
		),
		'my_female_gender' => array(
				'NAME'     => 'Женщины',
				'MODULE'   => 'my',
				'SORT'     => 300,
				'GROUP'    => 'gender',
				'BG_COLOR' => '#4bbedb',
				'SPLIT_BY' => 'my_mood',
			),
	);
	}
```




Обработчики необходимо зарегистрировать:




```

$eventManager->addEventHandler('conversion', 'OnSetDayContextAttributes', array('MyConversionHandlers', 'setDayContextAttributes'));
$eventManager->addEventHandler('conversion', 'OnGetAttributeTypes'      , array('MyConversionHandlers', 'getAttributeTypes'      ));
```




Теперь атрибуты контекста будут устанавливаться для каждого пользователя каждый день.




Если пользователь в определенный день уже заходил на наш сайт до того, как были добавлены новые атрибуты, то контекст для него уже установлен без этих атрибутов. Чтобы переопределить контекст, не дожидаясь следующего дня, нужно очистить

			куки


**Cookie** - это текстовая строка информации, которую веб-сервер передает в браузер посетителя сайта и которая сохраняется в файле на устройстве посетителя сайта. Как правило, используется для определения уникальности посетителя, времени его последнего визита, личных настроек, уникального идентификатора корзины покупок и т.д.

[Подробнее](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=21538)...

		 `PHPSESSID` и `BITRIX_CONVERSION_CONTEXT` для сайта в браузере.




Если зайти на страницу

			Пульс конверсии

                    Маркетинг &gt; Пульс конверсии

		, то в выпадающем меню со списком групп атрибутов добавится новый пункт `'gender'`. Чтобы задать более понятное название созданной группе, нужно добавить еще один метод:




```

// информация о группах для модуля Конверсия
	static function getAttributeGroupTypes()
	{
		return array(
			'gender' => array('NAME' => 'Пол', 'SORT' => 300),
		);
	}
```




И зарегистрировать его в системе:




```

$eventManager->addEventHandler('conversion', 'OnGetAttributeGroupTypes' , array('MyConversionHandlers', 'getAttributeGroupTypes' ));
```




Как можно заметить, атрибуты могут иметь, а могут и не иметь значений. Все зависит от того, как решено организовать и выводить данные.




Например, можно было бы не вводить два атрибута без значений: `'my_male_gender'` и `'my_female_gender'`, а обойтись одним: `'my_gender'`, со значениями: `'male'` и `'female'`. Но в этом случае существует ряд ограничений.
Так, если создатель другого модуля решит, что ему нужен еще один вариант атрибута в группе `'gender'`, то он не сможет попросту добавить еще один  атрибут `'his_neuter_gender'` в своем модуле, ему придется править всю реализацию.





Также на странице Пульс конверсии можно делать срез только по самим атрибутам, имеющим общую группу, а не по их значениям. Но это вовсе не означает, что атрибуты с группой не должны иметь значений. Например, модуль Конверсия определяет атрибут `'Органический трафик'` в группе `'Источники с которых заходили'`, со значениями в виде поисковых систем. Несколько других модулей добавляют свои атрибуты в эту группу таким же образом. А как раз на детальной странице делается срез по значениям этих атрибутов.





### Еще раз подчеркнем главное






- Атрибуты имеющие `GROUP` будут доступны на странице Пульса конверсии.
- На детальной странице в данный момент реализована выборка по атрибуту имеющему значения, указанному в поле `SPLIT_BY`, но в будущем будет добавлена возможность строить сложные фильтры с различными вариантами атрибутов и значений.
- Если несколько атрибутов имеющих одну группу будут установлены, то будет использован тот атрибут, у которого поле `SORT` будет наименьшим.
