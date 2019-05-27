def add_item(tup,idx,item):
    tup=list(tup)
    if idx==0:
        tup[0]=item
    elif idx==len(tup)-1:
        tup[len(tup)-1]=item
    else:    
        tup.insert(idx,item)
    return tuple(tup)
