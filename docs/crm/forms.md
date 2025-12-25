# CRM-формы и Виджет на сайт

**Внимание!** Виджет работает на любом сайте, даже если он собран не на "1С-Битрикс: Управление сайтом". Но на сайте сделанном на "1С-Битрикс: Управление сайтом" нужно быть внимательным с версией Главного модуля. Требуется не ниже 19.0.0.


#### Примеры работы с виджетом на сайте

Добавление своего канала и кнопки


```
BX.addCustomEvent(document, "b24-sitebutton-load", function (e, instance){
	instance.buttons.add({
		'id': 'my-mail',
		'href': 'mailto: andrey@bitrix.ru',
		'title': 'Email me',
		'target': '_self',
		'sort': 1000,
		'icon': 'http://sparkysite.ru/medium/mails/mails01/mmail01.png',
		'onclick': function() {console.log('button my-mail clicked!!!');},
	});
});
```


| То же самое, с jQuery |
| --- |
| ``` $( document ).on( "b24-sitebutton-load", function (e, instance){ instance.buttons.add({ 'id': 'my-mail', 'href': 'mailto: andrey@bitrix.ru', 'title': 'Email me', 'target': '_self', 'sort': 1000, 'icon': 'http://sparkysite.ru/medium/mails/mails01/mmail01.png', 'onclick': function() {console.log('button my-mail clicked!!!');}, }); }); ``` |


Изменение заголовков панелей форм


```
BX.addCustomEvent(document, "b24-sitebutton-load-widget-crmform", function (e, widget){
	widget.caption = 'Заголовок формы';
});
BX.addCustomEvent(document, "b24-sitebutton-load-widget-callback", function (e, widget){
	widget.caption = 'Заголовок звонка';
});
```


| То же самое, с jQuery |
| --- |
| ``` $( document ).on( "b24-sitebutton-load-widget-crmform", function (e, widget){ widget.caption = 'Заголовок формы'; }); $( document ).on( "b24-sitebutton-load-widget-callback", function (e, widget){ widget.caption = 'Заголовок звонка'; }); ``` |


Передача предустановленных значений в CRM-форму


```
BX.addCustomEvent(document, "b24-sitebutton-form-init", function (e, form){
	form.fields = {
		'values': {
			'LEAD_PHONE': '+71111111111',
			'LEAD_NAME': 'Андрей'
		}
	};
});
```


| То же самое, с jQuery |
| --- |
| ``` $( document ).on( "b24-sitebutton-form-init", function (e, form){ form.fields = { 'values': { 'LEAD_PHONE': '+71111111111', 'LEAD_NAME': 'Андрей' } }; }); ``` |


Своё приветствие через события


```
BX.addCustomEvent(document, "b24-sitebutton-load", function (e, instance){
	instance.hello.setConditions([{
		'icon': 'http://crm.bitrix24.com/upload/main/76d/52b.jpg',
		'name': 'Виктория',
		'text': 'Привет! Нужна помощь?',
		'page': '',
		'delay': 1
	}]);
});
```


| То же самое, с jQuery |
| --- |
| ``` $( document ).on( "b24-sitebutton-load", function (e, instance){ instance.hello.setConditions([{ 'icon': 'http://crm.bitrix24.com/upload/main/76d/52b.jpg', 'name': 'Виктория', 'text': 'Привет! Нужна помощь?', 'page': '', 'delay': 1 }]); }); ``` |
