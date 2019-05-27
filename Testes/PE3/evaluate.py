def evaluate(a,x):
    soma=0
    for i in range(len(a)):
        soma+=a[i]*x**i
    return soma
