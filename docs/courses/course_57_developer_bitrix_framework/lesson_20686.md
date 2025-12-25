# Автоматический запуск бизнес-процессов и роботов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 1898 — Получение списка пользователей](lesson_1898.md)
- [Следующий: 21576 — Проверьте себя →](lesson_21576.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=57&LESSON_ID=20686

Автоматизация в CRM представлена бизнес-процессами (БП) и роботами. Обязанность инициировать запуск автоматизации возлагается на сам модуль CRM.




### Автозапуск бизнес-процессов




Автоматический запуск выполняется при добавлении или изменении сущности. Любая бизнес-логика, создающая или изменяющая сущность, должна после создания/изменения сущности выполнить следующий код:




```

$startParameters = []; //BP parameters

\CCrmBizProcHelper::AutoStartWorkflows(
    \CCrmOwnerType::Deal, // \CCrmOwnerType::Lead, ...
    $id,
    $isNew ? \CCrmBizProcEventType::Create : \CCrmBizProcEventType::Edit,
    $errors,
    $startParameters
);
```




где:




- `$startParameters` – значения параметров автоматически запускаемых шаблонов БП (если настроены);
- `$id` – идентификатор сущности;
- `$isNew` – если сущность только что создана, передаем событие *\CCrmBizProcEventType::Create*, в остальных случаях передаём *\CCrmBizProcEventType::Edit*;
- `$errors` – переменная будет содержать массив ошибок, если запуск БП прошел неудачно.





### Автозапуск роботов




Алгоритм запуска роботов аналогичен алгоритму запуска бизнес-процессов, однако использует более современный API.




После создания сущности и **автозапуска бизнес-процесса** необходимо выполнить следующий код:




```

//Region automation
$starter = new \Bitrix\Crm\Automation\Starter(\CCrmOwnerType::Deal, $id);
$starter->runOnAdd();
//end region
```





После изменения сущности и **автозапуска бизнес-процесса** нужно выполнить:




```

//Region automation
$starter = new \Bitrix\Crm\Automation\Starter(CCrmOwnerType::Deal, $id);
$starter->runOnUpdate($currentFields, $previousFields);
//end region
```




где:




- `$currentFields` – массив текущих значений полей сущности;
- `$previousFields` – массив предыдущих значений полей сущности.




Значения полей очень важны для запуска роботов, так как по ним определятся факт смены стадии и анализируются изменения полей (для триггеров **Изменены поля** и **Изменен ответственный**).




При этом, если в сущности бизнес-логикой меняется только стадия, то допускается передать только массив текущих полей с новой стадией, а массив предыдущих полей оставить пустым. Но этим можно пользоваться **в крайнем случае** (если запрос предыдущих значений полей избыточен в Вашем контексте):




```

//Region automation
$starter = new \Bitrix\Crm\Automation\Starter(CCrmOwnerType::Deal, $id);
$starter->runOnUpdate(['STAGE_ID' => 'NEXT'], []);
//end region
```




API запуска роботов поддерживает работу с контекстом. Можно указать пользователя, от которого будут запускаться роботы и интерфейс (сайт, мобильное приложение, REST, бизнес-процесс, импорт сущностей).




На данный момент контекст не анализируется ядром БП и не влияет на запуск бизнес-процессов и роботов, но в будущем будет учитываться. Рекомендуем сразу проставлять пользователя и интерфейс, чтобы позже не дописывать код:




```

$starter = new Bitrix\Crm\Automation\Starter(CCrmOwnerType::Deal, $id);

//Установка пользователя по ID
$starter->setUserId(1);
//Установка текущего пользователя
$starter->setUserIdFromCurrent();

//интерфейс сайта
$starter->setContextToWeb(); // используется по умолчанию, если не установлен другой

//интерфейс мобильного приложения
$starter->setContextToMobile();

//интерфейс REST приложения или Вебхука
$starter->setContextToRest();

//интерфейс БП (Роботы запускаются действиями БП)
$starter->setContextToBizproc();

//интерфейс импорта сущностей
$starter->setContextToImport();

//Запуск из другого модуля
$starter->setContextModuleId('voximplant');
```





### Пример запуска всей автоматизации (БП+Роботы)





Окончательный вариант запуска всей автоматизации (бизнес-процессы и роботы) с учетом ранее рассмотренных алгоритмов (реальный пример из компонента **crm.deal.details**):




```

\CCrmBizProcHelper::AutoStartWorkflows(
    \CCrmOwnerType::Deal,
    $ID,
    $isNew ? \CCrmBizProcEventType::Create : \CCrmBizProcEventType::Edit,
    $arErrors,
    isset($_POST['bizproc_parameters']) ? $_POST['bizproc_parameters'] : null
);

$starter = new \Bitrix\Crm\Automation\Starter(\CCrmOwnerType::Deal, $ID);
$starter->setUserIdFromCurrent();

if($isNew)
{
    $starter->runOnAdd();
}
elseif(is_array($previousFields))
{
    $starter->runOnUpdate($fields, $previousFields);
}
```
