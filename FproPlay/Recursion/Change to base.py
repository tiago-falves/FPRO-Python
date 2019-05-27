def rec_to_base(n,base):
    abc="0123456789ABCDEF"
    if n//base<1:
        return abc[n%base]
    return str(rec_to_base(n//base,base)) +abc[n%base]
