#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 8/18/19 2:42 PM
# @Author  : lkx-rog
# @Project : DataAnalysis
# @File    : 4.3
# @Software: PyCharm
# 面向数组
import numpy as np
import matplotlib.pyplot as plt


def array_oriented():
    points = np.arange(-5, 5, 0.01)
    xs, ys = np.meshgrid(points, points)
    print("ys\n", ys)

    z = np.sqrt(xs ** 2 + ys ** 2)
    print("z\n", z)

    plt.imshow(z, cmap=plt.cm.gray)
    plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
    plt.show()


def condition_logic():
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])
    result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
    print("result:\n", result)

    result1 = np.where(cond, xarr, yarr)
    print("result1:\n", result1)
    arr = np.random.randn(4, 4)
    print("arr:\n", arr)
    print("where(arr>0, 2, -2):\n", np.where(arr > 0, 2, -2))
    print("where(arr>0, 2, arr):\n", np.where(arr > 0, 2, arr))


def unit_queue():
    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    print("name", np.unique(names))
    print(np.in1d(names, ['Joe', 'Will']))


if __name__ == '__main__':
    unit_queue()
