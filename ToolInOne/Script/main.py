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
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        wifi = QPushButton("WIFI密码查看")
        lantern = QPushButton("启动LANATERN")
        wallpaper = QPushButton("壁纸命名")

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(wifi, 0, 0, 1, 1)  # WiFi密码查看
        grid.addWidget(lantern, 0, 1, 1, 1)  # 蓝灯
        grid.addWidget(wallpaper, 0, 2, 1, 1)  # 壁纸规范命名

        self.setLayout(grid)
        # 环境配置
        self.setWindowTitle('ITool')
        self.setWindowIcon(
            QIcon(r'D:\Codes\Python_MS\ToolInOne\Doc\Pics\tool.png'))
        self.setFixedSize(400/0.618, 400)
        self.move(200, 200)

    def paintEvent(self, event):
        bgQp = QPainter(self)
        # mainBackGround = os.path.join(self.srcpath, 'Background-5.jpg')
        mainBackGround = r"D:\Codes\Python_MS\ToolInOne\Doc\Pics\WallPaper_260.jpg"
        bg = QPixmap(mainBackGround)
        bgQp.drawPixmap(self.rect(), bg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Itool()
    demo.show()
    sys.exit(app.exec_())
