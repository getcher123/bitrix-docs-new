# Модификация простого компонента в составе сложного

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2304 — Простой пример кастомизации компонента](lesson_2304.md)
- [Следующий: 4880 — Тип параметров CUSTOM →](lesson_4880.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2900

При работе с комплексным компонентом можно модифицировать один или несколько простых компонентов, а остальные остаются стандартные.

Например, необходимо в компоненте **socialnetwork.user_groups**, который в составе комплексного компонента **socialnetwork_group** выводит список групп, увеличить длину выводимого описания группы с 50 до 100 символов (специально выберем простую модификацию чтобы акцентировать внимание на самом процессе).

- Скопируйте шаблон комплексного компонента.
  Теперь в шаблоне сайта имеем шаблон комплексного компонента, перейдя в который увидим большой набор файлов в папке `/local/templates/<шаблон сайта>/components/bitrix/socialnetwork_group/.default`.
  Каждый из файлов вызывается на определённой странице социальной сети и подключает требуемые простые компоненты.
  Теперь надо найти файл, который подключает тот компонент, который нужно изменить. В нашем случае это **index.php.**
  Остальные файлы в шаблоне комплексного компонента, расположенного в шаблоне сайта, можно удалить. Комплексный компонент будет подключать эти файлы из ядра. А значит, они будут обновляться.
- Теперь в оставшемся файле заменяем
  ```
  $APPLICATION->IncludeComponent(
              "bitrix:socialnetwork.user_groups",
  ```
  на
  ```
  $APPLICATION->IncludeComponent(
              "custom:socialnetwork.user_groups",
  ```
- Копируем папку `/bitrix/components/bitrix/socialnetwork.user_groups` в `/local/components/custom/socialnetwork.user_groups`.
- в файле `/local/components/custom/socialnetwork.user_groups/component.php` заменяем
  ```
  "GROUP_DESCRIPTION" => (strlen($arGroup["DESCRIPTION"]) > 50 ? substr($arGroup["DESCRIPTION"], 0, 50)."..." : $arGroup["DESCRIPTION"]),
  ```
  на
  ```
  "GROUP_DESCRIPTION" => (strlen($arGroup["DESCRIPTION"]) > 100 ? substr($arGroup["DESCRIPTION"], 0, 100)."..." : $arGroup["DESCRIPTION"]),
  ```



Теперь весь функционал социальной сети остаётся стандартный, кроме компонента **socialnetwork.user_groups**.
