from os import getenv
from typing import Callable
from telebot.types import Message

def auth(endpoint: Callable[[Message], None]) -> Callable[[Message], None]:
    def wrapper(message: Message) -> None:
        if message.from_user.id == int(getenv(key='MY_ID')):
            endpoint(message)
    return wrapper