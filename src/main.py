from bot import bot
from os import getenv, listdir
from _utils.async_run import async_run
from _utils.filters import auth
from telebot.types import Message
from threading import Thread

RUNNING: dict[str, Thread] = {}

@bot.message_handler(commands=['start'])
@auth
def on_start(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id, text='Hello!')
    
@bot.message_handler(commands=['stop'])
@auth
def on_stop(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id,
                     text='Bot is stopped')
    exit(code=0)

@bot.message_handler(commands=['running'])
@auth
def on_running(message: Message) -> None:
    text: str = '\n'.join([f'{index + 1}: {name}'
                           for index, name
                           in enumerate(RUNNING.keys())])
    bot.send_message(chat_id=message.from_user.id,
                     text='Nothing is running' if text == '' else text)
    
@bot.message_handler(commands=['projects'])
@auth
def on_projects(message: Message) -> None:
    text: str = '\n'.join([f'{index + 1}: {name}'
                           for index, name
                           in enumerate(listdir(path=getenv(key='PROJECTS')))])
    bot.send_message(chat_id=message.from_user.id,
                     text='No projects' if text == '' else text)

@bot.message_handler(content_types=['document'])
@auth
def on_document(message: Message) -> None:
    reply: Message = bot.send_message(chat_id=int(getenv(key='MY_ID')),
                                      text='Project assembly...')
    project_thread: Thread = async_run(file_id=message.document.file_id)
    RUNNING.update({ project_thread.name: project_thread })
    bot.edit_message_text(text=f'{project_thread.name} is running',
                          chat_id=int(getenv(key='MY_ID')),
                          message_id=reply.id)

if __name__ == '__main__':
    bot.infinity_polling()