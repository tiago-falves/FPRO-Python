def rm_letter_rev(l, astr):
    s=""
    astr=astr.replace(l,"")
    for i in astr:
        s=i+s
    return s
