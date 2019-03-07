#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  15:28
# 两个链表的第一个公共结点


class Node(object):
    def __init__(self, v):
        self.v = v
        self.next = None


def func(n1, n2):
    res = None
    stack1 = []
    stack2 = []
    while n1:
        stack1.append(n1)
        n1 = n1.next
    while n2:
        stack2.append(n2)
        n2 = n2.next

    while stack1:
        tmp = stack1.pop()
        if tmp == stack2.pop():
            res = tmp
        else:
            break
    return res


if __name__ == '__main__':
    pass
