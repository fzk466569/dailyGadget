#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:55


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def Print(self, pRoot):
        # write code here
        if not pRoot.left and not pRoot.right:
            return pRoot.val
        stack1 = []
        stack1.append(pRoot)
        output = []
        is_ou = False
        while (len(stack1) > 0):
            print(type(stack1[0]), type(stack1))
            temp = []
            temp_len = len(stack1)
            # print(temp_len)
            for i in range(temp_len):
                out_node = stack1.pop(0)
                # print(out_node.left,'hsihidsd')
                if out_node.left is not None:
                    stack1.append(out_node.left)
                if out_node.right is not None:
                    stack1.append(out_node.right)
                temp.append(out_node.val)
            # print(stack1)
            if not is_ou:
                output.extend(temp)
            else:
                output.extend(temp[::-1])
            is_ou = ~is_ou

        return output

    def Print2(self, root):
        if not root.left and not root.right:
            return root.val

        stack = []




if __name__ == '__main__':
    here = TreeNode(8)
    here.left = TreeNode(6)
    here.right = TreeNode(10)
    here.left.left = TreeNode(5)
    here.left.right = TreeNode(7)
    here.right.left = TreeNode(9)
    here.right.right = TreeNode(11)
    print(Solution().Print(here))
