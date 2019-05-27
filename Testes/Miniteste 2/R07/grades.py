# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:16:58 2018

@author: Carlos Lousada
"""

def sort_grades(records):
    from statistics import mean as media
    result = tuple(sorted(sorted(sorted(records, key = lambda x : x[1]), key = lambda y : y[0]), key = lambda z : media(z[2]), reverse = True))
    return result