# -*- coding:utf-8 -*-
__author__ = "Peace4Lv"
__date__ = "2021-03-29"

'''
    数据备份
    1.数据比较
    2.数据拷贝
'''
import os
import sys
from shutil import copy
import path
from datetime import datetime

tic = datetime.now().microsecond
toc = tic

while toc - tic < 1000:
    toc = datetime.now().microsecond

# toc = datetime.now().microsecond
print((toc-tic))

print('数据备份')
