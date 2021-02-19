# -*- coding:utf-8 -*-

__author__ = "Peace4Lv"
__date__ = "2021-2-18"

import pathlib
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon, QPolygon, QColor, QPainter, QPixmap, QPainterPath
from PyQt5.QtCore import Qt, QPoint, QTimer, QPointF, QTime


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


class AnalogClock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analog Clock")
        self.setGeometry(100, 800, 200, 200)
        self.setFixedSize(200, 200)
        self.Dial = ClockDial(self)
        # self.setWindowIcon(QIcon(self.Dial.imgFile_M))
        self._setupUI()

    def _setupUI(self):
        self.Dial.setGeometry(0, 0, 200, 200)
        SettingBtn = QPushButton("1", self)
        SettingBtn.setFixedSize(20, 20)
        SettingBtn.move(160, 180)

        BtnStart = QPushButton("s", self)
        BtnStart.setFixedSize(20, 20)
        BtnStart.move(20, 50)

        BtnStop = QPushButton("2", self)
        BtnStop.setFixedSize(20, 20)
        BtnStop.move(160, 50)

    # 背景设置
    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.drawBackFigure(painter)
        painter.end()

    def drawBackFigure(self, painter):
        painter.setPen(QColor(52, 115, 189))
        painter.setBrush(QColor(52, 115, 189))
        painter.drawRect(0, 0, self.width(), self.height())
        size = self.size()
        if False:
            painter.setPen(QColor(222, 1, 14))
            if size.height() <= 1 or size.height() <= 1:
                return

            for i in range(1000):
                x = random.randint(1, size.width() - 1)
                y = random.randint(1, size.height() - 1)
                painter.drawPoint(x, y)


class ClockDial(QWidget):
    imgPath = pathConfig()
    imgFile = str()
    imgFile_M = str()
    imgFilePath = str()
    if len(imgPath) == 1 and isinstance(imgPath, list):
        imgFilePath = pathlib.Path(imgPath[0])
        imgFile = imgFilePath.joinpath("表盘-1.png")
        imgFile_M = imgFilePath.joinpath("Deer.ico")
        if imgFile.exists():
            imgFile = imgFile.__str__()
            print("image file config finished", imgFile)
        else:
            print("image 1 config failed")
        if imgFile_M.exists():
            imgFile_M = imgFile_M.__str__()
            print("image file config finished", imgFile_M)
        else:
            print("image 2 config failed")

    hourHand = QPolygon([
        QPoint(4, 6),
        QPoint(-4, 6),
        QPoint(0, -50)
    ])
    minuteHand = QPolygon([
        QPoint(4, 4),
        QPoint(-4, 4),
        QPoint(0, -70)
    ])
    hourColor = QColor(33, 211, 230)
    minuteColor = QColor(10, 85, 93)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        # self.setWindowTitle("Analog Clock")
        # self.setGeometry(100, 800, 200, 200)
        # self.setWindowIcon(QIcon(self.imgFile_M))

    def paintEvent(self, event):
        side = min(self.width(), self.height())  # 最小边
        time = QTime.currentTime()  # 获取系统当前时间

        painter = QPainter(self)
        # 抗锯齿
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        painter.translate(self.width() / 2, self.height() / 2)  # 坐标偏置

        # painter.setPen(Qt.NoPen)
        painter.setBrush(self.hourColor)

        # 表盘主背景
        self.target = QPixmap(self.size())
        self.target.fill(Qt.transparent)

        imgB = self.imgFile
        p = QPixmap(imgB).scaled(
            200, 200, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        path = QPainterPath()
        path.addRoundedRect(
            -100, -100, 200, 200, 50, 50)
        painter.setClipPath(path)
        painter.drawPixmap(-100, -100, p)

        # 表盘中心图标
        imgM = self.imgFile_M
        pm = QPixmap(imgM).scaled(
            50, 50, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        painter.drawPixmap(-25, -60, pm)
        # 整点刻度
        painter.setPen(self.hourColor)
        for i in range(12):
            painter.drawLine(QPointF(85, 0), QPointF(96, 0))
            # painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.setPen(self.minuteColor)
        for j in range(60):  # 小刻度
            if (j % 5) != 0:
                painter.drawLine(QPointF(85, 0), QPointF(92, 0))
                # painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(self.hourColor)

        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(self.hourHand)  # 画三角形
        painter.restore()

        painter.setPen(Qt.NoPen)
        painter.setBrush(self.minuteColor)
        painter.save()

        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(self.minuteHand)
        painter.restore()

        painter.setPen(QColor(0, 0, 0))
        painter.drawEllipse(-5, -5, 10, 10)  # 画圆。参数是外接矩形左上点和长宽


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AnalogClock()
    w.show()
    sys.exit(app.exec_())
