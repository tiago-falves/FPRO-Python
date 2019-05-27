d=int(input("insert a digit "))
num=int(input("Insert a number "))
a=num
i=0
soma=0
while a!=0:
    a=a//10
    i+=1
for i in range(i):
    b=num%10
    if b > d:
        soma+=b*2
    num=num//10    
print(soma)