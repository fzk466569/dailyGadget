#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  11:18
# 翻转单词顺序列

from Queue import deque


def func(s):
    q = deque()
    for x in s.split():
        q.append(x)
    ret = ''
    while q:
        i = q.pop()
        ret += i + ' '
    return ret


if __name__ == '__main__':
    print(func('I am a student'))
