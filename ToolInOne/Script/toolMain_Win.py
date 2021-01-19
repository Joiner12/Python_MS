# -*- coding:utf-8 -*-
__author__ = "Peace4Lv"
__date__ = "2021-1-8"


import sys
from PyQt5.QtCore import Qt, pyqtSignal, QPoint, QSize
from PyQt5.QtGui import QFont, QEnterEvent, QPainter, QColor, QPen, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtWidgets import QTextEdit, QGridLayout, QApplication
from Wifi import Wifi
from textArea import textArea
from launcher import Launcher


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self._setupUI()

    def _setupUI(self):
        self.setWindowTitle('ITool')
        self.buttonName = ["WIFI密码查看", "VPN",
                           "壁纸命名", "Musictool", "1", "2"]
        mainLayout = QHBoxLayout(spacing=0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        #sublayout -grid
        grid = QGridLayout()
        grid.setSpacing(0)
        # wifi code checker
        self.wifibutton = Wifi()
        # VPN
        # D:\Softwares\ChromeGo\2.蓝灯翻墙1.cmd
        # D:\MusicTool\MusicTools v1.9.1.0.exe
        filepath_1 = r"D:\Softwares\ChromeGo\蓝灯翻墙1.cmd"
        self.vpn = Launcher(
            filepath=filepath_1,
            buttonname="VPN",
            processname="lartern.exe")
        # MUSIC TOOL
        self.musictool = Launcher(
            filepath=r"D:\MusicTool\MusicTools v1.9.1.0.exe",
            buttonname="Musictool",
            processname="MusicTools.exe")
        # reserve
        self.reservebutton = Launcher(buttonname="...")

        # infomation area
        self.stateBox = textArea()
        # add button
        grid.addWidget(self.wifibutton, 0, 0, 1, 1)
        grid.addWidget(self.vpn, 1, 0, 1, 1)
        grid.addWidget(self.musictool, 2, 0, 1, 1)
        grid.addWidget(self.reservebutton, 3, 0, 1, 1)
        #
        mainLayout.addLayout(grid)
        mainLayout.addWidget(self.stateBox)
        mainLayout.setStretch(0, 1)
        mainLayout.setStretch(1, 9)
        mainLayout.setSpacing(10)

        self.setLayout(mainLayout)
        self.setFixedSize(400/0.618, 400)
        self.move(200, 200)
        # 绑定sender
        self.wifibutton.button.clicked.connect(self.buttonClikced)
        self.vpn.button.clicked.connect(self.buttonClikced)
        self.musictool.button.clicked.connect(self.buttonClikced)
        self.reservebutton.button.clicked.connect(self.buttonClikced)

    def paintEvent(self, event):
        bgQp = QPainter(self)
        mainBackGround = r"D:\Codes\Python_MS\ToolInOne\Doc\Pics\background-1.png"
        bg = QPixmap(mainBackGround)
        bgQp.drawPixmap(self.rect(), bg)

    def buttonClikced(self):
        sender = self.sender()
        text = sender.text()
        print(text)
        if text in self.buttonName:
            # wifi 密码
            if text == self.buttonName[0]:
                # repack info
                wifiprofiles = "<h1>名称:密码<hr></h1>"
                wifiprofiles += self.wifibutton.GetProfileWifi(choice=2)
                self.stateBox.ModifyText(
                    flag='p', infoIn=wifiprofiles)
            # vpn
            if text == self.buttonName[1]:
                self.stateBox.ModifyText(
                    flag='p', infoIn=self.buttonName[1])

            if text == self.buttonName[2]:
                self.stateBox.ModifyText(
                    flag='p', infoIn=self.buttonName[2])

            if text == self.buttonName[3]:
                self.stateBox.ModifyText(
                    flag='p', infoIn=self.buttonName[3])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())
