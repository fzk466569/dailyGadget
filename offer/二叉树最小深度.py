#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:56


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def parse(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif not root.left:
        return parse(root.right) + 1
    elif not root.right:
        return parse(root.left) + 1
    else:
        return min(parse(root.left), parse(root.right))


def parse_board(root):
    depth = 0
    cur = [root]
    next_layer = []
    while cur:
        depth += 1
        for node in cur:
            if not node.left or not node.right:
                return depth + 1
            else:
                next_layer.append(node.left)
                next_layer.append(node.right)
        cur = next_layer
    return 0

