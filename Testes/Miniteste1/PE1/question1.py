num=int(input("Insert a number with 3 digits "))
a=num
soma=0
for i in range (3):
    b=a%10
    soma+=b**3
    a=a//10
if soma==num:
    print("True")
else:
    print("False")