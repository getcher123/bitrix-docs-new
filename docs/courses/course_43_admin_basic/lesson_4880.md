# Тип параметров CUSTOM

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2900 — Модификация простого компонента в составе сложного](lesson_2900.md)
- [Следующий: 2851 — Ещё пара примеров работы →](lesson_2851.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=4880

Тип параметров **CUSTOM** предоставляет разработчику полную свободу кастомизации. Например, есть какой-то системный или сторонний компонент. В зависимости от шаблона возникает необходимость добавить к компоненту какие-то свои настройки.

Реализуется это с помощью:

| \| **Параметр** \| **Описание** \|<br>\| --- \| --- \|<br>\| JS_FILE \| файл с JS кодом ответственным за отображение кастомной опции. \|<br>\| JS_EVENT \| callback функция которая будет вызвана после загрузки JS_FILE \|<br>\| JS_DATA \| дополнительные данные, передаваемые в JS_EVENT \| |
| --- |

Пример JS_DATA:

```
{
data:JS_DATA, //JS_DATA из .parameters.php
oCont: td,    /* контейнер, в котором предлагается размещать кастомный контрол  управления параметром */
oInput: input,//input в котором и будет предаваться значение параметра на сервер при сохранении
propertyID:"MAP_DATA",//название параметра
propertyParams: { /*...*/ },//Объект содержащий всё то же, что и массив параметра в .parameters.php
fChange:function(){ /*...*/ },//callback для вызова, при изменении параметра
getElements:function(){ /*...*/ }//возвращает объект со всеми параметрами компонента
}
```

#### Реализация в штатном компоненте

Рассмотрим пример использования типа параметров **CUSTOM** в штатном компоненте **map.google.view**.

**Примечание**: для использования компонентов Google необходимо иметь ключ доступа. Инструкция по получению ключа находится [в документации](https://dev.1c-bitrix.ru/user_help/components/content/google_maps/map_google_key.php).

В файле **.parameters.php** видим:

```
$arComponentParameters = array(
//...
'MAP_DATA' => array(
	'NAME' => GetMessage('MYMS_PARAM_DATA'),
	'TYPE' => 'CUSTOM',
	'JS_FILE' => '/bitrix/components/bitrix/map.google.view/settings/settings.js',
	'JS_EVENT' => 'OnGoogleMapSettingsEdit',
	'JS_DATA' => LANGUAGE_ID.'||'.GetMessage('MYMS_PARAM_DATA_SET'),
	'DEFAULT' => serialize(array(
		'google_lat' => GetMessage('MYMS_PARAM_DATA_DEFAULT_LAT'),
		'google_lon' => GetMessage('MYMS_PARAM_DATA_DEFAULT_LON'),
		'google_scale' => 13
	)),
	'PARENT' => 'BASE',
	)
//...
);
```

В файле `/bitrix/components/bitrix/map.google.view/settings/settings.js`:

```
function JCEditorOpener(arParams)
{
	this.jsOptions = arParams.data.split('||');
	this.arParams = arParams;

	var obButton = document.createElement('BUTTON');//создаём кнопку
	this.arParams.oCont.appendChild(obButton);// добавляем в контейнер

	obButton.innerHTML = this.jsOptions[1];//текст из JS_DATA

	obButton.onclick = BX.delegate(this.btnClick, this);//навешиваем callback'и
	this.saveData = BX.delegate(this.__saveData, this);
}
```

По нажатию кнопки открывается диалог, который генерируется в `/bitrix/components/bitrix/map.google.view/settings/settings.php`. В запросе к **settings.php** передаётся текущее значение `MAP_DATA`.

**Заголовок**

```
$obJSPopup->ShowTitlebar();
$obJSPopup->StartDescription('bx-edit-menu');
```

```

<p><b><? echo GetMessage('MYMV_SET_POPUP_WINDOW_TITLE')?></b></p><!-- Заголовок диалогового окна-->
<p class="note"><? echo GetMessage('MYMV_SET_POPUP_WINDOW_DESCRIPTION')?></p><!-- Описание -->
```

**Блок контента**



```
$obJSPopup->StartContent();
```

**Блок кнопок**

```
$obJSPopup->StartButtons();
```

**Кнопка сохранения**



```
<input type="submit" value="<?echo GetMessage('MYMV_SET_SUBMIT')?/>" onclick="return jsGoogleCE.__saveChanges();"/>
```



```
$obJSPopup->ShowStandardButtons(array('cancel'));//кнопка отмены
$obJSPopup->EndButtons();
```

В __saveChanges() данные сериализуются в строку и записываются в oInput, функцию сериализации на js в формат php можно посмотреть в `bitrix/components/bitrix/map.google.view/settings/settings_load.js`. В компоненте десериализация проводится из `$arParam[~MAP_DATA]`.

**Локализация**

Языковой файл находится в `lang/ru/.parameters.php`. При использовании типа параметров **CUSTOM** не забывайте добавлять сообщения в этот файл.

Список ссылок по теме:

- Пример подключения [календаря](http://blog.yasla.net/2013/11/bx-component-params-custom.html) в настройках компонента.
- Пример подключения [форумов](https://dev.1c-bitrix.ru/community/webdev/user/172310/blog/11649/) для механизма комментариев в каталоге.
