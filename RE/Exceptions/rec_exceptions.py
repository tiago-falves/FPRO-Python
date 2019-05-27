def rec_exceptions(l):
    a=[]
    for i in l:
        try:
            i()
        except Exception as error:
            a+=[error]
        else:
            a+=rec_exceptions(i())
    return a
