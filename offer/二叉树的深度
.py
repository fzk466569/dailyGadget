#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  11:28
# 二叉树的深度


class Node(object):
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


def func(root):
    """

    :param root: Node
    :return:
    """
    if not root:
        return 0
    elif not root.left and root.right:
        return 1
    else:
        return max(func(root.left), func(root.right)) + 1

