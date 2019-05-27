def concatenate(n1,n2):
    n1=int(n1)
    n2=int(n2)
    n21=n2
    j=1
    while int(n21/10) != 0:
        n21=int(n21/10)
        j+=1
    result=n1*10**j+n2
    return result
n=int(input("n"))
m=int(input("m"))
a=concatenate(n,m)
print(a)