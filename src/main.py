from bot import bot
from os import getenv
from _async import async_run
from _filters import auth
from telebot.types import Message
from threading import Thread

RUNNING: list[Thread] = []

@bot.message_handler(commands=['start'])
@auth
def on_start(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id, text='Hello!')

@bot.message_handler(commands=['running'])
@auth
def on_running(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id,
                     text=str([f'{index + 1}: {project.name}'
                               for index, project
                               in enumerate(RUNNING)]))

@bot.message_handler(content_types=['document'])
@auth
def on_document(message: Message) -> None:
    reply: Message = bot.send_message(chat_id=int(getenv(key='MY_ID')),
                                      text='Project assembly...')
    project_thread: Thread = async_run(file_id=message.document.file_id)
    RUNNING.append(project_thread)
    bot.edit_message_text(text=f'{project_thread.name} is running',
                          chat_id=int(getenv(key='MY_ID')),
                          message_id=reply.id)

if __name__ == '__main__':
    bot.infinity_polling()