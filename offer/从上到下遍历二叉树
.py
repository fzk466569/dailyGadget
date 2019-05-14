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


def parse(root):
    """

    :param root: TreeNode
    :return:
    """
    data = []
    if not root:
        return
    cur = [root]
    data.append([node.val for node in cur])
    next_nodes = []
    while cur:
        for node in cur:
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)
        cur = next_nodes
        next_nodes = []
        if cur:
            data.append([node.val for node in cur])
    return data
