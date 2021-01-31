# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from buttonstyle import*


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(1024, 600)
        # 窗口主部件
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        # 左侧部件
        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置布局为网格
        # 右侧部件
        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)
        # 部件排列
        self.main_layout.addWidget(
            self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占12行2列
        self.main_layout.addWidget(
            self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占12行10列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        """
            无边框相关模块
        """
        # self.left_close = QtWidgets.QPushButton("") # 关闭按钮
        self.left_close = QtWidgets.QPushButton(
            qtawesome.icon('fa.times', color='white'), "")
        # self.left_visit = QtWidgets.QPushButton("") # 空白按钮
        self.left_visit = QtWidgets.QPushButton(
            qtawesome.icon('fa.square-o', color='white'), "")
        # self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_mini = QtWidgets.QPushButton(
            qtawesome.icon('fa.minus', color='white'), "")
        self.left_close.clicked.connect(self.close_window)  # 关联
        self.left_mini.clicked.connect(self.showMinimized)

        self.left_label_1 = QtWidgets.QPushButton("常用工具")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("音乐工具")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("Reserved")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(
            qtawesome.icon('fa.signal', color='white'), "VPN")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(
            qtawesome.icon('fa.wifi', color='white'), "WIFI Checker")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(
            qtawesome.icon('fa.download', color='white'), "MusicTool")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(
            qtawesome.icon('fa.home', color='white'), "...")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(
            qtawesome.icon('fa.download', color='white'), "...")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(
            qtawesome.icon('fa.heart', color='white'), "...")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(
            qtawesome.icon('fa.comment', color='white'), "...")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(
            qtawesome.icon('fa.star', color='white'), "...")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(
            qtawesome.icon('fa.question', color='white'), "遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)

        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        # 顶部搜索框部件
        self.right_bar_widget = QtWidgets.QWidget()
        self.right_bar_layout = QtWidgets.QGridLayout()
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' '+'搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("搜索工具....")

        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(
            self.right_bar_widget_search_input, 0, 1, 1, 8)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

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

        self.right_recommend_layout.addWidget(self.recommend_button_1, 0, 0)
        self.right_recommend_layout.addWidget(self.recommend_button_2, 0, 1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_5, 0, 4)

        self.right_layout.addWidget(self.right_recommend_widget, 1, 0, 2, 9)

        self.right_playconsole_widget = QtWidgets.QWidget()  # 播放控制部件
        self.right_playconsole_layout = QtWidgets.QGridLayout()  # 播放控制部件网格布局层
        self.right_playconsole_widget.setLayout(self.right_playconsole_layout)

        self.console_label = QtWidgets.QLabel("information")

        self.right_playconsole_layout.addWidget(self.console_label, 0, 0)
        self.right_playconsole_layout.setAlignment(
            QtCore.Qt.AlignCenter)  # 设置布局内部件居中显示

        self.right_layout.addWidget(self.right_playconsole_widget, 10, 0, 1, 9)

        self.left_close.setFixedSize(16, 16)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(16, 16)  # 设置按钮大小
        self.left_mini.setFixedSize(16, 16)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(button_close_style)
        self.left_visit.setStyleSheet(button_max_style)
        self.left_mini.setStyleSheet(button_mini_style)

        self.left_widget.setStyleSheet(left_widget_style)

        self.right_bar_widget_search_input.setStyleSheet(
            right_bar_widget_search_input_style)

        self.right_widget.setStyleSheet(right_widget_style)
        self.right_recommend_widget.setStyleSheet(
            right_recommend_widget_style)
        self.right_playconsole_widget.setStyleSheet(
            right_playconsole_widget_style)

        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setAutoFillBackground(False)  # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        self.main_layout.setSpacing(0)

    # 无边框的拖动
    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    # 关闭按钮动作函数
    def close_window(self):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
