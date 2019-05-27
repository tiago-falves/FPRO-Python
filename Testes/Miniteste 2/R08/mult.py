def mult (M,N):
    
    if len(N)!=len(M[0]):
        
        return []
    else:
        soma=0
        b=[]
        for i in range (len(M)):
            a=[]
            for j in range(len(N[i])):
                soma=0
                for k in range(len(M[i])):
                    soma+=M[i][k]*N[k][j]
                a.append(soma)
            b.append(a)
        return b
print(mult([[0, 1, 2], [2, 1, 0], [4, 1, 3], [1, 6, -2]], [[2, 1], [7, 8], [2, -10]]))