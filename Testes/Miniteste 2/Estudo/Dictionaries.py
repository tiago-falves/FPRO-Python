def academy_awards(alist):
    d={}
    for i in alist:
        if i[1] not in d:
            d[i[1]]=1
        else:
            d[i[1]]+=1
    return d
def fight(heroes, villain):
    for i in heroes:
        if i["category"]==villain["category"]:
            if i["health"]>=villain["health"]:
                return "{} defeated the villain and now has a score of {}".format(i["name"],i["score"]+1)
            else:
                villain["health"]-=i["health"]/2
    return "{} prevailed with {}HP left".format(villain["name"],villain["health"])
def most_frequent(alist):
    d={}
    
    for i in alist:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    a=min(d)
    maxi=max(d.values())
    for i in d:
        if d[i]==maxi:
            if i>a:
                a=i
    return a
def sort_by_key(dict):
    t=[]
    for i in dict:
        t.append((i,dict[i]))    
    return sorted(sorted(t,key=lambda x: x[1]),key=lambda y: y[0])

    
def tfidf(documents):
    d={}
    lista=[]
    import math
    for i in range(len(documents)):
        lista.append(0)
        documents[i]=documents[i].split()
        for j in range(len(documents[i])):
            documents[i][j]=documents[i][j].lower()

    for i in range(len(documents)):
        for j in range(len(documents[i])):
            if documents[i][j] not in d:
                d[documents[i][j]]=lista.copy()
                d[documents[i][j]][i]=1
            else:
                d[documents[i][j]][i]+=1
    
    for i in d:
        n=0
        for j in d[i]:
            if j!=0:
                n+=1
        for k in range(len(d[i])):
            d[i][k]=round(d[i][k]*math.log(len(documents)/n),3)
            
    return d



























    
