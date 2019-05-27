def roman_to_integer(astring):
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    soma=0
    for ch in range(len(astring)-1):
        if d[astring[ch]]<d[astring[ch+1]]:
            soma-=d[astring[ch]]
        else:
            soma+=d[astring[ch]]
    soma+=d[astring[len(astring)-1]]
    return soma
        
