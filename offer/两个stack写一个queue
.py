#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  12:39
# 两个stack写一个queue


class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, v):
        self.stack1.append(v)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            if not self.stack1:
                raise Exception()
            else:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


