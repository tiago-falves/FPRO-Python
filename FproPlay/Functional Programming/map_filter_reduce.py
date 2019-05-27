def map_filter_reduce(lst, f1, f2, f3):
    from functools import reduce
    return reduce(f3,map(f2,filter(f1,lst)))
