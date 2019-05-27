def ordem(records):
    soma=0
    for i in records[2]:
        soma+=i
    avg=soma/len(records[2])
    return (-avg,records[0],records[0])
def grades(records):
    new=sorted(records,key=ordem)
    return new

records=(('João', 'up20186042', (90, 87)),('Ana', 'up20186040', (90, 90)),('José', 'up20186063', (70, 90)),('Ana', 'up20186061', (90, 90)),('Tiago', 'up20186070', (100, 90)))
print(grades(records))
    