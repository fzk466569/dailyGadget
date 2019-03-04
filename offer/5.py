#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:05
# 斐波那契数列


def mem(func):
    cache = dict()

    def wrap(*args, **kwargs):
        if args in cache:
            return cache.get(args)
        else:
            cache[args] = func(*args, **kwargs)
        return cache[args]

    return wrap


@mem
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return func(n - 1) + func(n - 2)


if __name__ == '__main__':
    print(func(29))
    print(func(30))
    print(func(31))
    print(func(32))
    print(func(33))
    print(func(34))
