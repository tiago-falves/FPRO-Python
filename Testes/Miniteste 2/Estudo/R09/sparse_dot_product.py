def sparse_dot_product(dict1, dict2):
    soma=0
    for keys1 in dict1:
        for keys2 in dict2:
            if keys1==keys2:
                soma+=dict1[keys1]*dict2[keys2]
    return soma
