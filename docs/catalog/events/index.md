# События


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeDiscountAdd | перед добавлением новой скидки. | CCatalogDiscount::Add | 14.0.4 |
| OnBeforeDiscountUpdate | перед обновлением существующей скидки. | CCatalogDiscount::Update | 14.0.4 |
| OnBeforeCouponAdd | перед добавлением купона. | CCatalogDiscountCoupon::Add | 12.0.0 |
| OnBeforeCouponDelete | перед удалением купона. | CCatalogDiscountCoupon::Delete | 12.0.0 |
| OnBeforeCouponUpdate | перед изменением купона. | CCatalogDiscountCoupon::Update | 12.0.0 |
| OnBeforeDiscountDelete | перед удалением скидки. | CCatalogDiscount::Delete | 12.5.0 |
| OnBeforeDocumentDelete | перед удалением документа. | CCatalogDocs::delete | 12.5.1 |
| OnBeforeIBlockElementDelete | перед удалением элемента. | CCatalog::OnBeforeIBlockElementDelete | 10.0.2 |
| OnCouponAdd | при добавлении купона. | CCatalogDiscountCoupon::Add | 12.0.0 |
| OnCouponDelete | при удалении купона. | CCatalogDiscountCoupon::Delete | 12.0.0 |
| OnCouponUpdate | при изменении купона. | CCatalogDiscountCoupon::Update | 12.0.0 |
| OnDiscountAdd | в случае успешного добавления скидки. | CCatalogDiscount::Add | 11.0.5 |
| OnDiscountDelete | при удалении скидки. | CCatalogDiscount::Delete | 11.0.5 |
| OnDiscountUpdate | случае успешного изменения параметров скидки. | CCatalogDiscount::Update | 11.0.5 |
| OnDocumentBarcodeDelete | после OnBeforeDocumentDelete в методе CCatalogStoreDocsBarcodeAll::OnBeforeDocumentDelete. | CCatalogStoreDocsBarcodeAll::OnBeforeDocumentDelete | 12.5.1, устарел с 22.0 Вместо него необходимо использовать **OnDocumentDelete**. Формат параметров обработчика тот же: `function ($id)`- где $id содержит идентификатор документа |
| OnDocumentElementDelete | после OnDocumentBarcodeDelete в методе CCatalogStoreDocsElementAll::OnDocumentBarcodeDelete. | CCatalogStoreDocsElementAll::OnDocumentBarcodeDelete | 12.5.1, устарел с 22.0 Вместо него необходимо использовать **OnDocumentDelete**. Формат параметров обработчика тот же: `function ($id)`- где $id содержит идентификатор документа |
| OnGenerateCoupon | при генерации купона. | CatalogGenerateCoupon | 11.0.5 |
| OnGetDiscountResult | в конце метода CCatalogProduct::GetDiscount. | CCatalogDiscount::GetDiscount | 11.5.2 |
| OnGetDiscountSave | в начале метода CCatalogDiscSave::GetDiscount. | CCatalogDiscountSave::GetDiscount | 11.5.2 |
| OnGetNearestQuantityPrice | в начале метода CCatalogProduct::GetNearestQuantityPrice. | CCatalogProduct::GetNearestQuantityPrice | 11.0.5 |
| OnGetNearestQuantityPriceResult | перед окончанием работы метода CCatalogProduct::GetNearestQuantityPrice. | CCatalogProduct::GetNearestQuantityPrice | 11.0.5 |
| OnGetOptimalPrice | при поиске оптимальной цены товара. | CCatalogProduct::GetOptimalPrice | 11.0.5 |
| OnGetOptimalPriceResult | перед окончанием работы метода CCatalogProduct::GetOptimalPrice. | CCatalogProduct::GetOptimalPrice | 11.0.5 |
| OnCountPriceWithDiscount | при пересчете цены, к которой применена скидка. | CCatalogProduct::CountPriceWithDiscount | 11.0.5 |
| OnCountPriceWithDiscountResult | перед окончанием работы метода CCatalogProduct::CountPriceWithDiscount. | CCatalogProduct::CountPriceWithDiscount | 11.0.5 |
| OnSaleOrderSumm | при вычислении накопительной скидки. | CCatalogDiscountSave::__SaleOrderSumm | 11.5.2 |
| OnBeforePriceAdd | перед добавлением новой цены товара. | CPrice::Add | 8.0.4 |
| OnBeforePriceUpdate | перед изменением существующей цены. | CPrice::Update | 5.1.1 |
| OnBeforePriceDelete | перед удалением существующей цены. | CPrice::Delete | 10.0.5 |
| OnPriceDelete | в процессе удаления существующей цены. | CPrice::Delete | 10.0.5 |
| OnBeforeProductPriceDelete | перед удалением цен в методе CPrice::DeleteByProduct(). | CPrice::DeleteByProduct | 10.0.5 |
| OnProductPriceDelete | в процессе удаления цен в методе CPrice::DeleteByProduct(). | CPrice::DeleteByProduct | 10.0.5 |
| OnBeforeProductAdd | перед добавлением товара. | [CCatalogProduct::Add](../classes/ccatalogproduct/add.md) | 11.0.5 |
| OnBeforeCatalogDelete | перед удалением записи о том, что инфоблок является торговым каталогом. | CCatalog::Delete | 3.2.1 |
| OnBeforeGroupAdd | перед добавлением типа цены. | CCatalogGroup::Add | 4.0.4 |
| OnBeforeGroupDelete | перед удалением типа цены. | CCatalogGroup::Delete | 4.0.4 |
| OnBeforeGroupUpdate | перед изменением типа цены. | CCatalogGroup::Update | 4.0.4 |
| OnBeforeProductUpdate | перед изменением свойств товара. | [CCatalogProduct::Update](../classes/ccatalogproduct/ccatalogproduct__update.bc9a623b.md) | 5.1.1 |
| OnCatalogDelete | при удалении записи о том, что инфоблок является торговым каталогом. | CCatalog::Delete | 3.2.1 |
| OnGetDiscount | при получении скидки. | CCatalogDiscount::GetDiscount | 5.1.0 |
| OnGroupAdd | при добавлении нового типа цены. | CCatalogGroup::Add | 12.5.5 |
| OnGroupDelete | при удалении типа цены. | CCatalogGroup::Delete | 4.0.4 |
| OnGroupUpdate | при изменении типа цены. | CCatalogGroup::Update | 4.0.4 |
| OnPriceAdd | при добавлении нового ценового предложения. | CPrice::Add | 5.9.0 |
| OnPriceUpdate | при изменении существующего ценового предложения. | CPrice::Update | 5.1.1 |
| OnProductAdd | при добавлении товара. | [CCatalogProduct::Add](../classes/ccatalogproduct/add.md) | 5.9.0 |
| OnProductUpdate | в процессе изменения свойств товара. | [CCatalogProduct::Update](../classes/ccatalogproduct/ccatalogproduct__update.bc9a623b.md) | 5.1.1 |
| OnGetDiscountByPrice | для изменения логики метода GetDiscountByPrice. | CCatalogDiscount::GetDiscountByPrice | 5.1.0 |
| OnGetDiscountByProduct | для изменения логики метода GetDiscountByProduct. | CCatalogDiscount::GetDiscountByProduct | 5.1.0 |
| OnBeforeCatalogImport1C | событие, вызываемое перед началом процедуры обмена с 1С. Событие компонента **catalog.import.1c** |  | 11.5.4 |
| OnSuccessCatalogImport1C | после успешного импорта товаров из 1С. Событие компонента **catalog.import.1c** |  | 11.5.4 |
| OnBeforeStoreProductAdd | перед созданием новой записи о добавлении товара на склад. | CCatalogStoreProduct::Add | 12.5.4 |
| OnBeforeStoreProductDelete | перед удалением записи из таблицы остатков товара. | CCatalogStoreProductAll::Delete | 12.5.4 |
| OnBeforeStoreProductUpdate | перед изменением записи в таблице остатков товара. | CCatalogStoreProductAll::Update | 12.5.4 |
| OnStoreProductAdd | в случае успешного создания новой записи о добавлении товара на склад. | CCatalogStoreProduct::Add | 12.5.4 |
| OnStoreProductDelete | в случае успешного удаления записи из таблицы остатков товара на складе. | CCatalogStoreProductAll::Delete | 12.5.4 |
| OnStoreProductUpdate | в случае успешного изменения записи в таблице остатков товара. | CCatalogStoreProductAll::Update | 12.5.4 |
| OnBeforeCatalogStoreUpdate | перед обновлением параметров склада. | CCatalogStore::Update | 12.5.6 |
| OnCatalogStoreUpdate | в случае успешного изменения параметров склада. | CCatalogStore::Update | 12.5.6 |
| OnBeforeCatalogStoreDelete | перед удалением склада. | CCatalogStore::Delete | 12.5.6 |
| OnCatalogStoreDelete | при удалении существующего склада. | CCatalogStore::Delete | 12.5.3 |
| OnBeforeCatalogStoreAdd | перед добавлением нового склада. | CCatalogStore::Add | 12.5.6 |
| OnCatalogStoreAdd | в случае успешного добавления нового склада. | CCatalogStore::Add | 12.5.6 |
