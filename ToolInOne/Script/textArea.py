# -*- coding:utf-8 -*-
__author__ = "Peace4Lv"
__date__ = "2021-1-10"
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *


import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QLabel
from random import randint


class textArea(QWidget):
    def __init__(self):
        super().__init__()
        self.SetupUI()

    def SetupUI(self):
        mainlayout = QVBoxLayout()
        self.textarea = QLabel()
        mainlayout.addWidget(self.textarea)
        if False:
            changebutton = QPushButton("change")
            mainlayout.addWidget(changebutton)
            changebutton.clicked.connect(self.__clickedFcn)
        self.setLayout(mainlayout)
        # self.setGeometry(100, 200, 600, 200)

    def ModifyText(self, flag='h1', infoIn=''):
        if flag == 'h1':
            showtext = '''<h1 style = "color:#0D0D0D;font-size:20px;font-weight:bold;">''' + \
                infoIn + '''</h1>'''
        elif flag == 'h2':
            showtext = '''<h2 style = "color:#0D0D0D;font-size:18px;font-weight:bold;">''' + \
                infoIn + '''</h1>'''
        elif flag == 'p':
            showtext = ''' < p style = "color:#00868B;font-size:16PX;font-weight:bold;" > ''' + \
                infoIn + ''' < /p >'''
        else:
            showtext = ''' < p style = "color:#00868B;font-size:16PX;font-weight:bold;" > ''' + \
                'text area' + ''' < /p >'''
        self.textarea.setText(showtext)

    def __clickedFcn(self):
        flags = ['h1', 'h2', 'p']
        self.ModifyText(flag=flags[randint(0, 2)],
                        infoIn="也许世界就这样<hr>也许世界就这样<hr>也许世界就这样")

    def mouseDoubleClickEvent(self, event):
        self.ModifyText(flag='other',
                        infoIn="information area")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = textArea()
    demo.show()
    sys.exit(app.exec_())
