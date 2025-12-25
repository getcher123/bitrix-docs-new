# События

В модуле есть две сущности:


- планерка
- вопрос планерки

Эти сущности независимы друг от друга, то есть вопрос планерки напрямую к планерке не привязан. Вопрос может участвовать в их любой планёрке без ограничений. В связи с этим возникает понятие **instance** - участие вопроса в планерке. Но помимо осуществления стандартной связи "многое к многим" эта сущность несет еще некоторые дополнительные функции. В частности, к ней привязываются ответственные, отчеты, состояние на начало/конец планерки и косвенно привязываются задачи.

**Примечание**. При некоторых действиях события могут не вызываться, например, при удалении планерки обработчики удаления привязок вопросов (типа **instance**) вызываться не будут.


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAfterMeetingAdd | после добавлении собрания | CAllMeeting::Add | 11.0 |
| OnAfterMeetingDelete | после удалении собрания | CAllMeeting::Delete | 11.0 |
| OnAfterMeetingInstanceAdd | после добавления вопроса планёрки к конкретному собранию | CAllMeetingInstance::Add | 11.0 |
| OnAfterMeetingInstanceDelete | после удаления вопроса планёрки из конкретного собрания | CAllMeetingInstance::Delete | 11.0 |
| OnAfterMeetingInstanceUpdate | после обновления вопроса планёрки в рамках конкретного собрания | CAllMeetingInstance::Update | 11.0 |
| OnAfterMeetingItemAdd | после добавления вопроса планёрки | CAllMeetingItem::Add | 11.0 |
| OnAfterMeetingItemDelete | после удаления вопроса планёрки | CAllMeetingItem::Delete | 11.0 |
| OnAfterMeetingItemUpdate | после изменения вопроса планёрки | CAllMeetingItem::Update | 11.0 |
| OnAfterMeetingReportAdd | после добавления отчёта | CAllMeetingReports::Add | 11.0 |
| OnAfterMeetingReportDelete | после удаления отчета | CAllMeetingReports::Delete | 11.0 |
| OnAfterMeetingReportUpdate | после изменения отчёта | CAllMeetingReports::Update | 11.0 |
| OnAfterMeetingUpdate | после изменения собрания | CAllMeeting::Update | 11.0 |
| OnBeforeMeetingAdd | перед добавлением собрания | CAllMeeting::Add | 11.0 |
| OnBeforeMeetingDelete | перед удалением собрания | CAllMeeting::Delete | 11.0 |
| OnBeforeMeetingInstanceAdd | перед добавлением вопроса планёрки к конкретному собранию | CAllMeetingInstance::Add | 11.0 |
| OnBeforeMeetingInstanceDelete | перед удалением вопроса планёрки из конкретного собрания | CAllMeetingInstance::Delete | 11.0 |
| OnBeforeMeetingInstanceUpdate | перед обновлением вопроса планёрки в рамках конкретного собрания | CAllMeetingInstance::Update | 11.0 |
| OnBeforeMeetingItemAdd | перед добавлением вопроса планёрки | CAllMeetingItem::Add | 11.0 |
| OnBeforeMeetingItemDelete | перед удалением вопроса планёрки | CAllMeetingItem::Delete | 11.0 |
| OnBeforeMeetingItemUpdate | перед изменением вопроса планёрки | CAllMeetingItem::Update | 11.0 |
| OnBeforeMeetingReportAdd | перед добавлением отчёта | CAllMeetingReports::Add | 11.0 |
| OnBeforeMeetingReportDelete | перед удалением отчёта | CAllMeetingReports::Delete | 11.0 |
| OnBeforeMeetingReportUpdate | перед изменением отчёта | CAllMeetingReports::Update | 11.0 |
| OnBeforeMeetingUpdate | перед изменением собрания | CAllMeeting::Update | 11.0 |
