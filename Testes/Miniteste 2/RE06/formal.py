def formal(name):
    a=name.split()
    s=a[len(a)-1]+","
    a=a[0:len(a)-1]
    for word in a:
        s+=" "+ word[0]+"."
    return s
    
s=formal("Aníbal António Cavaco Silva")
print(s)