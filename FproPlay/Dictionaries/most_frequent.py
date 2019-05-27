def most_frequent(alist):
    d={}
    
    for i in alist:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    a=min(d)
    maxi=max(d.values())
    for i in d:
        if d[i]==maxi:
            if i>a:
                a=i
    return a