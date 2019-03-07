#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  12:24
# 判断二叉树是否为左右对称二叉树


def is_mirror(l_node, r_node):
    if l_node is None and r_node is None:
        return True
    elif l_node and r_node:
        return l_node.v == r_node.v and is_mirror(l_node.left, r_node.right) and is_mirror(l_node.right, r_node.left)
    return False


def func(root):
    if not root:
        return True
    else:
        return is_mirror(root.left, root.right)





