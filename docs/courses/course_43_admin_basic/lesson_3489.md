# Отложенные функции

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2921 — Работа с базами данных](lesson_2921.md)
- [Следующий: 2916 — Файл init.php →](lesson_2916.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3489

### Отложенные функции

> **Отложенные функции** - технология, позволяющая задавать **заголовок страницы**, **пункты навигационной цепочки**, **CSS стили**, **дополнительные кнопки** в **панель управления**, **мета-теги** и т.п. с помощью функций используемых непосредственно в **теле страницы**. Соответствующие результаты работы этих функций выводятся в **прологе**, то есть выше по коду, чем они были заданы.





Технология была создана в первую очередь для использования в компонентах, которые, как правило, выводятся в теле страницы, но при этом внутри них могут быть заданы заголовок страницы, добавлен пункт в навигационную цепочку, добавлена кнопка в панель управления и так далее. Отложенные функции нельзя использовать в файлах шаблона компонента: **template.php** и **result_modifier.php** (так как результаты их выполнения кешируются).

Внутри отложенной функции можно подключать компоненты, но при этом необходимо вручную подключать файлы **CSS** и **js**.

**Примечание**: Есть ряд новых функций, которые могут работать в условиях кеширования (*SetViewTarget*, *EndViewTarget*). Но такие функции новые, ещё не описаны в документации и их надо рассматривать скорее как исключение, чем как правило.

### Алгоритм работы

1. Любой исходящий поток из PHP скрипта буферизируется.
2. Как только в коде встречается одна из следующих функций:
  или другая функция, обеспечивающая откладывание выполнения какой-либо функции, то:
  Таким образом, существует стек A, в котором находится весь контент страницы, разбитый на части. В этом же стеке есть пустые элементы, предназначенные для их дальнейшего заполнения результатами отложенных функций.
     Также существует стек B, в котором запоминаются имена и параметры отложенных функции в порядке их следования в коде.

  - [CMain::ShowTitle](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/showtitle.php),
  - [CMain::ShowCSS](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/showcss.php),
  - [CMain::ShowNavChain](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/shownavchain.php),
  - [CMain::ShowProperty](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/showproperty.php),
  - [CMain::ShowMeta](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/showmeta.php),
  - [CMain::ShowPanel](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/showpanel.php)

  1. весь буферизированный до этого контент запоминается в очередном элементе **стека A**;
  2. в **стек A** добавляется пустой элемент, который в дальнейшем будет заполнен результатом выполнения **отложенной** функции;
  3. имя **отложенной** функции запоминается в **стеке B**;
  4. буфер очищается и буферизация снова включается.
3. В конце страницы в **служебной части эпилога** выполняются следующие действия:

  1. все отложенные функции из **стека B** начинают выполняться одна за другой;
  2. результаты их выполнения вставляются в специально предназначенные для этого места в **стек A**;
  3. весь контент из **стека A** "склеивается" (конкатенируется) и выводится на экран.



Таким образом, технология позволяет фрагментировать весь контент страницы, разбивая его на части с помощью специальных функций, обеспечивающих временное откладывание выполнения других функций (отложенных функций). В конце страницы все отложенные функции выполняются одна за другой и результаты их выполнения вставляются в отведенные для этого места внутри фрагментированного контента страницы. Затем весь контент склеивается и отправляется браузеру посетителя сайта.



**Внимание!** При использовании этой технологии необходимо учитывать, что над результатами работы функций, обеспечивающих откладывание других функций, **нельзя** выполнять какие-либо действия.

Значение, возвращаемое отложенной функцией, не возвращается, а сразу выводится в месте вызова **AddBufferContent**, а всё, что выводится в отложенной функции, будет выведено до начала шаблона.

Пример кода, в котором отложенная функция не будет отрабатывать код в шаблоне как ожидается:

```

if (!$APPLICATION->GetTitle())
	echo "Стандартная страница";
else
	echo $APPLICATION->GetTitle();
```

А такой код будет работать:

```
$APPLICATION->AddBufferContent('ShowCondTitle');

function ShowCondTitle()
{
	global $APPLICATION;
if (!$APPLICATION->GetTitle())
	return "Стандартная страница";
else
	return $APPLICATION->GetTitle();
}
```

Ещё один пример

```
$page_title = $APPLICATION->GetPageProperty($title);
if (strlen($page_title)<=0) $page_title = "Заголовок страницы по умолчанию";
echo $page_title;
```

этот код не будет работать по той причине, что все отложенные функции выполняются в самом конце страницы, в служебной части эпилога.

Пример:

```
<?
require($_SERVER["DOCUMENT_ROOT"]."/bitrix/header.php");
$APPLICATION->SetTitle("Старый заголовок");
?>
<?
global $APPLICATION;
$strTitle = $APPLICATION->GetTitle();
echo $strTitle." - Заголовок страницы";

$APPLICATION->SetTitle('Новый заголовок');
?>
<?require($_SERVER["DOCUMENT_ROOT"]."/bitrix/footer.php");?>
```

На странице будет напечатано - **Старый заголовок**, а в браузере - **Новый заголовок**.

### Задействованные группы функций

| \| **Имя функции обеспечивающей откладывание** **Выполнение какой функции откладывается****Дополнительные связанные функции** \|  \|  \|<br>\| --- \| --- \| --- \|<br>\| [CMain::ShowTitle](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/showtitle.php) \| [CMain::GetTitle](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/gettitle.php) \| [CMain::SetTitle](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/settitle.php) \|<br>\| [CMain::ShowCSS](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/showcss.php) \| [CMain::GetCSS](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/getcss.php) \| [CMain::SetTemplateCSS](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/settemplatecss.php)<br> [CMain::SetAdditionalCSS](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/setadditionalcss.php) \|<br>\| [CMain::ShowNavChain](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/shownavchain.php) \| [CMain::GetNavChain](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/getnavchain.php) \| [CMain::AddChainItem](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/addchainitem.php) \|<br>\| [CMain::ShowProperty](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/showproperty.php) \| [CMain::GetProperty](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/getproperty.php) \| [CMain::SetPageProperty](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/setpageproperty.php)<br> [CMain::SetDirProperty](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/setdirproperty.php) \|<br>\| [CMain::ShowMeta](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/showmeta.php) \| [CMain::GetMeta](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/getmeta.php) \| [CMain::SetPageProperty](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/setpageproperty.php)<br> [CMain::SetDirProperty](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/setdirproperty.php) \|<br>\| [CMain::ShowPanel](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/showpanel.php) \| [CMain::GetPanel](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/getpanel.php) \| [CMain::AddPanelButton](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/addpanelbutton.php) \| |
| --- |

Технология позволяет создавать отложенные функции с помощью метода [CMain::AddBufferContent](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/addbuffercontent.php).

Список ссылок по теме:

- [Вызов компонента через отложенную функцию.](http://dev.1c-bitrix.ru/community/webdev/user/2106/blog/2345/) (блог)
