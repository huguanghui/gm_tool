# coding:utf-8
import sys
import ctypes

from common import resource
from common.config import config
from common.setting import APP_NAME, RELEASE_URL
from common.style_sheet import setStyleSheet
from common.version_manager import VersionManager

# from components.dialog_box.dialog import Dialog

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from View.setting_interface import SettingInterface

from .ui_main import Ui_MainWindow


class TiFileInfo(ctypes.Structure):
    _fields_ = [
        ("btime", ctypes.c_uint32),
        ("btime_ms", ctypes.c_uint16),
        ("channel", ctypes.c_uint16),
        ("etime", ctypes.c_uint32),
        ("tags", ctypes.c_uint32),
        ("size", ctypes.c_uint32),
        ("res", ctypes.c_uint32 * 3)
    ]


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.versionManager = VersionManager()
        # create sub interface
        self.initWindow()
        self.initWidget()

    def initWindow(self):
        self.resize(800, 600)
        self.setWindowIcon(QIcon(":/images/logo/logo.png"))
        self.setWindowTitle(APP_NAME)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

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
        self.btn_open.clicked.connect(self.file_open)
        self.actionVersion.triggered.connect(self.checkUpdate)

    def file_open(self):
        file_name = QFileDialog.getOpenFileName(
            self, "Open File", "./", "All Files(*);;Text Files(*.txt)"
        )
        print(file_name[0])
        self.read_file(file_name[0])

    def read_file(self, file_path):
        with open(file_path, 'rb') as file:
            # 读取文件数据
            data = file.read(32)
            print(data)
            # 将数据转换为TiFileInfo结构体对象
            file_info = TiFileInfo.from_buffer_copy(data)
            # 打印结构体成员
            print("btime:", file_info.btime)
            print("btime_ms:", file_info.btime_ms)
            print("channel:", file_info.channel)
            print("etime:", file_info.etime)
            print("tags:", file_info.tags)
            print("size:", file_info.size)
            # struct_size = ctypes.sizeof(TiFileInfo)
            # print("Struct size:", struct_size)
