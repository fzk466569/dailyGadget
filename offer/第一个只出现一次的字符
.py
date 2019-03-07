#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  16:11
# 第一个只出现一次的字符


def func(s):
    res = []
    kv = {}.fromkeys(s, 0)
    for x in s:
        kv[x] += 1
    for k, v in kv.items():
        if v == 1:
            res.append(k)
    return res


if __name__ == '__main__':
    data = 'asfshakgsdhfjsfbjvhasfnweuhvbkfjsdkafhksaj'
    print(func(data))
