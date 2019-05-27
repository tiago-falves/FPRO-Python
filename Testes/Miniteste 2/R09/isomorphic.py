def isomorphic(astring1, astring2):
    d={}
    e=[]
    lista=[]
    lista1=[]
    s=""
    k=0
    for ch in range(len(astring2)):
        
        if astring1[ch] not in lista1:
            lista1.append(astring1[ch])
            d[astring1[ch]]=astring2[ch]
            if d[astring1[ch]] not in e:
                e.append(astring2[ch])
                
                lista.append((astring1[ch],astring2[ch]))
            else:
                s="'"+astring1+"' and '"+astring2+"' are not isomorphic"
                k=1
                break
        else:
            continue
    if k!=1:
        
        s="'"+astring1+"' and '"+astring2+"' are isomorphic because we can map: "+str(lista)
    return s

print(isomorphic('turtle', 'tletur'))   