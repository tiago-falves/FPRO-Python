def uppercase(astring):
    import string
    k=0
    for i in range(3):
        if astring[i]==astring[i].upper() and astring[i] not in string.punctuation:
            
            k+=1
    if k!=0:
        return astring.upper()
    else:
        return astring
