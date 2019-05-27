def translate(astring,table):
    a=""
    for i in astring:
        k=0
        for j in table:
            if i==j[0]:
                a+=str(j[1])
                k+=1
        if k==0:
            a+=i
    return a
