def mult(M,N):
    l=[]
    m=[]
    if len(M[0])!=len(N):
        return []
    else:
        for i in range(len(M)):
            l=[]
            for j in range(len(N[i])):
                soma=0
                for k in range(len(M[i])):
                    soma+=M[i][k]*N[k][j]
                l.append(soma)
            m.append(l)
    return m
print(mult([[0, 1, 2], [2, 1, 0], [4, 1, 3], [1, 6, -2]], [[2, 1], [7, 8], [2, -10]]))