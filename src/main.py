from bot import bot
from telebot.types import Message

@bot.message_handler(commands=['start'])
def on_start(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id, text='Hello!')

if __name__ == '__main__':
    bot.infinity_polling()