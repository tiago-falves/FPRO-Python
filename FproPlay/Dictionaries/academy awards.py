def academy_awards(alist):
    d={}
    for i in alist:
        if i[1] not in d:
            d[i[1]]=1
        else:
            d[i[1]]+=1
    return d
            
