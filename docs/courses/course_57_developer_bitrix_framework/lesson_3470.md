# Составные действия

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3471 — Свойства действий](lesson_3471.md)
- [Следующий: 23034 — Общий алгоритм →](lesson_23034.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=57&LESSON_ID=3470

|  | ### Объединение действий в одно |
| --- | --- |




Составные действия наследуются от абстрактного класса *CBPCompositeActivity*, который, в свою очередь, наследуется от класса [CBPActivity](http://dev.1c-bitrix.ru/api_help/bizproc/bizproc_classes/CBPActivity/index.php). Класс *CBPCompositeActivity* обеспечивает поддержку возможности включать внутрь действия дочерние действия. Например, составным является стандартное действие *CBPParallelActivity* (параллельное выполнение), которое содержит в себе дочерние действия, соответствующие веткам параллельного выполнения.




Класс *CBPCompositeActivity* содержит член `arActivities`, с помощью которого можно обращаться к дочерним действиям.




Например, при запуске действия необходимо запустить первое дочернее действие и дождаться его завершения. Для этого можно использовать следующий код:




```
class CBPMyActivity
	extends CBPCompositeActivity    // наследуем, так как составное действие
	implements IBPEventActivity	// обработка события завершения дочернего //действия
{
	// Исполняемый метод действия
	public function Execute()
	{
		// Возьмем первое дочернее действие
		$activity = $this->arActivities[0];
		// Подпишемся на событие изменения статуса дочернего действия
		//  (завершение)
		$activity->AddStatusChangeHandler(self::ClosedEvent, $this);
		// Отправим дочернее действие исполняющей среде на выполнение
		$this->workflow->ExecuteActivity($activity);
		// Вернем указание исполняющей среде, что действие еще выполняется
		return CBPActivityExecutionStatus::Executing;
	}

	// Обработчик события изменения статуса интерфейса IBPEventActivity
	// Параметром передается действие, изменившее статус
	protected function OnEvent(CBPActivity $sender)
	{
		// Отпишемся от события изменения статуса дочернего действия
		// (завершения)
		$sender->RemoveStatusChangeHandler(self::ClosedEvent, $this);
		// Дочернее действие завершено, выполняем другой необходимый нам код
		// Например завершаем действие
		$this->workflow->CloseActivity($this);
	}
}
```
