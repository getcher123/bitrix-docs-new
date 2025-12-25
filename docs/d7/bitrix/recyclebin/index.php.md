# Корзина удаленных сущностей

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/recyclebin/index.php

Модуль управления корзиной удаленных сущностей (задач и шаблонов).

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('recyclebin');
```

| Класс | Описание | С версии |
| --- | --- | --- |
| [Recyclebin](https://dev.1c-bitrix.ru/api_d7/bitrix/recyclebin/recyclebin/index.php) | Класс содержит методы для работы с корзиной удаленных сущностей (задач и шаблонов). | 18.0.1 |

#### Пример

(написание своего обработчика для работы с корзиной сущностей "Задачи")

В первую очередь необходимо создать класс менеджера, который будет возвращать необходимые данные при запросе Корзиной:

**\Bitrix\Tasks\Integration\Recyclebin\Manager**

```
class Manager
{
	const TASKS_RECYCLEBIN_ENTITY = 'tasks_task';
	const TASKS_TEMPLATE_RECYCLEBIN_ENTITY = 'tasks_template';
	const MODULE_ID = 'tasks';

	public static function OnModuleSurvey()
	{
		$data = [];

		$data[self::TASKS_RECYCLEBIN_ENTITY] = array(
			'NAME'    => Loc::getMessage('TASKS_RECYCLEBIN_ENTITY_NAME'), // Название сущности
			'HANDLER' => \Bitrix\Tasks\Integration\Recyclebin\Task::class // Класс обработчик сущности
		);

		$data[self::TASKS_TEMPLATE_RECYCLEBIN_ENTITY] = array(
			'NAME'    => Loc::getMessage('TASKS_TEMPLATE_RECYCLEBIN_ENTITY_NAME'),
			'HANDLER' => \Bitrix\Tasks\Integration\Recyclebin\Template::class
		);

		return new EventResult(
			EventResult::SUCCESS, [
			'NAME' => Loc::getMessage('TASKS_RECYCLEBIN_MODULE_NAME'),
			'LIST' => $data
			], self::MODULE_ID
		);
	}
}

```

Затем необходимо "зарегистрировать" этот менеджер в события Корзины:

```
$eventManager = \Bitrix\Main\EventManager::getInstance();

//Recyclebin
$eventManager->registerEventHandler(
	'recyclebin',
	'OnModuleSurvey',
	'tasks',
	'\Bitrix\Tasks\Integration\Recyclebin\Manager',
	'OnModuleSurvey'
);

```

Теперь, когда мы открываем корзину, она выполняет метод **\Bitrix\Recyclebin\Recyclebin::getAvailableModules()**, который сообщает ей, с какими сущностями она готова работать.

Далее необходимо описать "Класс обработчик сущности". В нем и будут происходить главные действия.
Обработчик должен реализовывать интерфейс **\Bitrix\Recyclebin\Internals\Contracts\Recyclebinable** для того, чтобы иметь возможность работать с корзиной.

```
interface Recyclebinable
{

	/**
	* Метод восстановления из корзины
	*
	* @param Entity $entity
	*
	* @return boolean
	*/
	public static function moveFromRecyclebin(Entity $entity);

	/**
	* Метод удаления из корзины
	*
	* @param Entity $entity
	*
	* @return boolean
	*/
	public static function removeFromRecyclebin(Entity $entity);

	/**
	* Метод предпросмотра в корзине
	*
	* @param Entity $entity
	*
	* @return boolean
	*/
	public static function previewFromRecyclebin(Entity $entity);

	/**
	* Метод, который предоставляет переводы результатов действий.
	* NOTIFY - Задача успешно удалена/Восстановлена
	* CONFIRM - Вы уверены, что хотите восстановить/удалить задачу?
	*
	* @return array
	*
	* [
	*	'NOTIFY'=> [
	*		'RESTORE' => Loc::getMessage(''),
	*		'REMOVE' => Loc::getMessage(''),
	*	],
	*	'CONFIRM' => [
	*		'RESTORE' => Loc::getMessage(''),
	*		'REMOVE' => Loc::getMessage('')
	*	]
	*/
	public static function getNotifyMessages();
}

```

Такие обработчики нужно описывать для каждой восстанавливаемой сущности (со своими переводами).

Когда задача будет удаляться, вызовется метод **OnBeforeTaskDelete** (это событие надо зарегистрировать отдельно).

```
use Bitrix\Recyclebin\Internals\Entity;

public static function OnBeforeTaskDelete($taskId, array $task = [])
{
	$recyclebin = new Entity($taskId, Manager::TASKS_RECYCLEBIN_ENTITY, Manager::MODULE_ID); // создаем объект корзины
	$recyclebin->setTitle($task['TITLE']); // задаем заголовок

	$additionalData = self::collectTaskAdditionalData($taskId); //каким либо образом собираем информацию, которую необходимо сохранить в корзине в формате действие-данные
// например [MEMBERS=>[1,2,3,4,5]], затем по ключу MEMBERS мы будем знать, что восстанавливать
	if ($additionalData)
	{
		foreach ($additionalData as $action => $data)
		{
			$recyclebin->add($action, $data);  // добавляем в корзину
		}
	}

	$result = $recyclebin->save(); // сохраняем в корзине
	$resultData = $result->getData();

	return $resultData['ID']; // получаем ID созданной корзины
}

```

Восстановление:

```
use Bitrix\Recyclebin\Internals\Entity;

public static function moveFromRecyclebin(Entity $entity)
{
	$result = new Result();

	$connection = Application::getConnection();

		$connection->queryExecute(
			'UPDATE '.TaskTable::getTableName().' SET ZOMBIE=\'N\' WHERE ID='.$entity->getEntityId()
		); // восстановил задачу (в данном случае пришлось в обход АПИ, потому что не поддерживается такой функционал

		$arLogFields = array(
			"TASK_ID" => $entity->getEntityId(),
			"USER_ID" => User::getId(),
			"CREATED_DATE" => new DateTime(),
			"FIELD" => 'RENEW'
		);

	$log = new \CTaskLog();
	$log->Add($arLogFields); // добавил в лог задачи информацию об востановлении

	$dataEntity = $entity->getData(); // получил сохраненные данные из корзины

	if ($dataEntity)
	{
		foreach ($dataEntity as $value)
		{
			$data = unserialize($value['DATA']);
			$action = $value['ACTION'];

			self::restoreTaskAdditionalData($entity->getEntityId(), $action, $data); // на основе сохраненного массива восстанавливаем данные
		}
	}

	$task = \CTaskItem::getInstance($entity->getEntityId(), 1);
	$task->update([], ['FORCE_RECOUNT_COUNTER'=>'Y']); // пересчитываем счетчики задач

	return $result; // результат работы
}

```
