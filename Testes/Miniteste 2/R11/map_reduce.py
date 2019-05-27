def map_reduce(n1,n2):    
    import functools
    
    l=[n*n for n in range(n1,n2) if n%2!=0]
    
    return functools.reduce(lambda x,y:x*y if x*y<50 else x+y,l)
    
        
print(map_reduce(25,75))        
        
    
    
    
    
    