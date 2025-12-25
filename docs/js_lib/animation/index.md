# Анимация


### Описание и методы

Класс **BX.easing** позволяет создавать анимацию на странице. Анимация в контексте веб-страницы - это изменение стиля DOM-элемента.

Перед использованием методов класса BX.easing необходимо подключить расширение **core_fx.js**.


```
CJSCore::Init(array("fx"));
```


| Метод | Описание | С версии |
| --- | --- | --- |
| BX.easing | Конструктор. | 12.5 |
| BX.easing.prototype.animate | Запускает анимацию. | 12.5 |
| BX.easing.prototype.animateProgress | Редко используемый метод. Запускает анимацию, но на каждой итерации вместо функции-обработчика **step**, вызывается функция-обработчик **progress**. | 12.5 |
| BX.easing.prototype.stop(completed) | Останавливает анимацию на текущем шаге. Если completed=true, то дополнительно выполнится функция-обработчик окончания анимации. | 12.5 |
| Анимационные функции | Функции, которые позволяют делать различного вида плавные анимации. | 12.5 |

---
### Пример использования


```
var banner = BX("my-banner");
var easing = new BX.easing({
	duration : 500,
	start : { height : 0, opacity : 0 },
	finish : { height : 100, opacity: 100 },
	transition : BX.easing.transitions.quart,
	step : function(state){
		banner.style.height = state.height + "px";
		banner.style.opacity = state.opacity/100;
	},
	complete : function() {
		banner.style.display = "none";
	}
});
easing.animate();
```

---
