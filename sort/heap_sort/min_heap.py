#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  18:31


class MinHeap(object):
    def __init__(self, size):
        self.data = [None] * (size + 1)
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def shift_up(self, k):
        while k > 1:
            if self.data[k] < self.data[k / 2]:
                self.data[k], self.data[k / 2] = self.data[k / 2], self.data[k]
                k /= 2
            else:
                break

    def shift_down(self, k):
        while k < self.count:
            cr = 2 * k  # child_right
            if cr < self.count and self.data[cr] > self.data[cr + 1]:
                cr += 1
            if self.data[k] > self.data[cr]:
                self.data[cr], self.data[k] = self.data[k], self.data[cr]
            else:
                break
            k = cr

    def insert(self, item):
        self.data[self.count + 1] = item
        self.count += 1
        self.shift_up(self.count)

    def extract_min(self):
        if self.is_empty():
            return
        else:
            res = self.data[1]
            self.data[1] = self.data[self.count]
            self.count -= 1
            self.shift_down(1)
            return res


if __name__ == '__main__':
    import random
    mh = MinHeap(10)
    for x in range(10):
        mh.insert(random.randint(0, 100))
    print(mh.data)
    mh.extract_min()
    print(mh.data)

