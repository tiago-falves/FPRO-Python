# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:01:35 2018

@author: Gustavo
"""


def local_minima(alist,n):
    n = n//2
    final = []
    test = []
    for index,num in enumerate(alist):
        if index-n<0:
            test = alist[:index+n+1]
            if num == min(test):
                final += [(num,index)]
        else:
            test = alist[index-n:index+n+1]
            if num == min(test):
                final += [(num,index)] 
    for j in range(1,n+1):
        for i in range(len(final)-j):
            if final[i][0] == final[i+1][0] and int(final[i][1])+j == int(final[i+1][1]):
                final.remove(final[i+1])
                break
    return final
print(local_minima([2, 1, 1, 1, 7, 3, 1], 5))