def is_orthogonal(mx):
    l=[]
    m=[]
    for i in range(len(mx)):
        soma=0
        l=[]
        for j in range(len(mx[i])):
            soma=0
            for k in range(len(mx)):
                soma+=mx[i][k]*mx[k][j]
            l.append(soma)
        m.append(l)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i==j:
                if m[i][j]!=1:
                    return False
            else:
                if m[i][j]!=0:
                    return False
                
    return True
