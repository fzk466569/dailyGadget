#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  11:47
# 顺时针打印矩阵


def func(m):
    q = []

    def up2down(x, y):
        q.append(m[x][y + 1])

    def down2up(x, y):
        q.append(m[x][y - 1])

    def left2right(x, y):
        q.append(m[x+1][y])

    def right2left(x, y):
        q.append(m[x-1][y])

    rows = len(m)
    cols = len(m[0])
    for i in range(rows):
        left2right(0, i)
        for j in range(cols, step=-1):




if __name__ == '__main__':
    matrix = [range(0, 5), range(5, 10), range(10, 15), range(15, 20)]
    print(func(matrix))
