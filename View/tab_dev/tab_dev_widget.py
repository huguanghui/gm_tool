# coding:utf-8
import sys
import ctypes
import time
import vlc
import os

from common import resource
from common.config import config
from common.setting import APP_NAME, RELEASE_URL
from common.style_sheet import setStyleSheet
from common.version_manager import VersionManager

# from components.dialog_box.dialog import Dialog

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QWidget

from .ui_tab_dev import Ui_TabDev


class TabDevWidget(QWidget, Ui_TabDev):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        # create sub interface
        self.initWindow()
        self.initWidget()

    def initWindow(self):
        self.vlc_instance = vlc.Instance()
        self.media_player = self.vlc_instance.media_player_new()
        self.media_player.set_hwnd(self.video_frame.winId())

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
        self.btn_play.clicked.connect(self.onPlay)

    def onPlay(self):
        print("play")
        media = self.vlc_instance.media_new("rtsp://admin:admin@192.168.31.117/0/0")
        self.media_player.set_media(media)
        self.media_player.play()