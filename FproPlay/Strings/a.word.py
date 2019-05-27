#n=input("Insira uma frae")
#import string
#upp=0
#low=0
#for i in n:
#    if i in string.ascii_uppercase:
#        upp+=1
#    else:
#        low+=1
#if upp<=low:
#    print(n.lower())
#else:
#    print(n.upper())



records=(('João', 'up20186042', (90, 87)),('Ana', 'up20186040', (90, 90)),('José', 'up20186063', (70, 90)),('Ana', 'up20186061', (90, 90)),('Tiago', 'up20186070', (100, 90)))
print(sorted(records,key=lambda x: (-sum(x[2])//len(x[2]),x[0],x[1])))