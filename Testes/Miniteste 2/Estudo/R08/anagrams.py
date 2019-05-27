def anagrams(alist):
    lista=[]
    listacopias=[]
    listacopias1=[]
    cont=-1
    for frase in alist:
        cont+=1
        for frase1 in alist:
            copia=frase1
            k=0
            if frase!=frase1 and len(frase1.replace(" ",""))==len(frase.replace(" ","")) and frase not in listacopias :
                for chi in range(len(frase)):
                    bool1=copia.find(frase[chi])
                    if bool1==-1 and len(copia)==0:
                        k+=1
                    else:
                        copia=copia[0:chi]+copia[chi+1:len(copia)]
                if k==0:   
                    if frase in listacopias1:
#                        lista.append([frase1])
                        lista[cont].append(frase1)
                        lista[cont]=sorted(lista[cont])
                    else:
                        
                        lista.append(sorted(([frase,frase1])))
                    listacopias.append(frase1)
                    listacopias1.append(frase)
                    
             
    return sorted(lista) #Porque que nao funciona o sorted
                        
                        
                
print(anagrams(["they see", "eat", "The eyes", "car has", "ate", "a crash", "tea"]))