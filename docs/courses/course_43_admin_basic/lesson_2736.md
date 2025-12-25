# Пример. Внешние файлы css

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2895 — Пример. Добавление типа отсутствия](lesson_2895.md)
- [Следующий: 4881 — Пример. Редактирование шаблона меню →](lesson_4881.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2736

С версии 15.5.1 появилась штатная поддержка вызова стороннего файла **css**. Под сторонним файлом понимается как локальный файл вне компонента так и файл на внешнем домене.

Для подключения такого файла в **template.php** необходимо прописать:

```
$this->addExternalCss("/local/styles.css");
$this->addExternalJS("/local/liba.js");
```

## До версии 15.5.1

Системной поддержки такой потребности "из коробки" не существовало. Задача решалась одним из трёх способов:

1. Подключение инлайном:
  ```
  <link href="/local/styles.css" type="text/css" rel="stylesheet" />
  ```
2. Код в самом компоненте:
  ```
  $APPLICATION->SetAdditionalCss("/local/styles.css");
  ```
3. Код в файле **component_epilog.php**:
  ```
  <?if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();
  global $APPLICATION;
  $APPLICATION->SetAdditionalCss("/local/styles.css");
  ```
