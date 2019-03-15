#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  16:07
# 最长公共前缀


def func(data):
    if not data:
        return
    a, b = min(data), max(data)
    for x in range(len(a)):
        if a[x] != b[x]:
            return a[:x]
    else:
        return a


if __name__ == '__main__':
    print(func(['a', 'aa']))
