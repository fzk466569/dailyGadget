#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  18:32
# 两个可迭代对象中的相同字符


def func(s1, s2):
    data = {}.fromkeys(s1, 0)
    for x in s2:
        if x in data:
            data[x] = 1
    for k, v in data.items():
        if v == 1:
            print(k)
    return


if __name__ == '__main__':
    s1 = 'fzk'
    s2 = 'fks'
    func(s1, s2)
