dec=int(input("Insert a number"))
a=dec
s=""
d=""
while dec!=0:
    a=dec%8
    s+=str(a)
    dec=dec//8
for i in range(-1,-len(s)-1,-1):
    d=d+s[i]
print(d)
    