# Как вывести произвольный контент в шаблоне сайта и компонента

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3514 — Примеры работы и решения проблем](lesson_3514.md)
- [Следующий: 3235 — Разработка шаблонов страниц →](lesson_3235.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3855

Усовершенствованные методы буферизации в шаблоне позволяют более не использовать *CBitrixComponentTemplate::EndViewTarget()* ввиду того, что конец шаблона вызывает завершение буферизации автоматически.

Описанные ниже способы по своей сути похожи на Включаемые области. Только Включаемая область это файл подключаемый в шаблоне сайта, а указанные методы - это область, которая формируется в коде шаблона.

Можно использовать как в шаблоне сайта, так и в шаблоне компонента.

Теперь есть поддержка стандартного кеширования в компонентах.

- **template.php**:
  ```
  <?$this->SetViewTarget("sidebar");?>
  	<div class="element-filter">
  		<!--вывод фильтра -->
  	</div>
  <?$this->EndViewTarget();?>
  <div class="element-list">
  	<!--вывод списка -->
  </div>
  ```
- **header.php**:
  ```
  <div id="sidebar">
  	<?$APPLICATION->ShowViewContent("sidebar")?>
  </div>
  ```

#### Методы, доступные в шаблоне (через $this)

- *CBitrixComponentTemplate::SetViewTarget($view, $pos)*
- *CBitrixComponentTemplate::EndViewTarget()*

#### Методы глобального объекта $APPLICATION

- [Cmain::AddViewContent($view, $content, $pos)](/api_help/main/reference/cmain/addviewcontent.php)
- [Cmain::ShowViewContent($view)](/api_help/main/reference/cmain/showviewcontent.php)

где:

- `$view` – идентификатор буферизируемой области;
- `$content` – буферизируемый контент;
- `$pos` – сортировка вывода контента.

**Примечание:** одному идентификатору **$view** может соответствовать несколько буферов. Последовательность вывода контента определяется сортировкой **$pos**.
