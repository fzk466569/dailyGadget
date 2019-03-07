#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:27
# 在O(1)时间删除链表结点


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


def func(root, del_node):
    if not del_node:
        return
    if root is del_node:
        root.next = None
        return root.next
    elif del_node.next is None:
        p = root.next
        while p:
            if p.next is del_node:
                p.next = None
            p = p.next
    return root


if __name__ == '__main__':
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node4 = ListNode(15)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    func(node1, node3)
    print(node3.val)
    func(node1, node3)
    print(node3.val)
    print(node2.val)
    func(node1, node1)
    print(node1.val)
    func(node1, node1)
    print(node1.val)
