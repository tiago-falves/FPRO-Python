def soup(matrix,word):

    
    def extra(matrix,word,i,j):
        if len(word)==0:
            return True
        for k in range(i-1,i+2):
            for l in range(j-1,j+2):
                if k>=0 and l >= 0 and k < len(matrix) and l < len(matrix[0]):
                    if word[0]==matrix[i][j]:
                        return extra(matrix,word[1:0],i,j)
        else:
            return False

    a=(1,2,3,4,5,6)
    b=("A","B","C","D","E","F")
    for i in range(len(matrix)):       
        for j in range(len(matrix[i])):
            if extra(matrix,word,i,j):
                return str(b[i])+str(a[j])
                

mx = (('X', 'A', 'B', 'N', 'T', 'O'),('Y', 'T', 'N', 'R', 'I', 'T'),('U', 'P', 'O', 'M', 'D', 'S'),('I', 'O', 'H', 'U', 'O', 'O'),('R', 'T', 'E', 'L', 'Q', 'X'),('I', 'W', 'J', 'K', 'P', 'Z'))         
print(soup(mx, 'HOTEL'))       
            