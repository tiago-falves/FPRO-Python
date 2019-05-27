def raise_exception(alist, value):
    l=[]
    for i in alist:
        try:
            if i<=value:
                raise ValueError('{} is not greater than {}'.format(i,value))
        except ValueError as error:
            l.append(error)
    return l
