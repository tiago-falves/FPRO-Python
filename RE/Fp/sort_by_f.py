def sort_by_f(l):
    return sorted(l,key=lambda x:5-x if x>=5 else x)
def map_reduce(n1,n2):
    from functools import reduce
    return [x**2  for x in range(n1,n2)]
print(map_reduce(0, 10))
            