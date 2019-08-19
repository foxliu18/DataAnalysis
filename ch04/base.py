#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 7/14/19
# @Author  : lkx-rog
# @Project : DataAnalysis
# @File    : base.py
# @Software: PyCharm
import numpy as np
import datetime
my_arr = np.arange(1000000)
my_list = list(range(1000000))

if __name__ == '__main__':

    # NumPy的方法比Python方法快

    start_arr = datetime.datetime.now()
    for _ in range(10): my_arr2 = my_arr * 2
    end_arr = datetime.datetime.now()
    print(end_arr - start_arr)

    start_list = datetime.datetime.now()
    for _ in range(10): my_list2 = [x * 2 for x in my_list]
    end_list = datetime.datetime.now()
    print(end_list - start_list)