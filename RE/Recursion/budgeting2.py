def budgeting2(budget, products, wishlist):
    soma=0
    d={}
    d1={}
    for desire in wishlist:
        soma+=products[desire]*wishlist[desire]
        d[desire]=products[desire]
    while soma >budget:
        maxi=max(d.values())
        n=budget//maxi   
        for i in wishlist:
            d[i]=products[i]
            if wishlist[i]==maxi:
                if n>=wishlist[i]:
                    d1[i]=wishlist[i]
                    del wishlist[i]
                    for desire in wishlist:
                        soma+=products[desire]*wishlist[desire]
                        d[desire]=products[desire]
                    return budgeting2(budget,products,wishlist)
                else:
                    wishlist[i]-=1
                    if wishlist[i]==0:
                        del wishlist[i]
                        del d[i]
                        soma-=products[i]
                break
    return wishlist
#    for desire in wishlist:
#        soma+=products[desire]*wishlist[desire]
#        d[desire]=products[desire]
#        
#    while soma>budget:
#        maxi=max(d.values())
#        n=budget//maxi
#        
#        for i in wishlist:
#            
#            if d[i]==maxi:
#                if wishlist[i]<=n:
#                    d1[i]=
#                wishlist[i]-=1
#                if wishlist[i]==0:
#                    del wishlist[i]
#                    del d[i]
#                soma-=products[i]
#                break
#                
print(budgeting2(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40,'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))