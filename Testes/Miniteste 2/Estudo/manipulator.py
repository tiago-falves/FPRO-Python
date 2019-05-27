def manipulator(l, cmds):
    s=""
    for cm in cmds:
        cm=cm.split()
        if cm[0]=="insert":
            l.insert(int(cm[1]),int(cm[2]))
        elif cm[0]=="print":
            s+=str(l)+" "
        elif cm[0]=="remove":
            l.remove(int(cm[1]))
        elif cm[0]=="append":
            l.append(int(cm[1]))
        elif cm[0]=="sort":
            l.sort()
        elif cm[0]=="pop":
            l.pop()
        elif cm[0]=="reverse":
            l.reverse()
        s.strip()
    return s   
   
        
