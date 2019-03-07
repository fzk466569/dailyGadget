#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  15:17
# 旋转数组的最小数字


def converse(l):
    while l[0] > l[-1]:
        length = len(l)
        mid = length / 2
        if l[mid] < l[0]:
            l = l[:mid + 1]
            break
        else:
            l = l[mid:]
    t = l[0]
    for x in l:
        if x < t:
            return x
        else:
            t = x
    return 0


if __name__ == '__main__':
    print(converse([6, 7, 8, 1, 2, 3, 4, 5]))
