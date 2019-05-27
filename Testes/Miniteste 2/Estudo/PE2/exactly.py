def exactly(s):
    k=0
    resultado=()
    for i in range(len(s)-1):
        k=0
        if s[i] in "0123456789":
            for j in range(i+1,len(s)):
                if s[j]=="?":
                    k+=1                
                if s[j] in "0123456789" and int(s[j])+int(s[i])==10:
                    if k==3:
                        resultado+=(s[i]+s[j],)
                        break
                    else:
                        return "The sequence {} is NOT OK with first violation with pair: {}".format(s,(s[i]+s[j],))
    return "The sequence {} is OK with the pairs: {}".format(s,resultado)

print(exactly("aa6?9"))   
                     
                    
                