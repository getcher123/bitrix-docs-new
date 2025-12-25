# Список событий

Ниже представлены списки событий главного модуля. Для регистрации обработчика укажите в качестве идентификатора модуля - "main".


### Выполнение страницы

События, вызывающиеся в процессе выполнения страницы:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnPageStart | в начале выполняемой части пролога сайта, после подключения всех библиотек и отработки **агентов**. |  | 3.0.6 |
| OnBeforeProlog | в выполняемой части пролога сайта (после события OnPageStart). |  | 3.0.6 |
| OnProlog | в начале визуальной части пролога сайта. | CAllMain::PrologActions | 4.0.14 |
| OnEpilog | в конце визуальной части эпилога сайта. |  | 3.3.21 |
| OnAfterEpilog | в конце выполняемой части эпилога сайта (после события OnEpilog). |  | 3.0.11 |
| OnBeforeEndBufferContent | перед выводом буферизированного контента | CAllMain::EndBufferContent | 9.5.0 |
| OnBeforeRestartBuffer | перед сбросом буфера контента | CAllMain::RestartBuffer | 6.5.4 |
| OnEndBufferContent | при выводе буферизированного контента. | CAllMain::EndBufferContent | 7.0.1 |


#### Смотрите также


- Этапы выполнения страницы

---
### Пользователи и авторизация

События при работе с пользователями и авторизация:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeUserRegister | до попытки зарегистрировать нового пользователя | CUser::Register | 4.0.6 |
| OnAfterUserRegister | после попытки регистрации нового пользователя | CUser::Register | 4.0.6 |
| OnBeforeUserSimpleRegister | до попытки упрощённой регистрации нового пользователя | CUser::SimpleRegister | 4.0.6 |
| OnAfterUserSimpleRegister | после попытки упрощённой регистрации нового пользователя | CUser::SimpleRegister | 4.0.6 |
| OnBeforeUserLogin | до попытки авторизации пользователя | CUser::Login | 4.0.6 |
| OnUserLoginExternal | перед попыткой авторизации пользователя, предназначен для проверки **внешней авторизации**. | CUser::Login | 4.0.6 |
| OnAfterUserLogin | после попытки авторизации пользователя | CUser::Login | 4.0.6 |
| OnBeforeUserLoginByHash | перед попыткой авторизации пользователя | CUser::LoginByHash | 4.0.6 |
| OnAfterUserLoginByHash | после попытки авторизации пользователя | CUser::LoginByHash | 4.0.6 |
| OnAfterUserAuthorize | после авторизации пользователя | CAllUser::Authorize | 4.0.6 |
| OnBeforeUserLogout | перед завершением сеанса авторизации пользователя | CUser::Logout | 4.0.6 |
| OnAfterUserLogout | после завершения сеанса авторизации пользователя | CUser::Logout | 4.0.6 |
| OnBeforeUserAdd | перед добавлением нового пользователя. | CAllUser::CheckFields | 4.0.16 |
| OnAfterUserAdd | после добавления нового пользователя. | CUser::Add | 4.0.16 |
| OnBeforeUserUpdate | перед изменением параметров пользователя. | CAllUser::CheckFields | 4.0.16 |
| OnAfterUserUpdate | после изменения параметров пользователя. | CAllUser::Update | 4.0.16 |
| OnBeforeUserDelete | перед удалением пользователя. | CAllUser::Delete | 3.0.10 |
| OnUserDelete | во время удаления пользователя. | CAllUser::Delete | 3.0.10 |
| OnExternalAuthList | для получения списка источников внешней авторизации. | CAllUser::GetExternalAuthList | 4.0.6 |
| OnBeforeUserChangePassword | перед сменой пользовательского пароля | CUser::ChangePassword | 4.0.14 |
| OnBeforeUserSendPassword | перед отправкой пользователю пароля | CUser::SendPassword | 4.0.14 |
| OnUserLogin | при попытке авторизации | CUser::Authorize | 3.3.0 |
| OnUserLogout | после завершения сеанса авторизации пользователя | CUser::Logout | 3.3.13 |
| OnSendUserInfo | при передаче данных о пользователе | CUser::SendUserInfo | 4.0.6 |
| OnAuthProvidersBuildList | при создании провайдеров авторизации | CAccess::__construct | 11.0.7 |


#### Смотрите также


- **Внешняя авторизация**

---
### Группы пользователей

События при работе с группами пользователей:| Событие | Вызывается | Метод | С версии | | --- | --- | --- | --- | | OnBeforeGroupDelete | перед удалением группы пользователей | CAllGroup::Delete | 3.0.10 | | OnGroupDelete | при удалении группы пользователей | CAllGroup::Delete | 3.0.10 | | OnAfterGroupAdd | после добавления новой группы пользователей | CAdminTabControl::Begin | 9.5.8 | | OnAfterGroupUpdate | после изменения группы пользователей | CGroup::Update | 9.5.8 | | OnBeforeGroupAdd | перед добавлением группы пользователей | CGroup::Add | 9.5.8 | | OnBeforeGroupUpdate | перед изменением группы пользователей | CGroup::Update | 9.5.8 |

