#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:00
# 从尾向头打印value


def printListFromTailToHead(listNode):
    # write code here
    ret = []
    head = listNode[0]
    while head:
        ret.append(head.value)
        head = head.next
    return ret[::-1]

