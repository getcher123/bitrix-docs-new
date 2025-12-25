# Список событий


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAddToHistory | перед добавлением записи в историю. | CBPHistoryService::AddHistory | 11.0.1 |
| OnBeforeDeleteFileFromHistory | перед удалением файла из истории. | CBPAllHistoryService::DeleteHistory | 11.0.4 |
| OnCreateWorkflow | при создании экземпляра бизнес-процесса. | CBPRuntime::CreateWorkflow | 11.0.4 |
| OnTaskAdd | при создании задания бизнес-процесса. | CBPTaskService::Add | 11.0.5 |
| OnTaskDelete | при удалении задания бизнес-процесса. | CBPAllTaskService::DeleteByWorkflow | 11.0.5 |
| OnTaskMarkCompleted | после того, как производится удаление записи о задании пользователя. Если в БП несколько заданий (для разных пользователей) событие вызовется несколько раз. | CBPAllTaskService::MarkCompleted | 11.0.5 |
| OnTaskUpdate | при обновлении задания бизнес-процесса. | CBPTaskService::Update | 11.0.5 |
| OnTaskDelegate | при делегировании задачи. | CBPTaskService::delegateTask | 16.0.3 |
