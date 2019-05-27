def collisions(alist):
    d={}
    for i in alist:
        soma=0
        for j in str(i):
            soma+=int(j)
        soma=soma%8
        if soma not in d:
            d[soma]=1
        else:
            d[soma]+=1
    return d
