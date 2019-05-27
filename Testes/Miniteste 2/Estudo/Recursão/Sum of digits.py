# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:39:32 2018

@author: tiago
"""

def rec_sum_digits(n):
    n=str(n)
    if len(n)==1:
        return n
    return int(n[0])+int(rec_sum_digits(int(n[1:])))
print(rec_sum_digits(45))