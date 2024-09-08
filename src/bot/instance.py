from os import getenv
from dotenv import load_dotenv
from telebot import TeleBot

if not load_dotenv():
    raise Exception('Unable to load .env file')
bot: TeleBot = TeleBot(token=getenv(key='TELEGRAM_API_KEY'),
                       parse_mode='Markdown',
                       skip_pending=True,
                       threaded=False,
                       num_threads=1)