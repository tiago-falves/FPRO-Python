num=int(input("insert an integer "))
x0=num
x1=(x0+num/x0)/2
while x0-x1>0.005:
    x1=(x0+num/x0)/2
    a=x1
    x2=(a+num/a)/2
    x1=x2
    x0=a     
print("%.3f"%x0)

