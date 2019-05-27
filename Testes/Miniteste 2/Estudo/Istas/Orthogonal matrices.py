def is_orthogonal(mx):
    m=mx.copy()
    v=[]

    n=[]
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            if i>j:
                (m[i][j],m[j][i])=(m[j][i],m[i][j])
    for i in range(len(mx)):
        soma=0
        v=[]
        for j in range(len(mx[i])):
            soma=0
            
            for k in range(len(mx)):
                soma+=m[i][k]*m[k][j]
            v.append(soma)
        n.append(v)
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            if i==j:
                if n[i][j]!=1:
                    return False
            else:
                if n[i][j]!=0:
                    return False
    return True
       