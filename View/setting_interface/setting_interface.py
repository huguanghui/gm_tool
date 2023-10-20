# coding:utf-8
from common.config import config
from common.setting import HELP_URL, FEEDBACK_URL, AUTHOR, VERSION, YEAR
from components.layout.expand_layout import ExpandLayout
from components.widgets.scroll_area import SmoothScrollArea
from PyQt5.QtCore import Qt, pyqtSignal, QOperatingSystemVersion
from PyQt5.QtWidgets import QLabel, QFrame, QHBoxLayout


class SettingInterface(QFrame):
    """ Setting interface """

    checkUpdateSig = pyqtSignal()
    crawlMetaDataFinished = pyqtSignal()
    musicFoldersChanged = pyqtSignal(list)
    acrylicEnableChanged = pyqtSignal(bool)
    downloadFolderChanged = pyqtSignal(str)
    minimizeToTrayChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)

        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName("settings")
        # setting label
        # self.settingLabel = QLabel(self.tr("Settings"), self)
        # self.settingLabel.setAlignment(Qt.AlignCenter)
