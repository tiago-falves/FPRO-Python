def ragnoli(N):
    if N==1:
        return "a"
    else:
        
        traços="-"
        s=""
        ntraços=N-2
        k=0
        abc="abcdefghijklmnopqrstuvwxyz"
        for i in range(N-1):
            k=0
            ntraços=(N-(i+1))*2
            s+=traços*ntraços
            for j in range(i+1):
                s+=abc[N-1-j]+"-"
            k=N-i
            for j in range(i):
                s+=abc[k]+"-"
                k+=1
            s=s[:len(s)-1]
            s+=traços*ntraços
            s+="\n"
        ntraços=0
        for i in range(N):
            s+=traços*ntraços
            for j in range(N-i):
                s+=abc[N-1-j]+"-"
            k=N-(N-i-1)
            
            for j in range(N-i-1):
                s+=abc[k]+"-"
                k+=1
            s=s[:len(s)-1]
            s+=traços*ntraços
            s+="\n"
            ntraços+=2
        return s

print(ragnoli(6))
        
        