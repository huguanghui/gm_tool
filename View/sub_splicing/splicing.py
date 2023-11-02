# coding:utf-8

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from components.widgets.subwin import SubWindow

from .ui_splicing import Ui_Splice


class ToolSplice(SubWindow):
    def __init__(self, name="ToolSplice", parent=None):
        super().__init__(name, parent, Ui_Splice())
