def soma(n):
    if len(n)==1:
        return n[0]
    return n[0]+soma(n[1:])
def int_str(n,base):
    b16="0123456789ABCDEF"
    if n//base==0:        
        return b16[n]
    return str(int_str(n//base,base))+ b16[n%base]
def soma_list(lista):#[1, 2, [3,4], [5,6]]
    total=0
    for i in lista:
        if type(i).__name__=="list":
            total+=soma_list(i)
        else:
            total+=i
    return total
def sum_n(n): #sumDigits(345) -> 12
    n=str(n)
    if len(n)==1:
        return int(n)
    return int(n[0])+sum_n(n[1:])
def reverse(s):
    if len(s)==1:
        return s[0]
    return reverse(s[1:] )+s[0]   
