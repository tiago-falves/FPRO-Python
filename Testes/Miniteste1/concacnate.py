def concatenate():
    n1=int(input("Insert a number"))
    n2=int(input("Insert a number"))
    n21=n2
    j=1
    while int(n21/10) != 0:
        n21=int(n21/10)
        j+=1
    result=n1*10**j+n2
    return result

a=concatenate()
print(a)