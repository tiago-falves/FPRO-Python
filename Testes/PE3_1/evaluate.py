def evaluate(a,x):
    result=0
    for i in range(len(a)):
        result+=a[i]*(x**i)
    return result
