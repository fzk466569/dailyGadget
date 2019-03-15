#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  16:40


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxarea, l, r = 0, 0, len(height) - 1
    while l < r:
        maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxarea


if __name__ == '__main__':
    data = [1, 23, 1, 2, 32, 3, 6]
    print(maxArea(data))
