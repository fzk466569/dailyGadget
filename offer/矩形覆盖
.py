#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:20
# 矩形覆盖


def func(n):
    # n 表示2*n里边的n
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return func(n - 1) + func(n - 2)


if __name__ == '__main__':
    print(func(3))
