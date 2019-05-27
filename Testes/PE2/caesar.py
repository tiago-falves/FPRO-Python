def caesar(message):
    s=""
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(message)):
        f=(((1+5**0.5)**i)-(1-5**0.5)**i)//((2**i)*5**0.5)
        if message[i] not in abc:
            s+=message[i]
        else:
            
            s+=abc[(abc.find(message[i])-int(f))%26]
    return s
