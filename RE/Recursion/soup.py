def soup(matrix,word):
    linhas="ABCDEF"
    colunas="123456"
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if word[0]==matrix[i][j] and extra(matrix,word[1:],i,j)==True:
                return linhas[i]+colunas[j]
    return None
def extra(matrix,word,i,j):
    if len(word)==0:
        return True
    else:
        for k in range(i-1,i+2):
            for w in range(j-1,j+2):
                if k>=0 and w>=0 and k<len(matrix) and w<len(matrix[0]):
                    if matrix[k][w]==word[0]:
                        if extra(matrix,word[1:],k,w)==False:
                            continue
                        else:
                            return extra(matrix,word[1:],k,w)
        return False
        
mx = (('X', 'A', 'B', 'N', 'T', 'O'),('Y', 'T', 'N', 'R', 'I', 'T'),('U', 'P', 'O', 'M', 'D', 'S'),('I', 'O', 'H', 'U', 'O', 'O'),('R', 'T', 'E', 'L', 'Q', 'X'),('I', 'W', 'J', 'K', 'P', 'Z'))
