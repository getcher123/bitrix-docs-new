# JS-класс к шаблону компонента

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8765 — Подключение JS-кода](lesson_8765.md)
- [Следующий: 6961 — JS-расширение медиаплеера →](lesson_6961.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=7971

Иногда при разработке компонента его шаблон необходимо наделить js-функциональностью, событиями и прочим. Выглядеть это может примерно так:

```
if (typeof(BX.CrmQuickPanelEdit) === 'undefined')
{
	BX.CrmQuickPanelEdit = function(id)
	{
		this._id = id;
		this._settings = {};
		this._submitHandler = BX.delegate(this._clickHandler, this);
		BX.bind(BX(this._id + '_submit'), 'click', this._submitHandler);
	};
	BX.CrmQuickPanelEdit.prototype =
	{
		initialize: function(id, settings)
	{
		this._id = id;
		this._settings = settings;
	},
		getId: function()
	{
		return this._id;
	},
	_clickHandler: function(e)
	{
		console.log(e);
	}
	};
	BX.CrmQuickPanelEdit.create = function(id, settings)
	{
	var _self = new BX.CrmQuickPanelEdit(id);
		_self.initialize(id, settings);
		return _self;
	};
}
```

Аналогичные подходы вы можете видеть в JS-ядре *Bitrix Framework* (расположен в `/bitrix/js/`). Разобравшись в данном примере вы сможете легче понимать JS-код разработчиков Битрикс.

Пример вызова:

```
<script type="text/javascript">
	BX.ready(function(){
		BX.CrmQuickPanelEdit.create('some_id', null);
	});
</script>
```

Если нужен паттерн "одиночка", то реализовать это можно как часть **create**:

```
BX.CrmQuickPanelEdit._self  = null;
BX.CrmQuickPanelEdit.create = function(id, settings)
{
	if (!this._self) {
	this._self = new BX.CrmQuickPanelEdit();
}
	this._self.initialize(id, settings);
	return this._self;
};
```

Что делает JS-класс: запоминает внутри себя некий ID (например, это может быть ID контейнера) и массив параметров, а также вешает обработчик на событие клика по кнопке подтверждения в форме указанного контейнера.
