def palindromes(astring):
    astring=astring.split() #so está aqui para possibilitar que o programa consiga receber mais do que uma palavra
    resultado=0
    for i in range(len(astring)):
        for j in range(len(astring[i])-1):
            palavra=astring[i][j]
            palavra_inv=astring[i][j]
            for h in range(j+1,len(astring[i])):
                palavra=palavra+astring[i][h]
                palavra_inv=astring[i][h]+palavra_inv
                if palavra==palavra_inv:
                    resultado=resultado+1
    return resultado