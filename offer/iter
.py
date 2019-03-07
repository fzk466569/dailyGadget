#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:55
# iter

from collections import Iterable


class A(Iterable):
    def __init__(self, name, age, obj):
        self.name = name
        self.age = age
        self.obj = [1, 2, 3, 4, 5, 6, 7, 8]

    def __iter__(self):
        for x in self.obj:
            yield x
            raise StopIteration


if __name__ == '__main__':
    a = A('fzk', 16, None)
    for x in a:
        print(x)
