# Реестр печатных форм

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 25862 — Битрикс поиск](lesson_25862.md)
- [Следующий: 25868 — 1СПАРК риски →](lesson_25868.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=25866

Сервис позволяет загружать сохраненные печатные формы *1С* из реестра документов *1С* в таймлайн сущностей *Битрикс24*. Сервис удобен, когда менеджеру *Битрикс24* нужна печатная форма *1С*, но доступа в *1С* нет. Сервис включен в подсистему интеграции сервисов и включается в её настройках.



Раздел Битрикс24 &gt; Настройки интеграции сервисов


 ![reestr1.png](../../../images/courses/48/dev.1c-bitrix.ru/upload/medialibrary/d32/n4rz89b0u889mwnx2ksreke4cdl9kh5h/reestr1.png)

Для корректной работы сервиса должно быть запущено подключение к *Битрикс24* (в разделе «1С + CRM Битрикс24»

			желтый фон

                    ![poisk1.png](../../../images/courses/48/dev.1c-bitrix.ru/upload/medialibrary/9b2/g2vdcbda8endz7jfzalk6twqlpi6t8ay/poisk1.png)

		 у настройки подключения).



Добавить печатную форму в реестр можно с помощью кнопки «В реестр» на форме печати документов.


 ![reestr2.png](../../../images/courses/48/dev.1c-bitrix.ru/upload/medialibrary/0e7/koqxjr2tudpgj0fvgupdiqd83raez572/reestr2.png)

Кнопка доступна только на универсальной печатной форме печати документов, поэтому если у печатной формы индивидуальная форма печати – кнопки не будет (в первую очередь это замечание относится к конфигурации **Бухгалтерия предприятия**.)



После нажатия на кнопку печатная форма попадает в

			реестр документов *1С*

                    ![reestr3.png](../../../images/courses/48/dev.1c-bitrix.ru/upload/medialibrary/0a0/6zqnu1l5f8000l0emznr49x8dv3nw61r/reestr3.png)

		, откуда ее можно "подтянуть" в *Битрикс24*.



В карточке Компании/Контакта/Лида/Сделки в выпадающем меню настройки подключения нажимается пункт

			Реестр документов 1С

                    ![reestr4.png](../../../images/courses/48/dev.1c-bitrix.ru/upload/medialibrary/7b7/pr3b2k1tcrtyzrec1e964c0goyxs0oei/reestr4.png)

		, выбирается нужный документ реестра и нажимается кнопка «Сохранить».



Документ

			сохраняется

                    ![reestr5.png](../../../images/courses/48/dev.1c-bitrix.ru/upload/medialibrary/b39/zq6eged235y4y05cyhvug3v409qub1f1/reestr5.png)

		 в таймлайне, откуда его можно

			открыть или переслать

                    ![reestr6.png](../../../images/courses/48/dev.1c-bitrix.ru/upload/medialibrary/56c/gp1yr8i25hnhy8l8p6pt6d2hld985e3l/reestr6.png)

		.
