def map_reduce(n1,n2):
    from functools import reduce
    return reduce(lambda x,y: x*y if x*y<50 else x+y,[x**2 for x in range(n1,n2) if x%2!=0])
    
