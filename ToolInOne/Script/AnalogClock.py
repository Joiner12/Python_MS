# -*- coding:utf-8 -*-

__author__ = "Peace4Lv"
__date__ = "2021-2-18"

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPainterPath
from PyQt5.QtCore import Qt,  QTimer
import pathlib
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


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
    print("image file config finished", imgFile)

    hourHand = QtGui.QPolygon([
        QtCore.QPoint(4, 10),
        QtCore.QPoint(-4, 10),
        QtCore.QPoint(0, -50)
    ])
    minuteHand = QtGui.QPolygon([
        QtCore.QPoint(4, 8),
        QtCore.QPoint(-4, 8),
        QtCore.QPoint(0, -70)
    ])
    hourColor = QtGui.QColor(33, 211, 230)
    minuteColor = QtGui.QColor(10, 85, 93)

    def __init__(self):
        super().__init__()
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        self.setWindowTitle("Analog Clock")
        self.resize(200, 200)

    def paintEvent(self, event):
        side = min(self.width(), self.height())  # 最小边
        time = QtCore.QTime.currentTime()  # 获取系统当前时间

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)  # 抗锯齿
        painter.translate(self.width() / 2, self.height() / 2)  # 坐标偏置
        painter.scale(side / 300.0, side / 300.0)  # 坐标系缩放

        painter.setPen(QtGui.QColor(0, 0, 0))
        painter.drawEllipse(-100, -100, 200, 200)  # 画圆。参数是外接矩形左上点和长宽

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self.hourColor)

        # 表盘
        painter.save()
        self.target = QtGui.QPixmap(self.size())
        self.target.fill(Qt.transparent)
        if False:
            imgB = r"D:\Code\Python\ToolInOne\Doc\Pics\表盘-1.jpg"
        else:
            imgB = self.imgFile
        self.radius = 10
        p = QtGui.QPixmap(imgB).scaled(self.width()/2, self.height()/2,
                                       Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
        path = QtGui.QPainterPath()
        path.addRoundedRect(
            -self.width()/2, -self.height()/2, self.width(), self.height(), self.radius, self.radius)
        painter.setClipPath(path)
        painter.drawPixmap(-self.width()/2, -self.height()/2, p)
        painter.restore()

        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(self.hourHand)  # 画三角形
        painter.restore()

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self.minuteColor)
        painter.save()

        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(self.minuteHand)
        painter.restore()

        painter.setPen(QtGui.QColor(0, 0, 0))
        painter.drawEllipse(-5, -5, 10, 10)  # 画圆。参数是外接矩形左上点和长宽


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ClockDial()
    w.show()
    sys.exit(app.exec_())
