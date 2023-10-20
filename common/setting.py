# coding: utf-8
from pathlib import Path
from PyQt5.QtCore import QStandardPaths

# change DEBUG to False if you want to compile the code to exe
DEBUG = True


YEAR = 2023
AUTHOR = "hgh"
VERSION = "v0.0.1"
APP_NAME = "GMTool"
HELP_URL = ""
FEEDBACK_URL = "https://github.com/huguanghui/pyqt5_test/issues"
RELEASE_URL = "https://github.com/huguanghui/pyqt5_test/releases/latest"


if DEBUG:
    CONFIG_FOLDER = Path('AppData').absolute()
else:
    CONFIG_FOLDER = Path(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)) / APP_NAME

CONFIG_FILE = CONFIG_FOLDER / "config.json"

print(f"FOLDER: {CONFIG_FOLDER}")
