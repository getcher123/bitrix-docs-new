# События модуля блогов


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeBlogAdd | перед добавлением блога. | CBlog::Add | 5.0.2 |
| OnBlogAdd | при добавлении блога. | CBlog::Add | 5.0.2 |
| OnBeforeBlogUpdate | перед изменением блога. | CBlog::Update | 5.0.2 |
| OnBlogUpdate | при изменении блога. | CBlog::Update | 5.0.2 |
| OnBeforeBlogDelete | перед удалением блога. | CBlog::Delete | 5.0.1 |
| OnBlogDelete | при удалении блога. | CBlog::Delete | 5.0.1 |
| OnBeforeCommentAdd | перед добавлением комментария. | CBlogComment::Add | 9.5.0 |
| OnBeforeCommentDelete | перед удалением комментария. Текст ошибки, зарегистрированной в обработчике этого события, отображается в интерфейсе живой ленты. | CBlogComment::Delete | 9.5.0 |
| OnBeforeCommentUpdate | перед изменением комментария. | CBlogComment::Update | 9.5.0 |
| OnBeforePostAdd | перед добавлением сообщения. | CBlogPost::Add | 9.5.0 |
| OnBeforePostDelete | перед удалением сообщения. | CBlogPost::Delete | 9.5.0 |
| OnBeforePostUpdate | перед изменением сообщения. | CBlogPost::Update | 9.5.0 |
| OnCommentAdd | при добавлении комментария. | CBlogComment::Add | 9.5.0 |
| OnCommentDelete | при удалении комментария. | CBlogComment::Delete | 9.5.0 |
| OnCommentUpdate | при изменении комментария. | CBlogComment::Update | 9.5.0 |
| OnPostAdd | при добавлении сообщения. | CBlogPost::Add | 9.5.0 |
| OnPostDelete | при удалении сообщения. | CBlogPost::Delete | 9.5.0 |
| OnPostUpdate | при изменении сообщения. | CBlogPost::Update | 9.5.0 |
| videoConvert | при конвертации видео. | blogTextParser::blogConvertVideo | 9.0.0 |
| BlogImageSize | при конвертировании тега типа ``` [IMG ID=12345] ``` в строку типа *&ltimg .../>* | blogTextParser::blogTextParser |  |
| OnBeforePostUserFieldUpdate | после изменения\добавления сообщения в блог, но перед обновлением пользовательских свойств. | CBlogPost::Update |  |
| OnBlogPostMentionNotifyIm | после отправки уведомления об упоминании в сообщении\комментарии. | CBlogPost::NotifyIm |  |
