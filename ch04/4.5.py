#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 8/19/19 10:55 PM
# @Author  : lkx-rog
# @Project : DataAnalysis
# @File    : 4.5
# @Software: PyCharm
import numpy as np
from numpy.linalg import inv, qr


def algebra_demo():
    x = np.array([[1., 2., 3.], [4., 5., 6.]])
    y = np.array([[6., 23.], [-1, 7], [8, 9]])
    print("x*y\n", x.dot(y))
    print(np.dot(x, y))
    print(x @ y)


def linalg_demo():
    X = np.random.randn(5, 5)
    print("X:\n", X)
    mat = X.T.dot(X)
    print("inv(mat):\n", inv(mat))
    print("mat.dot(inv(mat)):\n", mat.dot(inv(mat)))
    q, r = qr(mat)
    print("r:\n", r)


if __name__ == '__main__':
    linalg_demo()
