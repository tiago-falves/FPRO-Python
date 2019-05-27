def interleave(alist1,alist2):
    lista=[]
    if len(alist1)<len(alist2):
        alist2=alist2[:len(alist1)]
    else:
        alist1=alist1[:len(alist2)]
    for i in range(len(alist1)):
        if type(alist1[i]).__name__!="list":
            lista+=[alist1[i]]
            lista+=[alist2[i]]
        else:
            lista+=interleave(alist1[i],alist2[i])
    return lista
