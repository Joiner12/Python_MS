# -*- coding:utf-8-*-
__author__ = "Peace4Lv"
__date__ = "2021-01-05"

"""
    reference:
    1.online color picker:https://www.w3cschool.cn/tools/index?name=cpicker

"""
# 按钮样式-1
buttonStyle_1 = (
    "QPushButton{border-radius:4px;font-size:16px;font-weight:bold;color:rgb(2, 9, 34);}"
    "QPushButton{border:2px solid rgb(118,154,40);}"
    "QPushButton:hover{background:rgb(118,154,40);}"
)

# 按钮样式-2 enable = False
buttonStyle_2 = (
    "QPushButton{border-radius:4px;font-size:16px;font-weight:bold;color:#ff5500;}"
    "QPushButton{border:2px solid rgb(118,154,40);}"
    "QPushButton:hover{background:rgb(118,154,40);}"
)

buttonStyle_3 = (
    "QPushButton{border-radius:4px;font-size:16px;font-weight:bold;color:#ff5500;}"
    "QPushButton{border:2px solid rgb(118,154,40);}"
    "QPushButton:hover{background:rgb(118,154,40);}"
)

buttonStyle_4 = (
    "QPushButton{font-size:16px;font-weight:bold;color:yellow;font-family:SimHei;}"
    "QPushButton{background-color:#4D8AB3;}"
    "QPushButton{border-radius: 10px;min-width: 10em;padding: 6px;}"
    "QPushButton:hover{background:rgb(118,154,40);}"
)
# select area style
selectAreaStyle = (
    "QListWidget{font-size:16px;font-weight:bold;color:rgb(67, 9, 34);}"
    "QListWidget{border:4px;border-radius:4px;}"
    "QListWidget{background-color:transparent;}"
)

"""
"""
# button style
buttonStyle_5 = ("QPushButton{border: none; color: white; }"
                 '''QPushButton{border: none;border-bottom: 1px solid white;font-size: 18px;font-weight: 700;
                 font-family: "Helvetica Neue", Helvetica, Arial, sans-serif}'''
                 "QPushButton: hover{border-left: 4px solid red; font-weight: 700;}")

button_close_style = (
    "QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}")
button_mini_style = (
    "QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}")
button_max_style = (
    "QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}")

right_widget_style = ('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

right_recommend_widget_style = '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            '''
right_playconsole_widget_style = '''
            QPushButton{
                border:none;
            }
        '''

left_widget_style = ('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QWidget#left_widget{
            background:gray;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
        }
        ''')

right_bar_widget_search_input_style = (
    '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
        }''')
