from bot import bot
from os import getenv, listdir
from _utils.filters import auth
from telebot.types import Message

@bot.message_handler(commands=['saved'])
@auth
def on_projects(message: Message) -> None:
    PROJECTS: str = getenv(key='PROJECTS')
    SAVED: str = f'{PROJECTS}\\saved'
    text: str = '\n'.join([f'{index}: {name}'
                           for index, name
                           in enumerate(listdir(path=SAVED), start=1)])
    bot.send_message(chat_id=message.from_user.id,
                     text='No projects' if text == '' else text)