# coding:utf-8
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QWidget

from components.widgets.subwin import SubWindow

from .ui_help import Ui_HelpWindow


class HelpDoc(SubWindow):
    def __init__(self, name="HelpDoc", parent=None):
        super().__init__(name, parent, Ui_HelpWindow())
        self.ui.textBrowser.setSource(QUrl.fromLocalFile("Readme.html"))
