#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:51

from collections import OrderedDict


class LRUCache(object):
    def __init__(self):
        self.size = 5
        self.data = OrderedDict()

    def get(self, k):
        if k in self.data.keys():
            tmp = self.data[k]
            del self.data[k]
            self.data[k] = tmp
            return self.data[k]
        else:
            return -1

    def insert(self, k, v):
        if len(self.data) >= self.size:
            self.data.popitem(last=False)
            self.data[k] = v
        else:
            self.data[k] = v


if __name__ == '__main__':
    lru = LRUCache()
    lru.insert(2, 3)
    lru.insert(3, 3)
    lru.insert(4, 3)
    lru.insert(5, 3)
    lru.insert(6, 3)
    lru.insert(7, 3)
    lru.insert(8, 3)
    lru.insert(9, 3)
    lru.insert(10, 3)
    print(lru.data)
