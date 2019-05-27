def budgeting(budget, products, wishlist):
    soma=0
    dic={}
    dic1={}

    for items in wishlist:
        soma+= wishlist[items]*products[items]
        dic[items]=products[items]
        dic1[items]=products[items]
    minimum = min(dic.values())
    while soma>budget:
        dic=dic1.copy()
        for k in dic.keys():        
            if soma>budget:
                if dic[k] == minimum :
                    while soma>budget and wishlist[k]!=0:
                        wishlist[k] -= 1
                        soma-=dic[k]
        
                if wishlist[k]==0:
                    del wishlist[k]
                    del dic1[k]
                    if len(dic1)!=0:
                        
                        minimum=min(dic1.values())
                    else:
                        break
            else:
                break
    return wishlist

