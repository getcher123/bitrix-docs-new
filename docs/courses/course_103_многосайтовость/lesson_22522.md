# Страница ошибки 404 при многосайтовости

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3442 — Удаление сайтов](lesson_3442.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=103&LESSON_ID=22522

При многосайтовости для каждого из сайтов можно создать свою

			страницу ошибки 404


При запросе пользователем страницы, отсутствующей на сервере, последний автоматически генерирует страницу с соответствующей надписью. Причин появления такой страницы может быть несколько:

**-** некорректная ссылка на сайте;

**-** неправильно введенный пользователем адрес;

**-** документ, на который ведет ссылка, был удален.

[Подробнее](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=3577)...

		.




Для этого выполните следующие действия:




1. Создайте файл
  			.htaccess
  **.htaccess** (от англ. hypertext access) - файл дополнительной конфигурации веб-сервера **Apache**. Позволяет задавать большое количество дополнительных параметров и разрешений для работы веб-сервера в отдельном каталоге без изменения главного конфигурационного файла **httpd.conf**.
  [Подробнее](https://dev.1c-bitrix.ru/learning/course/index.php?bitrix_include_areas=Y&COURSE_ID=32&LESSON_ID=3295)...
  		 (если он ещё не создан). Разместите его в директории того сайта, для которого настраиваете страницу ошибки 404 (например, **/site2**). В этом файле пропишите код:
  ```
  ErrorDocument 404 /site2/404.php
  <IfModule mod_rewrite.c>
  	RewriteEngine Off
  </IfModule>
  ```
2. Создайте новый файл **404.php**. В качестве образца можно взять код из стандартного файла **404.php**, расположенного в корневом разделе сайта (Контент &gt; Структура сайта &gt; Файлы и папки).
  ## Содержимое стандартного файла 404.php
  В штатной установке *1С-Битрикс: Управление сайтом* файл 404.php содержит следующий код:
  ```
  <?
  // подключение файла обработки адресов urlrewrite.php
  include_once($_SERVER['DOCUMENT_ROOT'].'/bitrix/modules/main/include/urlrewrite.php');
  // установка HTTP статуса 404
  CHTTP::SetStatus("404 Not Found");
  @define("ERROR_404","Y");
  // скрывает боковую панель на странице
  define("HIDE_SIDEBAR", true);
  // подключение header.php
  require($_SERVER["DOCUMENT_ROOT"]."/bitrix/header.php");
  // установка заголовка страницы
  $APPLICATION->SetTitle("Страница не найдена");?>
  <! -- начало содержимого страницы 404.php -->
  	<div class="bx-404-container">
  		<div class="bx-404-block"><img src="<?=SITE_DIR?>images/404.png" alt=""></div>
  		<div class="bx-404-text-block">Неправильно набран адрес, <br>или такой страницы на сайте больше не существует.</div>
  		<div class="">Вернитесь на <a href="<?=SITE_DIR?>">главную</a> или воспользуйтесь картой сайта.</div>
  	</div>
  	<div class="map-columns row">
  		<div class="col-sm-10 col-sm-offset-1">
  			<div class="bx-maps-title">Карта сайта:</div>
  		</div>
  	</div>
  	<div class="col-sm-offset-2 col-sm-4">
  		<div class="bx-map-title"><i class="fa fa-leanpub"></i> Каталог</div>
  	</div>
  	<div class="col-sm-offset-1 col-sm-4">
  		<div class="bx-map-title"><i class="fa fa-info-circle"></i> О магазине</div>
  		// подключение компонента Карта сайта
  		<?
  		$APPLICATION->IncludeComponent(
  			"bitrix:main.map",
  			".default",
  			array(
  				"CACHE_TYPE" => "A",
  				"CACHE_TIME" => "36000000",
  				"SET_TITLE" => "N",
  				"LEVEL" => "3",
  				"COL_NUM" => "2",
  				"SHOW_DESCRIPTION" => "Y",
  				"COMPONENT_TEMPLATE" => ".default"
  			),
  			false
  		);?>
  	</div>
  <! -- окончание содержимого страницы 404.php -->
  <! --  подключение файла footer.php -->
  <?require($_SERVER["DOCUMENT_ROOT"]."/bitrix/footer.php");?>
  ```
  Откорректируйте созданный файл **404.php** в зависимости о того, какую информацию Вы хотите выводить на этой странице. Разместите этот файл **в той же директории**, что и созданный ранее файл **.htaccess**.




В результате при возникновении на этом сайте ошибки 404 будет отображена созданная Вами страница (в примере ниже удалён компонент **Карта сайта**, отредактирован текст и заменена картинка):




![](../../../images/courses/103/dev.1c-bitrix.ru/upload/medialibrary/36d/404-new_page.png)
