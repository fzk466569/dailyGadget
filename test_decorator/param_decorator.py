#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  17:30
# 带参装饰器


def param(name):
    def tag(func):
        def wrapper(text):
            value = func(text)
            print(func.__name__)
            return '{name}{value}{name}'.format(name=name, value=value)
        return wrapper
    return tag


@param('HTML')
def my_upper(text):
    value = text.upper()
    return value


if __name__ == '__main__':
    print(my_upper('sss'))
