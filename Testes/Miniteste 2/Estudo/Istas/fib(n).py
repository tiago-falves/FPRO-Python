def fib(n):
    if n==0 or n==1:
        return [0]
    lista=[0,1]
    for i in range(n-2):
        lista+=[lista[i]+lista[i+1]]
    return lista
def nth_lowest(lnum,n):
    for i in range(n-1):
        lnum.remove(min(lnum))
    return min(lnum)
def rotate_list(l):
    
    for i in range(3):
        aux=l[0]
        for j in range(len(l)-1):
            l[j]=l[j+1]
        l[len(l)-1]=aux
    return l
def fetch_middle(lists):
    lista=[]
    for i in lists:
        if len(i)%2!=0:
            lista.append(i[(len(i)-1)//2])
        else:
            lista.append((i[len(i)//2]+i[(len(i)-1)//2])/2)
    return lista
def pattern_hunting(l1, l2, p):
    lista=[]
    for i in range(len(l1)):
        if l1[i].find(p)!=-1:
            lista.append(l2[i])
        if l2[i].find(p)!=-1:
            lista.append(l1[i])
    lista.sort()
    lista.reverse()
    return lista
