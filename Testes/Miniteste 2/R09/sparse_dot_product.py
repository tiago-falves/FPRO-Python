def sparse_dot_product(dict1, dict2):

    soma=0
    for i in dict1:
        for j in dict2:
            if i==j:
                soma+=dict1[i]*dict2[j]
    return soma
        
        
        
        
sparse_dot_product({0: 1, 1: 1}, {2: 1, 3: 1})            
        