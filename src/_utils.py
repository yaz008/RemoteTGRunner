from bot import bot
from os import getenv, listdir
from subprocess import run
from telebot.types import File

def save_document(file_id: str) -> None:
    file_info: File = bot.get_file(file_id=file_id)
    archive: bytes = bot.download_file(file_path=file_info.file_path)
    with open(file='temp\\code.rar', mode='wb') as archive_file:
        archive_file.write(archive)

def unpack() -> None:
    PROJECTS_FOLDER: str = getenv(key='PROJECTS')
    TEMP: str = getenv(key='TEMP')
    ARCHIVE: str = f'{TEMP}\\code.rar'
    run(['unrar', 'x', ARCHIVE, PROJECTS_FOLDER],
        shell=True)
    
def run_project() -> None:
    PROJECTS_FOLDER: str = getenv(key='PROJECTS')
    PROJECT_NAME: str = listdir(path=PROJECTS_FOLDER)[0]
    PROJECT: str = f'{PROJECTS_FOLDER}\\{PROJECT_NAME}'
    PYTHON: str = getenv(key='PYTHON_v3_10_9')
    PIP: str = f'{PROJECT}\\.venv\\Scripts\\pip.exe'
    VENV_PYTHON: str = f'{PROJECT}\\.venv\\Scripts\\python.exe'
    run(['virtualenv', f'--python={PYTHON}', f'{PROJECT}\\.venv'])
    run([PIP, 'install', '-r', f'{PROJECT}\\requirements.txt'])
    run([VENV_PYTHON, f'{PROJECT}\\src\\main.py'])