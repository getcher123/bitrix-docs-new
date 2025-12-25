# Примеры

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3578 — Комплексный компонент и SEF режим](lesson_3578.md)
- [Следующий: 9901 — Модуль Поиск →](lesson_9901.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=5511

### Пример



Новости вида /about/news/23.html (ссылка для печати /about/news/print_23.html) вместо /about/news/detail.php?ID=23 (/about/news/detail.php?ID=23&print=Y)



- ```
  mod_rewrite
  RewriteEngine On
  RewriteBase /
  RewriteRule ^about/news/([0-9]+).html$ about/news/detail.php?ID=$1
  RewriteRule ^about/news/print_([0-9]+).html$ about/news/detail.php?ID=$1&print=Y
  ```
- Обработчик 404 ошибки
  ```
  <?if(preg_match("~^/about/news/(print_)?([0-9]+).html$~",$_SERVER["REQUEST_URI"],$match))
  {
  header("HTTP/1.1 200 OK");
  $_GET["print"] = (strlen($match[1])>0 ? "Y": "");
  $_REQUEST["ID"] = $match[2];
  include($_SERVER["DOCUMENT_ROOT"]."/about/news/detail.php");
  }
  else
  {
  define("ERROR_404", "Y");
  header("HTTP/1.1 404 Not Found");
  require($_SERVER["DOCUMENT_ROOT"]."/bitrix/header.php");
  $APPLICATION->SetTitle("404 - файл не найден");
  require($_SERVER["DOCUMENT_ROOT"]."/bitrix/footer.php");
  }
  ?>
  ```

### Дополнительно

#### Как убрать "PHPSESSID=..." из URL?



Чтобы избавиться от идентификатора сессии в URL, раскомментируйте строку в `/.htaccess`:



```
php_flag session.use_trans_sid off
```



Если это не дает результата, необходимо изменить значение параметра `session.use_trans_sid` на `Off` непосредственно в **php.ini** на сервере.



Удостоверьтесь, также, что значение параметра `session.use_cookies` установлено в `On`.





#### Как убрать из URL страницы знак вопроса?



Для этого необходимо выполнить следующие шаги:



- создать в каталоге `/news/` файл **.htaccess** со следующим содержимым:
  ```
  ErrorDocument 404 /news/404.php
  ```
- создать в каталоге `/news/` файл **404.php** со следующим содержимым:
  ```
  <?
  $arrPath = pathinfo($_SERVER["REQUEST_URI"]);
  function initialize_params($url)
  {
  if (strpos($url,"?")>0)
  {
  $par = substr($url,strpos($url,"?")+1,strlen($url));
  $arr = explode("#",$par);
  $par = $arr[0];
  $arr1 = explode("&",$par);
  foreach ($arr1 as $pair)
  {
  $arr2 = explode("=",$pair);
  global $$arr2[0];
  $$arr2[0] = $arr2[1];
  }
  }
  }
  initialize_params($_SERVER["REQUEST_URI"]);
  require($_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/main/include/prolog_before.php");
  $arr = explode("?",$arrPath["basename"]);
  $fname = $arr[0];
  if (strlen(trim($arrPath["extension"]))>0)
  {
  $arr = explode(".",$fname);
  $NEWS_ID = intval($arr[0]);
  if ($NEWS_ID>0)
  {
  $ID = $NEWS_ID;
  $APPLICATION->SetTitle("News Details");
  $sapi = php_sapi_name();
  if ($sapi=="cgi") header("Status: 200 OK"); else header("HTTP/1.1 200 OK");
  require_once($_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/iblock/iblock.php");
  CIblock::ShowPanel($IBLOCK_ID, $ID);
  include($_SERVER["DOCUMENT_ROOT"]."/bitrix/php_interface/include/news/news_detail.php"); // интерфейсный скрипт, который вызывается
                                                                                          //и в /news/detail.php
  }
  }
  require($_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/main/include/epilog.php");
  ?>
  ```
