# coding:utf-8
from PyQt5.QtCore import QLocale, Qt, QTranslator
from PyQt5.QtWidgets import QApplication

from common.application import SingletonApplication
from common.config import config, Language
from common.setting import APP_NAME
# from common.dpi_manager import DPI_SCALE
from View.main_window import MainWindow

import os
import sys
from inspect import getsourcefile
from pathlib import Path
os.chdir(Path(getsourcefile(lambda: 0)).resolve().parent)

# fix bug: qt.qpa.plugin: Could not load the Qt platform plugin "xcb"
if "QT_QPA_PLATFORM_PLUGIN_PATH" in os.environ:
    os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")

# enable high dpi scale
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
# os.environ["QT_SCALE_FACTOR"] = str(DPI_SCALE)


if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # app = QApplication(sys.argv)
    # app.setApplicationName(APP_NAME)
    app = SingletonApplication(sys.argv, APP_NAME)
    app.setStyle('Fusion')
    translator = QTranslator()
    language = config.get(config.language)  # type: Language
    print("language:", QLocale.system().name())
    if language == Language.AUTO:
        translator.load(QLocale.system(), ":/i18n/ptool.")
    elif language != Language.ENGLISH:
        translator.load(f":/i18n/ptools.{language.value}.qm")
    app.installTranslator(translator)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
