from bot import bot
from os import getenv, listdir
from _utils.filters import auth
from _utils.async_run import async_run
from handlers.document import RUNNING
from telebot.types import (Message,
                           CallbackQuery,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)

def get_not_running() -> None:
    PROJECTS: str = getenv(key='PROJECTS')
    SAVED: str = f'{PROJECTS}\\saved'
    running: set[str] = set([thread.name
                             for thread
                             in RUNNING.values()
                             if thread.is_alive])
    saved: set[str] = set(listdir(path=SAVED))
    return saved - running

def not_running_markup(projects: set[str]) -> InlineKeyboardMarkup:
    markup: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=1)
    for index, project in enumerate(projects, start=1):
        button: InlineKeyboardButton = InlineKeyboardButton(text=f'{index}: {project}',
                                                            callback_data=project)
        markup.add(button)
    return markup

@bot.message_handler(commands=['run'])
@auth
def on_running(_: Message) -> None:
    not_running: set[str] = get_not_running()
    if len(not_running) == 0:
        bot.send_message(chat_id=int(getenv(key='MY_ID')),
                         text='Nothing to run')
        return None
    markup: InlineKeyboardMarkup = not_running_markup(projects=not_running)
    bot.send_message(chat_id=int(getenv(key='MY_ID')),
                     text='Choose a project to run',
                     reply_markup=markup)
    
@bot.callback_query_handler(func=lambda _: True)
def on_callback(callback: CallbackQuery) -> None:
    project_name: str = callback.data
    async_run(project_name=project_name)
    bot.edit_message_text(text=f'{project_name} is running',
                          chat_id=int(getenv(key='MY_ID')),
                          message_id=callback.message.id)