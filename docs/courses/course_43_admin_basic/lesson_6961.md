# JS-расширение медиаплеера

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 7971 — JS-класс к шаблону компонента](lesson_7971.md)
- [Следующий: 9015 — Примеры кастомизации публичной части →](lesson_9015.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=6961

|  | ### Примеры работы на js с плеером |
| --- | --- |

Не забываем подключить расширение:

```
CJSCore::Init(['player']);
```

|  | #### Создание и инициализация плеера |
| --- | --- |

Здесь самое важное - передать mime-type для каждого файла. В данном примере плеер будет проходить по всем файлам из списка и проиграет первый, который сможет. Поэтому в списке должен быть один и тот же ролик с разными расширениями.

```
BX.ready(function()
{
	var player = new BX.Fileman.Player('player_id', {
		sources: [
		{
			src: 'https://dev.1c-bitrix.ru/download/files/video/learning/hermitage.mp4',
			type: 'video/mp4'
		}
		]
	});
	var playerNode = player.createElement();
	BX('player_node').appendChild(playerNode);
	player.init();
});
```

|  | #### Описание параметров плеера |
| --- | --- |

| \| **Параметр** \| **Тип** \| **Описание** \|<br>\| --- \| --- \| --- \| |  |  |
| --- | --- | --- |
| sources | array | Массив файлов для проигрывания |
| autostart | bool | Запускать автоматически или нет |
| hasFlash | bool | Установить *true*, если придётся проигрывать *.flv файлы. В этом случае плеер подгрузит swf-файл плеера. |
| playbackRate | float | От 0 до 3. Скорость проигрывания (работает не всегда). |
| volume | float | От 0 до 3. Громкость |
| startTime | int | Время в секундах, с которого надо начать проигрывание |
| onInit | function | Вызовется сразу после инициализации плеера |
| lazyload | bool | Если *true* - плеер будет инициализироваться только при нахождении на экране пользователя. |
| skin | string | Название класса-скина. CSS-файл надо предварительно загрузить самостоятельно. |
| width | int | Ширина плеера |
| height | int | Высота плеера |
| isAudio | bool | Установить *true*, если плеер нужен для проигрывания аудио. |




После создания получить объект плеера можно через менеджер

```
var player = BX.Fileman.PlayerManager.getPlayerById('player_id');
```

|  | #### Некоторые полезные методы |
| --- | --- |

| \| **Метод** \| **Описание** \|<br>\| --- \| --- \|<br>\| `player.createElement();` \| Создает html-ноду и возвращает её. \|<br>\| `player.isPlaying();` \| Возвращает *true*, если плеер сейчас проигрывает что-то. \|<br>\| `player.pause();` \| Ставит проигрывание на паузу. \|<br>\| `player.isEnded();` \| Возвращает *true*, если файл был проигран до конца. \|<br>\| `player.isReady();` \| Возвращает true, если плеер полностью инициализирован. \|<br>\| `player.play();` \| Запускает проигрывание. \|<br>\| `player.setSource({
<br>    src: 'path',
<br>    type: 'mime-type'
<br>});` \| Устанавливает источник проигрывания \|<br>\| `player.getSource();` \| Возвращает текущий источник \|<br>\| `player.init();` \| Выполняет инициализацию плеера. \|<br>\| `player.mute(status);` \| Включает / выключает звук \| |
| --- |

|  | #### Пример создания и инициализации аудио плеера |
| --- | --- |

```
BX.ready(function()
{
	var audioPlayer = new BX.Fileman.Player('audio_player_id', {
	isAudio: true,
	sources: [
		{
			src: '/upload/SampleAudio_0.7mb.mp3',
			type: 'audio/mp3'
		}
	],
	onInit: function(player)
	{
		// следующие три строки нужны, чтобы скрыть кнопку разворачивания на весь экран
		player.vjsPlayer.controlBar.removeChild('timeDivider');
		player.vjsPlayer.controlBar.removeChild('durationDisplay');
		player.vjsPlayer.controlBar.removeChild('fullscreenToggle');
		// это прячет большую кнопку плей
		player.vjsPlayer.hasStarted(true);
	}
	});
	var audioPlayerNode = audioPlayer.createElement();
	BX('audio_player_node').appendChild(audioPlayerNode);
	audioPlayer.init();
});
```
