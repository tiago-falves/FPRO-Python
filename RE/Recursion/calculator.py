def calculator(expr):
    if type(expr).__name__!="tuple":
#        
#        if expr[1]=="+":
#            return expr[0]+expr[2]
#        elif expr[1]=="*":
#            return expr[0]*expr[2]
#        elif expr[1]=="-":
#            return expr[0]-expr[2]

        return expr
    
    
    else:
        
        if expr[1]=="+":
            return calculator(expr[0])+expr[2]
        elif expr[1]=="*":
            return calculator(expr[0])*expr[2]
        elif expr[1]=="-":
            return calculator(expr[0])-expr[2]

