def batch_norm(alist,batch_size):
    l=[]
    m=[]
    for i in range(len(alist)):
        l=[]
        if len(alist)<=batch_size:
            m.append(alist)
            break
        else:       
            for j in range(batch_size):
                l.append(alist[j])
            m.append(l)
            alist=alist[batch_size:]
    for i in range(len(m)):
        m[i]=list(map(lambda x: x-sum(m[i])//len(m[i]),m[i]))
        yield m[i]
    
print(list(batch_norm([10, 1, -12, 5, 1, 3, 7, 3, 3], 5)))