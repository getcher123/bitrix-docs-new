# События


### Дела


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnActivityAdd | при добавлении дела к сущности. | CCrmActivity::Add | 12.0.2 |
| OnActivityDelete | при удалении дела. | CCrmActivity::Delete | 12.0.2 |
| OnActivityUpdate | при изменении дела. | CCrmActivity::Update | 12.0.2 |
| OnBeforeActivityDelete | перед удалением дела. | CCrmActivity::Delete | 12.0.2 |

---
### Каталог товаров


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeCrmCatalogDelete | перед удалением каталога товаров crm. | CCrmCatalog::Delete | 11.5.0 |
| OnCrmCatalogDelete | при удалении каталога товаров CRM. | OnCrmCatalogDelete | 11.5.0 |

---
### Почтовый шаблон


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeMailTemplateDelete | перед удалением почтового шаблона. | CCrmMailTemplate::Delete | 12.5.0 |
| OnMailTemplateAdd | при добавлении почтового шаблона. | CCrmMailTemplate::Add | 12.5.0 |
| OnMailTemplateDelete | при удалении почтового шаблона. | CCrmMailTemplate::Delete | 12.5.0 |
| OnMailTemplateUpdate | при изменении почтового шаблона. | CCrmMailTemplate::Update | 12.5.0 |

---
### Товары


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeCrmProductDelete | перед удалением товара crm. | CCrmProduct::Delete | 11.5.0 |
| OnCrmProductDelete | при удалении товара CRM. | CCrmProduct::Delete | 11.5.0 |
| OnAfterCrmProductUpdate | после обновления товара CRM. | CCrmProduct::Update | 11.5.0 |

---
### Компании


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAfterCrmCompanyAdd | после добавления компании. | CCrmCompany::Add | 10.0.1 |
| OnAfterCrmCompanyUpdate | после изменения компании. | CCrmCompany::Update | 10.0.1 |
| OnBeforeCrmCompanyDelete | перед удалением компании. | CCrmCompany::Delete | 10.0.1 |
| OnBeforeCrmCompanyAdd | перед добавлением компании | CCrmCompany::Add | 10.0.1 |
| OnBeforeCrmCompanyUpdate | перед изменением компании | CCrmCompany::Update | 10.0.1 |
| OnAfterCrmCompanyDelete | после удаления компании. | CCrmCompany::Delete | 10.0.1 |
| OnAfterExternalCrmCompanyAdd | после добавления внешней компании. | CCrmCompany::Add | 10.0.1 |

---
### Контакты


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAfterCrmContactAdd | после добавления контакта. | CCrmContact::Add | 10.0.1 |
| OnAfterCrmContactUpdate | после изменения контакта. | CCrmContact::Update | 10.0.1 |
| OnBeforeCrmContactDelete | перед удалением контакта. | CCrmContact::Delete | 10.0.1 |
| OnBeforeCrmContactAdd | перед добавлением контакта. | CCrmContact::Add | 10.0.1 |
| OnBeforeCrmContactUpdate | перед изменением контакта. | CCrmContact::Update | 10.0.1 |
| OnAfterExternalCrmContactAdd | после добавления внешнего контакта. | CCrmContact::Add | 10.0.1 |
| OnAfterCrmContactDelete | после удаления контакта. | CCrmContact::Delete | 10.0.1 |

---
### Сделки


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAfterCrmDealAdd | после добавления сделки. | CCrmDeal::Add | 10.0.1 |
| OnAfterCrmDealUpdate | после изменения сделки. | CCrmDeal::Update | 10.0.1 |
| OnBeforeCrmDealDelete | перед удалением сделки. | CCrmDeal::Delete | 10.0.1 |
| OnBeforeCrmDealAdd | перед добавлением сделки. | CCrmDeal::Add | 10.0.1 |
| OnBeforeCrmDealUpdate | перед изменением сделки. | CCrmDeal::Update | 10.0.1 |
| OnAfterCrmDealDelete | после удаления сделки. | CCrmDeal::Delete | 10.0.1 |
| OnAfterExternalCrmDealAdd | после добавления внешней сделки. | CCrmDeal::Add | 10.0.1 |
| OnAfterCrmDealProductRowsSave | после добавления товара в сделку. | CCrmDeal::SaveProductRows | 10.0.1 |
| OnBeforeCrmDealProductRowsSave | перед добавлением товара в сделку. | CCrmDeal::SaveProductRows | 22.500 |

