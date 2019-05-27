def rm_letter_rev(l,astr):
    a=""
    for i in range(-1,-len(astr)-1,-1):

        if astr[i]!=l:
            a+=astr[i]           
    return a
