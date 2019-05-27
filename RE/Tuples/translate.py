def translate(astring,table):
    d={}
    s=""
    for i in table:

        d[i[0]]=i[1]
    for i in astring:
        if i in d:
            s+=str(d[i])
        else:
            s+=i
    return s
