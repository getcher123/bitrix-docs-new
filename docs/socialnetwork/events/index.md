# События


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeSocNetUserToGroupDelete | перед удалением связи между пользователем и рабочей группой. | CSocNetUserToGroup::Delete | 7.0.5 |
| OnSocNetUserToGroupDelete | в момент удаления связи между пользователем и рабочей группой. | CSocNetUserToGroup::Delete | 7.0.5 |
| OnBeforeSocNetGroupAdd | перед созданием рабочей группы. | CSocNetGroup::Add | 7.0.5 |
| OnSocNetGroupAdd | после добавления новой рабочей группы. | CSocNetGroup::Add | 7.0.5 |
| OnBeforeSocNetGroupUpdate | перед изменением параметров рабочей группы. | CSocNetGroup::Update | 7.0.5 |
| OnSocNetGroupUpdate | после изменения рабочей группы. | CSocNetGroup::Update | 7.0.5 |
| OnFillSocNetFeaturesList | при инициализации модуля социальной сети после заполнения массива дополнительного функционала. | CSocNetAllowed::RunEventForAllowedFeature | 7.0.6 |
| OnBeforeSocNetGroupDelete | перед удалением рабочей группы. | CSocNetGroup::Delete | 7.0.6 |
| OnSocNetGroupDelete | в момент удаления рабочей группы. | CSocNetGroup::Delete | 7.0.6 |
| OnBeforeSocNetFeatures | перед удалением дополнительного функционала. | CSocNetFeatures::Delete | 7.0.6 |
| OnSocNetFeatures | в момент удаления дополнительного функционала. | CSocNetFeatures::Delete | 7.0.6 |
| OnBeforeSocNetFeaturesUpdate | перед изменением параметров дополнительного функционала. | CSocNetFeatures::Update | 7.0.6 |
| OnSocNetFeaturesUpdate | после изменения записи дополнительного функционала. | CSocNetFeatures::Update | 7.0.6 |
| OnBeforeSocNetFeaturesPermsDelete | перед удалением прав на дополнительный функционал. | CSocNetFeaturesPerms::Delete | 7.0.6 |
| OnSocNetFeaturesPermsDelete | в момент удаления права на дополнительный функционал. | CSocNetFeaturesPerms::Delete | 7.0.6 |
| OnBeforeSocNetFeaturesPermsUpdate | в методе изменения параметров права на доступ к дополнительному функционалу до изменения. | CSocNetFeaturesPerms::Update | 7.0.6 |
| OnSocNetFeaturesPermsUpdate | после изменения права на дополнительный функционал. | CSocNetFeaturesPerms::Update | 7.0.6 |
| OnBeforeSocNetMessagesDelete | перед удалением сообщения. | CSocNetMessages::Delete | 7.0.6 |
| OnSocNetMessagesDelete | в момент удаления сообщения. | CSocNetMessages::Delete | 7.0.6 |
| OnBeforeSocNetFeaturesAdd | перед созданием новой записи дополнительного функционала. | CSocNetFeatures::Add | 7.0.6 |
| OnSocNetFeaturesAdd | после добавления нового дополнительного функционала. | CSocNetFeatures::Add | 7.0.6 |
| OnBeforeSocNetFeaturesPermsAdd | перед созданием записи права на дополнительный функционал. | CSocNetFeaturesPerms::Add | 7.0.6 |
| OnSocNetFeaturesPermsAdd | после добавления новой записи права на дополнительный функционал. | CSocNetFeaturesPerms::Add | 7.0.6 |
| OnBeforeSocNetMessagesAdd | перед созданием сообщения. | CSocNetMessages::Add | 7.0.6 |
| OnSocNetMessagesAdd | после добавления нового сообщения. | CSocNetMessages::Add | 7.0.6 |
| OnBeforeSocNetMessagesUpdate | перед изменением параметров сообщения. | CSocNetMessages::Update | 7.0.6 |
| OnSocNetMessagesUpdate | после изменения сообщения. | CSocNetMessages::Update | 7.0.6 |
| OnBeforeSocNetUserToGroupAdd | перед созданием связи между пользователем и рабочей группой. | CSocNetUserToGroup::Add | 7.0.6 |
| OnSocNetUserToGroupAdd | после добавления новой связи между пользователем и рабочей группой. | CSocNetUserToGroup::Add | 7.0.6 |
| OnBeforeSocNetUserToGroupUpdate | перед изменением параметров связи между пользователем и рабочей группой. | CSocNetUserToGroup::Update | 7.0.6 |
| OnSocNetUserToGroupUpdate | после изменения связи между пользователем и рабочей группой. | CSocNetUserToGroup::Update | 7.0.6 |
| OnBeforeSocNetUserRelationsAdd | перед созданием связи между пользователями. | CSocNetUserRelations::Add | 7.1.0 |
| OnSocNetUserRelationsAdd | после добавления новой связи между пользователями. | CSocNetUserRelations::Add | 7.1.0 |
| OnBeforeSocNetUserRelationsUpdate | перед изменением параметров связи между пользователями. | CSocNetUserRelations::Update | 7.1.0 |
| OnSocNetUserRelationsUpdate | после изменения связи между пользователями. | CSocNetUserRelations::Update | 7.1.0 |
| OnSocNetUserRelationsDelete | в момент удаления связи между пользователями. | CSocNetUserRelations::Delete | 7.1.0 |
| OnBeforeSocNetUserRelationsDelete | перед удалением связи между пользователями. | CSocNetUserRelations::Delete | 7.1.0 |
| OnParseSocNetComponentPath | при включенной поддержке ЧПУ компонента социальной сети в самом начале работы компонента. Позволяет подключить свои пути для ЧПУ в комплексном компоненте соцсети. ``` OnParseSocNetComponentPathHandler (&$arDefaultUrlTemplates404, &$arCustomPagesPath, $arParams) { } ``` |  |  |
| OnFillSocNetAllowedSubscribeEntityTypes | добавляет тип сущности Живой ленты. | CSocNetAllowed::RunEventForAllowedEntityType | 10.0.0 |
| OnBeforeSocNetLogRightsAdd | при добавлении прав на запись Живой ленты. | CSocNetLogRights::Add | 11.0.11 |
| OnBeforeSocNetLogRightsUpdate | при изменении прав на запись Живой ленты. | CSocNetLogRights::Update | 11.0.11 |
| OnSocNetSendRequestToJoinGroup | при отправке запроса на вступление в группу соцсети | CSocNetUserToGroup::SendRequestToJoinGroup | 11.0.15 |
| OnSocNetUserConfirmRequestToBeMember | при получении подтверждения запроса о членстве в группе соцсети | CSocNetUserToGroup::UserConfirmRequestToBeMember | 11.0.15 |
| OnSocNetUserRejectRequestToBeMember | при получении отклонении запроса о членстве в группе соцсети | CSocNetUserToGroup::UserRejectRequestToBeMember | 11.0.15 |
| OnBeforeSocNetLogCommentAdd | перед добавлением комментария в Живую ленту. | CSocNetLogComments::Add | 11.0.16 |
| OnAfterSocNetLogCommentAdd | после добавления комментария в Живую ленту. | CSocNetLogComments::Add | 11.0.16 |
| OnAfterSocNetLogUpdate | после изменения записи Живой ленты. | CSocNetLog::Update | 16.5.5 |
| OnAfterSocNetLogAdd | после добавлении записи Живой ленты. | CSocNetLog::Add | 16.5.5 |
| OnSocNetGroupSubjectAdd | после создания темы рабочих групп. | CSocNetGroupSubject::Add |  |
| OnSocNetGroupSubjectDelete | перед удалением темы рабочих групп. | CSocNetGroupSubject::Delete |  |
| OnSocNetGroupSubjectUpdate | вызывается после изменения темы рабочих групп. | CSocNetGroupSubject::Update |  |
