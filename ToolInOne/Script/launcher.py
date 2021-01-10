# -*- coding:utf-8 -*-
__author__ = "Peace4Lv"
__date__ = "2020-1-10"

import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from os import path
from buttonstyle import *
"""
D:\Codes\Python_MS\ToolInOne\Doc\Pics\vpn.png
D:\Codes\Python_MS\ToolInOne\Doc\Pics\musictool.png
"""


class Launcher(QWidget):
    launchInfo = {}

    def __init__(self, filepath="", iconfile="", buttonname=""):
        self.launchInfo['filepath'] = filepath
        self.launchInfo['iconfile'] = iconfile
        self.launchInfo['buttonname'] = buttonname
        super().__init__()
        self.__setpUI()

    def __setpUI(self):
        mainlayout = QVBoxLayout()
        self.button = QPushButton()
        self.button.setStyleSheet(buttonStyle_1)
        self.button.clicked.connect(self.__clickedFcn)
        # icon
        try:
            icon = self.launchInfo['iconfile']
            self.button.setIcon(QIcon(QPixmap(icon)))
        except:
            pass
            # buttonname
        try:
            buttonname = self.launchInfo['buttonname']
            self.button.setText(buttonname)
        except:
            self.button.setText('button')
        mainlayout.addWidget(self.button)
        self.setLayout(mainlayout)

    def __clickedFcn(self):
        print("pring")

    def printButtonInfo(self):
        print("button info")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Launcher(
        filepath="", iconfile=r"D:\Codes\Python_MS\ToolInOne\Doc\Pics\vpn.png", buttonname="VPN")
    demo.show()
    sys.exit(app.exec_())
