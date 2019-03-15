#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  17:18


from functools import wraps


def parse(func):
    @wraps(func)
    def wraper(*args, **kwargs):
        print(func.__name__)
        r = func(*args, **kwargs)
        return r
    return wraper


@parse
def print_name():
    return 1


if __name__ == '__main__':
    print(print_name())
