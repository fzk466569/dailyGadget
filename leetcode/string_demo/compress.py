#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  13:31


def zip_string(iniString):
    # write code here
    print(iniString)
    count = 0
    t = iniString[0]
    rs = ''
    for x in iniString:
        if x == t:
            count += 1
        else:
            if count != 1:
                rs += t + str(count)
            else:
                rs += t
            t = x
            count = 1
    rs += t + str(count)
    return rs


if __name__ == '__main__':
    s = 'aabcccccaaa'
    s1 = 'welcometonowcoderrrrr'
    print(zip_string(s1))
