def question1(num):
    soma=0
    num=str(num)
    for i in num:
        soma+=int(i)**3
    if soma==int(num):
        return True
    return False
def question2(d,num):
    soma=0
    num=str(num)
    for i in num:
        if int(i)>d:
            soma+=2*int(i)
    return soma
def question3(names,ages):
    s=""
    for i in zip(names,ages):
        s+=i[0]+"-"+str(i[1])+" "
    return s.strip()
def q4(tS,tC,tR):
    if tS+tC+tR>4:
        print("Time")
    elif 1.5/tS<2:
        print("Swimming")
    elif 40/tC<20:
        print("Cycling")
    elif 10/tR<8:
        print("Running")
    else:
        print(tS+tC+tR)
def octal(dec):
    s=""
    for i in range(len(str(dec))+1):
        s=str(dec%8)+s
        dec=dec//8
    return int(s)
        