---
### Файлы и права

События при работе с файлами и правами:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeChangeFile | на изменение файла сразу после его сохранения. | CAllMain::SaveFileContent | 8.5.1 |
| OnChangePermissions | при изменении прав доступа к файлу или папке. | CAllMain::RemoveFileAccessPermission | 3.0.3 |
| OnFileDelete | при удалении файла из таблицы **b_file**. | CFile::Delete | 10.0.5 |
| OnAfterResizeImage | после изменения размера изображения | CFile::ResizeImageGet | 10.0.11 |
| OnBeforeChangeFile | перед изменением файла | CMain::SaveFileContent | 8.5.1 |
| OnBeforeResizeImage | перед изменением размера изображения | CFile::ResizeImageGet | 10.0.11 |
| OnFileCopy | при копировании файла | CFile::CopyFile | 10.0.11 |
| OnFileSave | при сохранении файла Пример использования: при сохранении обрезает оригинал до 1920*1920 ``` AddEventHandler("main",'OnFileSave','OnFileSave'); function OnFileSave(&$arFile, $fileName, $module) { $arNewFile = CIBlock::ResizePicture($arFile, array("WIDTH" => 1920, "HEIGHT" => 1920, "METHOD" => "resample")); if(is_array($arNewFile)) $arFile = $arNewFile; else $APPLICATION->throwException("Ошибка масштабирования изображения в свойстве \"Файлы\":".$arNewFile); } ``` | CFile::SaveFile | 10.0.11 |
| OnGetFileSRC | при получении адреса изображения | CFile::GetFileSRC | 10.0.11 |
| OnMakeFileArray | при создании массива, описывающего файл | CFile::MakeFileArray | 10.0.11 |
| OnSearchGetFileContent | при индексации модулем поиска | CUserTypeFile::__GetFileContent | 11.0.0 |
| OnTaskOperationsChanged | при изменении уровня доступа | CTask::SetOperations | 11.0.6 |

---
### Шаблоны почтовых сообщений

События при работе с шаблонами почтовых сообщений:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeEventMessageDelete | перед удалением почтового шаблона. | CAllEventMessage::Delete | 3.0.10 |
| OnEventMessageDelete | во время удаления почтового шаблона | CEventMessage::Delete | 3.0.10 |
| OnBeforeEventAdd | перед добавлением почтового события | CEvent::Send | 6.0.2 |
| OnBeforeEventSend | перед отправкой почтового события | CEvent::HandleEvent | 6.0.2 |

---
### Сайты

События при работе с сайтами:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeSiteDelete | перед удалением сайта. | CAllSite::Delete | 4.0.6 |
| OnSiteDelete | в момент удаления сайта. | CAllSite::Delete | 4.0.6 |
| OnBeforeSiteAdd | перед добавлением сайта в систему | CSite::CheckFields | 9.1.2 |
| OnBeforeSiteUpdate | перед изменением сайта | CSite::CheckFields | 9.1.2 |

---
### Языки

События при работе с языками:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAfterLanguageAdd | после добавления языка. | CAllLanguage::Add | 25.0.0 |
| OnBeforeLanguageDelete | перед удалением языка. | CAllLanguage::Delete | 3.3.21 |
| OnLanguageDelete | в момент удаления языка | CAllLanguage::Delete | 3.3.21 |
| OnBeforeLangDelete | перед удалением языка из системы | CSite::Delete | 3.0.10 |
| OnLangDelete | при удалении языка из системы | CSite::Delete | 3.0.10 |

---
### Панель управления и админ. часть

События при работе с панелью управления и административной частью:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnPanelCreate | в момент сбора данных для построения панели управления в публичной части сайта. | CTopPanel::InitPanelIcons | 3.0.14 |
| [OnAdminContextMenuShow](onadmincontextmenushow.md) | при выводе в административном разделе панели кнопок. | CAdminContextMenu::Show | 9.5.10 |
| [OnAdminListDisplay](onadminlistdisplay.md) | при выводе в административном разделе списка элементов. | CAdminList::Display | 9.5.10 |
| OnAdminTabControlBegin | при выводе в административном интерфейсе формы редактирования. | CAdminTabControl::Begin | 9.5.10 |
| OnAfterSetOption_ | после изменения настроек модуля | COption::SetOptionString | 6.5.8 |
| OnBuildGlobalMenu | при построении меню в административной части | CAdminMenu::Init | 6.0.3 |


#### Смотрите также


- **Обработка событий**
- **Связи и взаимодействие модулей**

---
### Рейтинги

