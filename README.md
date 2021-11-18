# telegram_space
Набор утилит для управления телеграм-каналом с автоматическим постингом картинок с космической тематикой.

# Установка
Вам понадобится установленный Python 3.6-3.9 и git.

Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/telegram_space
```

Создайте в этой папке виртуальное окружение:
```bash
$ python3 -m venv [полный путь до папки telegram_space]
```

Активируйте виртуальное окружение и установите зависимости:
```bash
$ cd telegram_space
$ source bin/activate
$ pip install -r requirements.txt
```
# Использование
Заполните прилагающийся .env.exapmle файл и переименуйте его в .env или иным образом задайте переменные среды:
* NASA_TOKEN - токен от NASA API.
* TELEGRAM_TOKEN - токен телеграм-бота.
* TELEGRAM_CHANNEL_NAME - короткая ссылка телеграм-канала (@some_name).
* TELEGRAM_POSTING_LATENCY - число секунд задержки между постингом картинок. Можно не задавать, в таком случае задержка будет равной одним суткам.
* IMAGES_FOLDER - путь к папке с картинками. Можно не задавать, в таком случае картинки будут сохраняться в папку images в директории с программой. В случае если программа не найдет папку, то создаст её.

Наиболее простой способ запустить бота - вызвать simple_start.py. Находясь в директории с программой исполните:
```bash
$ bin/python simple_start.py
```

Программа поочередно скачает картинки с NASA и SpaceX, а затем запустит бота.

Однако, при необходимости, скрипты можно использовать и отдельно друг от друга:

## fetch_spacex.py
```bash
$ bin/python fetch_spacex.py
```
Загружает фотографии с последнего запуска SpaceX с приложенными фотографиями. Файлы получают имя в формате spacex{num}.jpg, где num порядковый номер фотографии.

## fetch_nasa.py
```bash
$ bin/python fetch_nasa.py
```
Загружает 40 картинок дня и 5 изображений EPIC с API NASA. Требует, чтобы была задана переменная окружения NASA_TOKEN.

Картинки дня сохраняются в файлы с форматом nasa{num}.{ext}, где num порядковый номер, а ext - расширение файла. Иногда картинок дня может оказаться чуть меньше из-за того, что NASA API отдает вместо изображения youtube-видео.

Файлы EPIC сохраняются с таким же названием файла, как и в архиве NASA.

## bot.py
```bash
$ bin/python bot.py
```
Реализует автоматический постинг изображений в заданном телеграм-канале.

Изображения берутся из папки IMAGES_FOLDER.
Требует, чтобы были заданы переменные окружения TELEGRAM_TOKEN и TELEGRAM_CHANNEL_NAME. В случае если задана переменная окружения TELEGRAM_LATENCY, то задержка между постами берется из нее. В противном случае задержка принимается равной суткам.


## file_workers.py
Содержит набор функций для работы с файлами. Реализует скачивание файла и определение расширения файла из url.

## config.py
Содержит логику для работы с настройками программы. Получает переменные окружения, преобразует в необходимый тип, создает папку изображений, если ее не было.