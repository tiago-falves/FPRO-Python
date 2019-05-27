#4. Crazy letter soup

def extra(matrix,word,c,l):   
   
    if len(word)==0:
        return True
    
           
    if l+1<len(matrix) and matrix[l+1][c]==word[0]:
        return extra(matrix,word[1:],c,l+1)
    
    elif l+1<len(matrix) and c+1<len(matrix) and matrix[l+1][c+1]==word[0]:
        return extra(matrix,word[1:],c+1,l+1)
            
    elif c+1<len(matrix) and matrix[l][c+1]==word[0]:
        return extra(matrix,word[1:],c+1,l)
    
    elif l+1<len(matrix) and c-1>=0 and matrix[l+1][c-1]==word[0]:
        return extra(matrix,word[1:],c-1,l+1)
            
    elif l-1>=0 and c+1<len(matrix) and matrix[l-1][c+1]==word[0]:
        return extra(matrix,word[1:],c+1,l-1)
    
    elif c-1>=0 and matrix[l][c-1]==word[0]:
        return extra(matrix,word[1:],c-1,l)
            
    elif l-1>=0 and c-1>=0 and matrix[l-1][c-1]==word[0]:
        return extra(matrix,word[1:],c-1,l-1)
    
    elif l-1>=0 and matrix[l-1][c]==word[0]:
        return extra(matrix,word[1:],c,l-1)


def soup(matrix, word):
    
    for i in range(len(matrix)):      
        for j in range(len(matrix[0])):
        
            if matrix[i][j]==word[0] and extra(matrix,word[1:],j,i)==True:
                return chr(65+i)+str(j+1)
mx = (('X', 'A', 'B', 'N', 'T', 'O'),('Y', 'T', 'N', 'R', 'I', 'T'),('U', 'P', 'O', 'M', 'D', 'S'),('I', 'O', 'H', 'U', 'O', 'O'),('R', 'T', 'E', 'L', 'Q', 'X'),('I', 'W', 'J', 'K', 'P', 'Z'))
print(soup(mx, 'PORTO'))
    
