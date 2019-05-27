def pattern_hunting(l1, l2, p):
    l=[]
    for i in range(len(l1)):
        if l1[i].find(p)!=-1:
            l.append(l2[i])
        elif l2[i].find(p)!=-1:
            l.append(l1[i])
    return sorted(l,key=None,reverse=True)
