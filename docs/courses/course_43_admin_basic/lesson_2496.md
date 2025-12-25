# Пример работы с БД

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 9221 — Балансировка запросов в кластере](lesson_9221.md)
- [Следующий: 7843 — Миграция на MySQL →](lesson_7843.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2496

Практический пример работы с Базой данных через API D7 на основе создания собственного компонента. Создадим компонент:

```
<?php

class d7SQL extends CBitrixComponent
{
	var $connection;
	var $sqlHelper;
	var $sql;

	function __construct($component = null)
	{
		parent::__construct($component);
		$this->connection = \Bitrix\Main\Application::getConnection();
		$this->sqlHelper = $this->connection->getSqlHelper();

		//Строка запроса. Выбираем все логины, активных пользователей
		$this->sql = 'SELECT LOGIN FROM b_user WHERE ACTIVE = \''.$this->sqlHelper->forSql('Y', 1).'\' ';
	}

	/*
	* Возвращаем все значения
	*/
	function var1()
	{
		$recordset = $this->connection->query($this->sql);
			while ($record = $recordset->fetch())
		{
			$arResult[]=$record;
		}

		return $arResult;
	}

	/*
	* Возвращаем первые два значения
	*/
	function var2()
	{
		$recordset = $this->connection->query($this->sql,2);
		while ($record = $recordset->fetch())
		{
			$arResult[]=$record;
		}

		return $arResult;
	}

	/*
	* Возвращаем два значения, отступая два элемента от начала
	*/
	function var3()
	{
		$recordset = $this->connection->query($this->sql,2,2);
		while ($record = $recordset->fetch())
		{
		$arResult[]=$record;
		}

		return $arResult;
	}

	/*
	* Возвращаем сразу первый элемент из запроса
	*/
	function var4()
	{
		$arResult = $this->connection->queryScalar($this->sql);

		return $arResult;
	}

	/*
	* Выполняем запрос, не возвращая результат, т. е. INSERT, UPDATE, DELETE
	*/
	function var5()
	{
		$this->connection->queryExecute('UPDATE b_user SET ACTIVE = \'N\' WHERE LOGIN=\'test\' ');//Заменить на UPDATE
	}

	/*
	* Модифицируем результат
	*/
	function var6()
	{
		$recordset = $this->connection->query($this->sql);
		$recordset->addFetchDataModifier(
			function ($data)
			{
				$data["LOGIN"] .= ": Логин пользователя";
				return $data;
			}
		);
		while ($record = $recordset->fetch())
		{
			$arResult[]=$record;
		}

		return $arResult;
	}

	public function executeComponent()
	{
		//$this->arResult = $this->var1();

		//$this->arResult = $this->var2();

		//$this->arResult = $this->var3();

		//$this->arResult = $this->var4();

		//$this->var5();

		$this->arResult = $this->var6();

		$this->includeComponentTemplate();
	}
};
```

В коде объявлены три переменные:

1. `connection` - хранит подключение к базе данных;
2. `sqlHelper`- хранит объект конкретного класса формирования sql запросов;
3. `sql` - sql запрос.

В конструкторе класса получаем соединение через приложения, которые, кроме всего прочего, являются точкой входа.

Так же у нас здесь формируется строка запроса: выбираются из таблицы пользователей логины всех пользователей, которые активны, то есть поле **ACTIVE** установлено в `Y`. В строке запроса использован метод [forSql](http://dev.1c-bitrix.ru/api_d7/bitrix/main/db/sqlhelper/forsql.php), который делает входные параметры безопасными. Так же он может ограничить длину строки. В нашем случае он показан для примера: передан `Y` и указано что длина не должна быть больше одного символа.

Через приложение выполняется запрос и получаются все значения, соответствующие значению.

Функция **var1**: в ней осуществляется запрос и с помощью [fetch](http://dev.1c-bitrix.ru/api_d7/bitrix/main/db/result/fetch.php) получаются результаты. Типизированные данные возвращаются сразу в виде типа, а не в виде строк или чисел.

## Возвращаем все значения

```
/*
* Возвращаем все значения
*/
	function var1()
	{
		$recordset = $this->connection->query($this->sql);
		while ($record = $recordset->fetch())
		{
			$arResult[]=$record;
		}

		return $arResult;
	}
```

Функция **var2**. Здесь выполняется тот же самый запрос, но указывается лимит на количество получаемых элементов. В нашем случае 2.

## Возвращаем первые два значения

```
/*
* Возвращаем первые два значения
*/
	function var2()
		{
		$recordset = $this->connection->query($this->sql,2);
		while ($record = $recordset->fetch())
		{
			$arResult[]=$record;
		}

		return $arResult;
	}
```

Функция **var3**. Выполняется тот же самый запрос, но указываются два дополнительных параметра. Такая запись означает, то, что возвратятся два элемента. Это последний параметр. И эти элементы возвращаются нам начиная со второй позиции. Это второй параметр. То есть отступаем два элемента и отдаем два, начиная с третьего элемента.

## Возвращаем два значения, отступая два элемента от начала

```
/*
* Возвращаем два значения, отступая два элемента от начала
*/
	function var3()
	{
		$recordset = $this->connection->query($this->sql,2,2);
		while ($record = $recordset->fetch())
		{
			$arResult[]=$record;
		}

		return $arResult;
	}
```

Функция **var4** - скалярный запрос, то есть когда возвращается первый, единственный результат выборки.

## Возвращаем сразу первый элемент из запроса

```
/*
* Возвращаем сразу первый элемент из запроса
*/
	function var4()
	{
		$arResult = $this->connection->queryScalar($this->sql);

		return $arResult;
	}
```

Функция **var5** - выполнение запроса, без получения результата. Это нужно в случае **INSERT**, **UPDATE**, **DELETE**.

## Выполняем запрос, не возвращая результат

```
/*
 * Выполняем запрос, не возвращая результат, т. е. INSERT, UPDATE, DELETE
*/
	function var5()
	{
		$this->connection->queryExecute('UPDATE b_user SET ACTIVE = \'N\' WHERE LOGIN=\'test\' ');//Заменить на UPDATE
	}
```

Функция **var6** - модификация результата. Смотрим . С помощью метода [addFetchDataModifier](http://dev.1c-bitrix.ru/api_d7/bitrix/main/db/result/addfetchdatamodifier.php) объявляется функцию, которая на вход принимает массив результата для одного элемента и после модификации его возвращает. В нашем случае не сложный пример: просто к полю логин после двоеточия добавляется текст `Логин пользователя`.

## Модифицируем результат

```
/*
* Модифицируем результат
*/
	function var6()
	{
		$recordset = $this->connection->query($this->sql);
		$recordset->addFetchDataModifier(
			function ($data)
			{
				$data["LOGIN"] .= ": Логин пользователя";
				return $data;
			}
		);
		while ($record = $recordset->fetch())
		{
			$arResult[]=$record;
		}

		return $arResult;
	}
```

В метод *fetch* можно передать конвертер. Выглядит это так:

```
<?
$record = $recordset->fetch(\Bitrix\Main\Text\Converter::getHtmlConverter())
```

Допустимо использовать методы `Bitrix\Main\Text\Converter::getHtmlConverter` и `Bitrix\Main\Text\Converter::getXmlConverter`. Соответственно, они  подготавливают к выводу в **html** и в **xml**.  Происходит преобразование специальных символов в **html** сущности.
