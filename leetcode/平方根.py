#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  15:51


def parse(num):
    if num <= 1:
        return num
    else:
        d_min, d_max = 1, num
        tmp = 1
        while d_max - d_min > 1:
            if tmp * tmp <= num:
                d_min = tmp
            elif tmp * tmp == num:
                return tmp
            else:
                d_max = tmp
            tmp = (d_min + d_max) / 2
        return tmp


if __name__ == '__main__':
    print(parse(2))
