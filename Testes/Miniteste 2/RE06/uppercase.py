def uppercase(astring):  
    import string
    if astring[0] in string.punctuation or astring[1] in string.punctuation or astring[2] in string.punctuation:
        return astring
    else:
        if astring[0]== astring[0].upper() or astring[1]== astring[1].upper() or astring[2]== astring[2].upper():
            astring=astring.upper()
        return astring
