

def budgeting(budget, products, wishlist):
    adict = {}
    nproducts = {}
    for i in products:
        if i in products and (i in wishlist) == False:
            nproducts[i] = products[i]
    all(map(products.pop, nproducts))
    
    for r in range(sum(wishlist.values())):
        for key in list(wishlist.keys()):
            if wishlist[key] == 0:
                del products[key]
                del wishlist[key]
                
        adict = {}
        for k in wishlist:
            adict[k] = wishlist[k] * products[k]
        if sum(adict.values()) <= budget:
            return wishlist
    
        else:
            minimum = min(products.values())
            
            for k in products.keys():
                if products[k] == minimum:
                    wishlist[k] += -1



 