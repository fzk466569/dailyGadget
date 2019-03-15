#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  12:28


def func(prices):
    if len(prices) < 2:
        return 0
    max_p = 0
    min_p = prices[0]
    for x in prices[1:]:
        if max_p < x - min_p:
            max_p = x - min_p
        if min_p > x:
            min_p = x
    return max_p


if __name__ == '__main__':
    print(func([7, 1, 5, 3, 6, 4]))