---
### Лиды


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAfterCrmLeadAdd | после добавления лида. | CCrmLead::Add | 10.0.0 |
| OnAfterCrmLeadUpdate | после изменения лида. | CCrmLead::Update | 10.0.0 |
| OnBeforeCrmLeadDelete | перед удалением лида. | CCrmLead::Delete | 10.0.0 |
| OnBeforeCrmLeadAdd | перед добавлением лида. | CCrmLead::Add | 10.0.0 |
| OnBeforeCrmLeadUpdate | перед изменением лида. | CCrmLead::Update | 10.0.0 |
| OnAfterCrmLeadDelete | после удалениея лида. | CCrmLead::Delete | 10.0.0 |
| OnAfterExternalCrmLeadAdd | после добавления внешнего лида. | CCrmLead::Add | 10.0.0 |
| OnAfterCrmLeadProductRowsSave | после добавления товара в лид. | CCrmLead::SaveProductRows | 10.0.0 |

---
### Коммерческие предложения


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeCrmQuoteAdd | перед добавлением коммерческого предложения | CCrmQuote::Add |  |
| OnAfterCrmQuoteAdd | после добавления коммерческого предложения | CCrmQuote::Add |  |
| OnBeforeCrmQuoteUpdate | перед обновлением коммерческого предложения | CCrmQuote::Update |  |
| OnAfterCrmQuoteUpdate | после обновления коммерческого предложения | CCrmQuote::Update |  |
| OnBeforeCrmQuoteDelete | перед удалением коммерческого предложения | CCrmQuote::Delete |  |
| OnAfterCrmQuoteDelete | после удаления коммерческого предложения | CCrmQuote::Delete |  |
| OnBeforeCrmQuoteNumberSet | перед присвоением номера коммерческому предложению | CCrmQuote::SetQuoteNumber |  |
| OnAfterCrmQuoteProductRowsSave | после добавления товара в коммерческое предложение | CCrmQuote::SaveProductRows |  |

---
### Счета


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeCrmInvoiceUpdate | перед обновлением счёта | CCrmInvoice::Add |  |
| OnBeforeCrmInvoiceAdd | перед добавлением счёта | CCrmInvoice::Add |  |
| OnBeforeCrmInvoiceDelete | перед удалением счёта | CCrmInvoice::Delete |  |
| OnAfterCrmInvoiceDelete | после удаления счёта | CCrmInvoice::Delete |  |
| OnBeforeCrmInvoiceSetStatus | перед установкой статуса счёта | CCrmInvoice::SetStatus |  |
| OnAfterCrmInvoiceSetStatus | после установки статуса счёта | CCrmInvoice::SetStatus |  |

---
### Корзина


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAfterMoveToRecycleBin | после перемещения документа в корзину | BaseController::fireAfterMoveToBinEvent |  |
| OnAfterRecoverFromRecycleBin | после восстановления документа из корзины | BaseController::fireAfterRecoverEvent |  |
| OnAfterEraseFromRecycleBin | после очистки корзины | BaseController::fireAfterEraseEvent |  |

---
### Другие события


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnGetEntityTypes | после построения списка типов сущностей. | CCrmStatus::GetEntityTypes | 11.5.0 |
| OnAfterCrmAddEvent | после добавления события. | CCrmEvent::Add | 10.0.6 |
| OnGetActivityProviders | при получении списка активных провайдеров | ProviderManager::getProviders |  |
| OnBeforeCrmAddEvent | перед добавлением события. | CCrmEvent::Add | 10.0.6 |
| OnBeforeCrmEventDelete | перед удалением события. | CCrmEvent::Delete | 10.0.6 |
| OnBeforeCrmEventDeleteByElement | перед удалением всех событий, связанных с конкретной сущностью. | CCrmEvent::DeleteByElement | 10.0.6 |
| *****OnCrmStatusGetList | при запросе CCrmStatus::GetStatus | OnCrmStatusGetList | 12.5.7 |
| ***** используется для переопределения статусов в базе данных. Рекомендуется не использовать. |  |  |  |

---




