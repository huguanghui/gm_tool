from PyQt5.QtCore import QThread, pyqtSignal


class TestTaskThread(QThread):
    _finished = pyqtSignal(dict)
    _update_log = pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def run(self):
        print("TestTaskThread run")
