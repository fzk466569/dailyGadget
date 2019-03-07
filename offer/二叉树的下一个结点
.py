#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  12:01
# 二叉树的下一个结点


class Node(object):
    def __init__(self, v, p, l, r):
        self.v = v
        self.parent = None
        self.left = None
        self.right = None


def func(root):
    """

    :param root: Node
    :return:
    """
    if root.right:
        return root.right
    elif root.parent and root.parent.left is root:
        temp = root.parent
        while temp.left:
            temp = temp.left
        return temp
    elif root.parent and root.parent.right is root:
        while True:
            temp = root.parent
            if temp.parent.left is temp:
                return temp
            return None
    else:
        return 'fuck'
