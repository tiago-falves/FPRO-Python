def fetch_middle(lists):
    """gosto de sopa"""
    
    l=[]
    for i in lists:
        if len(i)%2==0:
            l.append((i[len(i)//2]+i[len(i)//2-1])/2)
        else:
            l.append(i[len(i)//2])
    return l
            
lists=[[1,2,3],[4,5,6],[7,8,9,10]]
print(fetch_middle(lists))