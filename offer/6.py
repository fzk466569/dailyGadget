#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:05
# 跳台阶


def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return func(n - 1) + func(n - 2)


if __name__ == '__main__':
    print(func(3))
    print(func(4))
