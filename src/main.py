from bot import bot
from _utils import save_document, unpack, run_project
from filters import auth
from telebot.types import Message

@bot.message_handler(commands=['start'])
@auth
def on_start(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id, text='Hello!')

@bot.message_handler(content_types=['document'])
@auth
def on_document(message: Message) -> None:
    save_document(file_id=message.document.file_id)
    unpack()
    run_project()

if __name__ == '__main__':
    bot.infinity_polling()