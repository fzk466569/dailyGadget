#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  15:18
# 合并两个有序数组


def func(l1, m, l2, n):
    # 并不规范，新开辟了m+n个空间
    if not l1 or not l2:
        return l2 or l1

    data = []
    i = 0
    j = 0
    while i < m and j < n:
        print(l1[i], l2[j])

        if l1[i] < l2[j]:
            data.append(l1[i])
            if i < m:
                i += 1
        else:
            data.append(l2[j])
            if j < n:
                j += 1
    if i >= m:
        data.extend(l2[j:])
    else:
        data.extend(l1[i:])
    return data


if __name__ == '__main__':
    print(func([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
