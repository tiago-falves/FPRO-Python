def fetch_middle(lists):
    l=[]
    for i in lists:
        if len(i)%2==0:
            l.append((i[len(i)//2-1]+i[len(i)//2])/2)
        else:
            l.append(i[len(i)//2])
    return l