| ![](../images/de1549b326.jpg) 10 **Tigra2009**07.06.2013 13:01:14 |  |  |
| --- | --- | --- |
| Пример массива $arFields для добавления лида: \| Код \| \| --- \| \| ``` Array[18] TITLE => "тестовый лид" COMPANY_TITLE => "название компани" NAME => "имя" LAST_NAME => "фамилия" SECOND_NAME => "отчество" POST => "должность" ADDRESS => "адрес" COMMENTS => "комментарий" SOURCE_DESCRIPTION => "Дополнительно об источнике" STATUS_DESCRIPTION => "сведения о статусе" OPPORTUNITY => "10" CURRENCY_ID => "UAH" EXCH_RATE => "1" SOURCE_ID => "CALL" STATUS_ID => "IN_PROCESS" ASSIGNED_BY_ID => "509" OPENED => "Y" FM => Array[4] EMAIL => Array[3] n1 => Array[2] VALUE => "test1@gmail.com" VALUE_TYPE => "WORK" n2 => Array[2] VALUE => "test2@gmail.com" VALUE_TYPE => "WORK" n3 => Array[2] VALUE => "test3@gmail.com" VALUE_TYPE => "WORK" PHONE => Array[3] n1 => Array[2] VALUE => "телефон рабочий 1" VALUE_TYPE => "WORK" n2 => Array[2] VALUE => "телефон рабочий 2" VALUE_TYPE => "WORK" n3 => Array[2] VALUE => "телефон мобильный 1" VALUE_TYPE => "MOBILE" WEB => Array[1] n1 => Array[2] VALUE => "сайт корпоративный" VALUE_TYPE => "WORK" IM => Array[1] n1 => Array[2] VALUE => "скайп" VALUE_TYPE => "SKYPE" ``` \| | Код | ``` Array[18] TITLE => "тестовый лид" COMPANY_TITLE => "название компани" NAME => "имя" LAST_NAME => "фамилия" SECOND_NAME => "отчество" POST => "должность" ADDRESS => "адрес" COMMENTS => "комментарий" SOURCE_DESCRIPTION => "Дополнительно об источнике" STATUS_DESCRIPTION => "сведения о статусе" OPPORTUNITY => "10" CURRENCY_ID => "UAH" EXCH_RATE => "1" SOURCE_ID => "CALL" STATUS_ID => "IN_PROCESS" ASSIGNED_BY_ID => "509" OPENED => "Y" FM => Array[4] EMAIL => Array[3] n1 => Array[2] VALUE => "test1@gmail.com" VALUE_TYPE => "WORK" n2 => Array[2] VALUE => "test2@gmail.com" VALUE_TYPE => "WORK" n3 => Array[2] VALUE => "test3@gmail.com" VALUE_TYPE => "WORK" PHONE => Array[3] n1 => Array[2] VALUE => "телефон рабочий 1" VALUE_TYPE => "WORK" n2 => Array[2] VALUE => "телефон рабочий 2" VALUE_TYPE => "WORK" n3 => Array[2] VALUE => "телефон мобильный 1" VALUE_TYPE => "MOBILE" WEB => Array[1] n1 => Array[2] VALUE => "сайт корпоративный" VALUE_TYPE => "WORK" IM => Array[1] n1 => Array[2] VALUE => "скайп" VALUE_TYPE => "SKYPE" ``` |
| Код |  |  |
| ``` Array[18] TITLE => "тестовый лид" COMPANY_TITLE => "название компани" NAME => "имя" LAST_NAME => "фамилия" SECOND_NAME => "отчество" POST => "должность" ADDRESS => "адрес" COMMENTS => "комментарий" SOURCE_DESCRIPTION => "Дополнительно об источнике" STATUS_DESCRIPTION => "сведения о статусе" OPPORTUNITY => "10" CURRENCY_ID => "UAH" EXCH_RATE => "1" SOURCE_ID => "CALL" STATUS_ID => "IN_PROCESS" ASSIGNED_BY_ID => "509" OPENED => "Y" FM => Array[4] EMAIL => Array[3] n1 => Array[2] VALUE => "test1@gmail.com" VALUE_TYPE => "WORK" n2 => Array[2] VALUE => "test2@gmail.com" VALUE_TYPE => "WORK" n3 => Array[2] VALUE => "test3@gmail.com" VALUE_TYPE => "WORK" PHONE => Array[3] n1 => Array[2] VALUE => "телефон рабочий 1" VALUE_TYPE => "WORK" n2 => Array[2] VALUE => "телефон рабочий 2" VALUE_TYPE => "WORK" n3 => Array[2] VALUE => "телефон мобильный 1" VALUE_TYPE => "MOBILE" WEB => Array[1] n1 => Array[2] VALUE => "сайт корпоративный" VALUE_TYPE => "WORK" IM => Array[1] n1 => Array[2] VALUE => "скайп" VALUE_TYPE => "SKYPE" ``` |  |  |
|  |  |  |
