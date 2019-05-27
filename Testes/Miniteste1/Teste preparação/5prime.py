lower=int(input("Insert the lower number"))
upper=int(input("Insert the upper number"))
s=""
primo=True
for i in range(lower,upper+1):
    if i<=0 or i==1:
        primo=False
        i+=1
    for j in range(2,i//2+1):
        if i % j == 0:
            primo=False
            break
    if primo==True:
            s+=str(i)+" "
    primo=True
print(s)        
