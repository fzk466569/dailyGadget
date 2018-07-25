#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  15:15


def merge_sort(data):
    length = len(data)
    if length <= 1:
        return data
    mid = length // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


def merge(left, right):
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    data = [1, 23, 2, 31, 23, 21, 3, 12, 4, 12, 3, 12, 3, 1, 24]
    print(merge_sort(data))
