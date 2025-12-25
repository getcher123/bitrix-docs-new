# Правила форматирования CSS

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2506 — Правила оформления CSS](lesson_2506.md)
- [Следующий: 2508 — Тестирование верстки (чеклист) →](lesson_2508.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2507

- При создании правила для нескольких селекторов помещайте каждый селектор на отдельной строке.
- Перед открывающей скобкой ставьте один пробел.
- Внутри блока объявлений помещайте каждое объявление на отдельной строке.
- Добавляйте один уровень отступов перед каждым объявлением.
- Ставьте пробел после двоеточия внутри объявления.
- Всегда ставьте точку с запятой после последнего объявления в блоке.
- Ставьте закрывающую скобку на одной вертикальной линии с первым символом в селекторе.
- Ставьте пробел после каждой запятой в объявлениях со множественным значением.
- Разделяйте правила пустой строкой.
- Сортируйте свойства по принципу: свойства, сильно влияющие на элемент, в начале, а самые незначительно влияющие - в конце:
  Плохо:
  ```
      .crm-lead-form { margin: 34px; color: #000; }
      .crm-lead-title, .crm-invoice-title, .crm-company-title
      {
          position: relative;
          background: #000;
          height: 15px;
          padding: 10px;
          border: 1px solid red;
          margin: 12px 0 17px;
          display: block;
          color: #fff;
          width: 15px;
      }
  ```
      Хорошо:
  ```
  	.crm-lead-form {
  		margin: 34px;
  		color: #000;
      }
  	.crm-lead-title,
  	.crm-invoice-title,
  	.crm-company-title {
  		display: block;
  		position: relative;
  		width: 15px;
  		height: 15px;
  		padding: 10px;
  		border: 1px solid red;
  		margin: 12px 0 17px;
  		color: #fff;
  		background: #000;
  	}
  ```

  - `Display`
  - Позиционирование (`position`/float)
  - Боксовая модель (`width`/`height`/`margin`/`padding`/`border`/`box-sizing`)
  - Цвета и типографика
  - Остальное
- Для значений с пробелами (`font-family`, `url()`) и для свойства **content** используйте двойные кавычки.
  ```
  	.disk-user-profile {
  		font-family: "Helvetica Neue Light", Helvetica, Arial, sans-serif;
  	}
  	.disk-user-profile:after {
  		display: block;
  		content: "";
  	}
  ```
- Исключения
  К большим группам правил, состоящих из одного свойства, может применяться запись в одну строку. В таком случае следует ставить пробел после открывающей и перед закрывающей скобками.
  ```
  	.crm-column-title { width: 10%; }
  	.crm-column-author { width: 20%; }
  	.crm-column-actions { width: 30%; }
  	.menu-icon-create { background-position: 0 0; }
  	.menu-icon-delete { background-position: -15px -35px; }
  	.menu-icon-approve { background-position: -34px -35px; }
  ```
  Длинные значения свойств, разделяемые запятыми - как, например, набор градиентов или теней - могут быть помещены на отдельной строке каждое, чтобы повысить читабельность кода и сообщений в системе управления версиями. Формат записи может слегка различаться, один из вариантов приведён ниже.
  ```
  	.disk-info-popup {
  		box-shadow:
  			1px 1px 1px #000,
  			2px 2px 1px 1px #ccc inset;
  		background-image:
  			linear-gradient(#fff, #ccc),
  			linear-gradient(#f3c, #4ec);
  	}
  ```
