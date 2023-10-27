# coding:utf-8
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QFileDialog,
    QTableWidgetItem,
    QFrame,
    QAbstractItemView,
)

from components.widgets.subwin import SubWindow

from .ui_parse_index import Ui_ParseIndex

import ctypes
import time
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


class ParseIndexWindow(SubWindow):
    def __init__(self, name="ParseIndexWindow", parent=None):
        super().__init__(name, parent, Ui_ParseIndex())
        font = QFont("微软雅黑", 10)
        font.setBold(True)
        tab_header = self.ui.tab_list.horizontalHeader()
        tab_header.setFont(font)
        self.ui.tab_list.setFrameShape(QFrame.NoFrame)
        self.ui.tab_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tab_header.setFixedHeight(30)
        tab_header.resizeSection(0, 180)
        tab_header.resizeSection(1, 180)
        tab_header.resizeSection(2, 50)
        tab_header.resizeSection(3, 140)
        tab_header.resizeSection(4, 140)
        tab_header.resizeSection(5, 100)
        tab_header.setSectionsClickable(False)

        self.item_lists = []
        self.ui.btn_open.clicked.connect(self.file_open)

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
        self.ui.statusbar.showMessage(f"读取文件: {file_path}")
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
        for i in range(self.ui.tab_list.rowCount()):
            self.ui.tab_list.removeRow(0)
        item_num = len(self.item_lists)
        for i in range(item_num):
            item_info = self.item_lists[i]
            row = self.ui.tab_list.rowCount()
            self.ui.tab_list.setRowCount(row + 1)
            self.ui.tab_list.setRowHeight(row, 28)
            item = QTableWidgetItem(item_info["btime"])
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tab_list.setItem(row, 0, item)
            item = QTableWidgetItem(item_info["etime"])
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tab_list.setItem(row, 1, item)
            item = QTableWidgetItem(str(item_info["tag"]))
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tab_list.setItem(row, 2, item)
            item = QTableWidgetItem(item_info["size"])
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tab_list.setItem(row, 3, item)
            item = QTableWidgetItem(item_info["bps"])
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tab_list.setItem(row, 4, item)
            item = QTableWidgetItem(str(item_info["rec_tm"]))
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tab_list.setItem(row, 5, item)
