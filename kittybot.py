import os
import requests
import logging
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, Update


load_dotenv()

token = os.getenv('TOKEN')
URL = 'https://api.thecatapi.com/v1/images/search'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def get_new_image() -> str:
    '''Получить новую картинку котика'''
    try:
        response = requests.get(URL).json()
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url).json()

    random_cat = response[0].get('url')
    return random_cat


def new_cat(update: Update, context: CallbackContext) -> None:
    '''Отправить новую картинку котика'''
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def wake_up(update: Update, context: CallbackContext) -> None:
    '''Отправить приветственное сообщение и картинку котика'''
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Посмотри, какого котика я тебе нашёл'.format(name),
        reply_markup=button,
    )
    context.bot.send_photo(chat.id, get_new_image())


def main() -> None:
    '''Добавить хендлеры и начать поллинг'''
    updater = Updater(token=token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
