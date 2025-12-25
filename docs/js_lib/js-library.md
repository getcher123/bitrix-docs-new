# Сторонние библиотеки

Кроме собственной JS-библиотеки в Bitrix Framework используются включённые в продукт сторонние прориентарные библиотеки:


### amCharts

[Библиотека](https://www.amcharts.com/) для построения различных графиков, лицензия на которую включена 1С-Битрикс любой редакции.

Подключение библиотеки amCharts осуществляется стандартным способом:


```
CJSCore::Init(['amcharts']);
```

Подключать библиотеку необходимо в зависимости от типа графика:


```
amcharts - Базовая библиотека
amcharts_funnel – Воронка, пирамида Маслоу
amcharts_gauge – Диаграмма в виде спидометра
amcharts_pie – Круговая диаграмма
amcharts_radar – Радарная диаграмма
amcharts_serial – Обычные графики
amcharts_xy – График XY
```


---
### MaskedInput

Библиотека для указания масок ввода, альтернатива **jquery.maskedinput**.


```
<?php

CJSCore::Init(['masked_input']);
?>

<input type="text" id="phone" placeholder="Укажите ваш телефон" />

<script>
	BX.ready(function() {
		var result = new BX.MaskedInput({
			mask: '+7 999 999 99 99', // устанавливаем маску
			input: BX('phone'),
			placeholder: '_' // символ замены +7 ___ ___ __ __
		});

		result.setValue('9000000000'); // устанавливаем значение
	});
</script>
```


---
### PhoneNumber

Для масок телефонного номера используйте библиотеку **phone_number**.


```
<?php

CJSCore::Init(['phone_number']);
?>

<span id="flag"></span>
<input type="text" id="number" placeholder="Укажите ваш телефон" />

<script>
	BX.ready(function() {
		new BX.PhoneNumber.Input({
			node: BX('number'),
			flagNode: BX('flag'), //
			flagSize: 16, // Размер флага [16, 24, 32]
			defaultCountry: 'ru', // Страна по-умолчанию
			onChange: function(e) {
				// вызывается при изменении значения
			}
		});
	});
</script>
```

---
