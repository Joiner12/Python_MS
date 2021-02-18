#-*- coding:utf-8 -*-

__author__ = "Peace4Lv"
__date__ = "2021-2-18"

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QPainter,QPainterPath
from PyQt5.QtCore import Qt,  QTimer
import pathlib
import sys

def pathConfig():
    retpath = list()
    p = pathlib.Path(__file__)
    p = pathlib.Path(p.parents[1])
    imgpath = p.joinpath('Doc', 'Pics')
    a = imgpath.exists()
    # D:\Code\Python\ToolInOne\Doc\Pics
    if imgpath.is_dir():
        imgpath = imgpath.__str__()
        retpath.append(imgpath)
    return retpath


class AnalogClock(QWidget):
    imgPath = pathConfig()
    if len(imgPath) == 1 and isinstance(imgPath, list):
        imgFile = imgPath[0]
    else:
        imgFile = None

    def __init__(self):
        super().__init__()

    def _setupUI(self):
        mainLayout = QVBoxLayout()
        Dial = ClockDial()
        SettingBtn = QPushButton()
        mainLayout.addWidget(SettingBtn, stretch=1, alignment=Qt.AlignHCenter)
        mainLayout.addWidget(Dial, stretch=1, alignment=Qt.AlignCenter)


class ClockDial(QWidget):
    imgPath = pathConfig()
    imgFile = str()
    if len(imgPath) == 1 and isinstance(imgPath, list):
        imgFile = pathlib.Path(imgPath[0])
        imgFile = imgFile.joinpath("表盘-1.jpg")
        if imgFile.exists():
            imgFile = imgFile.__str__()
    print("image file config finished",imgFile)

    def __init__(self):
        super().__init__()
        mainTimer = QTimer()
        mainTimer.timeout.connect(self.update)
        # mainTimer.start(1000)  # 1000ms

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        # qp.setRenderHint(QPainter.Antialiasing) #抗锯齿
        side = min(self.width(), self.height())
        qp.translate(self.width()/2, self.height()/2)
        self.target = QPixmap(self.size())
        self.target.fill(Qt.transparent)
        imgB = self.imgFile
        self.radius = 100
        p = QPixmap(imgB).scaled(200,200,Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setRenderHint(QPainter.HighQualityAntialiasing, True)
        qp.setRenderHint(QPainter.SmoothPixmapTransform, True)
        path = QPainterPath()
        path.addRoundedRect(
            0, 0, self.width(), self.height(), self.radius, self.radius)
        qp.setClipPath(path)
        qp.drawPixmap(0, 0, p)
        self.setPixmap(self.target)
        qp.end()

    # def drawImg(self,event,qp):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ClockDial()
    w.show()
    sys.exit(app.exec_())
