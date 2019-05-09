#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:26
# 计算二进制中1的个数
# 把一个数减去1，再与原来的数进行与运算，将能把最右边的1变成0。这样，一个整数的二进制中有多少个1，就执行多少次。


def func(num):
    a = 0
    while num:
        print num
        num = num & (num - 1)
        a = a + 1
    return a


if __name__ == '__main__':
    print(func(10))
