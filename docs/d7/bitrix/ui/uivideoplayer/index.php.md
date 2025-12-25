# Видеоплеер

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/uivideoplayer/index.php

Расширение `ui.video-player` воспроизводит видео и аудио с использованием библиотеки video.js. Доступен с версии UI 24.1000.0.

### Подключение

Объект `BX.UI.VideoPlayer.PlayerManager` предоставляет доступ к плеерам на странице. Метод `getPlayerById` возвращает объект по его идентификатору:

```
BX.UI.VideoPlayer.PlayerManager.getPlayerById(
    playerId
)
```

`BX.UI.VideoPlayer.Player` создает объект для каждого плеера на странице.

JS

```
import { Player } from 'ui.video-player'; // es6
new Player(id, params);

new BX.UI.VideoPlayer.Player(id, params); // es5
```

PHP

```
\Bitrix\Main\UI\Extension::load('ui.video-player');
```

### Параметры

| Параметр<br>`тип` | Описание |
| --- | --- |
| id<br>`string` | Идентификатор элемента DOM, в котором будет инициализирован плеер |
| params<br>`Object` | Коллекция параметров для настройки плеера |

**Параметр** `params`

| Параметр<br>`тип` | Описание |
| --- | --- |
| sources<br>`аrray` | Список объектов, описывающих источники медиафайлов для воспроизведения.<br><br>Каждый объект должен содержать свойства:<br><br>- `src` — URL или путь к медиафайлу, например, видео или аудио<br>- `type` — MIME-тип медиафайла. Например, `video/mp4` для видеофайлов формата MP4 или `audio/mp3` для аудиофайлов формата MP3 |
| autostart<br>`boolean` | Автоматически запускать воспроизведение.<br><br>По умолчанию — `false` |
| playbackRate<br>`number` | Скорость воспроизведения.<br><br>Значение по умолчанию — `1` Допустимые значения от `0.5` до `3` |
| volume<br>`number` | Громкость плеера.<br><br>Значение по умолчанию — `0.8` |
| startTime<br>`number` | Начальное время воспроизведения в секундах.<br><br>По умолчанию — `0` |
| skin<br>`string` | CSS класс для скина плеера.<br><br>По умолчанию — пустая строка |
| isAudio<br>`boolean` | Использовать аудио режим.<br><br>По умолчанию — `false` |
| width<br>`number` | Ширина плеера.<br><br>По умолчанию — `560` для видео и `400` для аудио |
| height<br>`number` | Высота плеера.<br><br>По умолчанию — `315` для видео и `30` для аудио |
| duration<br>`number \| null` | Продолжительность видео.<br><br>По умолчанию — `null` |
| muted<br>`boolean` | Отключить звук по умолчанию.<br><br>По умолчанию — `false` |

### Методы

Получить объект плеера:

```
var player = BX.UI.VideoPlayer.PlayerManager.getPlayerById(
    playerId
);
```

Методы работы с объектом плеера:

| Метод | Описание |
| --- | --- |
| player.isPlaying() | Проверяет, идет ли воспроизведение. Если да — возвращает `true` |
| player.isEnded() | Проверяет, остановилось ли воспроизведение после проигрывания файла целиком. Если да — возвращает `true` |
| player.isReady() | Возвращает `true`, если плеер до конца инициализирован |
| player.getElement() | Получает html-ноду плеера |
| player.createElement() | Возвращает ноду, аналогично методу getElement, если плеер вставлен в документ. Если ноды нет — создает ее, но не вставляет в документ |
| player.setSource(source) | Устанавливает трек плеера. Рекомендуется передавать объект вида<br><br>```<br>{<br>    src: 'путь к файлу',<br>    type: 'mime-type'<br>}<br>``` |
| player.getSource() | Возвращает текущий трек |
| player.mute() | Выключает звук плеера |
| player.play() | Запускает воспроизведение |
| player.pause() | Останавливает воспроизведение |

### Пример

Код создает видеоплеер на веб-странице, который воспроизводит указанное видео.

```
// Импортируем Player
import { Player } from 'ui.video-player';

// Создаем новый объект плеера с идентификатором 'player_id'
const player = new Player(
    'player_id',
	{
		// Указываем источник видео
		sources: [
			{
				src: 'https://dev.1c-bitrix.ru/download/files/video/learning/hermitage.mp4', // URL видеофайла
				type: 'video/mp4' // Тип видеофайла
			}
		],
		autostart: true, // Автоматически запускать воспроизведение
		width: 640, // Установить ширину плеера
		height: 360 // Установить высоту плеера
	}
);

// Создаем HTML-элемент для плеера
const playerNode = player.createElement();

// Находим элемент на странице с идентификатором 'video'
const node = document.getElementById('video');

// Добавляем созданный элемент плеера в найденный элемент на странице
node.appendChild(playerNode);

// Инициализируем плеер
player.init();
```
