def rearrange(l):
    return list(filter(lambda x: x<=0,l))+list(filter(lambda y: y>0,l))