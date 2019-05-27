def rm_letter_rev(l, astr):
    a=astr.replace(l,"")
    s=""
    for ch in a:
        s= ch +s
    return s
