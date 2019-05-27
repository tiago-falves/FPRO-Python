def recursive_dot(l1,l2):
    soma=0
    def extra(l1,l2,soma):
        for i in range(len(l1)):
            if type(l1[i]).__name__=="list":
                
                return extra(l1[i],l2[i],soma)
                
            else:
                soma+=l1[i]*l2[i]
        return soma
    return extra(l1,l2,soma)
print(recursive_dot([[5, 3, 1], [2, 4]], [[4, 2, 0], [1, 3]]))            
                