#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 8/19/19 10:42 PM
# @Author  : lkx-rog
# @Project : DataAnalysis
# @File    : 4.4
# @Software: PyCharm
import numpy as np


def save_load_demo():
    arr = np.arange(10)
    np.save('some_array', arr)


if __name__ == '__main__':
    save_load_demo()
    print(np.load('some_array.npy'))
