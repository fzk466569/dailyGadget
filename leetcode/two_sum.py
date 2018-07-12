#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  18:06


def two_sum(array, value):
    for i, x in enumerate(array):
        num = value - x
        if num in array:
            return [i, array.index(num)]
    return [-1, 1]


if __name__ == '__main__':
    array = [2, 7, 11, 15]
    print(two_sum(array, 9))
