# Получение суммы значений полей связанных инфоблоков

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5744 — Копирование значений полей элементов в свойства](lesson_5744.md)
- [Следующий: 3484 — Вывод свойств элемента инфоблока →](lesson_3484.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=5761

Допустим, что у нас имеются связанные инфоблоки и поставлена следующая **задача**: необходимо в специальном поле элемента инфоблока получить сумму значений полей связанных элементов.

**Решение** возможно как с использованием модуля **Интернет-магазин**, так и без него. При использовании интернет-магазина все инфоблоки должны иметь свойства торгового каталога с указанием цены в соответствующих полях.
Если используется редакция без интернет-магазина, то все поля исходных инфоблоков должны иметь тип число и (в рамках данного решения) иметь код **PRICE**.

Пусть поле результирующего инфоблока называется **COST**. Его тип должен быть - число. В поле "Значение по умолчанию" параметра **COST** должно быть внесено выражение типа:

- {PROP_1_PRICE}+{PROP_2_PRICE}+... - для редакций с Интернет-магазином.
- {PROP_1} + {PROP_2}+... - для редакций без Интернет- магазина.

Код ниже приведен для вывода результата в компоненте **catalog.section**. Для вывода результатов в другом компоненте требуется модификация кода. Приведенный код вносится в файл **result_modifer.php** указанного компонента:

```

<?
//Эту строчку можно раскомментировать и посмотреть содержимое arResult
//того компонента под который будет адаптирован этот модификатор
//echo "<pre>",htmlspecialchars(print_r($arResult, 1)),"</pre>";

//Символьный код свойства значение по умолчанию которого содержит выражения
//результат вычисления будет показан шаблоном компонента
//Само выражение представляет собой исполняемый eval'ом PHP код
//в котором по шаблонам вида {<СИМВОЛЬНЫЙ КОД СВОЙСТВА>} будут подставлены конкретные значения
//Эти свойства должны быть выбраны в настройках компонента и доступны через arResult
//в противном случае надо воспользоваться функцией CIBlockElement::GetProperty для доступа к БД
//Эти свойства должны быть НЕ множественными
//Пример выражения: "({PROP_1_PRICE} + {PROP_2_PRICE}) * {PROP_COUNTER}"
//Обратите внимание на _PRICE - это указание на необходимость выборки цены привязанного элемента!
   //Само свойство должно иметь символьный код PROP_1 и PROP_2 соответственно

$CALCULATOR_CODE="COST";
//ИД цены которая будет браться для вычислений
$PRICE_ID = 1;
//Идентификатор инфоблока (для разных компонент надо брать разные поля arResult)
$IBLOCK_ID = $arResult["IBLOCK_ID"];
//Получаем метаданные свойства "Калькулятора"
$arProperty = CIBlockProperty::GetPropertyArray($CALCULATOR_CODE, $IBLOCK_ID);
//Если такое свойство есть и у него задано выражение для вычислений:
if($arProperty && strlen($arProperty["DEFAULT_VALUE"]) > 0)
{
	//Цикл по всем элементам каталога
	foreach($arResult["ITEMS"] as $i => $arElement)
	{
		//Берем выражение "Калькулятора"
		$EQUATION = $arProperty["DEFAULT_VALUE"];
		//Проверим надо ли выполнять подстановку шаблонов
		if(preg_match_all("/(\\{.*?\\})/", $EQUATION, $arMatch))
		{
			//Цикл по всем использованным в выражении свойствам
			$arPropCodes = array();
			foreach($arMatch[0] as $equation_code)
			{
				//Это "цена" и она потребует больших усилий
				$bPrice = substr($equation_code, -7)=="_PRICE}";
				//Символьный код свойства значение которого будет подставлено в выражение
				$property_code = ($bPrice? substr($equation_code, 1, -7): substr($equation_code, 1, -1));
				if($bPrice)
				{
					//Находим связанный элемент
					$rsLinkedElement = CIBlockElement::GetList(
						array(),
						array(
							"=ID" => $arElement["PROPERTIES"][$property_code]["~VALUE"],
							"IBLOCK_ID" => $arElement["PROPERTIES"][$property_code]["~LINK_IBLOCK_ID"]
						),
						false, false,
						array(
							"ID", "IBLOCK_ID", "CATALOG_GROUP_".$PRICE_ID, "PROPERTY_PRICE"
						)
					);
					$arLinkedElement = $rsLinkedElement->Fetch();
					//Забираем его цену
					if($arLinkedElement["CATALOG_PRICE_".$PRICE_ID])
						$value = doubleval($arLinkedElement["CATALOG_PRICE_".$PRICE_ID]);
					else
						$value = doubleval($arLinkedElement["PROPERTY_PRICE_VALUE"]);
				}
				else
				{
					//Если вам потребуются не только числа, но и строки
					//избавьтесь от doubleval и добавьте экранирование строковых символов
					$value = doubleval($arElement["PROPERTIES"][$property_code]["~VALUE"]);
				}
				//Подстановка значения
				$EQUATION = str_replace($equation_code, $value, $EQUATION);
			}

		}
		//Собственно вычисление
		$VALUE = @eval("return ".$EQUATION.";");
		//и сохрание его результата для показа в шаблоне
		$arResult["ITEMS"][$i]["DISPLAY_PROPERTIES"][$CALCULATOR_CODE] = $arResult["ITEMS"][$i]["PROPERTIES"][$CALCULATOR_CODE];
		$arResult["ITEMS"][$i]["DISPLAY_PROPERTIES"][$CALCULATOR_CODE]["DISPLAY_VALUE"] = htmlspecialchars($VALUE);
	}
}
?>
```
