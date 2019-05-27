#def soup(matrix, word):
#    for i in range(len(matrix)):
#        for j in range(len(matrix[i])):
#            if matrix[i][j]==word[0]:
#                matrix==[matrix[i-1][j-1:j+1]]
#                
#    
#    return None
a="P"
mx = (('X', 'A', 'B', 'N', 'T', 'O'),('Y', 'T', 'N', 'R', 'I', 'T'),('U', 'P', 'O', 'M', 'D', 'S'),('I', 'O', 'H', 'U', 'O', 'O'),('R', 'T', 'E', 'L', 'Q', 'X'),('I', 'W', 'J', 'K', 'P', 'Z'))
for i in range(len(mx)):
    k=0
    for j in range(len(mx[i])):
        if mx[i][j]=="P":
            mx1=(mx[i-1][j-1:j+1],mx[i,j-1:j+1],mx[i+1,j-1:j+1])
            k+=1
            break
    if k!=0:
        break
print(mx1)

    
            