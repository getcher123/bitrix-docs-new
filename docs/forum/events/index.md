# События модуля Форум


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| GetAuditTypesForum |  | CEventForum::GetAuditTypes | 11.0.0 |
| OnAfterForumDelete | после удаления форума. | CForumNew::Delete |  |
| onAfterForumAdd | после добавления форума. | CForumNew::Add |  |
| onAfterForumUpdate | после редактирования форума. | CForumNew::Update |  |
| onAfterGroupForumsAdd | после добавления группы форума. | CForumGroup::Add |  |
| onAfterGroupForumsUpdate | после редактирования группы форума. | CForumGroup::Update |  |
| onAfterMessageAdd | после добавления сообщения форума. | CForumMessage::Add |  |
| onAfterMessageDelete | после удаления сообщения форума. | CForumMessage::Delete |  |
| onAfterMessageUpdate | после редактирования сообщения форума. | CForumMessage::Update |  |
| onAfterPMCopy | после копирования персонального сообщения. | CForumPrivateMessage::Copy | 11.5.1 |
| onAfterPMSend | после отправки персонального сообщения. | CForumPrivateMessage::Send | 11.5.1 |
| onAfterTopicAdd | после добавления темы форума. | CForumTopic::Add |  |
| onAfterTopicDelete | после удаления темы форума. | CForumTopic::Delete |  |
| onAfterTopicUpdate | после редактирования темы форума. | CForumTopic::Update |  |
| onAfterUserAdd | после добавления пользователя форума. | CForumUser::Add |  |
| onAfterUserDelete | после удаления пользователя форума. | CForumUser::Delete |  |
| onAfterUserUpdate | после редактирования пользователя форума. | CForumUser::Update |  |
| onBeforeForumAdd | перед добавлением форума. | CForumNew::Add |  |
| OnBeforeForumDelete | перед удалением форума. | CForumNew::Delete |  |
| onBeforeForumUpdate | перед редактированием форума. | CForumNew::Update |  |
| onBeforeGroupForumsAdd | перед созданием группы форумов. | CForumGroup::Add |  |
| onBeforeGroupForumsUpdate | перед редактированием группы форумов. | CForumGroup::Update |  |
| onBeforeMailMessageSend | перед отправкой сообщения на почту. | CForumMessage::SendMailMessage | 12.5.1 |
| onBeforeMessageAdd | перед добавлением сообщения форума. | CForumMessage::Add |  |
| onBeforeMessageDelete | перед удалением сообщения форума. | CForumMessage::Delete |  |
| onBeforeMessageUpdate | перед редактированием сообщения форума. | CForumMessage::Update | 11.5.1 |
| onBeforePMCopy | перед копированием персонального сообщения. | CForumPrivateMessage::Copy | 11.5.1 |
| onBeforePMDelete | перед удалением персонального сообщения. | CForumPrivateMessage::Delete | 11.5.1 |
| onBeforePMMakeRead | перед чтением персонального сообщения. | CForumPrivateMessage::MakeRead | 11.5.1 |
| onBeforePMSend | перед отправкой персонального сообщения. | CForumPrivateMessage::Send | 11.5.1 |
| onBeforePMUpdate | перед редактированием персонального сообщения. | CForumPrivateMessage::Update | 11.5.1 |
| onBeforeTopicAdd | перед добавлением темы форума. | CForumTopic::Add |  |
| onBeforeTopicDelete | перед удалением темы форума. | CForumTopic::Delete |  |
| onBeforeTopicUpdate | перед редактированием темы форума. | CForumTopic::Update |  |
| onBeforeUserAdd | перед добавлением пользователя форума. | CForumUser::Add |  |
| onBeforeUserDelete | перед удалением пользователя форума. | CForumUser::Delete |  |
| onBeforeUserUpdate | перед редактированием пользователя форума. | CForumUser::Update |  |
| OnForumDelete | при удалении форума. | CForumNew::Delete |  |
| onMessageModerate | при модерировании сообщения форума. | ForumModerateMessage | 12.0.2 |
