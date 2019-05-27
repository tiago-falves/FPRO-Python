# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:28:44 2018

@author: Gustavo
"""


def anagrams(alist):
    result=[]
    m=0
    for i in alist:
        result.append([])
        result[m].append(i)
        result1=[]
        for j in alist:
            if i!=j:
                f= list(i.lower().replace(" ",""))
                f.sort()
                g= list(j.lower().replace(" ",""))
                g.sort()
                if f==g:
                    result1.append(i)
                    result1.append(j)
                    alist.remove(j)
        for p in result1:
            if p not in result[m]:
                result[m].append(p)
        result[m]=sorted(result[m])
        m+=1
    result=sorted(result, key=lambda x:x[0].lower())            
    return result
    
                    
                    
                    
print(anagrams(["they see", "eat", "The eyes", "car has", "ate", "acrash", "tea"]))






