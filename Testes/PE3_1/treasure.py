def treasure(clues):
    ponto=clues[(0,0)]
    def extra(ponto):
        
        if ponto not in clues:
            return ponto
        
        return extra(clues[ponto])
    return extra(ponto)

