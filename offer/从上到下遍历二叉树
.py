#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  15:15
# 从上到下遍历二叉树


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def func(root):
    A = []
    result = []
    if not root:
        return result
    A.append(root)
    while A:
        current_root = A.pop(0)
        result.append(current_root.val)
        if current_root.left:
            A.append(current_root.left)
        if current_root.right:
            A.append(current_root.right)

