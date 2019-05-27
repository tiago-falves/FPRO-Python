def manipulator(l,cmds):
    s=""
    for order in cmds:
        order=order.split()
        if order[0]=="insert":
            l.insert(int(order[1]),int(order[2]))
        elif order[0]=="print":
            s+=str(l)+" "
        elif order[0]=="remove":
            l.remove(int(order[1]))
        elif order[0]=="append":
            l.append(int(order[1]))
        elif order[0]=="sort":
            l=sorted(l,key=lambda y:int(y))
        elif order[0]=="pop":
            l.pop()
        elif order[0]=="reverse":
            l.reverse()
    return s
         
        