# -*- coding:utf-8-*-
__author__ = "Peace4love"
__date__ = "2020年12月22日"

import sys
from datetime import datetime
import os
import re
# 查看WiFi账号密码


def ShowWifi():
    a = datetime.now().strftime("%A, %d. %B %Y %I:%M %p")
    print(a)
    try:
        f1 = os.popen("netsh wlan show profiles")
    except:
        print("error")
    if not f1 is None:
        f = f1.read()
        ftemp = list()
        # configall = re.findall("所有用户配置文件 : [\w]*", f, re.M)
        configall = re.findall("(?<=所有用户配置文件 : )(.*)", f, re.M)
        print("WIFI connection found in PC number is %d \n" % (len(configall)))
        for j in configall:
            j_key = FindKey(j)
            print(j, ":", j_key)
        f1.close()
    print("task finished")


def FindKey(name=""):
    if not len(name) > 0:
        cmdline = "echo not a valid key connection"
        f = os.popen(cmdline)
        # print(f.read())
        f.close()
        keyword_prt = "did not find password"
    else:
        cmdline = 'netsh wlan show profile name=\"'+name+'\" key=clear'
        f1 = os.popen(cmdline)
        f2 = f1.read()
        f1.close()
        try:
            keyword_prt = re.findall("(?<=关键内容            : )(.*)", f2, re.M)
            keyword_prt = keyword_prt[0]
        except:
            keyword_prt = "did not find password"
    return keyword_prt


if __name__ == "__main__":
    ShowWifi()
