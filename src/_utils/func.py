from bot import bot
from os import getenv
from subprocess import run
from telebot.types import File

def save_document(file_id: str) -> None:
    file_info: File = bot.get_file(file_id=file_id)
    archive: bytes = bot.download_file(file_path=file_info.file_path)
    with open(file='projects\\_temp\\.rar', mode='wb') as archive_file:
        archive_file.write(archive)

def unpack() -> None:
    PROJECTS_FOLDER: str = getenv(key='PROJECTS')
    SAVED: str = f'{PROJECTS_FOLDER}\\saved'
    ARCHIVE: str = f'{PROJECTS_FOLDER}\\_temp\\.rar'
    run(['unrar', 'x', ARCHIVE, SAVED], shell=True)
    
def setup_project(name: str) -> None:
    PROJECTS_FOLDER: str = getenv(key='PROJECTS')
    PROJECT: str = f'{PROJECTS_FOLDER}\\saved\\{name}'
    PYTHON: str = getenv(key='PYTHON')
    PIP: str = f'{PROJECT}\\.venv\\Scripts\\pip.exe'
    run(['virtualenv', f'--python={PYTHON}', f'{PROJECT}\\.venv'])
    run([PIP, 'install', '-r', f'{PROJECT}\\requirements.txt'])

def run_project(name: str) -> None:
    PROJECTS_FOLDER: str = getenv(key='PROJECTS')
    PROJECT: str = f'{PROJECTS_FOLDER}\\saved\\{name}'
    VENV_PYTHON: str = f'{PROJECT}\\.venv\\Scripts\\python.exe'
    run([VENV_PYTHON, f'{PROJECT}\\src\\main.py'])