def genealogy(l):
    def f_order(elem):
        
        if elem[1]=="sibling":
            y=0
        elif elem[1]=="parent":
            y=1
        elif elem[1]=="cousin":
            y=2
        else:
            y=3
        return y
               
    return sorted(sorted(l,key=lambda y:y[0]),key=f_order)
