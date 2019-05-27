def count_exceptions(f,n1,n2):
    k=0
    for i in range(n1,n2+1):
        try:
            f(i)
        except Exception:
            k+=1
    return k
                    
