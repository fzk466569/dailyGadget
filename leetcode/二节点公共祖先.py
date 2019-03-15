#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:24


def LowestParent(root, p, q):
    stack = [root]
    par_child = {root: None}
    while stack:
        node = stack.pop()
        if node.left:
            par_child[node.left] = node
            stack.append(node.left)
        if node.right:
            par_child[node.right] = node
            stack.append(node.right)
    res = set()
    while p:
        res.add(p)
        p = par_child[p]
    while q not in res:
        q = par_child[q]
    return q
