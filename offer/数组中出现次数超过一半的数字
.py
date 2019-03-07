#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  17:16
# 数组中出现次数超过一半的数字


class DefaultDict(dict):
    def __missing__(self, key):
        return 0


def func(l):
    hash = DefaultDict()
    for x in l:
        hash[x] += 1

    length = len(l)
    for k, v in hash.items():
        if v > length / 2:
            return k
    return 0


if __name__ == '__main__':
    print(func([1, 2, 3, 4, 5, 1, 2, 3, 2, 2, 2, 2, 2, 22, 2]))
