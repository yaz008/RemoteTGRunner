from bot import bot
from handlers.document import RUNNING
from _utils.filters import auth
from telebot.types import Message

@bot.message_handler(commands=['running'])
@auth
def on_running(message: Message) -> None:
    text: str = '\n'.join([f'{index}: {thread.name}'
                           for index, thread
                           in enumerate(RUNNING.values(), start=1)
                           if thread.is_alive()])
    bot.send_message(chat_id=message.from_user.id,
                     text='Nothing is running' if text == '' else text)