#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  16:36


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        data = []
        d = {'{': '}', '(': ')', '[': ']'}
        for x in s:
            if x in d.keys():
                data.append(x)
            else:
                if not data:
                    return False
                tmp = data.pop(-1)
                if x != d[tmp]:
                    return False
        if not data:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('))[]}'))
