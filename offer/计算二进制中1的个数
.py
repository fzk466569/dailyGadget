#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:26
# 计算二进制中1的个数


def func(num):
    a = 0
    while num:
        num = num & (num - 1)
        a = a + 1
    return a


if __name__ == '__main__':
    print(func(10))
