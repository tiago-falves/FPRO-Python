def unique(atuple):
    s=()
    for i in range(len(atuple)):
        k=0
        for j in range(i+1,len(atuple)):
            if atuple[i]==atuple[j]:
                k+=1
        if k==0:
            s+=(atuple[i],)
    s=tuple(sorted(s))
    return s
        

            
            