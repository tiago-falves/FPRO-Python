def isomorphic(astring1,astring2):
    d={}
    d1={}
    lista=[]
    for i in range(len(astring1)):
        if astring1[i] not in d:
            d[astring1[i]]=astring2[i]
            lista.append((astring1[i],astring2[i]))
        else:
            if d[astring1[i]]!=astring2[i] :
                return "{} and {} are not isomorphic".format(astring1,astring2)
        if astring2[i] not in d1:
            d1[astring2[i]]=astring1[i]
        else:
            if d1[astring2[i]]!=astring1[i] :
                return "{} and {} are not isomorphic".format(astring1,astring2)
            
    return "'{}' and '{}' are isomorphic because we can map: {}".format(astring1,astring2,lista)
            
