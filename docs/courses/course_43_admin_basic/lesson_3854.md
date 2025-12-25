# Административные страницы в публичке

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3853 — Контекстное меню элементов списка](lesson_3853.md)
- [Следующий: 5258 — Пользовательские формы редактирования элементов →](lesson_5258.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3854

- Метод генерирует Javascript, открывающий URL в popup-окне:
  ```
  $APPLICATION->GetPopupLink(Array(
  	"URL"=> "URL страницы, которая откроется в popup-окне",
  	"PARAMS" => Array(
  		"width" => 780,
  		"height" => 570,
  		"resizable" => true,
  		"min_width" => 780,
  		"min_height" => 400
  		)
  	)
  );
  ```
- Метод генерирует кнопки управления элементами и разделами инфоблока:
  ```
  CIBlock::GetPanelButtons(
  	$IBLOCK_ID = 0, //ID инфоблока
  	$ELEMENT_ID = 0, //ID елемента инфоблока
  	$SECTION_ID = 0, //ID раздела инфоблока
  	$arOptions = Array(
  		"SECTION_BUTTONS" => true, //генерировать кнопки для управления разделами
  		"SESSID" => false, //добавлять ссылку в авторизованный token
  		"RETURN_URL" => "",
  		"LABELS" => Array() //надписи кнопок, по умолчанию берутся из настроек инфоблока
  	)
  );
  ```
