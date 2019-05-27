def flatten(alist):
    r=[]
    for i in alist:
        if type(i).__name__!="list":
            r+=[i]
        else:
            r+=flatten(i)
    return r
