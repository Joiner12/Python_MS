# -*- coding:utf-8 -*-
'''
    多输入对话框
    [1]自定义输入框https://www.jianshu.com/p/7b5a40bb74fb
    [2]QLineEdit https://blog.csdn.net/jia666666/article/details/81510502
    [3]QDateTimeEdit https://blog.csdn.net/jia666666/article/details/81589442
    [4]去掉空格 https://blog.csdn.net/qingquanyingyue/article/details/93907224
    [5]stylesheet https://doc.qt.io/qt-5/stylesheet-examples.html
    [6]模态设置 https://www.tutorialspoint.com/pyqt/pyqt_qdialog_class.htm
         https://blog.csdn.net/jia666666/article/details/81539733
    [7]窗口间信号传递 https://blog.csdn.net/jia666666/article/details/81781697
    [8]List of All Members for QDialogButtonBox https://doc.qt.io/qt-5/qdialogbuttonbox-members.html
    [9]exit https://stackoverflow.com/questions/27031673/qdialogbuttonbox-buttons-not-responding

'''

import sys
import os
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PathManager as pathm


class MultiInputDialog(QDialog):
    timedateStyle_1 = ("QDateTimeEdit{border-radius:4px;font-size:16px;font-weight:bold;color:rgb(6, 75, 177);}"
                       "QDateTimeEdit{border:2px solid rgb(189, 189, 189);}"
                       "QDateTimeEdit{font-family:'Century'}")

    lineEditStyle_1 = ("QLineEdit{border-radius:4px;font-size:16px;font-weight:bold;color:rgb(6, 75, 177);}"
                       "QLineEdit{border:2px solid rgb(189, 189, 189);}"
                       "QLineEdit{font-family:'Century'}")
    srcpath = pathm.GetUiPath()

    signal_PieceInfo = pyqtSignal(str)

    def __init__(self, parent=None, handleflag=0):
        super().__init__(parent)
        self.setWindowTitle("Piece Info")
        self.setWindowIcon(QIcon(os.path.join(self.srcpath, "记录-1.png")))
        # 交互模态设置
        self.setWindowModality(Qt.ApplicationModal)
        # 无边框
        if False:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        # protop info
        self.pieceInfo = ""

        self.bingoLabel = QLabel("Bingo")
        style = ("QLabel{font-size:16px;font-weight:bold;color:green;font-family:'Century'}"
                 "QLabel{border-radius:4px;border:2px solid rgb(118,154,40);}"
                 "QLabel{background-color: #ABABAB;}"
                 "QLabel:title{text-align:center}")
        self.bingoLabel.setStyleSheet(style)
        self.bingoLabel.setVisible(False)
        # 手动添加log文件
        if handleflag == 1:
            try:
                # 获取最后一条日志 作为start protop
                recentLog = self.GetRecentLog(pathm.GetLogFile())
                a = recentLog.split("|")
                startProto = datetime.strptime(a[1], "%Y-%m-%d %H:%M:%S")
                self.GetStart = QDateTimeEdit(startProto)  # 创建日期+时间的组件
                self.GetStart.setDisplayFormat('yyyy-MM-dd hh:mm:ss')  # 显示样式
                self.GetStart.setStyleSheet(self.timedateStyle_1)
            except:
                self.GetStart = QDateTimeEdit(
                    QDateTime.currentDateTime())  # 创建日期+时间的组件
                self.GetStart.setDisplayFormat('yyyy-MM-dd hh:mm:ss')  # 显示样式
                self.GetStart.setStyleSheet(self.timedateStyle_1)

            self.GetFinish = QDateTimeEdit(
                QDateTime.currentDateTime())  # 创建日期+时间的组件
            self.GetFinish.setDisplayFormat('yyyy-MM-dd hh:mm:ss')  # 显示样式
            self.GetFinish.setStyleSheet(self.timedateStyle_1)

            # detail item
            self.Detail = QLineEdit()
            self.Detail.setStyleSheet(self.lineEditStyle_1)
            self.Detail.setPlaceholderText("what did you do")
            self.Detail.setClearButtonEnabled(True)
        # 修改最后一条log文件
        else:
            try:
                # 获取最新一条详细日志
                recentLog = self.GetRecentLog(pathm.GetLogFile())
                a = recentLog.split("|")
                startProto = datetime.strptime(a[0], "%Y-%m-%d %H:%M:%S")
                self.GetStart = QDateTimeEdit(startProto)  # 创建日期+时间的组件
                self.GetStart.setDisplayFormat('yyyy-MM-dd hh:mm:ss')  # 显示样式
                self.GetStart.setStyleSheet(self.timedateStyle_1)

                finishProto = datetime.strptime(a[1], "%Y-%m-%d %H:%M:%S")
                self.GetFinish = QDateTimeEdit(finishProto)  # 创建日期+时间的组件
                self.GetFinish.setDisplayFormat('yyyy-MM-dd hh:mm:ss')  # 显示样式
                self.GetFinish.setStyleSheet(self.timedateStyle_1)
                # detail item
                self.Detail = QLineEdit()
                self.Detail.setStyleSheet(self.lineEditStyle_1)
                self.Detail.setPlaceholderText(a[-1])
                self.Detail.setClearButtonEnabled(True)
            except:
                self.GetStart = QDateTimeEdit(
                    QDateTime.currentDateTime())  # 创建日期+时间的组件
                self.GetStart.setDisplayFormat('yyyy-MM-dd hh:mm:ss')  # 显示样式
                self.GetStart.setStyleSheet(self.timedateStyle_1)

                self.GetFinish = QDateTimeEdit(
                    QDateTime.currentDateTime())  # 创建日期+时间的组件
                self.GetFinish.setDisplayFormat('yyyy-MM-dd hh:mm:ss')  # 显示样式
                self.GetFinish.setStyleSheet(self.timedateStyle_1)
                self.Detail = QLineEdit()
                self.Detail.setStyleSheet(self.lineEditStyle_1)
                self.Detail.setPlaceholderText("try failed ")
                self.Detail.setClearButtonEnabled(True)
        # button area
        buttonbox = QDialogButtonBox(self)
        buttonbox.setOrientation(Qt.Horizontal)
        buttonbox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        buttonbox.accepted.connect(self.isOk)
        buttonbox.rejected.connect(self.isCancle)

        # space item
        spacerItem = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # frame layout
        layout_2 = QVBoxLayout()

        layout_2.addWidget(self.GetStart, 0)
        layout_2.addWidget(self.GetFinish, 1)
        layout_2.addWidget(self.Detail, 2)
        layout_2.addItem(spacerItem)
        layout_2.addWidget(self.bingoLabel, 3)
        layout_2.addWidget(buttonbox, 4)

        # layout
        self.setLayout(layout_2)
        self.setFixedWidth(400)

    def isOk(self):
        # set info piece
        gap = datetime.strptime(self.GetFinish.text(), "%Y-%m-%d %H:%M:%S") - \
            datetime.strptime(self.GetStart.text(), "%Y-%m-%d %H:%M:%S")
        gap_m = int(gap.seconds/60)
        # did't change edit line protocol
        try:
            detail = self.Detail.text()
            detail = detail.strip()
            if len(detail) == 0:
                recentLog = self.GetRecentLog(pathm.GetLogFile())
                lastLogTemp = recentLog.split("|")
                detail = lastLogTemp[-1]

            if gap_m > 1:
                pieceInfo = self.GetStart.text()+"|"+self.GetFinish.text() + \
                    "|"+str(gap_m)+"|" + detail
                self.pieceInfo = pieceInfo
                # self.bingoLabel.setVisible(True)
                infoProto = 'T0:' + self.GetStart.text() + '\n' \
                    + 'T1:' + self.GetFinish.text() + '\n' \
                    + 'Gap:' + str(gap_m) + '\n' \
                    + 'Detail:' + detail
                reply = QMessageBox.question(self, 'Save Message',
                                             infoProto, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.emitPiece()
                    self.close()
                    print('emit')
                    event.accept()
                else:
                    event.ignore()
        except:
            self.__reset__()

    def isCancle(self):
        self.close()

    def closeEvent(self, event):
        return

    # 静态方法
    @staticmethod
    def GetPieceInfo(self):
        return self.pieceInfo

    # 信号发射
    def emitPiece(self):
        self.signal_PieceInfo.emit(self.pieceInfo)
        self.GetStart.setDateTime(QDateTime.currentDateTime())
        self.GetFinish.setDateTime(QDateTime.currentDateTime())
        self.pieceInfo = ""

    def __reset__(self):
        # self.bingoLabel.setVisible(False)
        self.GetStart.setDateTime(QDateTime.currentDateTime())
        self.GetFinish.setDateTime(QDateTime.currentDateTime())
        self.pieceInfo = ""

    def GetRecentLog(self, logfile):
        # 参数检查 用try替换
        recentPiece = str()
        try:
            with open(logfile, mode="r", encoding="utf-8") as f:
                allIn = f.readlines()
                cnt = -1
                while (allIn[cnt].endswith('\n') and len(allIn[cnt]) == 1):
                    cnt -= 1
                    if cnt < -10:
                        break
                if not cnt < -10:
                    recentPiece = allIn[cnt]
        except:
            pass
        return recentPiece


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MultiInputDialog()
    if dialog.exec_():
        hs = int(dialog.GetStart.text())
        ls = int(dialog.GetFinish.text())
        print(hs, ls)
