#2. Calculator

def calculator(expr):
    if not isinstance(expr, tuple):
        return expr
        
    if expr[1] == "*":
        return calculator(expr[0]) * calculator(expr[2])
    elif expr[1] == "+":
        return calculator(expr[0]) + calculator(expr[2])
    elif expr[1] == "/":
        return calculator(expr[0]) / calculator(expr[2])
    elif expr[1] == "-":
        return calculator(expr[0]) - calculator(expr[2])
print(calculator(((1, '+', 2), '*', 3)))