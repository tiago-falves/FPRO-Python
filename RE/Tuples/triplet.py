def triplet(atuple):
    idx=(len(atuple),len(atuple),len(atuple))
    resultado=()
    for i in range(len(atuple)-2):
        for j in range(i+1,len(atuple)-1):
            for k in range(j+1,len(atuple)):
                if atuple[i]+atuple[j]+atuple[k]==0 and (i,j,k)<idx:
                    idx=(i,j,k)
                    resultado=(atuple[i],atuple[j],atuple[k])
    return resultado
