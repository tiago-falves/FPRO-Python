LE=int(input("Insert LE grade "))
RE=int(input("Insert RE grade "))
PE=int(input("Insert PE grade "))
TE=int(input("Insert TE grade "))
if LE>100 or RE>100 or PE>100 or TE>100 or LE<0 or RE<0 or PE<0 or TE<0:
    print("Input error")
elif PE<40 or TE<40:
    print("RFC")
else:
    grade= (LE + RE + 4 * PE + 4 * TE) / 50
    print(int(grade))
