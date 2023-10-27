# coding:utf-8
import os
import pickle

from common import resource
from common.config import config
from common.setting import APP_NAME, RELEASE_URL
from common.style_sheet import setStyleSheet
from common.version_manager import VersionManager

# from components.dialog_box.dialog import Dialog

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices, QFont
from PyQt5.QtWidgets import (
    QMessageBox,
    QApplication,
    QMainWindow,
    QFileDialog,
    QTableWidgetItem,
    QFrame,
    QAbstractItemView,
    QProgressBar,
    QLabel,
)

from View.setting_interface import SettingInterface
from View.tab_unit import TabUnitWidget
from View.tab_dev import TabDevWidget
from View.sub_parse_index import ParseIndexWindow

from .ui_main import Ui_MainWindow

CACHE_FILEPATH = "./config"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.versionManager = VersionManager()
        # create sub interface
        self.initWindow()
        self.initWidget()

    def initWindow(self):
        self.resize(1200, 800)
        self.setWindowIcon(QIcon(":/images/logo/logo.png"))
        self.setWindowTitle(APP_NAME)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.sub_windows = list()
        self.filename = "./config/ImageToolsSubWindows.tmp"
        self.sub_windows_list = list()
        self.need_clear_cache = False
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as fp:
                self.sub_windows_list = pickle.load(fp)

    def initWidget(self):
        self.setQss()
        self.connectSignalToSlot()
        self.onInitFinished()

    def onInitFinished(self):
        """initialize finished slot"""

        # check for updates
        # if config.get(config.checkUpdateAtStartUp):
        #     self.checkUpdate(True)

    def setQss(self):
        self.mdiArea.setStyleSheet("QTabBar::tab { height: 30px;}")
        setStyleSheet(self, "main_window")

    def checkUpdate(self, ignore=False):
        """check software update

        Parameters
        ----------
        ignore: bool
            ignore message box when no updates are available
        """
        print("check update")
        if self.versionManager.hasNewVersion():
            self.showMessageBox(
                self.tr("Updates available"),
                self.tr("A new version")
                + f" {self.versionManager.lastestVersion[1:]} "
                + self.tr("is available. Do you want to download this version?"),
                True,
                lambda: QDesktopServices.openUrl(QUrl(RELEASE_URL)),
            )
        elif not ignore:
            self.showMessageBox(
                self.tr("No updates available"),
                self.tr(
                    "Groove Music has been updated to the latest version, feel free to use it."
                ),
            )

    def showMessageBox(
        self, title: str, content: str, showYesButton=False, yesSlot=None
    ):
        """show message box"""
        # w = Dialog(title, content, self)
        # if not showYesButton:
        #     w.cancelButton.setText(self.tr('Close'))

        # if w.exec() and yesSlot is not None:
        #     yesSlot()

    def connectSignalToSlot(self):
        """connect signal to slot"""
        self.subwindow_function = {
            "ParseIndexWindow": [self.actionParseIndex, ParseIndexWindow],
        }
        self.actionVersion.triggered.connect(self.checkUpdate)
        for key, value in self.subwindow_function.items():
            value[0].triggered.connect(
                lambda win_name=key, win_object=value[1]: self.add_sub_window(
                    win_name, win_object
                )
            )

    def add_sub_window(self, name, win_object):
        sub_window = win_object(parent=self)
        self.mdiArea.addSubWindow(sub_window)
        self.sub_windows.append(sub_window)
        sub_window.show()

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        # reply = QMessageBox().question(
        #     self,
        #     "ImageTools",
        #     "是否要退出程序？",
        #     QMessageBox.Yes | QMessageBox.No,
        #     QMessageBox.No,
        # )
        msgBox = QMessageBox()
        msgBox.setWindowFlags(msgBox.windowFlags() | Qt.WindowStaysOnTopHint)
        msgBox.setWindowFlags(msgBox.windowFlags() & ~Qt.WindowMinMaxButtonsHint)
        msgBox.setWindowTitle("ImageTools")
        msgBox.setText("是否要退出程序？")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.button(QMessageBox.Yes).setText("是")
        msgBox.button(QMessageBox.No).setText("否")
        reply = msgBox.exec_()
        if reply == QMessageBox.Yes:
            if self.need_clear_cache == False:
                if not os.path.exists(CACHE_FILEPATH):
                    os.mkdir(CACHE_FILEPATH)
                sub_windows_list = list()
                while len(self.sub_windows) > 0:
                    if self.sub_windows[0].name is not None:
                        sub_windows_list.append(self.sub_windows[0].name)
                        self.sub_windows[0].close()
                with open(self.filename, "wb") as fp:
                    pickle.dump(sub_windows_list, fp)
            else:
                # 清楚缓存
                if os.path.exists(CACHE_FILEPATH):
                    for files in os.listdir(CACHE_FILEPATH):
                        filepath = os.path.join(CACHE_FILEPATH, files)
                        if os.path.isfile(filepath):
                            os.remove(filepath)
            event.accept()
        else:
            event.ignore()
