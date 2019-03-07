#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  16:45
# 连续子数组的最大和


def func(array):
    max_ending_here = max_so_far = array[0]
    for x in array[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


if __name__ == '__main__':
    print(func([1, 23, 2, -11, 23, 12, -123, 123, 213, -45, 325]))
