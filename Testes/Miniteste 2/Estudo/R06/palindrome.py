def palindrome(astring):
    k=0
    for i in range(len(astring)-1):
        for j in range(i+2,len(astring)+1):
            s=astring[i:j]
            if s==s[-1::-1]:
                k+=1
            print(s)
    a="For string '{}': {} palindrome substrings".format(astring,k)
    
    return a
