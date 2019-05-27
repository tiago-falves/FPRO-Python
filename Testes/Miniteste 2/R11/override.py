# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 17:18:05 2018

@author: João Gonçalves
"""

def override(l1, l2):
     return sorted([i for i in l2] + [i for i in l1 if (i[0] not in (t[0] for t in l2))], key= lambda x:x[0])

print(override([('a','b'),('c','d')], [('b','a'),('d','c')]))
