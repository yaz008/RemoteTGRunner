from bot import bot
from _utils.filters import auth
from telebot.types import Message

@bot.message_handler(commands=['start'])
@auth
def on_start(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id, text='Hello!')