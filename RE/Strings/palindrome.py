def palindrome(astring):
    k=0
    for i in range(len(astring)-1):
        for j in range(i+2,len(astring)+1):
            frase=astring[i:j]
            print(frase)

            if frase==frase[-1::-1]:
                k+=1
    return k
