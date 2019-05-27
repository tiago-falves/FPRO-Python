def day_name(n):
    n=int(n)
    if n==0:
        return "Sunday"
    elif n==1:
        return "Monday"
    elif n==2:
        return "Tuesday"
    elif n==3:
       return "Wednesday"
    elif n==4:
        return "Thursday"
    elif n==5:
        return "Friday"
    elif n==6:
        return "Saturday"
    else:
        return None
def day_num(n):
    if n=="Sunday":
        return 0
    elif n=="Monday":
        return 1
    elif n=="Tuesday":
        return 2
    elif n=="Wednesday":
       return 3
    elif n=="Thursday":
        return 4
    elif n=="Friday":
        return 5
    elif n=="Saturday":
        return 6
    else:
        return None
def day_add(day,n):
    
    a=day_num(day)
    b=(a+n)%7
    return day_name(b)
day=input("Insira um dia da semana ")
n=int(input("Daqui a quantos dias quer saber?"))
a=day_add(day,n)
print(a)
    