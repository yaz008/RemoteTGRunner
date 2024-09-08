from bot import bot
from _utils.filters import auth
from telebot.types import Message

@bot.message_handler(commands=['stop'])
@auth
def on_stop(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id,
                     text='Bot is stopped')
    exit(code=0)