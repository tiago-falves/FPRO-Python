def gcd(a,b):
    r=a%b
    if r==0:
        return a
    elif r==1:
        return 1
    return gcd(b,r)
gcd(10,4)