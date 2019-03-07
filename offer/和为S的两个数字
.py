#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  11:36
# 和为S的两个数字


def func(l, sum):
    data = {}
    for i in l:
        if sum - i in l:
            if sum - i not in data:
                data[i] = sum - i
    d = sorted(data.keys())
    min1 = data[d[0]] * d[0]
    min2 = data[d[-1]] * d[-1]
    return min(min1, min2)


if __name__ == '__main__':
    datas = range(1, 20)
    sum_of_data = 15
    print(func(datas, sum_of_data))
