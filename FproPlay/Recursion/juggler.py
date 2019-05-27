def juggler(n,p):
    if p==0:
        return n
    if juggler(n,p-1)%2==0:
        return int(juggler(n,p-1)**(1/2))
    else:
        return int(juggler(n,p-1)**(3/2))
print(juggler(3,1))

