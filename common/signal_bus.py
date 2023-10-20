# coding:utf-8
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtMultimedia import QMediaPlaylist

# from common.crawler import SongQuality, QueryServerType

# from .database.entity import AlbumInfo, SingerInfo, SongInfo
from .singleton import Singleton


class SignalBus(Singleton, QObject):
    """ Signal bus in App """
    appMessageSig = pyqtSignal(object)          # APP 发来消息
    appErrorSig = pyqtSignal(str)               # APP 发生异常
    appRestartSig = pyqtSignal()                # APP 需要重启
    selectionModeStateChanged = pyqtSignal(bool)  # 进入/退出 选择模式


signalBus = SignalBus()
