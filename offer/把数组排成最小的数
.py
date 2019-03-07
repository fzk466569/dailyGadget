#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  17:31
# 把数组排成最小的数


def func(numbers):
    if not numbers:
        return ""
    numbers = list(map(str, numbers))
    numbers.sort(cmp=lambda x, y: cmp(x + y, y + x))
    return '0' if numbers[0] == '0' else ''.join(numbers)


if __name__ == '__main__':
    print(func([213, 124321, 324123, 2314, 5]))
    print(cmp('5', '10'))
