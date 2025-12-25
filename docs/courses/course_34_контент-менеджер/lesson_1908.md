# Приложения для публикации в блог

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8635 — Список стикеров](lesson_8635.md)
- [Следующий: 12998 — Основные задачи менеджера интернет-магазина →](lesson_12998.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=34&LESSON_ID=1908

Для управления сообщениями блога можно использовать любые текстовые редакторы, поддерживающие

			MetaWeblog API

                    **MetaWeblog API (MWA)** является интерфейсом, который позволяет внешним программам управлять сообщениями в блоге. Интерфейс построен на XML-RPC протоколе.

		.




Использование MetaWeblog API предоставляет следующие возможности:



- Управление сообщениями блога одного или нескольких сайтов из blog-клиента или текстового редактора (большинство поддерживают **MetaWeblog API**).
- Возможность добавить свой функционал (который будет управлять вашими сайтами), не вдаваясь в логику работы продуктов "1С-Битрикс", а используя **MetaWeblog API**.


<!-- В курсе будет рассмотрена настройка таких редакторов на блоги сайта на примере программы &lt;b&gt;MS Word&lt;/b&gt;.

&lt;p&gt;Описанные методы публикаций можно использовать как для сайтов, созданных на платформе PHP, так и для сайтов, созданных на платформе ASP.NET.&lt;/p&gt; -->





Например:



| Windows Live Writer<br>10 января 2017 г. поддержка Windows Essentials 2012 и всех её приложений, включая **Windows Live Writer**, прекращена. Программное обеспечение больше не доступно для загрузки у Microsoft.<br>Выпущено ответвление Windows Live Writer с открытым исходным кодом под названием [Open Live Writer](https://www.microsoft.com/ru-ru/p/open-live-writer/9nblggh5279m#activetab=pivot:overviewtab). | [Semagic](http://semagic.sourceforge.net/index.html) | [BlogJet](http://www.codingrobots.com/blogjet/) | [Post2Blog](http://www.post2blog.com) |
| --- | --- | --- | --- |
| [W.bloggar](http://www.wbloggar.com/) | [Wordpress](http://ru.wordpress.org/) | [Zoundry Raven](http://www.zoundry.com/) | [BlogDesk](http://www.blogdesk.org/en/index.htm) |
| [Thingamablog](http://www.thingamablog.com/) | [Alive Diary](http://www.vitolab.com/products.htm/10) | [ScribeFire](http://www.scribefire.com/) | [WB Editor](http://www.wbeditor.com/) |
| [Flock](http://flock.com/) | [RocketPost2](http://www.anconia.com/rocketpost/) |  |  |



<!-- &lt;td&gt;LJ.NET&lt;/td&gt; -->

<!-- &lt;td&gt;Bleezer&lt;/td&gt; -->

<!-- &lt;td&gt;Ecto&lt;/td&gt; -->

<!-- &lt;td&gt;Deepest Sender&lt;/td&gt; -->

<!-- &lt;td&gt;QTM&lt;/td&gt; -->


<!-- &lt;p&gt;Детали настройки данных программных продуктов могут отличаться от настройки MS Word, но их принципы аналогичны.&lt;/p&gt; -->



#### Примечания




Следует отметить некоторые моменты, которые необходимо учитывать в процессе настройки:




- При публикации записи блога осуществляется авторизация пользователя. Если при авторизации осуществляется
  			редирект
                      Редирект  – это автоматическая переадресация посетителя с одного URL-адреса на другой.
  		 или другие действия, использование **MetaWeblog** на данный момент невозможно.
- Для загрузки в блог картинок и видео необходимо использовать **File Transfer Protocol (FTP)**.
