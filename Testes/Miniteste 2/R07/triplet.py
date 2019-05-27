def triplet(atuple):
    index=(len(atuple),len(atuple),len(atuple))
    for i in range(len(atuple)-2):
        for j in range(i+1,len(atuple)-1):
            for k in range(j+1,len(atuple)):
                if atuple[i]+atuple[j]==-atuple[k]:
                    if (i,j,k)<index:
                        index=(i,j,k)
                        s=(atuple[i],atuple[j],atuple[k])
    if index==(len(atuple),len(atuple),len(atuple)):
        s=()
    return s
