def collisions(alist):
    d={}
    for hash1 in alist:
        n=hash1
        soma=0
        for i in range(len(str(hash1))):
            a=n%10
            n=n//10
            soma+=a
        soma=soma%8
        if soma not in d:
            d[soma]=1
        else:
            d[soma]+=1
    
    return d
        