#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  16:59


def reverseInteger2(number):
    # python2
    gewei = number / 100
    shiwei = number % 100 / 10
    baiwei = number % 10
    new_num = gewei + shiwei * 10 + baiwei * 100
    return int(new_num)


def reverseInteger3(number):
    # python3
    gewei = number // 100
    shiwei = number % 100 // 10
    baiwei = number % 10
    new_num = gewei + shiwei * 10 + baiwei * 100
    return int(new_num)


if __name__ == '__main__':
    print(reverseInteger2(123))
    print(reverseInteger3(123))
