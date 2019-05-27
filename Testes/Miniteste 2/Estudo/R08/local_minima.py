def local_minima(alist,n):
    l=[]
    for i in range(n//2):
        k=0
        for j in range(n//2+i+1):
            if j!=i:

                if alist[i]>alist[j] or (j<i and alist[j]==alist[i]) :
                    k+=1
                
        if k==0:
            l.append((alist[i],i))
        
    for i in range(n//2,len(alist)-n//2):
        k=0
        for j in range(i-(n//2),i+(n//2)+1):
            
            if j!=i:
                 if alist[i]>alist[j] or (j<i and alist[j]==alist[i]):
                    k+=1
        if k==0:
            l.append((alist[i],i))
    for i in range(len(alist)-n//2,len(alist)):
        k=0
        for j in range(-n//2+i,len(alist)):
            if j!=i:
                if alist[i]>alist[j] or (j<i and alist[j]==alist[i]):
                    k+=1
        if k==0:
            l.append((alist[i],i))
    return l
print(local_minima([0, 3, 3, 14, 5, 7, 4], 3))
                
                    
                    
                    
        