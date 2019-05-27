def minion(astring):
    used_k=[]
    copia=astring
    resultado_k=0
    resultado_s=0
    frase_result_k=""
    frase_result_s=""
    final=""
    comprimento=len(astring)
    for k in range(comprimento):
        copia=astring
        for i in range(comprimento):
            if copia[0] in "AEIOU":
                if copia[0:k+1] not in used_k:
                    used_k.append(copia[0:k+1])
                    resultado_k+=count(astring,copia[0:k+1])
                    frase_result_k+="- "+copia[0:k+1]+": "+str(count(astring,copia[0:k+1]))+"\n"
            else:
                if copia[0:k+1] not in used_k:
                    used_k.append(copia[0:k+1])
                    resultado_s+=count(astring,copia[0:k+1])
                    frase_result_s+="- "+copia[0:k+1]+": "+str(count(astring,copia[0:k+1]))+"\n"
                
            copia=copia[1:]
    
    frase_result_k=frase_result_k.strip()
    frase_result_s=frase_result_s.strip()

    if resultado_k>resultado_s:
        final="The winner was Kevin with a total of "+str(resultado_k)+" points:\n"+frase_result_k
    elif resultado_k==resultado_s:
        final="It was a draw!"
    else:
        final="The winner was Stuart with a total of "+str(resultado_s)+" points:\n"+frase_result_s
        
        
    
    return final

def count(astring,ch):
    k=0
    for i in range(len(astring)-len(ch)+1):
        if astring[i:i+len(ch)]==ch:

            k+=1
    return k

print(minion("ANANAS"))         
                
        