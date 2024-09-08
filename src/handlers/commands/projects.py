from bot import bot
from os import getenv, listdir
from _utils.filters import auth
from telebot.types import Message

@bot.message_handler(commands=['projects'])
@auth
def on_projects(message: Message) -> None:
    text: str = '\n'.join([f'{index + 1}: {name}'
                           for index, name
                           in enumerate(listdir(path=getenv(key='PROJECTS')))])
    bot.send_message(chat_id=message.from_user.id,
                     text='No projects' if text == '' else text)