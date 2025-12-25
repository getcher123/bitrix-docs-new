# События

**Внимание!**Для событий с префиксом *onBefore**** - если обработчик возвращает false, то метод прекращает свою работу.


### Статистика голосования


| Событие | Входные параметры | Вызывается | Метод | С версии |
| --- | --- | --- | --- | --- |
| onVoteReset | [$voteId] | После сброса статистики | \Bitrix\Vote\Vote::resetStatistic($voteId) | 12.0.5 |
| onBeforeVoting | [&$eventFields, &$answers] | До момента фиксации голоса | \Bitrix\Vote\Event::add | 12.0.5 |
| onAfterVoting | [$voteId, $eventId, $userId] | После успешной фиксации голоса | \Bitrix\Vote\Vote::registerEvent | 12.0.5 |

---
### Опросы как сущность


| Событие | Входные параметры | Вызывается | Метод | С версии |
| --- | --- | --- | --- | --- |
| onBeforeVoteAdd | [&$fields] | Перед добавлением опроса | \Bitrix\Vote\VoteTable::onBeforeAdd | 8.5.0 |
| onAfterVoteAdd | [$id, $fields] | После добавления опроса | \Bitrix\Vote\VoteTable::onAfterAdd | 8.5.0 |
| onBeforeVoteUpdate | [$id, &$fields] | Перед изменением опроса | \Bitrix\Vote\VoteTable::onBeforeUpdate | 8.5.0 |
| onAfterVoteUpdate | [$id, $fields] | После изменения опроса | \Bitrix\Vote\VoteTable::onAfterUpdate | 8.5.0 |
| onBeforeVoteDelete | [&$id] | Перед удалением опроса | \CVote::Delete | 12.0.5 |
| onAfterVoteDelete | [$id] | После удаления опроса | \CVote::Delete | 12.0.5 |

---
### Вопросы


| Событие | Входные параметры | Вызывается | Метод | С версии |
| --- | --- | --- | --- | --- |
| onBeforeVoteQuestionAdd | [&$fields] | Перед добавлением вопроса | \CVoteQuestion::Add | 8.5.0 |
| onAfterVoteQuestionAdd | [$id, $fields] | После добавления вопроса | \CVoteQuestion::Add | 8.5.0 |
| onBeforeVoteQuestionUpdate | [$id, &$fields] | Перед изменением вопроса | \CVoteQuestion::Update | 8.5.0 |
| onAfterVoteQuestionUpdate | [$id, $fields] | После изменения вопроса | \CVoteQuestion::Update | 8.5.0 |
| onBeforeVoteQuestionDelete | [$id, $voteId] | Перед удалением вопроса | \CVoteQuestion::Delete | 8.5.0 |
| onAfterVoteQuestionDelete | [$id, $voteId] | После удаления вопроса | \CVoteQuestion::Delete | 8.5.0 |
| onVoteQuestionActivate | [$id, boolean $active] | При активации вопроса | \CVoteQuestion::setActive | 12.5.0 |

---
### Ответы


| Событие | Входные параметры | Вызывается | Метод | С версии |
| --- | --- | --- | --- | --- |
| onBeforeVoteAnswerAdd | [&$fields] | Перед добавлением ответа | \CVoteAnswer::Add | 8.5.0 |
| onAfterVoteAnswerAdd | [$id, $fields] | После добавления ответа | \CVoteAnswer::Add | 8.5.0 |
| onBeforeVoteAnswerUpdate | [$id, &$fields] | Перед изменением ответа | \CVoteAnswer::Update | 8.5.0 |
| onAfterVoteAnswerUpdate | [$id, $fields] | После изменения ответа | \CVoteAnswer::Update | 8.5.0 |
| onBeforeVoteAnswerDelete | [$id, $questionId, $voteId] | Перед удалением ответа | \CVoteAnswer::Delete | 8.5.0 |
| onAfterVoteAnswerDelete | [$id, $questionId, $voteId] | После удаления ответа | \CVoteAnswer::Delete | 8.5.0 |

---
### Группы опросов


| Событие | Входные параметры | Вызывается | Метод | С версии |
| --- | --- | --- | --- | --- |
| onBeforeVoteChannelAdd | [&$fields] | Перед добавлением группы опросов | \CVoteChannel::Add | 12.0.5 |
| onAfterVoteChannelAdd | [$id, $fields] | После добавления группы опросов | \CVoteChannel::Add | 12.0.5 |
| onBeforeVoteChannelUpdate | [&$fields] | Перед изменением группы опросов | \CVoteChannel::Update | 12.0.5 |
| onAfterVoteChannelUpdate | [$id, $fields] | После изменения группы опросов | \CVoteChannel::Update | 12.0.5 |
| onBeforeVoteChannelDelete | [&$id] | Перед удалением группы опросов | \CVoteChannel::Delete | 12.0.5 |
| onAfterVoteChannelDelete | [$id] | После удаления группы опросов | \CVoteChannel::Delete | 12.0.5 |
