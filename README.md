# Remote TG Runner

## Installation

Clone the repository

```sh
git clone https://github.com/yaz008/RemoteTGRunner.git
```

Create Python 3.10.9 virtual environment and run

```sh
pip install -r requirements.txt 
```

Create `.env` file:

```env
TELEGRAM_API_KEY="YOUR-BOT-TOKEN"
PROJECTS="ABSOLUTE-PATH-TO-PROJECTS-FOLDER"
TEMP="ABSOLUTE-PATH-TO-TEMP-FOLDER"
PYTHON_v3_10_9="PATH-TO-PYTHON_v3_10_9"
```

Create `code.rar` file in the `temp` folder

## Usage

1. Create `your-project-name.rar` archive

2. Send it to your bot

**Note:**

- As of now, only Python 3.10.9 is supported

- Main entry point must be `your-project-name/src/main.py`

## License

Remote TG Runner is a free, open-source software distributed under the [MIT License](LICENSE.txt)
