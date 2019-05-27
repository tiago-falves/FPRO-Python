def roman_to_integer(astring):
    soma=0
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    for i in range(len(astring)-1):
        
        if d[astring[i]]>=d[astring[i+1]]:
            soma+=d[astring[i]]
        else:
            soma-=d[astring[i]]
                        
    soma+=d[astring[len(astring)-1]]
    return soma  
roman_to_integer('MMMCMXCIX')