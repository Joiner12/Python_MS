# -*- coding:utf-8-*-
__author__ = "Peace4Lv"
__date__ = "2021年1月31日"

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome


class commonTools(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._setupUI()

    def _setupUI(self):
        commonToollayout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.setLayout(commonToollayout)

        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("apple-alt")  # 设置按钮文本
        self.recommend_button_1.setIcon(
            qtawesome.icon('fa.star', color='red'))  # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(90, 90))  # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.recommend_button_2 = QtWidgets.QToolButton()
        self.recommend_button_2.setText("apple-alt")
        self.recommend_button_2.setIcon(
            qtawesome.icon('fa.share', color='red'))
        self.recommend_button_2.setIconSize(QtCore.QSize(90, 90))
        self.recommend_button_2.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_3 = QtWidgets.QToolButton()
        self.recommend_button_3.setText("apple-alt")
        self.recommend_button_3.setIcon(
            qtawesome.icon('fa.shopping-basket', color='red'))
        self.recommend_button_3.setIconSize(QtCore.QSize(90, 90))
        self.recommend_button_3.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_4 = QtWidgets.QToolButton()
        self.recommend_button_4.setText("apple-alt")
        self.recommend_button_4.setIcon(
            qtawesome.icon('fa.space-shuttle', color='red'))
        self.recommend_button_4.setIconSize(QtCore.QSize(90, 90))
        self.recommend_button_4.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_5 = QtWidgets.QToolButton()
        self.recommend_button_5.setText("apple-alt")
        self.recommend_button_5.setIcon(
            qtawesome.icon('fa.angle-double-up', color='red'))
        self.recommend_button_5.setIconSize(QtCore.QSize(90, 90))
        self.recommend_button_5.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextUnderIcon)

        commonToollayout.addWidget(self.recommend_button_1, 0, 0)
        commonToollayout.addWidget(self.recommend_button_2, 0, 1)
        commonToollayout.addWidget(self.recommend_button_3, 0, 2)
        commonToollayout.addWidget(self.recommend_button_4, 1, 0)
        commonToollayout.addWidget(self.recommend_button_5, 1, 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    demo = commonTools()
    demo.show()
    sys.exit(app.exec_())
