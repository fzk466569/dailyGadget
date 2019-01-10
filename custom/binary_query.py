#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:59


def binary_search(datas, target):
    l, r = 0, len(datas)
    while l <= r:
        mid = l + (r - l) / 2
        if datas[mid] > target:
            r = mid - 1
        elif datas[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1


def ceil(datas, target):
    l, r = 0, len(datas)
    while r - l > 1:
        mid = l + (r - l) / 2
        if datas[mid] > target:
            r = mid
        elif datas[mid] < target:
            l = mid
        else:
            return mid
    if r - l == 1:
        return l


if __name__ == '__main__':
    datas = range(2, 10, 3)
    # i = binary_search(datas, 30)
    i = ceil(datas, 6)
    print(datas[i])
