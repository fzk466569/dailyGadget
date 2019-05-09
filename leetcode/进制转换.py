#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  16:59


def parse(num):
    res = 0
    while num:
        d = num % 7
        res = res * 10 + d
        num = num / 7
    return res


if __name__ == '__main__':
    print(parse(100))
