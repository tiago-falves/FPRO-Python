num=int(input("Insert an integer "))
soma=num+1
s="1"
for i in range(2,num//2+1):
    if num%i==0:
        soma+=i
        s+="+"+str(i)
print("for num="+str(num),"the output is",soma,"("+s+"+"+str(num)+")")
        
    