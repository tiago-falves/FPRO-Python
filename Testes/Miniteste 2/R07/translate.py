def translate(astring, table):
    s=""
    
    for i in astring:
        k=0
        for j in table:
            if i==str(j[0]):
                s+=str(j[1])
                k+=1
        if k==0:
            s+=i
    return s
