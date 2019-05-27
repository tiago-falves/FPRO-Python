def manipulator(l,cmds):
    s=""
    for i in cmds:
        i=i.split()
        if i[0]=="insert":
            l.insert(int(i[1]),int(i[2]))
        elif i[0]=="print":
            s+=str(l)+" "
        elif i[0]=="remove":
            l.remove(int(i[1]))
        elif i[0]=="append":
            l.append(int(i[1]))
        elif i[0]=="sort":
            l=sorted(l)
        elif i[0]=="pop":
            l.pop()
        elif i[0]=="reverse":
            l.reverse()
    s.strip()    
    return s

        