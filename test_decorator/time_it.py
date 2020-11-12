#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:39
from functools import wraps
import time


def clock(f):
    @wraps(f)
    def clockd(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        print('f.__name__: ', f.__name__)
        end = time.time()
        print('func {0} 耗时 {1} seconds'.format(f.__name__, end - start))
        return result

    return clockd


@clock
def test(times):
    time.sleep(times)
    return 'sssssssss'


if __name__ == '__main__':
    times = 1
    print(test(times))
    print(test.__name__)