События при работе с рейтингами:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAddRatingVote | после добавлении голоса за контент. | CRatings::Add | 11.0.5 |
| OnAfterCheckAllowVote | после проверки прав на голосование, перед добавление голоса, нужно вернуть массив вида `array('RESULT' => false, 'ERROR_TYPE' => 'тип ошибки', 'ERROR_MSG' => 'текст ошибки') `голос не будет засчитан, если вернуть true голос будет засчитан. | CRatingRule::Add | 11.0.15 |
| OnCancelRatingVote | после отмены ранее отданного голоса за контент. | CRatings::Update | 11.0.5 |
| OnAfterUpdateRatingRule | после обновления правила обработки рейтинга | CRatingRule::Update | 9.5.4 |
| OnBeforeDeleteRating | перед удалением рейтинга | CRatings::Delete | 9.5.0 |
| OnBeforeDeleteRatingRule | перед удалением правила обработки рейтинга | CRatingRule::Delete | 9.5.4 |
| OnGetRatingContentOwner | перед добавлением голоса для определения идентификатора автора контента | CRatings::AddRatingVote | 11.0.0 |
| OnGetRatingRuleConfigs | во время генерации страницы добавления (редактирования) правил обработки для получения настроек правил | CRatingRule::GetRatingRuleConfigs | 9.5.4 |
| OnGetRatingRuleObjects | при вызове правил обработки рейтинга | CRatingRule::GetRatingRuleObjects | 9.5.4 |
| OnGetRatingsConfigs | во время генерации страницы добавления (редактирования) правил обработки для получения объектов голосования к которым могут быть применены правила | CRatings::GetRatingConfigs | 9.5.0 |
| OnGetRatingsObjects | во время генерации страницы добавления (редактирования) рейтингов для получения настроек компонентов рейтинга | CRatings::GetRatingObjects | 9.5.0 |

---
### Парсинг текста

События при парсинге текста:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| TextParserAfter | после парсинга | CTextParser::convertText | 10.0.2 |
| TextParserAfterTags | после парсинга тегов | CTextParser::convertText | 10.0.2 |
| TextParserBefore | перед парсингом | CTextParser::convertText | 10.0.2 |
| TextParserBeforePattern | перед парсингом | CTextParser::convertText | 10.0.2 |
| TextParserBeforeTags | перед парсингом тегов | CTextParser::convertText | 10.0.2 |
| TextParserVideoConvert | при парсинге тега видео | CTextParser::convert_video | 10.0.2 |

---
### Обновление системы

События при обновлении системы:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnUpdatesInstalled | после установки обновлений. Имеет единственный параметр: массив вида: ``` Array ( "successModules" => $arSuccessModules, "loadModules" => $arLoadModules, "errorModules" => $arErrorModules, "modulesUpdates" => $arModulesUpdates ``` | CUpdateOutput::ShowBlockInfo | 7.0.12 |
| OnModuleUpdate | после обновления модуля | CUpdateClientPartner::UpdateStepModules | 7.1.1 |

---
### Установка модулей

События при установке модулей:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAfterRegisterModule | после регистрации модуля | RegisterModule | 12.0.8 |
| OnAfterUnRegisterModule | после деинсталляции модуля | UnRegisterModule | 12.0.8 |

---
### Пользовательские поля

События при работе с пользовательскими полями:


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnUserTypeBuildList | при построении списка пользовательских полей | CUserTypeManager::GetUserType | 6.0.2 |
| OnUserTypeRightsCheck | при проверке прав доступа на пользовательские поля | GetRights | 6.5.5 |
| OnAfterFetch | после выполнения выборки |  | 12.5.12 |
| onAfterUserTypeUpdate | после обновления пользовательского поля. Аргументы: - **$arFields** - массив полей после обновления - **$ID** - идентификатор поля. | **CUserTypeEntity** | 16.5.3 |
| OnAfterUserTypeDelete | после удаления пользовательского поля. Аргументы: - **$arFields** - массив полей удаленного элемента - **$ID** - идентификатор поля. | **CUserTypeEntity** | 16.5.3 |

---
### Прочие события


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAutoSaveRestore | при восстановлении автосохраненных данных | CAutoSave::_Restore | 11.0.1 |
| OnBeforeLocalRedirect | перед редиректом | LocalRedirect | 6.5.4 |
| OnLocalRedirect | при редиректе | LocalRedirect | 6.5.4 |
| OnCheckListGet | при отправке чеклиста | CCheckList::__construct | 11.0.1 |
| onAfterAjaxResponse | после обработки аяксового запроса к компоненту в аякс-режиме | ExecuteEvents | 7.0.0 |
| OnAfterShortUriAdd | после добавления короткой ссылки | CBXShortUri::Add | 12.5.0 |
| OnBeforeShortUriDelete | перед удалением короткой ссылки | CBXAllShortUri::Delete | 12.5.0 |

---




| ![](../images/73c151367a.jpg) 3 **Анатолий Кирсанов**19.04.2016 22:23:23 |
| --- |
| Ничего не сказано о событии 'main', 'OnAfterUserTypeAdd' и его результате array('PROVIDE_STORAGE' => true). |
|  |

<!-- vault-nav:start -->
## В этой папке

<details>
<summary>Показать файлы и папки</summary>

### Файлы

- [OnAdminContextMenuShow](onadmincontextmenushow.md)
- [OnAdminListDisplay](onadminlistdisplay.md)

</details>

<!-- vault-nav:end -->
