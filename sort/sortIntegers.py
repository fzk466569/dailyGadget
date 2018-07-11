#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  17:04


def sortIntegers(A):
    length = len(A)
    for x in range(length):
        min_index = x
        for y in range(x, length):
            if A[min_index] > A[y]:
                min_index = y
        A[min_index], A[x] = A[x], A[min_index]
    return A


if __name__ == '__main__':
    print(sortIntegers([1, 2, 2, 3, 4, 5, 2]))
