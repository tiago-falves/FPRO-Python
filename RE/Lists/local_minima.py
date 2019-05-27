def local_minima(alist,n):
    final=[]
    for i in range(len(alist)):
        if i<n//2:
            frase=alist[0:i+n//2]
            if alist[i]==min(frase):
                final.append((alist[i],i))
        else:
            frase=alist[i-n//2:i+n//2+1]
            if alist[i]==min(frase):
                final.append((alist[i],i))
    
    for j in range(1,n+1):
        for i in range(len(final)-j):
            if final[i][0] == final[i+1][0] and int(final[i][1])+j == int(final[i+1][1]) and n!=1:
                final.remove(final[i+1])
                break
    return final

print(local_minima([1, 5, 5, 2, 10, 10, 3], 1))
            