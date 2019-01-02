#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  15:40


def get_data(num1='', num2=''):
    a = 0
    res = ''
    if len(num1) < len(num2):
        num1 = num1.zfill(len(num2))
    else:
        num2 = num2.zfill(len(num1))
    for n in range(len(num1) - 1, -1, -1):
        tmp = int(num1[n]) + int(num2[n]) + a
        a = tmp / 10    # 商
        b = tmp % 10    # 余数
        res = str(b) + res
    if a:
        res = str(a) + res
    return res


if __name__ == '__main__':
    print get_data('123456789', '98765432123456789')
