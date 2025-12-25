# Создание шаблона формы

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5309 — Настройка статусов](lesson_5309.md)
- [Следующий: 5311 — Почтовый шаблон →](lesson_5311.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=5310

|  | #### Как будет выглядеть ваша форма |
| --- | --- |




Внешний вид формы добавления нового вопроса в систему **Вопрос-ответ** зависит от того, как вы [настроите шаблон](lesson_2928.md) веб-формы. Пусть шаблон выглядит, например, так:




![](../../../images/courses/48/dev.1c-bitrix.ru/images/admin_expert/ques_answer/form_pub.png)




На закладке **Шаблон формы** в визуальном редакторе добавьте элемент Название формы, а под ним задайте таблицу из 2-х столбцов и 5-и строк. В строках разместите элементы: Название вопроса (первый столбец) и сам вопрос (второй столбец). В последней строке разместите элементы для вывода CAPTCHA:




![](../../../images/courses/48/dev.1c-bitrix.ru/images/admin_expert/ques_answer/form_template1.png)




Всё, шаблон готов.







## Для любопытных: HTML-код формы выглядит так

В редакторе Вы можете переключиться в режим редактирования исходного кода (вторая кнопка на панели слева) и вставить туда указанный ниже код.


```


 <?=$FORM->ShowFormErrors()?>
<table width="323" height="257" class="data-table">
  <tbody>
    <tr><td valign="middle" align="right"><?=$FORM->ShowInputCaption("name","")?></td><td><?=$FORM->ShowInput('name')?></td></tr>
    <tr><td valign="middle" align="right"><?=$FORM->ShowInputCaption("email","")?></td><td><?=$FORM->ShowInput('email')?></td></tr>
    <tr><td valign="middle" align="right"><?=$FORM->ShowInputCaption("phone","")?></td><td><?=$FORM->ShowInput('phone')?></td></tr>
    <tr><td valign="top" align="right"><?=$FORM->ShowInputCaption("text","")?></td> <td><?=$FORM->ShowInput('text')?></td></tr>
    <tr><td><?=$FORM->ShowCaptchaImage()?></td><td> Введите символы с картинки <?=$FORM->ShowRequired()?>
        <br />
       <?=$FORM->ShowCaptchaField()?></td></tr>
    <tr><td colspan="2"><?=$FORM->ShowSubmitButton("","")?></td></tr>
   </tbody>
 </table>


```
