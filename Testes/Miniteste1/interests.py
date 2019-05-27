Principal_amount=int(input("the amount that the interest is provided on"))
Interest_rate=float(input("Insert the interest rate"))
Freq=int(input("the frequency that the interest is paid out (per year)"))
years=int(input("the number of years that the interest is calculated for"))
earning=Principal_amount*(1+(Interest_rate/Freq))**(Freq*years)
print("The earning is "+str(earning))

