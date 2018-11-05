#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:27


def parse(data, ori=''):
    '''
    :param data:iterable
    :param ori:str
    :return: None
    '''
    for n in range(len(data)):
        for y in range(n + 1, len(data[n:])):
            result.append(' '.join((ori, ''.join(data[:y]), ''.join(data[y:]))))
            if len(data[y:]) > 2:
                parse(data[y:], ''.join(data[:y]))


if __name__ == '__main__':
    data = 'abcd'
    # data.split()
    result = []     # 这是一个全局变量
    # data = ['a', 'b', 'c', 'd', 'e']
    parse(data)
    result = set([x.strip() for x in result])
    print(result)
    print(len(result))
