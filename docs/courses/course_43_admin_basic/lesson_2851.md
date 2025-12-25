# Ещё пара примеров работы

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 4880 — Тип параметров CUSTOM](lesson_4880.md)
- [Следующий: 2723 — Инфоблоки 2.0 →](lesson_2723.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2851

**Каким образом можно вывести капчу в своём компоненте?**

Пример использования CAPTCHA на странице. Ну а дальше - смотрите сами что куда вставлять: что в компонент (например, проверку), что в шаблон (например, вывод картинки)

```
<?
require($_SERVER["DOCUMENT_ROOT"]."/bitrix/header.php");
$APPLICATION->SetTitle("Title");
?>
<?
if (isset($submit)) {
	echo 'сабмит прошел...<br>';
	echo $myname.'<br>';
	echo $cap.'<br>';
	if (!$GLOBALS["APPLICATION"]->CaptchaCheckCode($cap, $captcha_sid))
	{
	$error=true;
	echo 'error captcha';
	}
}
?> <form id="linkForm" name="mailForm" action="test.php" method="post">
	<table cellspacing="3" cellpadding="0" width="100%" bgcolor="#eeeeee" border="0">
		<tbody>
			<tr><td valign="top" align="right">Моё имя *</td><td><input size="40" value="" name="myname" /></td></tr>
			<tr><td valign="top" align="right">CAPTCHA *</td><td><?
				$capCode = $GLOBALS["APPLICATION"]->CaptchaGetCode();
				?>
				<input type="hidden" name="captcha_sid" value="<?= htmlspecialchars($capCode) ?>">
				<img src="/bitrix/tools/captcha.php?captcha_sid=<?= htmlspecialchars($capCode) ?>" width="180" height="40"><br>
				<input size="40" value="" name="cap" /></td></tr>
			<tr><td valign="top" align="right"> </td><td><input type="submit" value="Отправить" name="submit" />  <input type="reset" value="Сбросить" name="Reset" /></td></tr>
		</tbody>
	</table>
</form><?require($_SERVER["DOCUMENT_ROOT"]."/bitrix/footer.php");?>
```

**Как сделать чтобы компонент на главной не виден, а на других был виден?**

Решение (добавить в шаблон компонента):

```
if ($curPage = $APPLICATION->GetCurPage(true))
{
	if (($curPage != "/index.php"))
		{
		....
		}
}
```
