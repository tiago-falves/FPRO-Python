def greatest(num):
    s=""
    num=list(str(num))
    num=sorted(num,key=None,reverse=True)
    for i in num:
        s+=str(i)
    return int(s)
    