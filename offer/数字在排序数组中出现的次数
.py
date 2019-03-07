#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:35
# 数字在排序数组中出现的次数


def func(n, l1):
    count = 0
    while True:
        length = len(l1)
        mid = length / 2

        if l1[mid] < n:
            l1 = l1[mid:]
        elif l1[mid] > n:
            l1 = l1[:mid]
        else:
            for v in l1:
                if v == n:
                    count += 1
            break

    return count


if __name__ == '__main__':
    print(func(1, [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 6, 7]))
    print(func(2, [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 6, 7]))
    print(func(3, [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 6, 7]))
    print(func(5, [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 6, 7]))
