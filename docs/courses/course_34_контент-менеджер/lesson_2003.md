# Двухэтапная авторизация

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 1996 — Авторизация на сайте](lesson_1996.md)
- [Следующий: 6921 — Подключение пользователем двухэтапной авторизации →](lesson_6921.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=34&LESSON_ID=2003

### Система одноразовых паролей




Система

			одноразовых паролей

                    Одноразовые пароли или двухэтапная авторизация - это метод защиты от шпионских программ с помощью авторизации в два этапа. Первый раз вводится логин пользователя и основной пароль. Второй раз вводится секретный код, который пользователь получает дополнительно.

		 дополняет стандартную авторизацию и значительно усиливает безопасность продуктов «1С-Битрикс». При каждой авторизации пользователь вводит новый секретный код, что исключает возможность его подбора злоумышленниками. Одноразовый пароль вы можете получить либо с помощью специальной программы у вас на телефоне, или с помощью специального

			USB-токена

                    ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/authorization/JaCarta_WebPass_sm.png)
[Подробнее](lesson_6860.md)...

		.




![](../../../images/courses/34/dev.1c-bitrix.ru/images/portal_admin/bitrixotp/otp.png)




## Зачем нужна двухэтапная авторизация

Использование системы одноразовых паролей позволяет **избежать**:



- последствий такого вида компьютерного мошенничества, как **сниффинг** - перехват и\или анализ сетевого трафика, предназначенного для других узлов, т.е. перехват пользовательских логинов и паролей, которые в ряде сетевых протоколов передаются в незашифрованном или слабозашифрованном виде;
- использования злоумышленником **закешированных паролей** на чужих компьютерах (Интернет-кафе и т.п);
- **последствий работы вирусов**, сканирующих трафик на предмет наличия в нем секретных сведений, или **кейлоггеров**, записывающих набираемые символы на компьютере и отправляющих полученную информацию создателям вредоносных программ.




Таким образом, использование одноразовых паролей для авторизации на сайте существенно затрудняет злоумышленникам получить несанкционированный доступ к интернет-проекту.




