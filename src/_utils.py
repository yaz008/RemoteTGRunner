from bot import bot
from os import getenv
from subprocess import run
from telebot.types import Message, File

def save_document(file_id: str) -> None:
    file_info: File = bot.get_file(file_id=file_id)
    archive: bytes = bot.download_file(file_path=file_info.file_path)
    with open(file='projects\\_temp\\code.rar', mode='wb') as archive_file:
        archive_file.write(archive)

def unpack() -> None:
    PROJECTS: str = getenv(key='PROJECTS')
    ARCHIVE: str = f'{PROJECTS}\\_temp\\code.rar'
    run(['unrar', 'x', ARCHIVE, PROJECTS],
        shell=True)