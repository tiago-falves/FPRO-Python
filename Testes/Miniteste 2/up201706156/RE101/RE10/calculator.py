# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:42:41 2018

@author: joao

2)
Write a function calculator(expr) that given an expression expr computes its value. The
expression expr is a nested tuple composed of (tuple/integer, operator, tuple/integer) or an
integer. The valid operators are: addition (+), subtraction (-) and multiplication (*).
Save the program in the file calculator.py
For example:
● calculator((1, '+', 2)) return the integer 3
● calculator(((1, '+', 2), '*', 3)) return the integer 9
"""
def calculator(expr):
    if type(expr) == int:
        return expr
        
    result = 0
    expr = list(expr)
    
    if type(expr[0]) == tuple:
        expr[0] = calculator(expr[0])
    if type(expr[2]) == tuple:
        expr[2] = calculator(expr[2])

    if expr[1] == '+':
        result = expr[0] + expr[2]

    elif expr[1] == '*':
        result = expr[0] * expr[2]

    elif expr[1] == '-':
        result = expr[0] - expr[2]

    return result            

print(calculator((1, '+', 2)))
print(calculator(((1, '+', 2), '*', 3)))
print(calculator(10))