#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  17:31
# 回文数


def is_palindrome(data):
    if data < 0:
        return False
    if data < 10:
        return True
    temp = 0
    while data > temp:
        temp = temp * 10 + data % 10
        data /= 10
    return data == temp or data == temp / 10


if __name__ == '__main__':
    print is_palindrome(343)
