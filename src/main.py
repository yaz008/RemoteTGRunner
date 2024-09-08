from bot import bot
from _utils import save_document, unpack
from telebot.types import Message

@bot.message_handler(commands=['start'])
def on_start(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id, text='Hello!')

@bot.message_handler(content_types=['document'])
def on_document(message: Message) -> None:
    save_document(file_id=message.document.file_id)
    unpack()

if __name__ == '__main__':
    bot.infinity_polling()