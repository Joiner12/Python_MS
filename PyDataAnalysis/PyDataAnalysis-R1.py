#-*- coding:utf-8 -*-
__author__ = "Risky Jr"
__date__ = "2020-5-29"
"""
    Python for data analysis
"""

import numpy as np


def Ufunc_1():
    arr_a = np.arange(5)
    arr_asqrt = np.sqrt(arr_a)
    arr_exp = np.exp(arr_a)

    ax = np.arange(-2, 2, 0.01)
    ay = np.arange(-2, 2, 0.01)
    axx, ayy = np.meshgrid(ax, ay)
    sm = axx**2
    print(axx.shape, axx.ndim, sm.shape)
    print("this is a pause line")


if __name__ == "__main__":
    Ufunc_1()