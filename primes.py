# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 18:21:54 2020

@author: stuar
"""


for i in range(4,10):
    for n in range(1,i):
        if i % n != 0:
            continue
        else:
            print(i)
            break