# coding:utf-8
import sys
import ctypes
import time

from common import resource
from common.config import config
from common.setting import APP_NAME, RELEASE_URL
from common.style_sheet import setStyleSheet
from common.version_manager import VersionManager

# from components.dialog_box.dialog import Dialog

from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtGui import QIcon, QDesktopServices, QFont
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QTableWidgetItem,
    QFrame,
    QAbstractItemView,
)

from View.setting_interface import SettingInterface
from View.tab_unit import TabUnitWidget
from View.tab_dev import TabDevWidget

from .ui_main import Ui_MainWindow
from enum import Enum


class LdbRectype(Enum):
    LDB_TYPE_ZERO = 0
    LDB_TYPE_FULL = 1
    LDB_TYPE_FIRST = 2
    LDB_TYPE_MIDDLE = 3
    LDB_TYPE_LAST = 4


class TiHeader(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("crc", ctypes.c_uint32),
        ("len", ctypes.c_uint16),
        ("type", ctypes.c_uint8),
    ]


class TiFileInfo(ctypes.Structure):
    _fields_ = [
        ("btime", ctypes.c_uint32),
        ("btime_ms", ctypes.c_uint16),
        ("channel", ctypes.c_uint16),
        ("etime", ctypes.c_uint32),
        ("tags", ctypes.c_uint32),
        ("size", ctypes.c_uint32),
        ("res", ctypes.c_uint32 * 3),
    ]


class TiSlice(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("header", TiHeader), ("file_info", TiFileInfo)]


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
        self.item_lists = []

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
        _translate = QCoreApplication.translate
        font = QFont("微软雅黑", 10)
        font.setBold(True)
        tab_header = self.tab_list.horizontalHeader()
        tab_header.setFont(font)
        self.tab_list.setFrameShape(QFrame.NoFrame)
        self.tab_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tab_header.setFixedHeight(30)
        tab_header.resizeSection(0, 180)
        tab_header.resizeSection(1, 180)
        tab_header.resizeSection(2, 50)
        tab_header.resizeSection(3, 140)
        tab_header.resizeSection(4, 140)
        tab_header.resizeSection(5, 100)
        tab_header.setSectionsClickable(False)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), _translate("MainWindow", "索引解析")
        )
        self.tab_dev = TabDevWidget()
        self.tab_dev.setObjectName("tab_dev_unit")
        self.tabWidget.addTab(self.tab_dev, "")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_dev), _translate("MainWindow", "设备管理")
        )
        self.tab_unit = TabUnitWidget()
        self.tab_unit.setObjectName("tab_dev_unit")
        self.tabWidget.addTab(self.tab_unit, "")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_unit), _translate("MainWindow", "测试样例")
        )
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

    def item_add(self, slice):
        b_local_time = time.localtime(slice.btime)
        b_time_str = time.strftime("%Y-%m-%d %H:%M:%S", b_local_time)
        e_local_time = time.localtime(slice.etime)
        e_time_str = time.strftime("%Y-%m-%d %H:%M:%S", e_local_time)
        file_size = slice.size / (1024 * 1024)
        formatted_size = "{:.2f}".format(file_size)
        bps = (slice.size / 1024) / (slice.etime - slice.btime)
        formatted_bps = "{:.2f}".format(bps)
        item = {
            "btime": b_time_str,
            "etime": e_time_str,
            "tag": slice.tags,
            "size": formatted_size,
            "bps": formatted_bps,
            "rec_tm": slice.etime - slice.btime,
        }
        self.item_lists.append(item)

    def read_file(self, file_path):
        self.status_bar.showMessage(f"读取文件: {file_path}")
        self.item_lists = []
        ti_head_sz = ctypes.sizeof(TiHeader)
        with open(file_path, "rb") as file:
            try:
                while True:
                    # 读取文件数据
                    head_data = file.read(ti_head_sz)
                    if not head_data:
                        break
                    head_slice = TiHeader.from_buffer_copy(head_data)
                    data = file.read(head_slice.len)
                    if head_slice.type == LdbRectype.LDB_TYPE_FULL.value:
                        slice = TiFileInfo.from_buffer_copy(data)
                        self.item_add(slice)
                    else:
                        if head_slice.type == LdbRectype.LDB_TYPE_FIRST.value:
                            is_ok = False
                            slice = data
                            while True:
                                head_data = file.read(ti_head_sz)
                                if not head_data:
                                    break
                                head_slice = TiHeader.from_buffer_copy(head_data)
                                data = file.read(head_slice.len)
                                slice = slice + data
                                if head_slice.type == LdbRectype.LDB_TYPE_LAST.value:
                                    is_ok = True
                                    break
                            if is_ok:
                                slice = TiFileInfo.from_buffer_copy(slice)
                                self.item_add(slice)
            except IOError as e:
                print(f"Error reading file: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
        self.tab_list_refresh()

    def tab_list_refresh(self):
        print("tab_list_refresh")
        for i in range(self.tab_list.rowCount()):
            self.tab_list.removeRow(0)
        item_num = len(self.item_lists)
        for i in range(item_num):
            item_info = self.item_lists[i]
            row = self.tab_list.rowCount()
            self.tab_list.setRowCount(row + 1)
            self.tab_list.setRowHeight(row, 28)
            item = QTableWidgetItem(item_info["btime"])
            item.setTextAlignment(Qt.AlignCenter)
            self.tab_list.setItem(row, 0, item)
            item = QTableWidgetItem(item_info["etime"])
            item.setTextAlignment(Qt.AlignCenter)
            self.tab_list.setItem(row, 1, item)
            item = QTableWidgetItem(str(item_info["tag"]))
            item.setTextAlignment(Qt.AlignCenter)
            self.tab_list.setItem(row, 2, item)
            item = QTableWidgetItem(item_info["size"])
            item.setTextAlignment(Qt.AlignCenter)
            self.tab_list.setItem(row, 3, item)
            item = QTableWidgetItem(item_info["bps"])
            item.setTextAlignment(Qt.AlignCenter)
            self.tab_list.setItem(row, 4, item)
            item = QTableWidgetItem(str(item_info["rec_tm"]))
            item.setTextAlignment(Qt.AlignCenter)
            self.tab_list.setItem(row, 5, item)
