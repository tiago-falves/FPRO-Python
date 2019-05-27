def no_consecutives1(k):
    a=0
    b=0
    lista=[]
    for i in range(2**k):
        a=str(bin(i))
        a=a[2:]
        a=a.zfill(3)
        lista.append(a)
    for j in range(len(lista)):
        a=0
        for k in range(len(lista[j])-1):
            if lista[j][k]=="1" and lista[j][k+1]=="1":
                a+=1
            else:
                continue
        if a==0:
            b+=1
    return b
