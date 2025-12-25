# Дополнительно

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 4514 — Данные до и после update](lesson_4514.md)
- [Следующий: 7983 — "Ленивые" параметры в событиях →](lesson_7983.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2816

**Вопрос**: Можно ли вызывать функцию [AddEventHandler](http://dev.1c-bitrix.ru/api_help/main/functions/module/addeventhandler.php) несколько раз для одного и того же события?

**Ответ**: Вызывать несколько раз функцию AddEventHandler с одинаковыми первыми двумя параметрами можно. Случаи, когда это не так (возможен лишь один обработчик на событие) очень редки. При повторном вызове желательно указывать четвёртый параметр, который отвечает за очерёдность вызова обработчиков. Если не указать этот параметр, то обработчики будут вызваны в порядке добавления.

#### Как обработчику события узнать, какое событие он обрабатывает?

Функция является обработчиком событий модулей (функция не знает каких модулей и каких событий). Но она должна, учитывая какое произошло событие, совершать различные действия.

**Вопрос:** как обработчику события узнать, какое событие он обрабатывает?

**Решение** зависит от способа инициализации.

1. **AddEventHandler** - сделайте прослойку.
  ```
  function OnAdd()
  {
  	RealHandler("add");
  }
  function OnUpdate()
  {
  	RealHandler("update");
  }
  ```
2. **RegisterModuleDependences** - при регистрации добавьте аргумент.
  ```
  $TO_METHOD_ARG = Array("argument"=>"OnUserDelete");
  RegisterModuleDependences("main", "OnUserDelete", "forum", "CForum", "OnUserDelete", $sort, $TO_PATH, $TO_METHOD_ARG);
  class CForum
  {
  	function OnUserDelete($arguments, &$arFields)
  	{
  		//Код обработчика
  	}
  }
  ```

**Вопрос:** Как осуществить поиск не только по названию товаров но и по описанию.

**Решение:** Нужно добавить свойство для поиска и в настройках свойства указываем что оно участвует в поиске. Далее:

```
// регистрируем обработчик
AddEventHandler("search", "BeforeIndex", "BeforeIndexHandler");
 // создаем обработчик события "BeforeIndex"
function BeforeIndexHandler($arFields)
{
	if(!CModule::IncludeModule("iblock")) // подключаем модуль
		return $arFields;
	if($arFields["MODULE_ID"] == "iblock")
		{
		$db_props = CIBlockElement::GetProperty(
			// Запросим свойства индексируемого элемента
			$arFields["PARAM2"],  // BLOCK_ID индексируемого свойства
			$arFields["ITEM_ID"],  // ID индексируемого свойства
			array("sort" => "asc"),  // Сортировка (можно упустить)
			Array("CODE"=>"CML2_ARTICLE"));  // CODE свойства (в данном случае артикул)
				if($ar_props = $db_props->Fetch())
				$arFields["TITLE"] .= " ".$ar_props["VALUE"];  // Добавим свойство в конец заголовка индексируемого элемента
		}
	return $arFields; // вернём изменения
}
```
