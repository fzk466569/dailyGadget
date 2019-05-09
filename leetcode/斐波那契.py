#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  17:03


def cache(func):
    data = {}

    def wrap(n):
        print(data)
        if n in data:
            res = data[n]
        else:
            res = func(n)
        data[n] = res
        return res
    return wrap


@cache
def parse(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return parse(n - 1) + parse(n - 2)


if __name__ == '__main__':
    print(parse(50))
