#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:24


def parse(l=[1, 2]):
    l.append(1)
    return l


def parse2():
    l1 = [1, 2]
    l2 = l1
    l2.append(5)
    print(l1)
    print(id(l1), id(l2))


if __name__ == '__main__':
    # ll = parse()
    # l2 = parse()
    # print(ll, l2)
    parse2()
