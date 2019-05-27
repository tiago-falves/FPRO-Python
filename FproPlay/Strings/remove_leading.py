def remove_leading(ip):
    s=""
    ip=ip.split(".")
    for i in ip:
        s+=str(int(i))+"."
    return s[:len(s)-1]

