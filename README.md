# Телеграм-бот на Python, отправляющий случайное фото с котиком для поднятия настроения
Отправляет случайную картину с котиками по запросу с веб-сервиса https://thecatapi.com/.

**Имя в telegram:** KittyBot *(@LoveyKittyBot)*

## Задача
Реализовать обработку сообщений и отправку картинок ботом через работу с внешним API - Bot API в Telegram.

## Технологии

    Python 3.7.9
    requests==2.26.0
    flake8==3.9.2
    flake8-docstrings==1.6.0
    pytest==6.2.5
    python-dotenv==0.19.0
    python-telegram-bot==13.7

## Функции модуля
```python
def get_new_image()
```
* Функция `get_new_image()` отправляет запрос к веб-сервису с котиками.
* Функция перехватывает ошибку при запросе к основному url и отправляет запрос к запасному (с собачками).
* Функция возвращает ссылку на полученную картинку.

---
---
```python
def new_cat(update, context)
```
* Функция `new_cat()` принимает на вход экземпляры классов `Update` и `CallbackContext`.
* При выполнении функции `new_cat()`для экземпляра `Update` вызывается свойство `effective_chat`, возвращающее
объект класса `telegram.Chat`. Он сохраняется в переменную `chat`.
* Для экземпляра `CallbackContext`, переданного в функцию как `context`, вызывается метод
`send_photo` объекта `telegram.ext.ExtBot`, в который передаётся свойство `id` объекта класса `Chat` и функция `get_new_image()`, передающая в метод картинку вторым аргументом. Метод отправляет переданную картинку в чат с `id` равным `chat.id`.

---
----
```python
def wake_up(update, context)
```
* Функция `wake_up()` принимает на вход экземпляры классов `Update` и `CallbackContext`.
* При выполнении функции для экземпляра `Update` вызывается свойство `effective_chat`, возвращающее
объект класса `telegram.Chat`. Он сохраняется в переменную `chat`.
* Для того же экземпляра вызывается свойство `message.chat.first_name`, возвращающее имя адресата (str). Оно сохраняется в переменную `name`.
* В переменную `button` сохраняется объект класса `ReplyKeyboardMarkup` с параметрами `KeyboardButton = '/newcat'` и `resize_keyboard=True`
(для создания кнопки \newcat с изменённым размером).
* Для экземпляра `CallbackContext`, переданного в функцию как `context`, поочерёдно вызываются методы
`send_message` и `send_photo` объекта `telegram.ext.ExtBot`. В `send_message` передаётся свойство `id` объекта класса `Chat`, текст сообщения-приветствия и объект класса `ReplyKeyboardMarkup` для отображения кнопки `button`. Метод отправляет заданный текст-приветсвие в чат с `id` равным `chat.id` и отображает переданную кнопку. Затем метод `send_photo` отправляет картинку в тот же чат.

---
----
```python
def main()
```
* Функция `main()` создаёт объект класса `Updater` с `token`, взятым из переменных окружения (.env).
* Для этого объекта поочерёдно вызывается метод `add_handler` экземпляра класса `telegram.ext.Dispatcher`. В метод передаётся экземпляры класса CommandHandler с параметрами `command='start'`, `callback=wake_up` и `command='newcat'`, `callback=new_cat`, что позволяет для команды `\start (\newcat)` вызвать функцию `wake_up (new_cat)` и неявно передать в неё экземпляры `Update` и `CallbackContext`.
* Для того же объекта `updater` вызывается метод `start_polling`, который начинает отправлять запросы к серверу Telegram и проверять обновления (каждые 10 секунд по умол.). Метод `idle` позволяет прервать отправку запросов в терминале комбинацией CTRL+C.

## Как запустить проект
```
git clone https://github.com/BU-Marina/kitty_bot
```

```
cd kitty_bot
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

Если у вас linux/MacOS:

```
. venv/bin/activate
```

Если у вас Windows:

```
. venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Добавить токен своего бота в переменные окружения через .env:

```
mv .env.example .env
nano .env
```

Вставить токен своего бота, сохранить изменения и выйти из режима (ctrl+o -> Enter -> ctrl+x)

Запустить проект:

```
python kittybot.py
```

Запустить тесты:

```
pytest
```

Запустить бота в telegram:

```
\start
```

Получить помощь по взаимодействию с ботом в telegram:

```
\help
```
