# -*- coding:utf-8 -*-
__author__ = "Peace4lv"
__date__ = "2021年1月3日"

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from buttonstyle import*


class Wifi(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        print("netsh wlan show profile")

    # ui setting
    def setupUi(self):
        # set button style
        button = QPushButton("WIFI密码查看")
        button.setStyleSheet(buttonStyle_1)
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(button)
        self.setLayout(mainlayout)

    def ShowName(self):
        print("我想对你说")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Wifi()
    demo.show()
    sys.exit(app.exec_())
