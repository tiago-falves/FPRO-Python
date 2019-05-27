def treasure(clues):
    if clues=={}:
        return (0,0)
    else:
        pista=clues[(0,0)]
        
        def extra(clues,pista):    
            if clues[pista] not in clues:
                return clues[pista]
            elif pista==clues[clues[pista]]:
                return pista
        return extra(clues,clues[pista])
#print(treasure({(0, 0): (10, 10), (30, 30): (10, 10), (10, 10): (50, 10), (50, 10): (10, 10), (-10, 10): (50, 10)}))
