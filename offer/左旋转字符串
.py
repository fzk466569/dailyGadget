#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:30
# 左旋转字符串


def func(s1, k):
    if not s1:
        return
    else:
        return s1[:k:-1] + s1[:k + 1]


if __name__ == '__main__':
    print(func('123456', 2))
