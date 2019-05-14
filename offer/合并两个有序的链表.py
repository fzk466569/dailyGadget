#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  11:50


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def __init__(self):
        pass

    def merge(self, root1, root2):
        '''
        :param root1: ListNode
        :param root2: ListNode
        :return: ListNode
        '''
        p, q = root1, root2
        head = ListNode(None)
        cur_node = ListNode(None)
        head.next = cur_node
        while p and q:
            if p.val < q.val:
                cur_node.next = p
                p = p.next
            else:
                cur_node.next = q
                q = q.next
            cur_node = cur_node.next
        return head.next



if __name__ == '__main__':
    pass
