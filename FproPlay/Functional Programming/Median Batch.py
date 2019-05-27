def batch_norm(alist, batch_size):
    lista=[]
    alist1=alist.copy()
    for i in range(len(alist)//batch_size):
        l=[]
        if len(alist1)<batch_size:
            yield alist1
        else:
            for j in range(batch_size):
                l.append(alist1[j])
            alist1=alist1[batch_size:]
        yield list(map(lambda x:x -sum(l)//len(l),l))

print(list(batch_norm([10, 1, -12, 5, 1, 3, 7, 3, 3], 5)))