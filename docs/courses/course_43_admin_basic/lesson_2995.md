# Пример. Исключение шаблона компонента из кэша

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2899 — Пример. Компонент в элементе ИБ](lesson_2899.md)
- [Следующий: 2978 — Сache Dependencies (тегированный кеш) →](lesson_2978.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2995

#### Универсальный способ исключения шаблона компонента из кэша

Часто возникают задачи, которым мешает кэширование шаблонов компонентов. Но только ради исключения шаблона из кэша не хочется кастомизировать компонент и от кэширования результата компонента отказываться тоже не хочется. Самый распространенный пример – голосование за элементы инфоблоков в списках или вывод рекламы.

Идея решения проста: переместить шаблон компонента в эпилог компонента:

1. Скопировать шаблон компонента в адресное пространство шаблона сайта.
2. В папке шаблона компонента создать файл **component_epilog.php** и полностью скопировать в него код из файла шаблона **template.php**. Затем в самом верху **component_epilog.php** сразу после проверки подключения эпилога ядра `<?if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();?>` перед началом непосредственно самого кода шаблона нужно добавить такой код:
  ```
  <?
  // заменяем $arResult эпилога значением, сохраненным в шаблоне
  if(isset($arResult['arResult'])) {
  	$arResult =& $arResult['arResult'];
  		// подключаем языковой файл
  	global $MESS;
  	include_once(GetLangFileName(dirname(__FILE__).'/lang/', '/template.php'));
  } else {
  	return;
  }
  ?>
  ```
3. Полностью очистить файл **template.php** и добавить такой код:
  ```
  <?if(!defined('B_PROLOG_INCLUDED')||B_PROLOG_INCLUDED!==true)die();
  ?>
  // добавляем к кэшируемому результату $arResult
  if(property_exists($component, 'arResultCacheKeys')) {
  	if(!is_array($component->arResultCacheKeys)) {
  		$component->arResultCacheKeys = array();
  	}
  	$sVarName = 'arResult';
  	$component->arResultCacheKeys[] = $sVarName;
  	$component->arResult[$sVarName] = $$sVarName;
  }
  ```

Теперь результат компонента кэшируется, а шаблон – нет.

Недостатки этого способа:

1. Увеличение размера кэша. С размером кэша можно бороться путем включения в кэш только необходимых данных
2. Шаблон все же постоянно генерирует html-код, что медленнее, чем вывод уже готового, ранее сформированного html-кода.



**Примечание**: если в компоненте используются методы [CBitrixComponent::InitComponentTemplate](https://dev.1c-bitrix.ru/api_help/main/reference/cbitrixcomponent/initcomponenttemplate.php) и  [CBitrixComponent::ShowComponentTemplate](https://dev.1c-bitrix.ru/api_help/main/reference/cbitrixcomponent/showcomponenttemplate.php), то такой компонент не подключает **component_epilog.php**. Например: bitrix:search.page.
