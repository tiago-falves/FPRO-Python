def mult(M,N):
    r=[]
    if len(M[0])==len(N):
        for i in range(len(M)):
            s=[]
            soma=0
            for j in range(len(N[i])):
                soma=0
                for k in range(len(M[i])):
                    soma+=M[i][k]*N[k][j]
                s.append(soma)
            r.append(s)
    return r
