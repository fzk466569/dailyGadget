#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  15:00
# 删除排序数组中的重复项


def func(data):
    if not data:
        return 0

    temp = data[0]
    j = 1
    for i, current in enumerate(data[1:], 1):
        if current != temp:
            data[i], data[j] = data[j], data[i]
            temp = current
            j += 1
    return j


if __name__ == '__main__':
    print(func([1, 1, 2]))
