def ugly(n):
    while n !=1:
        if n%2==0:
            n=n//2
        elif n%5==0:
            n=n//5
        elif n%3==0:
            n=n//3
        else:
            return False
    return True