def rotate_list(l):
    for j in range(3):
        a=l[0]
        for i in range(len(l)-1):
            l[i]=l[i+1]
        l[len(l)-1]=a
    return l
