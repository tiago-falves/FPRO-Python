def flatten(alist):
    lista=[]
    for i in alist:
        if type(i).__name__=="list":
            lista+= flatten(i)
        else:
            lista.append(i)
    return lista
