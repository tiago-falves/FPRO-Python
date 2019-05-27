def uppercase(astring):
    import string
    for i in astring[0:3]:
        if i==i.upper() and i not in string.punctuation:
            return astring.upper()
    return astring
