def isomorphic(astring1,astring2):
    dic={}
    lista=[]
    for chi in range(len(astring1)):
        if astring2[chi] in dic.values() or astring1[chi] in dic.keys():
            if dic[astring1[chi]]!= astring2[chi]:
                return "'"+ astring1+"' and '"+astring2+"' are not isomorphic"
        else:
            dic[astring1[chi]]=astring2[chi]
            lista.append((astring1[chi],astring2[chi]))
    
    return "'"+astring1+"'  and '"+astring2+"' are isomorphic because we can map: "+str(lista) 
print(isomorphic('turtle', 'tletur'))

#O caso em que nao so isomorficos esta errado! porque??