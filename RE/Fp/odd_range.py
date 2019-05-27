def odd_range(start,stop,step):
    if start%2==0:
        start+=1
    for i in range(start,stop,2*step):
        if i%2!=0:
            yield i
