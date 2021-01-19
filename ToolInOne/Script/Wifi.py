# -*- coding:utf-8 -*-
__author__ = "Peace4lv"
__date__ = "2021年1月3日"

# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
import re
import os
from datetime import datetime
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
import sys
from buttonstyle import*


class Wifi(QWidget):
    netshprofiles = {}
    checksignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi()

    # ui setting
    def setupUi(self):
        # set button style
        self.button = QPushButton("WIFI密码查看", clicked=self.checksignal.emit)
        self.checksignal.connect(self.ClickFcn)
        # button = QPushButton(
        #     "WIFI密码查看", clicked=self.checksignal.emit, font=font)
        self.button.setStyleSheet(buttonStyle_4)
        # button.clicked.connect(self.ClickFcn)
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.button)
        self.setLayout(mainlayout)

    """
        netsh wlan show profiles
        return{"WiFi name":"wifi code"}
    """

    def ClickFcn(self):
        # print("button pushed")
        # return
        self.ShowWifi()
    # 查看WiFi账号密码

    def ShowWifi(self):
        a = datetime.now().strftime("%A, %d. %B %Y %I:%M %p")
        self.netshprofiles = {}
        f1 = os.popen("netsh wlan show profiles")
        if not f1 is None:
            f = f1.read()
            f1.close()
        else:
            f1.close()
            return
        ftemp = list()
        # configall = re.findall("所有用户配置文件 : [\w]*", f, re.M)
        configall = re.findall("(?<=所有用户配置文件 : )(.*)", f, re.M)
        for j in configall:
            j_key = self.FindKey(j)
            self.netshprofiles[j] = j_key

    def FindKey(self, name=""):
        if len(name) > 0:
            cmdline = 'netsh wlan show profile name=\"'+name+'\" key=clear'
            f1 = os.popen(cmdline)
            f2 = f1.read()
            f1.close()
            try:
                keyword_prt = re.findall(
                    "(?<=关键内容            : )(.*)", f2, re.M)
                keyword_prt = keyword_prt[0]
            except:
                keyword_prt = "did not find password"
        else:
            keyword_prt = ""
        return keyword_prt

    def GetProfileWifi(self, choice=0):
        if choice == 1:  # return tuple
            return 10
        elif choice == 2:  # return string
            sret = ""
            for i in self.netshprofiles:
                sret += str(i) + ":" + str(self.netshprofiles[i])+"<hr>"
            if len(sret) == 0:
                return "empty profiles"
            else:
                return sret
        else:  # return dict
            return self.netshprofiles


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Wifi()
    demo.show()
    sys.exit(app.exec_())
