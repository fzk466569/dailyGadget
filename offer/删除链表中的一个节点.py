#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  11:45


class Node(object):
    def __init__(self, v):
        self.v = v
        self.next = None


class Solution(object):
    def __init__(self):
        pass

    def delete(self, node):
        '''

        :param node: Node
        :return: None
        '''
        next_node = node.next
        node.v = next_node.v
        node.next = next_node.next
