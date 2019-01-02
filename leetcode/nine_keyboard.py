#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:06

# from itertools import product 这个函数很好用，不过算法应该是不能这么用的


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    shuju = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    digits = list(digits)
    res = [i for i in shuju[digits[0]]]
    for i in digits[1:]:
        res = [m+n for m in res for n in shuju[i]]
    return res


if __name__ == '__main__':
    print(letterCombinations('43'))
