# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:42:38 2018

@author: joao

1)
Given a nested list alist (i.e., a list which may contain lists which themselves may contain
other lists, and so on), write a recursive Python function flatten(alist) that returns a single
list with each of the non-list elements, in order of occurrence. This process is known as list
flattening.
Save the program in the file flatten.py
For example:
● flatten(['Hello', [2, [[], False]], [True]]) returns the list: ['Hello',
2, False, True]
● flatten([[]]) returns the list: []
"""
def flatten(alist):
    result = []
    for element in alist:
        if type(element) == list:
            result += flatten(element)
        else:
            result.append(element)
    return result

print(flatten(['Hello', [2, [[], False]], [True]]))
print(flatten([[[[]]]]))


