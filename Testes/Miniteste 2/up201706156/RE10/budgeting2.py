#5. Budget version 2.0

def extra(price,budget,products,wishlist):
            
    missing=price-budget   
    save=""
    difference=10000
    
    for i in wishlist:
        
        if products[i]==missing:
            return i
        elif abs(missing-products[i])<difference:
            difference=abs(missing-products[i])
            save=i
    
    return save

def budgeting2(budget, products, wishlist):

    l=[]
    
    for i in wishlist:
        l.append((products[i],i)) 
        
    l.sort(reverse=True)
    dic={}

    for i in l:
        dic[i[1]]=i[0]
    price=0    
    for i in wishlist:
        price += products[i]*wishlist[i]
        dic[i]=wishlist[i]
        
    if price <= budget:
        return dic
    
    else: 
        i=extra(price,budget,products,dic)
        dic[i]-=1
        if dic[i]==0:
            del dic[i]
        return budgeting2(budget,products,dic)
