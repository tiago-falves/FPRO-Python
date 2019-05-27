#def rec_to_base(n,base):
#    if n==0:
#        return ""
#    else:
#        result=rec_to_base(n//base,base)
#        return str(result)+str(n%base)
def rec_to_base(n,base):
    if n==0:
        return ""    
    return str(rec_to_base(n//base,base))+str(n%base)
print(rec_to_base(20,16))