**Примечание:**Подробнее о системе одноразовых паролей (OTP) см. раздел [Безопасность](http://www.1c-bitrix.ru/products/cms/security/#tab-autentification-link) на сайте «1C-Битрикс».






#### Программы для одноразовых паролей




Для получения одноразового кода можно использовать разные программы. Главное, чтобы они поддерживали один из двух используемых в 1С-Битрикс

			алгоритмов генерации паролей


**по счетчику** ([HMAC-Based One-time Password](http://ru.wikipedia.org/wiki/HOTP), **HOTP**) - код будет доступен до тех пор, пока пользователь не запросит новый;

**по времени** ([Time-based One-time Password](http://ru.wikipedia.org/wiki/Time-based_One-time_Password_Algorithm), **TOTP**) - код будет доступен в течение 30 секунд с момента его получения, после чего он автоматически обновится.

		. Установка программы выполняется типовым для вашей мобильной операционной системы способом. Настройка программы, как правило, выполняется аналогично настройке фирменного приложения

			Bitrix24 OTP

                    Мобильное приложение Bitrix OTP от компании «1С-Битрикс» специально разработано для двухэтапной авторизации. Оно генерирует секретные коды для входа на порталы и сайты под управлением «Битрикс24» и «1С-Битрикс» и позволяет обойтись без использования брелков или посторонних программ.

[Подробнее ...](lesson_6819.md)

		, которое и рекомендуется использовать в случае Google Android и Apple iOS.




**Внимание!** Перед подключением двухэтапной авторизации проверьте правильность установленного времени и часового пояса в вашем мобильном устройстве.




<!-- &lt;div class="tab" id="otp_app"&gt;

&lt;h3 class="tab-title"&gt;&lt;i style="font-size: 25px;" class="fa fa-list  fa-border" aria-hidden="true"&gt;&lt;/i&gt;&nbsp;&nbsp;Перечень некоторых совместимых приложений&lt;/h3&gt;
&lt;a name="otp_app"&gt;&lt;/a&gt;

<br/>
&lt;table cellspacing="0" cellpadding="0"&gt;
  &lt;tbody&gt;
    &lt;tr bgcolor="white"&gt; &lt;td bgcolor="#8c8c8c"&gt;
        &lt;table cellspacing="1" cellpadding="5"&gt;
          &lt;tbody&gt;

    &lt;tr bgcolor="silver"&gt; &lt;td align="center" width="10%"&gt;&lt;b&gt;Устройство&lt;/b&gt;&lt;/td&gt; &lt;td align="center" width="30%"&gt;&lt;b&gt;Приложение&lt;/b&gt;&lt;/td&gt; &lt;td align="center"&gt;&lt;b&gt;Примечания&lt;/b&gt;&lt;/td&gt;  &lt;/tr&gt;

    &lt;tr bgcolor="white"&gt;
    &lt;td align="center"&gt;&lt;b&gt;Apple iOS&lt;/b&gt;&lt;/td&gt;
&lt;td align="center"&gt;
&lt;p&gt;&lt;a href="https://itunes.apple.com/ru/app/bitrix24-otp/id929604673?mt=8" target="_blank" /&gt;Bitrix24 OTP&lt;/a&gt; &lt;/p&gt;
&lt;p&gt;&lt;a href="https://itunes.apple.com/ru/app/google-authenticator/id388497605?mt=8" target="_blank" /&gt;Google Authenticator&lt;/a&gt; &lt;/p&gt;
&lt;p&gt;&lt;a href="https://itunes.apple.com/ru/app/freeotp/id872559395?mt=8" target="_blank" /&gt;FreeOTP Authenticator&lt;/a&gt;&lt;/p&gt;
&lt;/td&gt;

&lt;td&gt;
&lt;p&gt;iOS 6.0 и выше. По времени (TOTP) и по счетчику (HOTP).&lt;/p&gt;
&lt;p&gt;iOS 5.0 и выше. По времени (TOTP) и по счетчику (HOTP).&lt;/p&gt;
&lt;p&gt;iOS 7.0 и выше. По времени (TOTP) и по счетчику (HOTP).&lt;/p&gt;
&lt;/td&gt;
&lt;/tr&gt;

    &lt;tr bgcolor="#eeeeee"&gt;
&lt;td align="center"&gt;&lt;b&gt;Google Android&lt;/b&gt;&lt;/td&gt;
&lt;td align="center"&gt;
&lt;p&gt;&lt;a href="https://play.google.com/store/apps/details?id=com.bitrixsoft.otp&hl=ru" target="_blank" /&gt;Bitrix24 OTP&lt;/a&gt; &lt;/p&gt;
&lt;p&gt;&lt;a href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=ru" target="_blank" /&gt;Google Authenticator&lt;/a&gt; &lt;/p&gt;
&lt;p&gt;&lt;a href="https://play.google.com/store/apps/details?id=org.fedorahosted.freeotp&hl=ru" target="_blank" /&gt;FreeOTP Authenticator&lt;/a&gt;&lt;/p&gt;
&lt;/td&gt;
&lt;td&gt;
&lt;p&gt;Android 3.0 и выше. По времени (TOTP) и по счетчику (HOTP).&lt;/p&gt;
&lt;p&gt;Android 2.2 и выше. По времени (TOTP) и по счетчику (HOTP).&lt;/p&gt;
&lt;p&gt;Android 4.0 и выше. По времени (TOTP) и по счетчику (HOTP).&lt;/p&gt;
&lt;/td&gt;  &lt;/tr&gt;

    &lt;tr bgcolor="white"&gt;
    &lt;td align="center"&gt;&lt;b&gt;J2ME&lt;/b&gt;&lt;/td&gt;
&lt;td align="center"&gt;
&lt;p&gt;&lt;a href="https://code.google.com/p/gauthj2me/" target="_blank" /&gt;Google Authentification in Java Mobile, j2me&lt;/a&gt; &lt;/p&gt;
&lt;p&gt;&lt;a href="https://code.google.com/p/lwuitgauthj2me/" target="_blank" /&gt;Google Authenticator for J2ME phones&lt;/a&gt; &lt;/p&gt;
&lt;/td&gt;

&lt;td&gt;
&lt;p&gt;Для мобильных с J2ME. По времени (TOTP), ручной ввод секретного ключа.&lt;/p&gt;
&lt;p&gt;Для мобильных с J2ME на основе LWUIT-GUI. По времени (TOTP), ручной ввод секретного ключа.&lt;/p&gt;
&lt;/td&gt;
&lt;/tr&gt;

    &lt;tr bgcolor="#eeeeee"&gt;
&lt;td align="center"&gt;&lt;b&gt;Palm OS&lt;/b&gt;&lt;/td&gt;
&lt;td align="center"&gt;
&lt;p&gt;&lt;a href="https://code.google.com/p/gauthj2me/downloads/detail?name=gauth.prc&can=2&q=" target="_blank" /&gt;Google Authenticator for Palm OS&lt;/a&gt; &lt;/p&gt;
&lt;/td&gt;
&lt;td&gt;
&lt;p&gt;По времени (TOTP), ручной ввод секретного ключа.&lt;/p&gt;
&lt;/td&gt;  &lt;/tr&gt;


    &lt;tr bgcolor="#eeeeee"&gt;
&lt;td align="center"&gt;&lt;b&gt;MS Windows&lt;/b&gt;&lt;/td&gt;
&lt;td align="center"&gt;
&lt;p&gt;&lt;a href="https://winauth.github.io/winauth/index.html" target="_blank" /&gt;WinAuth&lt;/a&gt; &lt;/p&gt;
&lt;/td&gt;
&lt;td&gt;
&lt;p&gt;MS Windows 7|8, .NET Framework 4. По времени (TOTP), портативность, защита приложения паролем.&lt;/p&gt;
&lt;/td&gt;  &lt;/tr&gt;


		  &lt;/tbody&gt;
		&lt;/table&gt;
		&lt;/tr&gt;
	&lt;/tbody&gt;
  &lt;/table&gt;

&lt;/div&gt; -->
