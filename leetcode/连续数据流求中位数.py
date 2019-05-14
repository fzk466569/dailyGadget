#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:27
# python 内置的heapq只能实现最小堆
#
# 构建一个最大堆和一个最小堆，分别存储比中位数小的数和大的数。当目前两堆总数为偶数的时候，把数字存入最大堆，然后重排最大堆，如果最大堆的堆顶数字
# 大于最小堆堆顶数字，则把两个堆顶数字交换，重排两堆，此时两堆数字总数为奇数，直接输出最大堆堆顶数字即为中位数；如果当前两堆总数为技术的时候，
# 把数字存入最小堆，重排最小堆，如果最大堆的堆顶数字大于最小堆堆顶数字，则把两个堆顶数字交换，重排两堆，此时两堆数字总数为偶数，
# 取两堆堆顶数字做平均即为中位数。

import heapq


class MinHeap(object):
    def __init__(self):
        self.data = list()

    def insert(self, val):
        heapq.heappush(self.data, val)

    def pop(self):
        return heapq.heappop(self.data)

    def heapify(self):
        heapq.heapify(self.data)

    def get_top(self):
        if not self.data:
            return
        return self.data[0]


class MaxHeap(object):
    def __init__(self):
        self.data = list()

    def insert(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)

    def heapify(self):
        heapq.heapify(self.data)

    def get_top(self):
        if not self.data:
            return
        return -self.data[0]


def parse(datas):

    min_heap = MinHeap()
    max_heap = MaxHeap()
    max_heap.insert(datas[0])
    min_heap.insert(datas[1])
    flag = True
    for i, v in enumerate(datas[2:], 1):
        if i % 2 != 0:
            flag = False
            max_heap.insert(v)
            if max_heap.get_top() > min_heap.get_top():
                max_tmp, min_tmp = max_heap.pop(), min_heap.pop()
                max_heap.insert(min_tmp)
                min_heap.insert(max_tmp)
        else:
            flag = True
            min_heap.insert(v)
            if max_heap.get_top() > min_heap.get_top():
                max_tmp, min_tmp = max_heap.pop(), min_heap.pop()
                max_heap.insert(min_tmp)
                min_heap.insert(max_tmp)
    if flag:
        res = (min_heap.get_top() + max_heap.get_top()) / 2.0
    else:
        res = max_heap.get_top()
    return res


if __name__ == '__main__':
    import random
    # min_heap = MinHeap()
    values = range(0, 150)
    random.shuffle(values)
    print(parse(values))
