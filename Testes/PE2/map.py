def map(pos,steps):
    steps=steps.split("-")
    pos=list(pos)
    for i in steps:
        if i=="up":
            pos[1]+=1
        elif i=="down":
            pos[1]-=1
        elif i=="left":
            pos[0]-=1
        elif i=="right":
            pos[0]+=1
    return tuple(pos)
        
        
    
    
    