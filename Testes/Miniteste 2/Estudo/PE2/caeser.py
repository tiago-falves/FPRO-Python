def caesar(message):
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s=""
    for i in range(len(message)):
        
        F=(((1+5**0.5)**(fib(i)%26))-(1-5**0.5)**(fib(i)%26))/((2**(fib(i)%26))*5**0.5)
        
        if abc.find(message[i])==-1:
            s+=message[i]
        else:            
            s+=abc[int((abc.find(message[i])-fib(i))%26)]
    return s
        
def fib(n):
    f=[0,1]
    if n==0:
        return f[0]
    else:
        for i in range(2,n+1):
            f.append(f[i-2]+f[i-1])

        return f[len(f)-1]
print(caesar("FIBONACCI SEQUENCE"))