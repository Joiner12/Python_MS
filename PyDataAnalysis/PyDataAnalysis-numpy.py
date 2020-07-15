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

    ax = np.arange(-2, 2, 0.1)
    ay = np.arange(-2, 2, 0.1)
    axx, ayy = np.meshgrid(ax, ay)
    sm = axx**2
    print(axx.shape, axx.ndim, sm.shape)
    print("this is a pause line")


def Func_1():
    xarr = np.array([1.1, 2.1, 3.2, 4.3])
    yarr = np.array([1.2, 2.3, 3.4, 4.5])
    cond = np.array([True, False, True, False])
    condarr = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
    print(condarr)

    condarr_where = np.where(cond, xarr, yarr)
    print(condarr_where)


def Func_2():
    arr = np.random.randn(2, 5)
    print(arr)
    arr_m = np.mean(arr, axis=1)
    print(arr_m)
    arr_m = arr.mean()
    arr_std = arr.std()

    arr_m = np.mean(arr)
    arr_std = np.std(arr)


def Func_3():
    arr = np.array([False, False, True, False])
    # arr = np.array([0, 0, 1, 0])
    ans1 = arr.sum()
    print(ans1)
    ans2 = arr.any()
    print(ans2)
    ans3 = arr.all()
    print(ans3)


def Func_4():
    arr = np.random.randn(10)
    print(arr)
    arr.sort()
    print(arr)


if __name__ == "__main__":
    Func_4()