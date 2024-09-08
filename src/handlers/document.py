from bot import bot
from os import getenv
from _utils.filters import auth
from _utils.save import save
from _utils.async_run import async_run
from telebot.types import Message
from threading import Thread

RUNNING: dict[str, Thread] = {}

def remove_extension(name: str) -> str:
    return name.rsplit('.', maxsplit=1)[0]

@bot.message_handler(content_types=['document'])
@auth
def on_document(message: Message) -> None:
    reply: Message = bot.send_message(chat_id=int(getenv(key='MY_ID')),
                                      text='Assembly...')
    save(file_id=message.document.file_id)
    project_name: str = remove_extension(message.document.file_name)
    project_thread: Thread = async_run(project_name=project_name)
    RUNNING.update({ project_thread.name: project_thread })
    bot.edit_message_text(text=f'{project_thread.name} is running',
                          chat_id=int(getenv(key='MY_ID')),
                          message_id=reply.id)