# -*- coding:utf-8 -*-
__author__ = "Peace4lv"
__date__ = "2021年1月3日"

import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Itool(QWidget):
    selectAreaStyle = (
        "QListWidget{font-size:16px;font-weight:bold;color:rgb(67, 9, 34);}"
        "QListWidget{border:4px;border-radius:4px;}"
        "QListWidget{background-color:transparent;}")

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        mainLayout = QHBoxLayout()
        grid = QGridLayout()
        grid.setSpacing(1)
        buttonName = ["WIFI密码查看", "启动LANTERN", "壁纸命名", "壁纸下载", "1", "2"]
        # main layout button name
        positions = [(i, j) for i in range(8) for j in range(1)]
        for name, position in zip(buttonName, positions):
            if name == "":
                continue
            CurButton = QPushButton(name)
            grid.addWidget(CurButton, *position)

        stateBox = QLabel("NOTHING")
        mainLayout.addLayout(grid)
        mainLayout.addWidget(stateBox)
        mainLayout.setStretch(0, 2)
        mainLayout.setStretch(1, 8)
        mainLayout.setSpacing(10)
        self.setLayout(mainLayout)

        # 环境配置
        self.setWindowTitle('ITool')
        self.setWindowIcon(
            QIcon(r'D:\Codes\Python_MS\ToolInOne\Doc\Pics\tool.png'))
        self.setFixedSize(400/0.618, 400)
        self.move(200, 200)

    def paintEvent(self, event):
        bgQp = QPainter(self)
        mainBackGround = r"D:\Codes\Python_MS\ToolInOne\Doc\Pics\background-1.png"
        bg = QPixmap(mainBackGround)
        bgQp.drawPixmap(self.rect(), bg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Itool()
    demo.show()
    sys.exit(app.exec_())
