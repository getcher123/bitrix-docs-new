# Практика. Взаимодействие с контроллерами из Javascript

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 21160 — Практика. Советы](lesson_21160.md)
- [Следующий: 2692 — Практика. Постраничная навигация →](lesson_2692.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2192

Как в AJAX-действии использовать параметры компонента?

Часто бывает, что необходимо в аякс-запросе получить у компонента те же параметры, которые были при его отображении на странице.

- Нужно описать те параметры, которые нужно использовать в методе listKeysSignedParameters
  ```
        class ExampleComponent extends \CBitrixComponent implements \Bitrix\Main\Engine\Contract\Controllerable
        {
        	protected function listKeysSignedParameters()
        	{
        		//перечисляем те имена параметров, которые нужно использовать в аякс-действиях
        		return [
        			'STORAGE_ID',
        			'PATH_TO_SOME_ENTITY',
        		];
        	}
  ```
- Получить подписанные параметры в шаблоне и, например, передать в ваш js класс компонента
  ```
        <!--template.php-->
        <script type="text/javascript">
        	new BX.ExampleComponent({
        		signedParameters: '<?= $this->getComponent()->getSignedParameters() ?>',
        		componentName: '<?= $this->getComponent()->getName() ?>'
        	});
        </script>
  ```
- Вызывать *BX.ajax.runComponentAction* (как в примерах) c параметром **signedParameters**.
  ```
        BX.ajax.runComponentAction(this.componentName, action, {
        	mode: 'class',
        	signedParameters: this.signedParameters, //вот способ для передачи параметров компоненту.
        	data: data
        }).then(function (response) {
        	//some work
        });
  ```

В итоге в вашем аякс-действии можно использовать параметры STORAGE_ID, PATH_TO_SOME_ENTITY. При этом параметры подписаны и целостность контролируется ядром.

Если необходимо работать с подписанными параметрам внутри **ajax.php**, то используйте внутри действия контроллера метод *Controller::getUnsignedParameters()*, в нём будет массив распакованных данных.

|  |
| --- |

#### Дополнительно

- [Аякс-запрос из JavaScript'a к этому компоненту](https://dev.1c-bitrix.ru/api_help/js_lib/ajax/bx_ajax_runaction.php)
