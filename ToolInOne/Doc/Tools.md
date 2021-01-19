# Tool In One

​	使用PyQt将常用的小功能集合在一个软件中，方便调用管理。

- 电脑WiFi密码查看；
- VPN脚本启动；
- 壁纸管理（下载|重命名）
- ....

## 主页设计



![设计](D:\Softwares\TyporaPic\设计-1609680626663.png)



## lyrics board

效果图：

![lyricboard](D:\Softwares\TyporaPic\lyricboard.png)



思路：

根据lyrics文件时间戳，生成对应背景图片。



## you-get downloader

输入视频链接→选择视频格式→下载视频到指定文件夹



## issue

1. 按键点击绑定事件无法在模块外部响应；
2. 脚本无法正常启动外部程序（使用popen启用进程，脚本运行结束之后进程同时关闭）；
3. setstylesheet完全用法[Qt Style Sheets Examples — Qt for Python](https://doc.qt.io/qtforpython/overviews/stylesheet-examples.html)
4. ...



## Reference

[zetcode-pyqt5](http://zetcode.com/gui/pyqt