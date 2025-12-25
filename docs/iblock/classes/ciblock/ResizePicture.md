# ResizePicture


### Описание


```
array
CIBlock::ResizePicture(
	array arFile,
	array arResize
);
```

Метод выполняет масштабирование файла. Метод статический.

**Примечание**: обрабатываются только файлы JPEG, GIF и PNG (зависит от используемой библиотеки GD). Файл указанный в параметре arFile будет перезаписан.



#### Возвращаемое значение

Массив описывающий файл или строка с сообщением об ошибке.


#### Смотрите также


- CFile::MakeFileArray
- [CIBlock::SetFields](SetFields.md)

---
### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arFile | Массив, описывающий файл. Это может быть элемент массива $_FILES[имя] (или $HTTP_POST_FILES[имя]), а также результат метода CFile::MakeFileArray. С версии модуля **14.0.0** массив файла передается в ключе *VALUE*, а описание - в ключе *DESCRIPTION*. |
| arResize | Массив параметров масштабирования. Содержит следующие ключи: - WIDTH - целое число. Размер картинки будет изменен таким образом, что ее ширина не будет превышать значения этого поля. - HEIGHT - целое число. Размер картинки будет изменен таким образом, что ее высота не будет превышать значения этого поля. - METHOD - возможные значения: resample или пусто. Значение поля равное "resample" приведет к использованию функции масштабирования imagecopyresampled, а не imagecopyresized. Это более качественный метод, но требует больше серверных ресурсов. - COMPRESSION - целое от 0 до 100. Если значение больше 0, то для изображений jpeg оно будет использовано как параметр компрессии. 100 соответствует наилучшему качеству при большем размере файла. Параметры METHOD и COMPRESSION применяются только если происходит изменение размера. Если картинка вписывается в ограничения WIDTH и HEIGHT, то никаких действий над файлом выполнено не будет. |

---
### Примеры использования


```
<?
AddEventHandler("iblock", "OnBeforeIBlockElementAdd", Array("MyHandlers", "ResizeElementProperty"));
AddEventHandler("iblock", "OnBeforeIBlockElementUpdate", Array("MyHandlers", "ResizeElementProperty"));
class MyHandlers
{
	public static function ResizeElementProperty(&$arFields)
	{
		global $APPLICATION;
		//Код инфоблока, свойство которого нуждается в масштабировании
		$IBLOCK_ID = 1;
		//Идентификатор свойства
		$PROPERTY_ID = 15;
		//Наш инфоблок и значения свойства в наличии
		if(
			$arFields["IBLOCK_ID"] == $IBLOCK_ID
			&& is_array($arFields["PROPERTY_VALUES"])
			&& array_key_exists(15, $arFields["PROPERTY_VALUES"])
		)
		{
			foreach($arFields["PROPERTY_VALUES"][$PROPERTY_ID] as $key => $arFile)
			{
				//Изменяем размеры картинки
				$arNewFile = CIBlock::ResizePicture($arFile, array(
					"WIDTH" => 100,
					"HEIGHT" => 100,
					"METHOD" => "resample",
				));
				if(is_array($arNewFile))
					$arFields["PROPERTY_VALUES"][$PROPERTY_ID][$key] = $arNewFile;
				else
				{
					//Можно вернуть ошибку
					$APPLICATION->throwException("Ошибка масштабирования изображения в свойстве \"Файлы\":".$arNewFile);
					return false;
				}
			}
		}
	}
}
?>
```

---
