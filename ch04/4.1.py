#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 7/14/19
# @Author  : lkx-rog
# @Project : DataAnalysis
# @File    : 4.1.py
# @Software: PyCharm

import numpy as np


def index_ndarray():
    arr = np.arange(10)
    arr_slice = arr[5:8]
    print(arr)
    arr_slice[1] = 123456
    print(arr)

    arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print("arr3d:\n", arr3d)
    print("arr3d[0]:\n", arr3d[0])

    old_value = arr3d[0].copy()

    arr3d[0] = 42
    print("arr3d:\n", arr3d)

    arr3d[0] = old_value
    print("arr3d:\n", arr3d)

    print("arr3d[1, 0]:\n", arr3d[1, 0])


# ndarray 多维数组对象
def gen_ndarray():
    data = np.random.randn(2, 3)
    print(data)
    print(data * 10)
    print(data + data)
    print(data.shape)
    print(data.dtype)

    # 生成ndarray
    data1 = [6, 7.5, 8, 0, 1]
    arr1 = np.array(data1)
    print(arr1)

    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr2 = np.array(data2)
    print(arr2)


# numpy 算数计算
def numpy_cal():
    arr = np.array([[1., 2., 3.], [4., 5., 6.]])
    print('arr:\n', arr)
    print('arr*arr:\n', arr * arr)
    print('arr-arr:\n', arr - arr)
    print('1/arr:\n', 1 / arr)
    print('arr**0.5:\n', arr ** 0.5)
    arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
    print(arr2)
    print('arr2>arr:\n', arr2 > arr)


def boolean_index():
    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'bob'])
    data = np.random.randn(7, 4)
    print('names == "Bob" :\n', names == 'Bob')
    print('data:\n', data)
    print("data[names == 'Bob']: \n", data[names == 'Bob'])

    mask = (names == 'Bob') | (names == 'Will')
    print('mask:\n', mask)

    data[data < 0] = 0
    print('data>0:\n', data)


def magic_index():
    arr = np.empty((8, 4))
    for i in range(8):
        arr[i] = i
    print('arr:\n', arr)

    print('\narr[[4, 3, 0, 6]]:\n', arr[[4, 3, 0, 6]])
    print('\narr[[-3, -5, -7]]:\n', arr[[-3, -5, -7]])

    new_arr = np.arange(32).reshape((8, 4))
    print('\nnew_arr:\n', new_arr)
    print('\nnew_arr[[1, 5, 7, 2], [0, 3, 1, 2]]:\n', new_arr[[1, 5, 7, 2], [0, 3, 1, 2]])
    print('\nnew_arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]:\n', new_arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])


def transpose_axis():
    arr = np.arange(15).reshape((3, 5))
    print("arr:\n", arr)
    print('arr.T:\n', arr.T)

    new_arr = np.random.randn(6, 3)
    print('\nnew_arr:\n', new_arr)
    print('arr.T*arr:\n', np.dot(new_arr.T, new_arr))

    arr = np.arange(16).reshape((2, 2, 4))
    print('arr:\n', arr)
    print('\narr.T:\n', arr.T)
    print('\narr.transpose((1, 0, 2)):\n', arr.transpose((1, 0, 2)))


if __name__ == '__main__':
    transpose_axis()