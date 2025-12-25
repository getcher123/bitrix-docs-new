# CIBlockResult

**CIBlockResult** - вспомогательный класс для работы с объектами результатов выборок, наследуется от класса [CDBResult](../../../main/reference/cdbresult/index.md) и содержит все его параметры и методы. Объекты данного класса возвращают методы [CIBlockElement](../ciblockelement/index.md)::[GetList](../ciblockelement/getlist.md), [CIBlockElement](../ciblockelement/index.md)::[GetByID](../ciblockelement/getbyid.md) и функции [GetIBlockElementList](../../functions/getiblockelementlist.md), [GetIBlockElementListEx](../../functions/getiblockelementlistex.md). Использование методов этого объекта позволяет более гибко и эффективно работать с элементами информационных блоков.


#### Методы класса


| Метод | Описание | С версии |
| --- | --- | --- |
| [GetNext](getnext.md) | Возвращает из выборки список [полей элемента](../../fields.md#felement), с замененными ссылками в полях *DETAIL_PAGE_URL* и *LIST_PAGE_URL*. | 3.0.5 |
| [GetNextElement](getnextelement.md) | Возвращает объект [_CIBElement](../cibelement/index.md) элемента из выборки. | 3.1.3 |
| [SetUrlTemplates](seturltemplates.md) | Устанавливает шаблоны путей для элементов. | 7.1.3 |
| [SetSectionContext](setsectioncontext.md) | Метод устанавливает поля раздела в качестве родителя элемента для подстановки в шаблоны путей. | 7.1.3 |
