names = ["bart", "marie", "jo"]
ages = [23, 75, 19]
s=""
n=len(ages)
for i in range(n):
    s+=names[i]+"-"+str(ages[i])+" "
s=s.strip()
print(s)