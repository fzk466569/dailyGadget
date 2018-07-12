#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  16:24


def fun(a, b):
    yu = a & b
    yihuo = a ^ b
    while yu:
        temp = yu << 1
        yu = yihuo & temp
        yihuo = yihuo ^ temp
    return yihuo


if __name__ == '__main__':
    print(fun(12, 8))
