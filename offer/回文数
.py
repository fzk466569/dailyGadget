#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  15:21
# 回文数


def func(s1):
    length = len(s1)
    for i, x in enumerate(s1[:length / 2], 1):
        if x != s1[-i]:
            print(x, s1[-i])
            return False
    return True


if __name__ == '__main__':
    print(func('ssaaaass'))
