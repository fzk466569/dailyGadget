#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  13:46

import os

for file_name in os.listdir('.')[:-1]:
    with open(file_name) as f:
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        data = f.readline()[2:] + '.py'
        print(data)
        os.rename(file_name, data)
