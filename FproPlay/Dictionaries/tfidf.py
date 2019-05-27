def tfidf(documents):
    import math
    lista=[]
    l=[]
    d={}
    
    for i in range(len(documents)):
        documents[i]=documents[i].split()
        lista+=[x.lower() for x in documents[i]]
        for j in range(len(documents[i])):
            documents[i][j]=documents[i][j].lower()
    for j in documents:
        l+=[0]
    for i in lista:
        d[i]=l
        soma=0
        for j in range(len(documents)):
            d[i][j]=documents[j].count(i)
            if d[i][j]!=0:
                soma+=1
        d[i]=[round(x*math.log(len(documents)/soma),3) for x in d[i]]     
    return d
