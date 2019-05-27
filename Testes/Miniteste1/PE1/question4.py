tS=float(input("Insert time swimming "))
tC=float(input("Insert time Cycling "))
tR=float(input("Insert time running "))
if tS+tC+tR>4:
    print("Time")
elif 1.5/tS>=2 and 40/tC>=20 and 10/tR>=8:
    print(tS+tC+tR)
elif 1.5/tS <2:
    print("Swimming")
elif 40/tC<20:
    print("Cycling")
else:
    print("Running")
    