#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  18:36


class MaxHeap(object):
    def __init__(self, size):
        self.data = [None] * (size + 1)
        self.count = 0
        # self.data = [None, 890, 370, 424, 164, 360, 185, 396, 125, 157, 308]
        # self.count = 10

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def insert(self, item):
        self.data[self.count + 1] = item
        self.count += 1
        self.shift_up(self.count)

    def extract_max(self):
        res = self.data[1]
        self.data[1] = self.data[self.count]
        self.count -= 1
        self.shift_down(1)
        return res

    def shift_up(self, k):
        while k > 1:
            if self.data[k] > self.data[k / 2]:
                self.data[k], self.data[k / 2] = self.data[k / 2], self.data[k]
                k /= 2
            else:
                break

    def shift_down(self, h):
        while 2 * h <= self.count:
            cr = 2 * h
            # 如果有右孩子并且右孩子大于左孩子
            if cr + 1 <= self.count and self.data[cr + 1] > self.data[cr]:
                cr += 1
            if self.data[cr] > self.data[h]:
                self.data[cr], self.data[h] = self.data[h], self.data[cr]
            else:
                break
            h = cr


if __name__ == '__main__':
    import random
    mh = MaxHeap(100)
    for x in xrange(100):
        mh.insert(random.randint(1, 1000))
    print(mh.data)
    print mh.extract_max()
    print(mh.data)
