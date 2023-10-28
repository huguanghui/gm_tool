# coding:utf-8
import sys
import ctypes
import time

import resource_rc
from common.config import config
from common.setting import APP_NAME, RELEASE_URL
from common.style_sheet import setStyleSheet
from common.version_manager import VersionManager

# from components.dialog_box.dialog import Dialog

from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtGui import QIcon, QDesktopServices, QFont
from PyQt5.QtWidgets import QWidget

from .ui_tab_unit import Ui_TabUnit


class TabUnitWidget(QWidget, Ui_TabUnit):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        # create sub interface
        self.initWindow()
        self.initWidget()

    def initWindow(self):
        pass

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
        # setStyleSheet(self, "main_window")
        pass

    def connectSignalToSlot(self):
        """connect signal to slot"""
