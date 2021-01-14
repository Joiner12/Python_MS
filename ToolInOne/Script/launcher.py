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
import subprocess
"""
D:\Codes\Python_MS\ToolInOne\Doc\Pics\vpn.png
D:\Codes\Python_MS\ToolInOne\Doc\Pics\musictool.png
"""


class Launcher(QWidget):
    launchInfo = {}
    clickedSignal = pyqtSignal()
    processInfo = ""

    def __init__(self, filepath="", iconfile="", buttonname="", processname=""):
        self.launchInfo['filepath'] = filepath
        self.launchInfo['iconfile'] = iconfile
        self.launchInfo['buttonname'] = buttonname
        self.launchInfo['processname'] = processname
        super().__init__()
        self.__setpUI()

    def __setpUI(self):
        mainlayout = QVBoxLayout()
        self.button = QPushButton(self, clicked=self.clickedSignal.emit)
        self.button.setStyleSheet(buttonStyle_1)
        self.clickedSignal.connect(self.__clickedFcn)
        # self.button.clicked.connect(self.__clickedFcn)
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
        splittemp = list()
        filename = self.launchInfo['filepath']
        if not path.isfile(filename):
            self.processInfo = "wrong file path"
            return
        splittemp = path.splitext(filename)
        splitsuffix = splittemp[1]

        if self.checkProcessRunning(process_name=self.launchInfo['processname']):
            self.processInfo = self.launchInfo['processname'] + \
                " is already running..."
            return
        # according to suffix to determine
        if splitsuffix == ".exe":
            ex = subprocess.Popen(['start', filename], shell=True)
        if splitsuffix == ".cmd":
            cm = subprocess.Popen(['start', filename], shell=True)
            self.processInfo = self.launchInfo['processname'] + \
                " started succeed..."

    def printButtonInfo(self):
        return self.processInfo

    def checkProcessRunning(self, process_name="chrome.exe"):
        import psutil
        pids = psutil.pids()
        pid_names = list()
        for pid in pids:
            # print(psutil.Process(pid).name())
            pid_names.append(psutil.Process(pid).name())
        if process_name in pid_names:
            return True
        else:
            return False


if __name__ == "__main__":
    if True:
        app = QApplication(sys.argv)
        filepath_1 = r"D:\Softwares\ChromeGo\2.蓝灯翻墙1.cmd"
        # filepath_1 = r"D:\Softwares\ChromeGo\lantern.cmd"
        demo = Launcher(filepath=filepath_1,
                        iconfile=r"D:\Codes\Python_MS\ToolInOne\Doc\Pics\vpn.png",
                        buttonname="VPN",
                        processname="lantern.exe")
        demo.show()
        sys.exit(app.exec_())
