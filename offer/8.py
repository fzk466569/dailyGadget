#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:28
# 把字符串转换成整数


def legal(s):
    if s == '' or s < '0' or s > '9':
        return False
    return True


def func(s):
    status = 0
    flag = 1
    ret = 0
    if s[0] in ('+', '-'):
        status = 1
    for i in s:
        if i == '+':
            if status == 1:
                return 0
            status = 1
            continue
        elif i == '-':
            if status == 1:
                return 0
            status = 1
            flag = -1
        if legal(i):
            alpha = int(i)
            ret = ret * 10 + alpha
        else:
            return 0
    return ret * flag


if __name__ == '__main__':
    print(func('+123+213'))
