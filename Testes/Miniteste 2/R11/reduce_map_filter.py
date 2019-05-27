# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 16:27:04 2018

@author: João Gonçalves
"""
from functools import reduce
def reduce_map_filter(args):
    largs= list(args)
    if type(args[2])== tuple:
        largs[2]= reduce_map_filter(args[2])
        return reduce_map_filter(largs)    
    else:
        if args[0]== "map":
            return list(map(args[1], args[2]))
        elif args[0]== "reduce":
            return reduce(args[1], args[2])
        elif args[0]== "filter":
            return list(filter(args[1], args[2]))
        

print(reduce_map_filter(("map", lambda x: 2*x,("filter", lambda x: x%2 != 0,[1,2,3])))) 

