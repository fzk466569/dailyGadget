#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  15:04


def reverse(num):
    if not num:
        return
    flag = 1 if num > 0 else -1
    num = num if num > 0 else num * flag
    res = 0
    shang = num / 10
    yu = num % 10
    res += yu
    while shang:
        yu = shang % 10
        shang /= 10
        res = res * 10 + yu

    return res * flag


if __name__ == '__main__':
    print(reverse(-123))
