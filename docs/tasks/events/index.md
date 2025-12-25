# Список событий


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeTaskAdd | Перед добавлением задачи. | CTasks::Add | 10.0.5 |
| OnBeforeTaskDelete | Перед удалением задачи. | CTasks::Delete | 10.0.5 |
| OnBeforeTaskUpdate | Перед обновлением задачи. | CTasks::Update | 10.0.5 |
| OnTaskAdd | После добавления задачи. | CTasks::Add | 10.0.5 |
| OnTaskDelete | После удаления задачи. | CTasks::Delete | 10.0.5 |
| OnTaskUpdate | После обновления задачи. | CTasks::Update | 10.0.5 |
| OnBeforeTaskNotificationSend | Перед отправкой уведомлений в IM. | CTaskNotifications::SendMessage | 12.5.0 |
| OnBeforeTaskElapsedTimeAdd | Перед добавлением записи о затраченном времени в лог действий над задачей. | CTaskElapsedTime::Add | 14.0.16 |
| OnBeforeTaskElapsedTimeUpdate | Перед изменением записи о затраченном времени в логе действий над задачей. | CTaskElapsedTime::Update | 14.0.16 |
| OnBeforeTaskElapsedTimeDelete | Перед удалением записи о затраченном времени из лога действий над задачей. | CTaskElapsedTime::Delete | 14.0.16 |
| OnTaskElapsedTimeAdd | После добавления в лог действий над задачей записи о затраченном времени. | CTaskElapsedTime::Add | 12.5.0 |
| OnTaskElapsedTimeUpdate | После изменения в логе действий над задачей записи о затраченном времени. | CTaskElapsedTime::Update | 12.5.0 |
| OnTaskElapsedTimeDelete | После удаления из лога действий над задачей записи о затраченном времени. | CTaskElapsedTime::Delete | 12.5.0 |
| OnBaseAllowedActionsMapInit | При инициализации карты дозволенных действий над задачей. | CTaskItem::getBaseAllowedActions | 12.5.3 |
| OnTaskReminderAdd | При добавлении напоминания к задаче. | CTaskReminders::Add | 14.5.10 |






| ![image](../images/7dd82aba60.gif) 8 **Никита Кургалин**08.12.2016 16:24:59 |  |  |
| --- | --- | --- |
| Если нужно добавить исключение, нужно использовать "ActionFailedException": \| Код \| \| --- \| \| ``` throw new \Bitrix\Tasks\ActionFailedException("Для завершения задачи нужно оставить комментарий"); ``` \| | Код | ``` throw new \Bitrix\Tasks\ActionFailedException("Для завершения задачи нужно оставить комментарий"); ``` |
| Код |  |  |
| ``` throw new \Bitrix\Tasks\ActionFailedException("Для завершения задачи нужно оставить комментарий"); ``` |  |  |
|  |  |  |
