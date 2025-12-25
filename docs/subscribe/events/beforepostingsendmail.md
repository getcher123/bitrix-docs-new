# BeforePostingSendMail


### Описание и параметры


```
функция-обработчик(
	array arFields
);
```

Событие "BeforePostingSendMail" вызывается перед отправкой выпуска из метода CPosting::SendMessage.
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arFields* | Массив следующего содержания: - POSTING_ID - идентификатор выпуска. - EMAIL - адрес на который будет отправлен выпуск. - SUBJECT - заголовок письма (в кодированном виде, если установлена соответсветствующая настройка модуля). - BODY - тело письма уже отформатированное в соответствии со стандартом MIME. - HEADER - служебные заголовки. - EMAIL_EX - расширенная информация о получателе, см. Поля CPosting. |

Данный обработчик должен вернуть массив аналогичного содержания. Этот массив будет передан в качестве аргумента следующему обработчику. Проверка целостности результата обработчика в модуле не производится.

Если обработчик вернет не массив, то отправка письма выполняться не будет. Однако в случае возврата false письмо будет считаться не отправленным, иначе отправка будет отмечена как успешная.

---
### Смотрите также


- CPosting::SendMessage
- **Обработка событий**

---
### Пример функции-обработчика


```
<?// файл /bitrix/php_interface/init.php// регистрируем обработчикAddEventHandler("subscribe", "BeforePostingSendMail", Array("MyClass", "BeforePostingSendMailHandler"));
class MyClass
{
	// создаем обработчик события "BeforePostingSendMail"
	public static function BeforePostingSendMailHandler($arFields)
	{
		$USER_NAME = "Подписчик";
		//Попробуем найти подписчика.
		$rs = CSubscription::GetByEmail($arFields["EMAIL"]);
		if($ar = $rs->Fetch())
		{
			if(intval($ar["USER_ID"]) > 0)
			{
				$rsUser = CUser::GetByID($ar["USER_ID"]);
				if($arUser = $rsUser->Fetch())
				{
					$USER_NAME = $arUser["NAME"]." ".$arUser["LAST_NAME"];
				}
			}
		}
		$arFields["BODY"] = str_replace("#NAME#", $USER_NAME, $arFields["BODY"]);		return $arFields;	}}?>
```

---
