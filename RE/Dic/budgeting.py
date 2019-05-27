def budgeting(budget, products, wishlist):
    soma=0
    d={}
    for desire in wishlist:
        soma+=products[desire]*wishlist[desire]
        d[desire]=products[desire]
    while soma>budget:
        mini=min(d.values())
        for i in wishlist:
            if d[i]==mini:
                wishlist[i]-=1
                if wishlist[i]==0:
                    del wishlist[i]
                    del d[i]
                soma-=products[i]
                break
                
    return wishlist
#print(budgeting(300, {'printer': 75, 'cellphone': 30, 'shoes': 50, 'powerbank': 25, 'socks': 5}, {'cellphone': 1, 'shoes': 2, 'powerbank': 1, 'socks': 10}))
#print(budgeting(	4000, {'laptop': 900, 'mechanical keyboard': 120, 'book': 20, 'watch': 125, 'painting': 299}, {'laptop': 3, 'mechanical keyboard': 3, 'book': 1, 'watch': 1, 'painting': 4}))