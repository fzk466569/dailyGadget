# -*- coding: utf-8 -*-
import random


def quick_part(arr, l, r):
    # 返回值index保证arr[l.....p-1]<=arr[p]<=arr[p+1....r]
    index = l
    for i in range(l + 1, r + 1):
        if arr[i] < arr[l]:
            index += 1
            arr[i], arr[index] = arr[index], arr[i]
    arr[l], arr[index] = arr[index], arr[l]
    return index


def quick(arr, l, r):
    if l >= r:
        return
    index = quick_part(arr, l, r)
    quick(arr, l, index - 1)
    quick(arr, index + 1, r)
    return arr


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(10)]
    # arr = [3, 2, 2, 1, 2, 1, 2, 1, 4]
    print(arr)
    print(quick(arr, 0, 9))
