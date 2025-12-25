# Пользовательские свойства

Пользовательские свойства модуля информационных блоков позволяют изменять представление (формы ввода и т.п.) стандартных свойств расширяя их возможности. Фактически такое свойство представляет собой набор обработчиков событий вызываемых при построении административного интерфейса, публичной части сайта или API функций.

При первом обращении к методам пользовательских свойств вызываются обработчики события [OnIBlockPropertyBuildList](../../events/OnIBlockPropertyBuildList.md). Строится список свойств и при необходимости вызываются их методы.

Примеры конкретной реализации свойств можно посмотреть в файлах модуля информационных блоков **classes/general/prop_*.php**

#### Методы класса | Метод | Описание | С версии | | --- | --- | --- | | [GetUserTypeDescription](GetUserTypeDescription.md) | Описание свойства | 5.0.1 | | [CheckFields](CheckFields.md) | Проверка правильности значения | 5.0.1 | | [GetLength](GetLength.md) | Проверка длинны значения | 7.1.0 | | [ConvertToDB](ConvertToDB.md) | Сохранение в БД | 5.0.1 | | [ConvertFromDB](ConvertFromDB.md) | Извлечение из БД | 5.0.1 | | [GetPropertyFieldHtml](GetPropertyFieldHtml.md) | Отображение в форме редактирования | 5.0.1 | | [GetAdminListViewHTML](GetAdminListViewHTML.md) | Показ в списке | 6.0.3 | | [GetPublicViewHTML](GetPublicViewHTML.md) | Отображение в публичной части | 6.5.2 | | [GetPublicEditHTML](GetPublicEditHTML.md) | Редактирование в публичной части | 7.1.4 | | [GetSearchContent](GetSearchContent.md) | Индексация значений | 8.6.1 | | [PrepareSettings](PrepareSettings.md) | Сохранение настроек | 8.6.1 | | [GetSettingsHTML](GetSettingsHTML.md) | Редактирование настроек | 8.6.1 | | [GetPropertyFieldHtmlMulty](getpropertyfieldhtmlmulty.md) | Вывод формы редактирования множественного свойства. Если отсутствует, то используется [GetPropertyFieldHtml](GetPropertyFieldHtml.md) для каждого значения отдельно (у множественных свойств). | 5.0.1 | | [GetAdminFilterHTML](getadminfilterhtml.md) | Выводит html для фильтра по свойству на административной странице списка элементов инфоблока. | 7.0.1 | | [GetPublicFilterHTML](getpublicfilterhtml.md) | Выводит html для фильтра по свойству на публичной странице списка элементов инфоблока. | 8.0.1 |


#### Фильтрация

Для работы фильтра необходимо в *GetUserTypeDescription* добавить строчку вида:


```
"AddFilterFields" => array(__CLASS__,'AddFilterFields'),
```

и в классе объявить метод:


```
public static function AddFilterFields($arProperty, $control, &$arFilter, &$filtered)
```

Надо учитывать что этот метод не обязательный. Метод нужен только если фильтр сильно "не стандартный".
