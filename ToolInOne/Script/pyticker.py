from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class AnalogClock(QWidget):
    hourHand = QtGui.QPolygon([
        QtCore.QPoint(10, 8),
        QtCore.QPoint(-10, 8),
        QtCore.QPoint(0, -60)
    ])
    minuteHand = QtGui.QPolygon([
        QtCore.QPoint(8, 8),
        QtCore.QPoint(-8, 8),
        QtCore.QPoint(0, -70)
    ])
    hourColor = QtGui.QColor(255, 0, 0)
    minuteColor = QtGui.QColor(0, 255, 0)

    def __init__(self):
        super().__init__()
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        self.setWindowTitle("Analog Clock")
        self.resize(200, 200)

    def paintEvent(self, event):
        side = min(self.width(), self.height()) # 最小边
        time = QtCore.QTime.currentTime()  # 获取系统当前时间

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)  # 抗锯齿
        painter.translate(self.width() / 2, self.height() / 2) # 坐标偏置
        painter.scale(side / 300.0, side / 300.0) # 坐标系缩放

        painter.setPen(QtGui.QColor(0, 0, 0))
        painter.drawEllipse(-100, -100, 200, 200)  # 画圆。参数是外接矩形左上点和长宽

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(AnalogClock.hourColor)

        # 表盘
        painter.save()
        self.target = QtGui.QPixmap(self.size())
        self.target.fill(Qt.transparent)
        imgB = r"D:\Code\Python\ToolInOne\Doc\Pics\表盘-1.jpg"
        self.radius = 10
        p = QtGui.QPixmap(imgB).scaled(self.width(),self.height(),Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
        path = QtGui.QPainterPath()
        path.addRoundedRect(
            -100, -100, self.width(), self.height(), self.radius, self.radius)
        painter.setClipPath(path)
        painter.drawPixmap(-100, -100, p)
        painter.restore()

        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(AnalogClock.hourHand) # 画三角形
        painter.restore()

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(AnalogClock.minuteColor)
        painter.save()
    
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(AnalogClock.minuteHand)
        painter.restore()

        painter.setPen(QtGui.QColor(0, 0, 0))
        painter.drawEllipse(-5, -5, 10, 10)  # 画圆。参数是外接矩形左上点和长宽

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    clock = AnalogClock()
    clock.show()

    sys.exit(app.exec())
