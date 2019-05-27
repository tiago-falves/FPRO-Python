def min_path(matrix,a,b,visited=[]):
    best=100
    cont=0
    for i in range(a[0]-1,a[0]+2):
        for j in range(a[1]-1,a[1]+2):
            if (i,j)==b:
                return cont         
            if i>=0 and j>=0 and i<len(matrix) and j<len(matrix[0]) and (i,j)!=a:
                if matrix[i][j]==False:
                    matrix[i][j]=True
                    cont+=1
                    cont+=min_path(matrix,(i,j),b,visited)
                    if cont<best:
                        best=cont
                else:
                    continue
                
    return best
#mx = [[False]*4,[False, True, False, False],[False, True, False, False],[False]*4]
            
                    
                    
            