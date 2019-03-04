#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  13:46
# 二叉树的镜像


class Solution:
    def Mirror(self, root):
        if root is None:
            return
        self.Mirror(root.left)
        self.Mirror(root.right)
        root.left, root.right = root.right, root.left
