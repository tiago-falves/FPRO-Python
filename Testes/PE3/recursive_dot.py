def recursive_dot(l1,l2):
    soma=0
    for i in range(len(l1)):
        if type(l1[i]).__name__!="list":
            soma+=l1[i]*l2[i]
        else:
            soma+=recursive_dot(l1[i],l2[i])
    return soma
