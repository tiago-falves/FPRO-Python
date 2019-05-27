def pascal(n):
    from math import factorial
    a=""
    for i in range(n):
        for j in range(i+1):
            a+=str(factorial(i)//(factorial(j)*factorial(i-j)))+" "    
        a.strip()
        a+="\n"
    return a
print(pascal(5))
