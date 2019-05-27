def exactly(s):
    tup=()
    for i in range(len(s)):
        k=0
        if s[i] in "0123456789":
            for j in range(i+1,len(s)):
                if s[j]=="?":
                    k+=1
                elif s[j] in "0123456789":
                    if int(s[i])+int(s[j])==10:
                        if k==3:
                            tup+=(s[i]+s[j],)
                        else:
                            return "The sequence {} is NOT OK with first violation with pair: {}".format(s,(s[i]+s[j],))
    return "The sequence {} is OK with the pairs: {}".format(s,str(tup))
                
                