def sort_by_value(dict):
    a=[(i,dict[i]) for i in dict]
    return sorted(a,key=lambda x: x[0])
