# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './View/main_window/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 767)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, 6, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.btn_open = QtWidgets.QPushButton(self.widget)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout.addWidget(self.btn_open)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 6)
        self.verticalLayout_3.addWidget(self.widget)
        self.tab_list = QtWidgets.QTableWidget(self.tab)
        self.tab_list.setEnabled(True)
        self.tab_list.setObjectName("tab_list")
        self.tab_list.setColumnCount(6)
        self.tab_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_list.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_list.setHorizontalHeaderItem(5, item)
        self.verticalLayout_3.addWidget(self.tab_list)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 26))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.menuFile.setObjectName("menuFile")
        self.menuManger = QtWidgets.QMenu(self.menubar)
        self.menuManger.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuManger.setAutoFillBackground(False)
        self.menuManger.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.menuManger.setObjectName("menuManger")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.menuHelp.addAction(self.actionVersion)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuManger.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "请选择索引文件:"))
        self.btn_open.setText(_translate("MainWindow", "打开"))
        item = self.tab_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "开始时间"))
        item = self.tab_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "结束时间"))
        item = self.tab_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "类型"))
        item = self.tab_list.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "文件大小(MB)"))
        item = self.tab_list.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "平均码率(KB/s)"))
        item = self.tab_list.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "时长(sec)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuManger.setTitle(_translate("MainWindow", "Manger"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
