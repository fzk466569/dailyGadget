#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  18:25


class Node(object):
    def __init__(self, v):
        self.v = v
        self.next = None


def fun1(root):
    p = root
    q = root.next
    p.next = None

    while q:
        r = q.next
        q.next = p
        p, q = q, r
    return p


def fun2(root):
    pass


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    root1 = fun(n1)
    node = root1.next
    while node:
        print(node.v)
        node = node.next

