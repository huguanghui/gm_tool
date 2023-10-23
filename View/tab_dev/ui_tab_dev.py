# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './View/tab_dev/tab_dev.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabDev(object):
    def setupUi(self, TabDev):
        TabDev.setObjectName("TabDev")
        TabDev.resize(1074, 574)
        self.verticalLayout = QtWidgets.QVBoxLayout(TabDev)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(TabDev)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.video_frame = QtWidgets.QFrame(self.widget_2)
        self.video_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_frame.setObjectName("video_frame")
        self.verticalLayout_2.addWidget(self.video_frame)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(TabDev)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.rtsp_url = QtWidgets.QLineEdit(self.widget)
        self.rtsp_url.setObjectName("rtsp_url")
        self.horizontalLayout.addWidget(self.rtsp_url)
        self.btn_play = QtWidgets.QPushButton(self.widget)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout.addWidget(self.btn_play)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(TabDev)
        QtCore.QMetaObject.connectSlotsByName(TabDev)

    def retranslateUi(self, TabDev):
        _translate = QtCore.QCoreApplication.translate
        TabDev.setWindowTitle(_translate("TabDev", "Form"))
        self.label.setText(_translate("TabDev", "RTSP地址"))
        self.btn_play.setText(_translate("TabDev", "播放"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabDev = QtWidgets.QWidget()
    ui = Ui_TabDev()
    ui.setupUi(TabDev)
    TabDev.show()
    sys.exit(app.exec_())
