# Имена HTML полей веб-форм


### Вопросы веб-формы

При выводе веб-формы все [ответы](terms.md#answer) на [вопросы](terms.md#question) представляются в виде HTML полей, заполняя которые, пользователи отвечают на тот или иной вопрос. Ниже представлена таблица зависимости имен HTML-полей от типов ответов.


| Тип ответа | Описание | Имя HTML поля | Значение ответа |
| --- | --- | --- | --- |
| text | Однострочное текстовое поле. | form_text_*answer_id* | Текст, введенный с клавиатуры. |
| textarea | Многострочное текстовое поле. | form_textarea_*answer_id* | Текст, введенный с клавиатуры. |
| password | Однострочное текстовое поле для ввода пароля. | form_password_*answer_id* | Текст, введенный с клавиатуры. |
| date | Однострочное текстовое поле для ввода даты. | form_date_*answer_id* | Текст, введенный с клавиатуры. |
| radio | Переключатель одиночного выбора. | form_radio_*question_sid* | ID выбранного ответа. |
| dropdown | Выпадающий список одиночного выбора. | form_dropdown_*question_sid* | ID выбранного ответа. |
| checkbox | Флаг множественного выбора. | form_checkbox_*question_sid*[] | Массив ID выбранных ответов. |
| multiselect | Список множественного выбора. | form_multiselect_*question_sid*[] | Массив ID выбранных ответов. |
| file | Поле для ввода произвольного файла. | form_file_*answer_id* | Массив, описывающий загруженный файл. |
| image | Поле для ввода изображения. | form_image_*answer_id* | Массив, описывающий загруженный файл. |
| hidden ***** | Скрытое поле. | form_hidden_*answer_id* | Данные из скрытого поля формы. |
| ***** - доступно только для упрощенного режима редактирования веб-форм |  |  |  |


###### Принятые обозначения


- *answer_id* - ID [ответа](terms.md#answer); *question_sid*- символьный идентификатор [вопроса](terms.md#question).

---
### Поля веб-формы

Помимо ответов на вопросы веб-формы, необходимо выводить и редактировать значения [полей](terms.md#field) веб-формы. Ниже представлена таблица зависимости имен HTML полей от типов поля веб-формы.


| Тип поля | Описание | Имя HTML поля | Значение |
| --- | --- | --- | --- |
| text | Текст | form_textarea_ADDITIONAL_*field_id* | Текст, введенный с клавиатуры. |
| integer | Число | form_text_ADDITIONAL_*field_id* | Текст, введенный с клавиатуры. |
| date | Дата | form_date_ADDITIONAL_*field_id* | Текст, введенный с клавиатуры. |


###### Принятые обозначения


- *field_id* - ID [поля](terms.md#field) веб-формы.

---
### Смотрите также


- CForm::GetTextField CForm::GetTextAreaFieldCForm::GetPasswordFieldCForm::GetDateFieldCForm::GetRadioFieldCForm::GetCheckBoxFieldCForm::GetDropDownFieldCForm::GetMultiSelectFieldCForm::GetFileFieldCFormResult::GetDataByIDForHTML

---
