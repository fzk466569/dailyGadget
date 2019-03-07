#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  18:24
# 数组中重复的数字


class Dict(dict):
    def __missing__(self, key):
        return 0


def func(array):
    data = Dict()
    for x in array:
        data[x] += 1
        if data[x] == 2:
            return x
    return 0


if __name__ == '__main__':
    print(func([1, 2, 3, 12, 1, 3, 12, 31, 1]))
