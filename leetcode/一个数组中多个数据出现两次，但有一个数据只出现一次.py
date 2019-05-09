#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  13:52


def parse(data):
    data = [str(x) for x in data]
    d = '^'.join(data)
    return eval(d)


if __name__ == '__main__':
    print(parse([1, 2, 3, 1, 2, 3, 4]))
