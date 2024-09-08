# Remote TG Runner

## Installation

Clone the repository

```sh
git clone https://github.com/yaz008/RemoteTGRunner.git
```

Create Python virtual environment, activate it and run

```sh
pip install -r requirements.txt 
```

Run `setup.bat` to create `projects` and `temp` folders

```sh
./setup.bat
```

Create `.env` file:

```env
TELEGRAM_API_KEY="YOUR-BOT-TOKEN"
MY_ID="YOUR-TELEGRAM-ID"
PROJECTS="ABSOLUTE-PATH-TO-PROJECTS-FOLDER"
TEMP="ABSOLUTE-PATH-TO-TEMP-FOLDER"
PYTHON="PATH-TO-YOUR-PYTHON"
```

## Usage

1. Create `your-project-name.rar` archive

2. Send it to your bot

**Note:** Main entry point must be `your-project-name/src/main.py`

## License

Remote TG Runner is a free, open-source software distributed under the [MIT License](LICENSE.txt)
