def genealogy(l):
    
    def extra(tup):
        y=0
        if tup[1]=="sibling":
            y=0
        elif tup[1]=="parent":
            y=1
        elif tup[1]=="cousin":
            y=2
        elif tup[1]=="grandparent":
            y=3
        return y
    return sorted(sorted(l,key=lambda x:x[0]),key=extra)

