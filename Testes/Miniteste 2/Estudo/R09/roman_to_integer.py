def roman_to_integer(astring):
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    soma=0
    for chi in range(len(astring)-1):
        if roman[astring[chi]]<roman[astring[chi+1]]:
            soma-=roman[astring[chi]]
        else:
            soma+=roman[astring[chi]]
    soma+=roman[astring[len(astring)-1]]
    return soma
