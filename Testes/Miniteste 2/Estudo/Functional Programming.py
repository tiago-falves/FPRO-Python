def sort_by_f(l):
    return sorted(l,key =lambda x:5-x if x>=5 else x)
def map_reduce(n1,n2):
    import functools
    return functools.reduce(lambda z,y:  z*y if z*y<50 else z+y,[x**2 for x in range(n1,n2) if x%2!=0])
def odd_range(start, stop, step):
    for i in range(start,stop,step):
        if i%2!=0:
            yield i
def override(l1, l2):
    lista=[]
    for i in l1:
        k=0
        for j in l2:
            if j[0]==i[0]:
                k+=1
        if k==0:
            lista.append(i)
    return l2+lista
def map_filter_reduce(lst, f1, f2, f3):
    import functools   
    return functools.reduce(f3,map(f2,filter(f1,lst)))
def batch_norm(alist, batch_size):
    l=[]
    for i in range(0,len(alist),batch_size):
        l.append(alist[i:i+batch_size])
    for j in l:
        if len(j)%2==0:
            median=(j[len(j)//2]+j[len(j)//2-1])/2
        else:
            median=j[len(j)//2]
        for k in range(len(j)):
            j[k]=j[k]-median
        yield j
    
print(batch_norm([-1, 0, 1, 1, 2, 4], 3))
        
    
    
    
        
        