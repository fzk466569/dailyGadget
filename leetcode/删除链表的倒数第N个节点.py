#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  12:45
# 删除链表的倒数第N个节点


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def func(root, n):
    if not n:
        return root
    if not root.next:
        return

    i = 0
    node = root
    pre_node = None
    while node.next:
        node = node.next
        i += 1
        if i == n:
            pre_node = root
        elif i > n:
            pre_node = pre_node.next

    if pre_node:
        pre_node.next = pre_node.next.next
    else:
        return root.next
    return root


if __name__ == '__main__':
    root = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    root.next = node1
    node1.next = node2
    node2.next = node3
    r = func(root, 2)
    while r:
        print 'r.next', r.val
        r = r.next

