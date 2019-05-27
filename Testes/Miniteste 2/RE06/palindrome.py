def  palindrome(astring):
    k=0
    for i in range(len(astring)-1):
        sub=astring[i]
        for j in range(i+1,len(astring)):
            sub+= astring[j]
            if sub==sub[-1::-1]:
                k+=1
    a="For string '{}': {} palindrome substrings".format(astring,k)
    return a
