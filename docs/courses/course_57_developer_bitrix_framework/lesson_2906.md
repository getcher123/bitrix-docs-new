# Вывод в лог

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2905 — Как запустить из одного бизнес процесса другой?](lesson_2905.md)
- [Следующий: 2907 — Вывод в лог. Переменные →](lesson_2907.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=57&LESSON_ID=2906

|  | ### Сделаем вывод любых сообщений в лог |
| --- | --- |




Если разработчик поддастся желанию использовать в полную силу функционал бизнес-процессов, то ему потребуются дополнительные возможности функционала. Например, вывод любых сообщений в

			лог бизнес-процесса

                    При разработке и использовании уже готовых процессов бывает необходимо узнать подробности выполнения того или иного процесса / действия. Для этого в системе предусмотрен журнал выполнения бизнес-процессов (лог).

[Подробнее](lesson_3837.md)...

		.




Допустим, используется определение руководителя из предыдущего примера или просто необходимо вывести в лог текст заявки.



Есть два варианта решения: просто вывод в лог из действия PHP код или создание собственного действия Запись в лог. Рассмотрим оба варианта.




#### PHP код




Допустим, что при создании бизнес-процесса пользователь вводит текст какой-то заявки, который сохраняется в переменной `Text`.
Чтобы вывести в лог значение этой переменной нужно просто в действии **PHP код** добавить вызов:



```
$rootActivity = $this->GetRootActivity();
$this->WriteToTrackingService($rootActivity->GetVariable("Text"));

Или же просто вывести тестовое сообщение:
$this->WriteToTrackingService("Это тест");
```




#### Создание действия



Создайте недостающие папки относительно корня сайта:




- `bitrix\activities\custom`
- `bitrix\activities\custom\logactivity`
- `bitrix\activities\custom\logactivity\lang\ru`




В папке `/logactivity/` создайте файлы:



- **logactivity.php**
  ```
  <?
  if (!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();
  class CBPLogActivity
     extends CBPActivity
  {
     public function __construct($name)
     {
        parent::__construct($name);
        $this->arProperties = array(
           "Title" => "",
        );
     }
     public function Execute()
     {
        $rootActivity = $this->GetRootActivity();
        $this->WriteToTrackingService($rootActivity->GetVariable("Text"));
        return CBPActivityExecutionStatus::Closed;
     }
  }
  ?>
  ```
- **.description.php**
  ```
  <?
  if (!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();
  $arActivityDescription = array(
     "NAME" => GetMessage("BPMA_DESCR_NAME"),
     "DESCRIPTION" => GetMessage("BPMA_DESCR_DESCR"),
     "TYPE" => "activity",
     "CLASS" => "LogActivity",
     "JSCLASS" => "BizProcActivity",
     "CATEGORY" => array(
        "ID" => "other",
     ),
  );
  ?>
  ```




Создайте файл `logactivity\lang\ru\.description.php`:



```
<?
$MESS ['BPMA_DESCR_NAME'] = "Запись в лог";
$MESS ['BPMA_DESCR_DESCR'] = "Запись сообщения в лог";
?>
```




Теперь в дизайнере бизнес-процесов появилось новое действие **Запись в лог** в разделе **Прочее** и действие просто записывает в лог значение переменной `Text`.
